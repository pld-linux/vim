Summary:	Vim built with ncurses
Summary(pl):	Vim korzystaj±cy z bibliotek ncurses
Name:		vim
Version:	5.4h
Release:	2
Source0:        ftp://ftp.nl.vim.org/pub/vim/unreleased/unix/%{name}-%{version}-src.tar.gz
Source1:        ftp://ftp.nl.vim.org/pub/vim/unreleased/unix/%{name}-%{version}-rt.tar.gz
Source2:        ftp://ftp.nl.vim.org/pub/vim/unreleased/extra/%{name}-%{version}-extra.tar.gz
Source3:	gvim.wmconfig
Copyright:	GPL
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
URL:		http://www.vim.org/
BuildPrereq:	ncurses-static
BuildPrereq:	lesstif-devel
BuildPrereq:	gtk+-devel
BuildPrereq:	glib-devel
BuildPrereq:	gpm-devel
Obsoletes:	vim-gtk
Obsoletes:	vim-lesstif
Obsoletes:	vim-athena
Obsoletes:	vim-ncurses
Buildroot:	/tmp/%{name}-%{version}-root

%description 
The classic Unix text editor build with ncurses library. It adds
multiple windows, multi-level undo, block highliting, and many other
features to the standard vi program.

%description -l pl
Wersja edytora vim skompilowana z bibliotek± ncurses. W porownaniu z
edytorem vi, ta wersja oferuje dodatkowo pracê z wieloma plikami,
wielopoziomowe operacje cofnij, bloki, pod¶wietlanie sk³adni i wiele
innych usprawnieñ.

%package rt 
Summary:	Vim runtime files
Summary(pl):	Pliki przydatne edytorowi vim 
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for vim. If you want to take advantage of vim more powerful
features, you should install this package.

%description rt -l pl
W tym pakiecie znajdziesz dokumentacjê, makra, pliki konfiguracyjne i strony
podrêcznika edytora vim. Je¿eli zamierzasz korzystaæ z vim-a, powiniene¶
zainstalowaæ ten pakiet.

%package static
Summary:	Vim static
Summary(pl):	Vim skompilowany statycznie
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Provides:	vi
Obsoletes:	vi
Requires:	ncurses >= 4.2-12

%description static
The classic Unix text editor. This version is build with minimal
feature and is installed in /bin as a rescue tool. The installation of
this package is STRONGLY recommended.

%description static -l pl
Pakiet zawiera vim - klasyczny (unixowy) edytor tekstowy skompilowany 
statycznie. Instalacja tego pakietu jest MOCNO zalecana, mo¿e on pomóc
Tobie uratowaæ system w czasie awarii.

%package athena
Summary:	Vim built with X11 and athena support
Summary(pl):	Vim pod X-Window korzystaj±cy z Athena Widget Set
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Obsoletes:	vim-lesstif
Obsoletes:	vim-gtk
Obsoletes:	vim-ncurses
Obsoletes:	vim

%description athena 
The classic Unix text editor now also under X Window System! 
This version is build with Athena Widget Set. 

%description athena -l pl
Wersja edytora vim pracuj±ca w graficznym ¶rodowisku X Window
z wykorzystaniem Athena Widget Set.

%package lesstif
Summary:	Vim built with X11 and LessTif support
Summary(pl):	Vim pod X-Window korzystaj±cy z bibliotek LessTif
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Obsoletes:	vim-athena
Obsoletes:	vim-gtk
Obsoletes:	vim-ncurses
Obsoletes:	vim

%description lesstif
The classic Unix text editor now also under X Window System! 
This version is build with LessTif.

%description lesstif -l pl
Wersja edytora vim pracuj±ca w graficznym ¶rodowisku X Window
z wykorzystaniem LessTif.

%package gtk
Summary:	Vim built with X11 and gtk support
Summary(pl):	Vim pod X-Window korzystaj±cy z bibliotek gtk
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Obsoletes:	vim-athena
Obsoletes:	vim-lesstif
Obsoletes:      vim-ncurses
Obsoletes:	vim

