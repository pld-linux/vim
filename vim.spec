Summary:	Vi IMproved - a Vi clone
Summary(de):	VIsual editor iMproved
Summary(fr):	editeur VIM : VIsual editor iMproved
Summary(pl):	Vi IMproved - klon edytora Vi
Summary(tr):	Geliþmiþ bir vi sürümü
Name:		vim
Version:	5.7
Release:	7
License:	Charityware
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Group(de):	Applikationen/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}-src.tar.gz
Source1:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}-rt.tar.gz
Source2:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}-extra.tar.gz
Source3:	g%{name}-athena.desktop
Source4:	g%{name}-motif.desktop
Source5:	g%{name}-gtk.desktop
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-sysconfdir.patch
Patch3:		%{name}-docpath.patch
Patch4:		%{name}-speed_t.patch
Patch5:		ftp://ftp.home.vim.org/pub/vim/patches/5.7.001
Patch6:		ftp://ftp.home.vim.org/pub/vim/patches/5.7.002
Patch7:		ftp://ftp.home.vim.org/pub/vim/patches/5.7.003
Patch8:		ftp://ftp.home.vim.org/pub/vim/patches/5.7.004
Patch9:		ftp://ftp.home.vim.org/pub/vim/patches/5.7.005
Patch10:	ftp://ftp.home.vim.org/pub/vim/patches/5.7.006
Patch11:	ftp://ftp.home.vim.org/pub/vim/patches/5.7.007
Patch12:	ftp://ftp.home.vim.org/pub/vim/patches/5.7.008
Patch13:	ftp://ftp.home.vim.org/pub/vim/patches/5.7.009
URL:		http://www.vim.org/
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-static
BuildRequires:	glibc-static
BuildRequires:	gpm-devel
%{!?noathena:BuildRequires:	Xaw3d-devel}
%{!?nomotif:BuildRequires:	motif-devel}
%{!?nogtk:BuildRequires:	gtk+-devel}
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-enhanced
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text editor similar to Vi. Important improvements: multiple windows,
multi-level undo, block highliting, and many other.

%description -l de
Der Visual-Editor iMproved ist ein aktualisierter und erweiterter Klon
des vi-Editors, der mit praktisch allen UN*X-Systemen ausgeliefert
wird. Er bringt mehrere Fenster, mehrstufige Widerrufen-Funktion,
Block-Markierung und viele weitere Zusatzfunktionen im Vergleich zum
Standard-vi-Programm.

%description -l fr
L'éditeur VIsuel aMélioré est un clone mis à jour et doté de
caractéristiques supplémentaires de l'éditeur « vi » fourni avec
pratiquement tous les systèmes UN*X. Il ajoute les fenêtres
mutltiples, l'annulation a plusieurs niveaux, la mise en évidence des
blocs et autres caractéristiques au vi de base.

%description -l pl
Edytor tekstu podobny do Vi. Wa¿ne ulepszenia: mo¿liwo¶æ pracy w wielu
wielopoziomowa opcja 'cofnij', bloki, pod¶wietlanie sk³adni i wiele
innych.

%description -l tr
Standart vi metin düzenleyicisinin geliþmiþ hali; daha fazla komut,
birden fazla pencere desteði ve blok iþaretleme yetenekleri içerir.

%package static
Summary:	Staticly linked Vim
Summary(pl):	Statycznie zlinkowany Vim
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Group(de):	Applikationen/Editors/Vim
Provides:	vi
Obsoletes:	vi
Obsoletes:	vim-minimal
 
%description static
Text editor similar to Vi. This version is build with minimal feature
and is installed in /bin as a rescue tool. The installation of this
package is STRONGLY recommended.

%description static -l pl
Edytor tekstu podobny do Vi. Ta wersja zosta³a skompilowana statycznie
i posiada minimaln± ilo¶ci± dodatków. Jest instalowana w /bin jako
narzêdzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, mo¿e on pomóc Tobie uratowaæ system w czasie awarii.

%package rt 
Summary:	Vim runtime files
Summary(pl):	Pliki przydatne edytorowi Vim 
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Group(de):	Applikationen/Editors/Vim
Obsoletes:	vim-common

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for vim. If you want to take advantage of vim more
powerful features, you should install this package.

%description rt -l pl
W tym pakiecie znajdziesz dokumentacjê, makra, pliki konfiguracyjne i
strony podrêcznika dla edytora vim. Je¿eli chcesz korzystaæ z
zaawansowanych mo¿liwo¶ci vim-a, powiniene¶ zainstalowaæ ten pakiet.

%package -n gvim-athena
Summary:	Vim for X Window built with arena
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki Arena
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Group(de):	Applikationen/Editors/Vim
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-X11

%description -n gvim-athena
The classic Unix text editor now also under X Window System! This
version is build with Athena Widget Set.

%description -n gvim-athena -l pl
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem
biblioteki Athena Widget Set.

