Summary:	Vim built with ncurses
Summary(pl):	Vim korzystaj±cy z bibliotek ncurses
Name:		vim
Version:	5.4k
Release:	3
########	ftp://ftp.nl.vim.org/pub/vim/unreleased
Source0:        %{name}-%{version}-src.tar.gz
Source1:        %{name}-%{version}-rt.tar.gz
Source2:        %{name}-%{version}-extra.tar.gz
Patch0:		vim-fhs.patch
Copyright:	GPL
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
URL:		http://www.vim.org/
#BuildPrereq:	ncurses-static
#BuildPrereq:	gpm-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description 
The classic Unix text editor. This version is build with minimal
feature and is installed in /bin as a rescue tool. The installation of
this package is STRONGLY recommended.

%description 
Pakiet zawiera vim - klasyczny (unixowy) edytor tekstowy skompilowany 
statycznie. Instalacja tego pakietu jest MOCNO zalecana, mo¿e on pomóc
Tobie uratowaæ system w czasie awarii.

%package	rt 
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

%package	ncurses
Summary:	Vim ncurses
Summary(pl):	Vim ncurses
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Obsoletes:	vim-athena
Obsoletes:	vim-gtk
Obsoletes:	vim-lesstif

%description ncurses 
The classic Unix text editor build with ncurses library. It adds
multiple windows, multi-level undo, block highliting, and many other
features to the standard vi program.

%description ncurses -l pl
Wersja edytora vim skompilowana z bibliotek± ncurses. W porownaniu z
edytorem vi, ta wersja oferuje dodatkowo pracê z wieloma plikami,
wielopoziomowe operacje cofnij, bloki, pod¶wietlanie sk³adni i wiele
innych usprawnieñ.

%prep
%setup -q -b 1 -b 2
%patch -p1

%build
cd src

LDFLAGS="-static -s"; export LDFLAGS
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--enable-min-features \
	--datadir=/etc \
	--with-tlib=ncurses 
make vim
make xxd/xxd
mv vim vim.static
mv xxd/xxd xxd.static

make distclean
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-max-features \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--enable-gmp \
	--with-tlib=ncurses 
make vim
mv vim vim.ncurses

cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{bin,var/state/vim}
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,share/{vim/{doc,tutor},man/man1}}

install -s src/vim.static $RPM_BUILD_ROOT/bin/vi
install -s src/xxd.static $RPM_BUILD_ROOT/bin/xxd

install -s src/vim.ncurses $RPM_BUILD_ROOT%{_bindir}/vim
install    src/vimtutor	   $RPM_BUILD_ROOT%{_bindir}/vimtutor

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/*.1

install runtime/doc/vim.1 $RPM_BUILD_ROOT%{_mandir}/man1
install runtime/doc/vim.1 $RPM_BUILD_ROOT%{_mandir}/man1/vi.1
install runtime/doc/xxd.1 $RPM_BUILD_ROOT%{_mandir}/man1

install runtime/doc/vimtutor.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo ".so vi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ex.1
echo ".so vi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1
echo ".so vi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rview.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rvim.1

cp -a runtime/macros $RPM_BUILD_ROOT%{_datadir}/vim/macros
cp -a runtime/syntax $RPM_BUILD_ROOT%{_datadir}/vim/syntax
cp -a runtime/tutor/tutor  $RPM_BUILD_ROOT%{_datadir}/vim/tutor/tutor

install runtime/*.vim $RPM_BUILD_ROOT%{_datadir}/vim
install runtime/vimrc_example.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimrc

touch $RPM_BUILD_ROOT%{_bindir}/vi

install runtime/doc/*.txt $RPM_BUILD_ROOT%{_datadir}/vim/doc
install runtime/doc/tags  $RPM_BUILD_ROOT%{_datadir}/vim/doc

ln -sf vi $RPM_BUILD_ROOT/bin/ex
ln -sf vi $RPM_BUILD_ROOT/bin/view
ln -sf vi $RPM_BUILD_ROOT/bin/rview
ln -sf /bin/vi $RPM_BUILD_ROOT%{_bindir}/vi

ln -sf vim $RPM_BUILD_ROOT%{_bindir}/rvim

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/vi

%{_mandir}/man1/vi.1*
%{_mandir}/man1/ex.1*
%{_mandir}/man1/xxd.1*
%{_mandir}/man1/view.1*
%{_mandir}/man1/rview.1*

%dir /var/state/vim

%files ncurses
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/rvim

%{_mandir}/man1/vim.*
%{_mandir}/man1/rvim.*

%files rt
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/vimtutor

%dir %{_datadir}/vim
%{_datadir}/vim/macros

%dir %{_datadir}/vim/syntax
%{_datadir}/vim/syntax/*.vim

%{_datadir}/vim/tutor
%{_datadir}/vim/bugreport.vim
%{_datadir}/vim/filetype.vim
%{_datadir}/vim/scripts.vim
%{_datadir}/vim/mswin.vim
%{_datadir}/vim/ftoff.vim
%{_datadir}/vim/doc

%config %verify(not size mtime md5) %{_datadir}/vim/menu.vim
%config %verify(not size mtime md5) %{_datadir}/vim/vimrc

%changelog
* Sun Jun 13 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
   [5.4k-3]
-  added /var/state/vim -- FHS 2.0
-  build only vim-ncurses, vim-rt & vim (static) packages
-  added default symlink /usr/bin/vi -> /bin/vi

* Mon Jun 07 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [5.4k-2]
- fixed non-static builds

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
- symlink %{_bindir}/vi -> /bin/vi
- doc package moved to %{_datadir}/vim/doc (crazy cpio .. ;)

* Tue Feb  2 1999 Artur Frysiak <wiget@usa.net>
  [5.4d-1d]
- upgraded to 5.4d
- now %{_datadir}/vim/doc is symlink to /usr/doc/%{name}-rt-%{version}
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
- added %{_datadir}/vim/doc/{help.txt,tags} to rt subpackage (was missing)

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