%description gtk
The classic Unix text editor now also under X Window System!
This version is build with gtk.

%description gtk -l pl
Wersja edytora vim pracuj±ca w graficznym ¶rodowisku X Window
z wykorzystaniem gtk.

%prep
%setup -q -b 1 -b 2

%build
cd src

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-static -s" \
./configure %{_target} \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--enable-min-features \
	--datadir=/etc \
	--with-tlib=ncurses \
	--prefix=/usr
make vim
make xxd/xxd
mv vim vim.static
mv xxd/xxd xxd.static

make distclean
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--enable-max-features \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--enable-gmp \
	--with-tlib=ncurses \
	--prefix=/usr
make vim
mv vim vim.ncurses

make distclean
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
        --enable-max-features \
	--enable-gui=athena \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--enable-gmp \
	--with-tlib=ncurses \
	--prefix=/usr
make vim
mv vim vim.athena

make distclean
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
        --enable-max-features \
	--enable-gui=motif \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--enable-gmp \
	--with-tlib=ncurses \
	--prefix=/usr
make vim
mv vim vim.lesstif

make distclean
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
        --enable-max-features \
	--enable-gui=gtk \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--enable-gmp \
	--with-tlib=ncurses \
	--prefix=/usr
make vim
mv vim vim.gtk

cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -d $RPM_BUILD_ROOT/bin
install -d $RPM_BUILD_ROOT/usr/{bin,X11R6/bin,share/vim/{doc,tutor},man/man1}

# make prefix=$RPM_BUILD_ROOT/usr install

install -s src/vim.static $RPM_BUILD_ROOT/bin/vi
install -s src/xxd.static $RPM_BUILD_ROOT/bin/xxd

install -s src/vim.ncurses $RPM_BUILD_ROOT/usr/bin/vim.ncurses
install -s src/vim.athena  $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.athena
install -s src/vim.lesstif $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.lesstif
install -s src/vim.gtk     $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.gtk

install    src/vimtutor	   $RPM_BUILD_ROOT/usr/bin/vimtutor

