Summary:	Vi IMproved - a Vi clone
Summary(pl):	Vi IMproved - klon edytora Vi
Name:		vim
Version:	5.6
Release:	3
Copyright:	Charityware
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
URL:		http://www.vim.org
Source0:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}-src.tar.gz
Source1:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}-rt.tar.gz
Source2:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}-extra.tar.gz
Source3:	gvim.desktop
Patch:		vim-fhs.patch
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-static
BuildRequires:	gpm-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	lesstif-devel
BuildRequires:	gtk+-devel
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-enhanced
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text editor similar to Vi. Important improvements: multiple windows, 
multi-level undo, block highliting, and many other.   

%description -l pl
Edytor tekstu podobny do Vi. Wa¿ne ulepszenia: mo¿liwo¶æ pracy w wielu 
wielopoziomowa opcja 'cofnij', bloki, pod¶wietlanie sk³adni i wiele innych. 
  
%package static
Summary:	Staticly linked Vim
Summary(pl):	Statycznie zlinkowany Vim
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Provides:       vi
Obsoletes:      vi
Obsoletes:	vim-minimal
 
%description static
Text editor similar to Vi. This version is build with minimal feature  and 
is installed in /bin as a rescue tool. The installation of this package  is 
STRONGLY recommended.      

%description static -l pl
Edytor tekstu podobny do Vi. Ta wersja zosta³a skompilowana statycznie i 
posiada minimaln± ilo¶ci± dodatków. Jest instalowana w /bin jako narzêdzie 
dla administratora. Instalacja tego pakietu jest MOCNO zalecana, mo¿e on 
pomóc Tobie uratowaæ system w czasie awarii.      

%package rt 
Summary:	Vim runtime files
Summary(pl):	Pliki przydatne edytorowi Vim 
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Obsoletes:	vim-common

%description rt
This package contains macros, documentation, syntax configuration and  
manual pages for vim. If you want to take advantage of vim more powerful  
features, you should install this package.      

%description rt -l pl
W tym pakiecie znajdziesz dokumentacjê, makra, pliki konfiguracyjne i 
strony podrêcznika dla edytora vim. Je¿eli chcesz korzystaæ z 
zaawansowanych mo¿liwo¶ci vim-a, powiniene¶ zainstalowaæ ten pakiet.   

%package -n gvim-athena
Summary:	Vim for X Window built with LessTif
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki LessTif
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-X11

%description -n gvim-athena
The classic Unix text editor now also under X Window System! This version 
is build with Athena Widget Set.   

%description -n gvim-athena -l pl
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem 
biblioteki Athena Widget Set.   

%package -n gvim-lesstif
Summary:	Vim for X Window built with LessTif
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki LessTif
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-X11

%description -n gvim-lesstif
The classic Unix text editor now also under X Window System! This version 
is build with LessTif.   

%description -n gvim-lesstif -l pl
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem 
biblioteki LessTif.   

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki GTK
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-X11

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This version 
is build with GTK.   

%description -n gvim-gtk -l pl
Wersja edytora vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem 
biblioteki GTK.    

%prep
%setup -q -b 1 -b 2
%patch -p1

%build
cd src

LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--enable-gmp \
	--enable-max-features \
	--with-tlib=ncurses 
make vim
mv vim vim.ncurses

make distclean
LDFLAGS="-static -s"; export LDFLAGS
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-multibyte \
	--enable-min-features \
	--datadir=/etc \
	--with-tlib=tinfo
make vim
make xxd/xxd
mv vim vim.static
mv xxd/xxd xxd.static

make distclean
LDFLAGS="-s"; export LDFLAGS
%configure \
        --enable-max-features \
        --enable-gui=athena \
        --with-x \
        --disable-perlinterp \
        --disable-pythoninterp \
        --disable-tclinterp \
        --disable-cscope \
        --disable-gpm
make vim
mv vim gvim.athena

make distclean
LDFLAGS="-s"; export LDFLAGS
%configure \
        --enable-max-features \
        --enable-gui=motif \
        --with-x \
        --disable-perlinterp \
        --disable-pythoninterp \
        --disable-tclinterp \
        --disable-cscope \
        --disable-gpm
make vim
mv vim gvim.lesstif
 
make distclean
LDFLAGS="-s"; export LDFLAGS
%configure \
        --enable-max-features \
        --enable-gui=gtk \
        --with-x \
        --disable-perlinterp \
        --disable-pythoninterp \
        --disable-tclinterp \
        --disable-cscope \
        --disable-gpm
make vim
mv vim gvim.gtk

cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_var}/lib/vim,%{_sysconfdir},%{_prefix}/{bin,share/{vim/{doc,tutor},man/man1}}} \
	$RPM_BUILD_ROOT/{bin,usr/X11R6/{bin,share/applnk/Applications/Editors}}