%package -n gvim-motif
Summary:	Vim for X Window built with Motif
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki Motif
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Group(de):	Applikationen/Editors/Vim
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-X11

%description -n gvim-motif
The classic Unix text editor now also under X Window System! This
version is build with Motif.

%description -n gvim-motif -l pl
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem
biblioteki Motif.

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki GTK
Group:		Applications/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Group(de):	Applikationen/Editors/Vim
Requires:	%{name}-rt = %{version}
Obsoletes:	vim-X11

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This
version is build with GTK.

%description -n gvim-gtk -l pl
Wersja edytora vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem
biblioteki GTK.

%prep
%setup -q -b 1 -b 2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch6 -p2
%patch7 -p2
%patch8 -p2
%patch9 -p2
%patch10 -p2
%patch11 -p2
%patch12 -p2
%patch13 -p2

%build
cd src
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
%{__make} vim
mv -f vim vim.ncurses

%{__make} distclean
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
	--with-tlib=tinfo

%{__make} vim
%{__make} xxd/xxd
mv -f vim vim.static
mv -f xxd/xxd xxd.static

%{?noathena:#}%{__make} distclean
%{?noathena:#}%configure \
	--enable-max-features \
	--enable-gui=athena \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm
%{?noathena:#}%{__make} vim
%{?noathena:#}mv -f vim gvim.athena

%{?nomotif:#}%{__make} distclean
%{?nomotif:#}%configure \
	--enable-max-features \
	--enable-gui=motif \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm
%{?nomotif:#}%{__make} vim
%{?nomotif:#}mv -f vim gvim.motif

%{?nogtk:#}%{__make} distclean
%{?nogtk:#}%configure \
	--enable-max-features \
	--enable-gui=gtk \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm
%{?nogtk:#}%{__make} vim
%{?nogtk:#}mv -f vim gvim.gtk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_var}/lib/vim,%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim/{doc,tutor}} \
	$RPM_BUILD_ROOT{/usr/X11R6/bin,%{_applnkdir}/Development/Editors}

install src/vim.ncurses $RPM_BUILD_ROOT%{_bindir}/vim

install src/vim.static $RPM_BUILD_ROOT/bin/vi
install src/xxd.static $RPM_BUILD_ROOT/bin/xxd

install src/vimtutor $RPM_BUILD_ROOT%{_bindir}/vimtutor

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
mv -f $RPM_BUILD_ROOT%{_datadir}/vim/vimrc_example.vim $RPM_BUILD_ROOT%{_sysconfdir}/vim/vimrc
mv -f $RPM_BUILD_ROOT%{_datadir}/vim/gvimrc_example.vim $RPM_BUILD_ROOT%{_sysconfdir}/vim/gvimrc

install runtime/doc/*.txt $RPM_BUILD_ROOT%{_datadir}/vim/doc
install runtime/doc/tags  $RPM_BUILD_ROOT%{_datadir}/vim/doc

ln -sf vim $RPM_BUILD_ROOT%{_bindir}/rvim

ln -sf vi $RPM_BUILD_ROOT/bin/ex
ln -sf vi $RPM_BUILD_ROOT/bin/view
ln -sf vi $RPM_BUILD_ROOT/bin/rview

%{!?noathena:install src/gvim.athena $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.athena}
%{!?nomotif: install src/gvim.motif $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.motif}
%{!?nogtk:   install src/gvim.gtk $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.gtk}

%{!?nogtk:ln -sf gvim.gtk $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim}
%{!?nogtk:ln -sf gvim $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/rgvim}
%{!?nogtk:ln -sf gvim $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gview}
%{!?nogtk:ln -sf gvim $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/rgview}

%{!?noathena:install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?nomotif: install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?nogtk:   install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

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

%files rt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%dit %{_sysconfdir}/vim
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/menu
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/gvimrc

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

%{!?noathena:%files -n gvim-athena}
%{!?noathena:%defattr(644,root,root,755)}
%{!?noathena:%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.athena}
%{!?noathena:%{_applnkdir}/Development/Editors/gvim-athena.desktop}

%{!?nomotif:%files -n gvim-motif}
%{!?nomotif:%defattr(644,root,root,755)}
%{!?nomotif:%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.motif}
%{!?nomotif:%{_applnkdir}/Development/Editors/gvim-motif.desktop}

%{!?nogtk:%files -n gvim-gtk}
%{!?nogtk:%defattr(644,root,root,755)}
%{!?nogtk:%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.gtk}
%{!?nogtk:%attr(755,root,root) %{_prefix}/X11R6/bin/rgvim}
%{!?nogtk:%attr(755,root,root) %{_prefix}/X11R6/bin/rgview}
%{!?nogtk:%attr(755,root,root) %verify(not link) %{_prefix}/X11R6/bin/gvim}
%{!?nogtk:%{_applnkdir}/Development/Editors/gvim-gtk.desktop}
