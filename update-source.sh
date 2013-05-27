#!/bin/sh
# Usage:
# ./update-source.sh
# env variables controlling behaviour
#  build_package=[0|1] - build package when new version is fetched
#  publish_packages=[0|1] - publish built packages in ~/public_html/$dist/$arch
#  quiet=[0|1] - discard stdout of process

# work in package dir
dir=$(dirname "$0")
cd "$dir"

# abort on errors
set -e

# setup $quiet, you may override with env it
quiet=${quiet:-$(tty -s && echo 0 || echo 1)}
if [ "$quiet" = "1" ]; then
	# we do not want output when running on cron
	exec 1>/dev/null
fi

pkg=vim
specfile=$pkg.spec
basever=7.3
baseurl=ftp://ftp.vim.org/pub/editors/vim/patches/$basever
sources=ftp://ftp.vim.org/pub/editors/vim/patches/$basever/MD5SUMS

status=$(git status --porcelain sources)
if [ "$status" ]; then
	echo >&2 "sources status not clean; commit or stash any pending changes"
	echo "$status"
	exit 1
fi

if [ "$1" ]; then
	ver=$1
else
	echo "Fetching latest patches list..."
	wget -nv $sources -O sources.tmp 2>&1
	sort -k 2 -V < sources.tmp > sources.new
	# exclude files already in git tree
	git ls-files "$basever.*" | sed -e 's/\./\\./g;s/$/$/'| grep -vf - sources.new > sources
	rm sources.new sources.tmp
	# also update patches README
	wget -nv $baseurl/README -O README.patches 2>&1
	ver=$(tail -n1 sources | awk '{print $NF}')
fi

curpatch=$(awk '/^%define[ 	]+patchlevel[ 	]+/{print $NF}' $specfile)
curver=$basever.$curpatch

if [ "$curver" != "$ver" ]; then
	echo "Updating $specfile to $ver"
	patch=${ver#$basever.}
	if [ -z "$patch" ]; then
		echo >&2 "Will not set empty patchlevel"
		exit 1
	fi
	sed -i -e "
		s/^\(%define[ \t]\+patchlevel[ \t]\+\)[0-9]\+\$/\1$patch/
	" $specfile

	# fetch missing/mismatching files manually. faster than builder does that
	md5sum -c sources 2>/dev/null|awk -F: '$NF != " OK" {print $1}' | while read file; do
		echo "$baseurl/$file"
	done | wget -nv -i -

	WGET_OPTS="-nv" ../builder -g $specfile

	if [ "$build_package" != 0 ]; then
		dist=$(rpm -E %{pld_release})
		arch=$(rpm -E %{_host_cpu})
		outdir=$(readlink -f $dir)/BUILD-$dist-$arch
		logfile=$outdir/$pkg.log
		rpmdir=$outdir/RPMS
		install -d $rpmdir

		# setup custom logfile via $HOME_ETC hack
		# TODO: just add --logfile support for builder
		cat > $outdir/.builderrc <<-EOF
			if [ -n "$HOME_ETC" ]; then
				. "$HOME_ETC/.builderrc"
			elif [ -r ~/.builderrc ]; then
				. ~/.builderrc
			fi
			LOGFILE='$logfile'
		EOF

		> $logfile
		HOME_ETC=$outdir \
			../builder -bb --clean \
			--define "_unpackaged_files_terminate_build 1" \
			--define '_enable_debug_packages 0' \
			--define "_builddir $outdir" \
			--define "_rpmdir $rpmdir" \
			$specfile || {
			echo "Package build failed" >&2
			tail -n 1000 $logfile >&2
			exit 1
		}
		echo >&2 "Package build OK"

		rpmdest=~/public_html/$dist/$arch/
		if [ "$publish_packages" ] && [ "$(ls $rpmdir/*.rpm 2>/dev/null)" ]; then
			install -d $rpmdest
			umask 022
			chmod 644 $rpmdir/*.rpm
			mv -v $rpmdir/*.rpm $rpmdest/
			poldek --cachedir=$HOME/tmp --mkidx -s $rpmdest/ --mt=pndir
		fi
	fi

	# autocommit
	msg=$(mktemp)
	echo "updated to $ver" > $msg
	echo "" >> $msg
	over=$(git diff sources | awk '/^\+[0-9a-f]+/{over=$NF; gsub(/\./, "\\.",over); print over; exit}')
	sed -ne "/$over/,\$p" README.patches | sed -re 's,^[ 0-9]+ ,,' >> $msg
	git commit -F $msg $specfile sources
	rm -f $msg
else
	echo "$specfile already up to $ver"
fi
