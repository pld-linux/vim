Summary:	Vim static
Summary(pl):	Vim skompilowany statycznie
Name:		vim
Version:	5.4d
Release:	1d
#######		ftp://ftp.nl.vim.org/pub/vim/unreleased/unix
Source:		%{name}-%{version}-src.tar.gz
Source1:	%{name}-%{version}-rt.tar.gz
#######		ftp://ftp.nl.vim.org/pub/vim/unreleased/extra
Source2:	%{name}-%{version}-extra.tar.gz
Source3:	gvim.wmconfig
Patch:		%{name}-hold_gui_events.patch
Patch1:		%{name}-clip.patch
Copyright:	GPL
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
URL:		http://www.vim.org/
Buildroot:	/tmp/%{name}-%{version}-root

%description
The classic Unix text editor. This version is build with minimal
feature and is installed in /bin as a rescue tool. The installation of
this package is STRONGLY recommended.

%description -l pl
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

#%package	slang
#Summary:	Vim 5.3 built with slang
#Summary(pl):	Vim 5.3 korzystaj±cy z bibliotek Slang
#Group:		Applications/Editors/Vim
#Group(pl):	Alikacje/Edytory/Vim
#Obsoletes:	vim-ncurses

#%description slang
#The classic Unix text editor build with slang library. It adds
#multiple windows, multi-level undo, block highliting, and many other
#features to the standard vi program.

#%description slang -l pl
#Wersja edytora vim skompilowana z bibliotek± slang. W porownaniu z
#edytorem vi, ta wersja oferuje dodatkowo pracê z wieloma plikami,
#wielopoziomowe operacje cofnij, bloki, pod¶wietlanie sk³adni i wiele
#innych usprawnieñ.

%package	ncurses 
Summary:	Vim built with ncurses
Summary(pl):	Vim korzystaj±cy z bibliotek ncurses
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	ncurses
Obsoletes:	vim-slang

%description ncurses
The classic Unix text editor build with ncurses library. It adds
multiple windows, multi-level undo, block highliting, and many other
features to the standard vi program.

%description ncurses -l pl
Wersja edytora vim skompilowana z bibliotek± ncurses. W porownaniu z
edytorem vi, ta wersja oferuje dodatkowo pracê z wieloma plikami,
wielopoziomowe operacje cofnij, bloki, pod¶wietlanie sk³adni i wiele
innych usprawnieñ.

%package	athena
Summary:	Vim built with X11 and athena support
Summary(pl):	Vim pod X-Window korzystaj±cy z Athena Widget Set
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Obsoletes:	vim-lesstif
Obsoletes:	vim-gtk

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
Requires:	lesstif
Obsoletes:	vim-athena
Obsoletes:	vim-gtk

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
Requires:	gtk+
Obsoletes:	vim-athena
Obsoletes:	vim-lesstif

%description gtk
The classic Unix text editor now also under X Window System!
This version is build with gtk.

%description gtk -l pl
Wersja edytora vim pracuj±ca w graficznym ¶rodowisku X Window
z wykorzystaniem gtk.

%prep
%setup -q  -b 1 -b 2
%patch 
%patch1 -p1

%build
cd src

LDFLAGS=-static CFLAGS=-O ./configure --disable-gui --without-x \
--disable-perlinterp --disable-pythoninterp --disable-tclinterp \
--disable-cscope --enable-min-features \
--datadir=/etc --with-tlib=termcap --prefix=/usr
make vim
make xxd/xxd
mv vim vim.termcap
mv xxd/xxd xxd.termcap

#make distclean
#LDFLAGS=-s CFLAGS="$RPM_OPT_FLAGS" ./configure --disable-gui --without-x \
#--disable-perlinterp --disable-pythoninterp --disable-tclinterp \
#--disable-cscope --with-tlib=slang --prefix=/usr
#make
#mv src/vim src/vim.slang

make distclean
LDFLAGS=-s CFLAGS="$RPM_OPT_FLAGS" ./configure --disable-gui --without-x \
--disable-perlinterp --disable-pythoninterp --disable-tclinterp \
--disable-cscope --with-tlib=ncurses --prefix=/usr
make vim
mv vim vim.ncurses

make distclean
LDFLAGS=-s CFLAGS="$RPM_OPT_FLAGS" ./configure --enable-gui=athena --with-x \
--disable-perlinterp --disable-pythoninterp --disable-tclinterp \
--disable-cscope --with-tlib=termcap --prefix=/usr
make vim
mv vim vim.athena

