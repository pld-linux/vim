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