install -s src/vim.ncurses $RPM_BUILD_ROOT%{_bindir}/vim

install -s src/vim.static  $RPM_BUILD_ROOT/bin/vi
install -s src/xxd.static  $RPM_BUILD_ROOT/bin/xxd

install -s src/gvim.athena  $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.athena
install -s src/gvim.lesstif $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.lesstif
install -s src/gvim.gtk     $RPM_BUILD_ROOT/usr/X11R6/bin/gvim.gtk
 
install    src/vimtutor	   $RPM_BUILD_ROOT%{_bindir}/vimtutor

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/*.1

install runtime/doc/vim.1 $RPM_BUILD_ROOT%{_mandir}/man1
install runtime/doc/xxd.1 $RPM_BUILD_ROOT%{_mandir}/man1

install runtime/doc/vimtutor.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ex.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rview.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rvim.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vi.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1

cp -a runtime/macros $RPM_BUILD_ROOT%{_datadir}/vim/macros
cp -a runtime/syntax $RPM_BUILD_ROOT%{_datadir}/vim/syntax
cp -a runtime/tutor/tutor  $RPM_BUILD_ROOT%{_datadir}/vim/tutor/tutor

install runtime/*.vim $RPM_BUILD_ROOT%{_datadir}/vim
mv $RPM_BUILD_ROOT%{_datadir}/vim/vimrc_example.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimrc
mv $RPM_BUILD_ROOT%{_datadir}/vim/gvimrc_example.vim $RPM_BUILD_ROOT%{_datadir}/vim/gvimrc

install runtime/doc/*.txt $RPM_BUILD_ROOT%{_datadir}/vim/doc
install runtime/doc/tags  $RPM_BUILD_ROOT%{_datadir}/vim/doc

touch $RPM_BUILD_ROOT/usr/X11R6/bin/gvim

ln -sf vim $RPM_BUILD_ROOT%{_bindir}/rvim

ln -sf vi $RPM_BUILD_ROOT/bin/ex
ln -sf vi $RPM_BUILD_ROOT/bin/view
ln -sf vi $RPM_BUILD_ROOT/bin/rview

ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/rgvim
ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/gview
ln -sf gvim $RPM_BUILD_ROOT/usr/X11R6/bin/rgview
 
install %{SOURCE3} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Applications/Editors

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%post -n gvim-athena
ln -sf /usr/X11R6/bin/gvim.athena /usr/X11R6/bin/gvim

%post -n gvim-lesstif
ln -sf /usr/X11R6/bin/gvim.lesstif /usr/X11R6/bin/gvim

%post -n gvim-gtk
ln -sf /usr/X11R6/bin/gvim.gtk /usr/X11R6/bin/gvim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/rvim

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*

%{_mandir}/man1/vi.1*
%{_mandir}/man1/ex.1*
%{_mandir}/man1/xxd.1*
%{_mandir}/man1/view.1*
%{_mandir}/man1/rview.1*

%files -n gvim-athena
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/gvim.athena
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
%attr(755,root,root) %verify(not link) /usr/X11R6/bin/gvim
/usr/X11R6/share/applnk/Applications/Editors/gvim.desktop

%files -n gvim-lesstif
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/gvim.lesstif
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
%attr(755,root,root) %verify(not link) /usr/X11R6/bin/gvim
/usr/X11R6/share/applnk/Applications/Editors/gvim.desktop

%files -n gvim-gtk
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/gvim.gtk
%attr(755,root,root) /usr/X11R6/bin/rgvim
%attr(755,root,root) /usr/X11R6/bin/rgview
%attr(755,root,root) %verify(not link) /usr/X11R6/bin/gvim
/usr/X11R6/share/applnk/Applications/Editors/gvim.desktop

%files rt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%config(noreplace) %verify(not size mtime md5) %{_datadir}/vim/menu.vim
%config(noreplace) %verify(not size mtime md5) %{_datadir}/vim/vimrc
%config(noreplace) %verify(not size mtime md5) %{_datadir}/vim/gvimrc

%dir %{_var}/lib/vim

%dir %{_datadir}/vim
%{_datadir}/vim/doc
%{_datadir}/vim/macros
%{_datadir}/vim/syntax
%{_datadir}/vim/tutor

%{_datadir}/vim/bugreport.vim
%{_datadir}/vim/filetype.vim
%{_datadir}/vim/scripts.vim
%{_datadir}/vim/mswin.vim
%{_datadir}/vim/ftoff.vim
%{_datadir}/vim/optwin.vim

%{_mandir}/man1/vim.*
%{_mandir}/man1/rvim.*