rm -f $RPM_BUILD_ROOT/usr/man/man1/*.1

install runtime/doc/vim.1 $RPM_BUILD_ROOT/usr/man/man1
install runtime/doc/xxd.1 $RPM_BUILD_ROOT/usr/man/man1
install runtime/doc/vimtutor.1 $RPM_BUILD_ROOT/usr/man/man1

echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/vi.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/ex.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/view.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/gvim.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/gview.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/rvim.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/rview.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/rgvim.1
echo ".so vim.1" > $RPM_BUILD_ROOT/usr/man/man1/rgview.1

cp -a runtime/macros $RPM_BUILD_ROOT/usr/share/vim/macros
cp -a runtime/syntax $RPM_BUILD_ROOT/usr/share/vim/syntax
cp -a runtime/tutor/tutor  $RPM_BUILD_ROOT/usr/share/vim/tutor/tutor

install runtime/*.vim $RPM_BUILD_ROOT/usr/share/vim
install runtime/vimrc_example.vim $RPM_BUILD_ROOT/usr/share/vim/vimrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/wmconfig/gvim

touch $RPM_BUILD_ROOT/usr/bin/vim $RPM_BUILD_ROOT/usr/X11R6/bin/gvim

install runtime/doc/*.txt $RPM_BUILD_ROOT/usr/share/vim/doc
install runtime/doc/tags  $RPM_BUILD_ROOT/usr/share/vim/doc

ln -sf vi $RPM_BUILD_ROOT/bin/ex
ln -sf vi $RPM_BUILD_ROOT/bin/view
ln -sf vi $RPM_BUILD_ROOT/bin/rview
ln -sf /bin/vi $RPM_BUILD_ROOT/usr/bin/vi
ln -sf vim $RPM_BUILD_ROOT/usr/bin/rvim

ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/rgvim
ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/gview
ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/rgview

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -sf /usr/bin/vim.ncurses /usr/bin/vim

%post athena
ln -sf /usr/X11R6/bin/gvim.athena /usr/X11R6/bin/gvim
ln -sf /usr/X11R6/bin/gvim /usr/bin/vim

%post lesstif 
ln -sf /usr/X11R6/bin/gvim.lesstif /usr/X11R6/bin/gvim
ln -sf /usr/X11R6/bin/gvim /usr/bin/vim

%post gtk
ln -sf /usr/X11R6/bin/gvim.gtk /usr/X11R6/bin/gvim
ln -sf /usr/X11R6/bin/gvim /usr/bin/vim

%files 
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/vim.ncurses
%attr(755,root,root) /usr/bin/rvim
%attr(755,root,root) %ghost /usr/bin/vim

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*
%attr(755,root,root) /usr/bin/vi

%files athena
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/gvim.athena
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
/etc/X11/wmconfig/gvim
%attr(755,root,root) %ghost /usr/X11R6/bin/gvim
%attr(755,root,root) %ghost /usr/bin/vim

%files lesstif 
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/gvim.lesstif
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
/etc/X11/wmconfig/gvim
%attr(755,root,root) %ghost /usr/X11R6/bin/gvim
%attr(755,root,root) %ghost /usr/bin/vim

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/gvim.gtk
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
/etc/X11/wmconfig/gvim
%attr(755,root,root) %ghost /usr/X11R6/bin/gvim
%attr(755,root,root) %ghost /usr/bin/vim

%files rt
%defattr(644,root,root,755)

%attr(755,root,root) /usr/bin/vimtutor

/usr/man/man1/*

%dir /usr/share/vim
/usr/share/vim/macros

%dir /usr/share/vim/syntax
/usr/share/vim/syntax/*.vim

/usr/share/vim/tutor
/usr/share/vim/bugreport.vim
/usr/share/vim/filetype.vim
/usr/share/vim/scripts.vim
/usr/share/vim/mswin.vim
/usr/share/vim/ftoff.vim
/usr/share/vim/doc

%config %verify(not size mtime md5) /usr/share/vim/menu.vim
%config %verify(not size mtime md5) /usr/share/vim/vimrc

%changelog
* Wed Apr 21 1999 Artur Frysiak <wiget@pld.org.pl>
  [5.4h-1]
- build on rpm 3  

* Fri Mar 12 1999 Artur Frysiak <wiget@pld.org.pl>
  [5.4f-1]
- removed  vim-hold_gui_events.patch and vim-CMDLINE_COMPL.patch
- removed Requires: lesstif gtk+
- added --enable-gpm to configure

* Tue Feb 23 1999 Artur Frysiak <wiget@usa.net>
  [5.4e-1d]
- removed vim-clip.patch (now in 5.4e)
- added vim-CMDLINE_COMPL.patch (allow compile with --enable-min-features)
- added %%defattr macro to all subpackages

* Thu Feb 04 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [5.4d-2d]
- symlink /usr/bin/vi -> /bin/vi
- doc package moved to /usr/share/vim/doc (crazy cpio .. ;)

* Tue Feb  2 1999 Artur Frysiak <wiget@usa.net>
  [5.4d-1d]
- upgraded to 5.4d
- now /usr/share/vim/doc is symlink to /usr/doc/%{name}-rt-%{version}
- added missingok option to wmconfig files

* Wed Jan 13 1999 Artur Frysiak <wiget@usa.net>
  [5.4c-1d]
- upgraded to 5.4c
- added gtk subpackage
- using %%{version} makro in Summary tags
- some chenges in %%build section
- changed Group to Applications/Editors/Vim

* Sun Dec 27 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [5.3-4d]
- fixed some errors in rt subpackage. 
  by Ziemek Borowski <ziembor@mail.ceu.edu.pl>
- fixed etcdir in vim-static subpackage.

* Thu Nov 12 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [5.3-2d]
- added /usr/share/vim/doc/{help.txt,tags} to rt subpackage (was missing)

* Sun Oct 04 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [5.3-1]
- completely rewritten spec, added 4 subpackages

* Thu Aug 13 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [5.0-1d]
- build against glibc-2.1,
- translation modified for pl,
- added build-root support,
- added %changelog,
- fixed permissions fo ELF binaries.