make distclean
LDFLAGS=-s CFLAGS="$RPM_OPT_FLAGS" ./configure --enable-gui=motif --with-x \
--disable-perlinterp --disable-pythoninterp --disable-tclinterp \
--disable-cscope --with-tlib=termcap --prefix=/usr
make vim
mv vim vim.lesstif

make distclean
LDFLAGS=-s CFLAGS="$RPM_OPT_FLAGS" ./configure --enable-gui=gtk --with-x \
--disable-perlinterp --disable-pythoninterp --disable-tclinterp \
--disable-cscope --with-tlib=termcap --prefix=/usr
make vim
mv vim vim.gtk

cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -d $RPM_BUILD_ROOT/bin
install -d $RPM_BUILD_ROOT/usr/{bin,X11R6/bin,share/vim,man/man1}

# make prefix=$RPM_BUILD_ROOT/usr install

install -s src/vim.termcap $RPM_BUILD_ROOT/bin/vi
install -s src/xxd.termcap $RPM_BUILD_ROOT/bin/xxd

#install -s src/vim.slang $RPM_BUILD_ROOT/usr/bin/vim.slang

install -s src/vim.ncurses $RPM_BUILD_ROOT/usr/bin/vim.ncurses
install -s src/vim.athena  $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.athena
install -s src/vim.lesstif $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.lesstif
install -s src/vim.gtk     $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.gtk

rm -f $RPM_BUILD_ROOT/usr/man/man1/*.1

install runtime/doc/vim.1 $RPM_BUILD_ROOT/usr/man/man1
install runtime/doc/xxd.1 $RPM_BUILD_ROOT/usr/man/man1

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
cp -a runtime/tutor  $RPM_BUILD_ROOT/usr/share/vim/tutor

install runtime/*.vim $RPM_BUILD_ROOT/usr/share/vim
install runtime/vimrc_example $RPM_BUILD_ROOT/usr/share/vim/vimrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/wmconfig/gvim

touch $RPM_BUILD_ROOT/usr/bin/vim $RPM_BUILD_ROOT/usr/X11R6/bin/gvim

ln -sf ../../doc/%{name}-rt-%{version} $RPM_BUILD_ROOT/usr/share/vim/doc

ln -sf vi $RPM_BUILD_ROOT/bin/ex
ln -sf vi $RPM_BUILD_ROOT/bin/view
ln -sf vi $RPM_BUILD_ROOT/bin/rview

ln -sf vim $RPM_BUILD_ROOT/usr/bin/rvim

ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/rgvim
ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/gview
ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/rgview

bzip2 -9 $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

#%post slang
#ln -sf /usr/bin/vim.slang /usr/bin/vim

%post ncurses
ln -sf /usr/bin/vim.ncurses /usr/bin/vim

%post athena
ln -sf /usr/X11R6/bin/gvim.athena /usr/X11R6/bin/gvim

%post lesstif 
ln -sf /usr/X11R6/bin/gvim.lesstif /usr/X11R6/bin/gvim

%post gtk
ln -sf /usr/X11R6/bin/gvim.gtk /usr/X11R6/bin/gvim

%files
%attr(755,root,root) /bin/*

#%files slang
#%attr(711,root,root) /usr/bin/vim.slang
#%attr(711,root,root) /usr/bin/rvim
#%attr(711,root,root) %ghost /usr/bin/vim

%files ncurses
%attr(755,root,root) /usr/bin/vim.ncurses
%attr(755,root,root) /usr/bin/rvim
%attr(755,root,root) %ghost /usr/bin/vim

%files athena
%attr(755,root,root) /usr/X11R6/bin/gvim.athena
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/gvim
%attr(755,root,root) %ghost /usr/X11R6/bin/gvim

%files lesstif 
%attr(755,root,root) /usr/X11R6/bin/gvim.lesstif
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/gvim
%attr(755,root,root) %ghost /usr/X11R6/bin/gvim

%files gtk
%attr(755,root,root) /usr/X11R6/bin/gvim.gtk
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/gvim
%attr(755,root,root) %ghost /usr/X11R6/bin/gvim

%files rt
%defattr(644,root,root,755)
%doc runtime/doc/*.txt runtime/doc/tags
%attr(644,root,man) /usr/man/man1/*

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
- fixed etcdir in vim-ststic subpackage.

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
