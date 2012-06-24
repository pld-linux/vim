#
# Conditional build:
# bcond_off_static	- without static version
# bcond_off_athena	- without Athena Widgets-based gvim
# bcond_off_motif	- without Motif-based gvim
# bcond_off_gtk		- without gtk+-based gvim support
# bcond_off_gnome	- without gnome-based gvim support
#
Summary:	Vi IMproved - a Vi clone
Summary(de):	VIsual editor iMproved
Summary(fr):	editeur VIM : VIsual editor iMproved
Summary(pl):	Vi IMproved - klon edytora Vi
Summary(tr):	Geli�mi� bir vi s�r�m�
Name:		vim
Version:	6.0z
Release:	1
Epoch:		1
License:	Charityware
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Source0:	ftp://ftp.vim.org/pub/editors/vim/unreleased/unix/%{name}-%{version}-src.tar.gz
Source1:	ftp://ftp.vim.org/pub/editors/vim/unreleased/unix/%{name}-%{version}-rt.tar.gz
Source2:	ftp://ftp.vim.org/pub/editors/vim/unreleased/extra/%{name}-%{version}-extra.tar.gz
Source3:	ftp://ftp.vim.org/pub/editors/vim/unreleased/extra/%{name}-%{version}-lang.tar.gz
Source4:	g%{name}-athena.desktop
Source5:	g%{name}-motif.desktop
Source6:	g%{name}-gtk.desktop
Source7:	g%{name}-gnome.desktop
Patch0:		%{name}-sysconfdir.patch
URL:		http://www.vim.org/
BuildRequires:	ncurses-devel
%{!?bcond_off_static:BuildRequires:	ncurses-static}
%{!?bcond_off_static:BuildRequires:	glibc-static}
BuildRequires:	gpm-devel
%{!?bcond_off_athena:BuildRequires:	Xaw3d-devel}
%{!?bcond_off_motif:BuildRequires:	motif-devel}
%{!?bcond_off_gtk:BuildRequires:	gtk+-devel}
%{!?bcond_off_gnome:BuildRequires:	gnome-libs-devel}
%{!?bcond_off_gnome:BuildRequires:	esound-devel}
BuildRequires:	iconv
Requires:	%{name}-rt = %{version}
Requires:	iconv
%{?bcond_off_static:Requires:	%{name}-static = %{version}}
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
L'�diteur VIsuel aM�lior� est un clone mis � jour et dot� de
caract�ristiques suppl�mentaires de l'�diteur � vi � fourni avec
pratiquement tous les syst�mes UN*X. Il ajoute les fen�tres
mutltiples, l'annulation a plusieurs niveaux, la mise en �vidence des
blocs et autres caract�ristiques au vi de base.

%description -l pl
Edytor tekstu podobny do Vi. Wa�ne ulepszenia: mo�liwo�� pracy w wielu
oknach, wielopoziomowa opcja 'cofnij', bloki, pod�wietlanie sk�adni
i wiele innych.

%description -l tr
Standart vi metin d�zenleyicisinin geli�mi� hali; daha fazla komut,
birden fazla pencere deste�i ve blok i�aretleme yetenekleri i�erir.

%package static
Summary:	Staticly linked Vim
Summary(pl):	Statycznie zlinkowany Vim
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Provides:	vi
Obsoletes:	vi
Obsoletes:	vim-minimal
 
%description static
Text editor similar to Vi. This version is build with minimal feature
and is installed in /bin as a rescue tool. The installation of this
package is STRONGLY recommended.

%description static -l pl
Edytor tekstu podobny do Vi. Ta wersja zosta�a skompilowana statycznie
i posiada minimaln� ilo�� dodatk�w. Jest instalowana w /bin jako
narz�dzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, mo�e on pom�c Ci uratowa� system w czasie awarii.

%package rt 
Summary:	Vim runtime files
Summary(pl):	Pliki przydatne edytorowi Vim 
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	mktemp
Obsoletes:	vim-common

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for vim. If you want to take advantage of vim more
powerful features, you should install this package.

%description rt -l pl
W tym pakiecie znajdziesz dokumentacj�, makra, pliki konfiguracyjne i
strony podr�cznika dla edytora vim. Je�eli chcesz korzysta� z
zaawansowanych mo�liwo�ci vim-a, powiniene� zainstalowa� ten pakiet.

%package -n gvim-athena
Summary:	Vim for X Window built with Athena
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki Athena
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-athena
The classic Unix text editor now also under X Window System! This
version is build with Athena Widget Set.

%description -n gvim-athena -l pl
Wersja edytora Vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki Athena Widget Set.

%package -n gvim-motif
Summary:	Vim for X Window built with Motif
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki Motif
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-motif
The classic Unix text editor now also under X Window System! This
version is build with Motif.

%description -n gvim-motif -l pl
Wersja edytora Vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki Motif.

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki GTK
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This
version is build with GTK and GNOME.

%description -n gvim-gtk -l pl
Wersja edytora vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki GTK oraz GNOME.

%package -n gvim-gnome
Summary:	Vim for X Window built with gnome
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki GNOME
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gnome
The classic Unix text editor now also under X Window System! This
version is build with GNOME.

%description -n gvim-gnome -l pl
Wersja edytora vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki GNOME.

%prep
%setup -q -b 1 -b 2 -b 3 -n %{name}%(echo %{version} | sed -e "s#\.##g")
%patch0 -p1

%build
cd src
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-rubyinterp \
	--enable-cscope \
	--enable-gmp \
	--enable-max-features \
	--enable-multibyte \
	--with-tlib=ncurses \
	--enable-nls

%{__make} vim
mv -f vim vim.ncurses

%{?bcond_off_static:#}%{__make} distclean
%{?bcond_off_static:#}%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-multibyte \
	--enable-min-features \
	--with-tlib=tinfo \
	--disable-nls

%{?bcond_off_static:#}%{__make} vim
%{__make} xxd/xxd
%{?bcond_off_static:#}mv -f vim vim.static
mv -f xxd/xxd xxd.static

%{?bcond_off_athena:#}%{__make} distclean
%{?bcond_off_athena:#}%configure \
	--enable-max-features \
	--enable-gui=athena \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-rubyinterp \
	--enable-cscope \
	--enable-fontset \
	--disable-gpm \
	--without-gnome \
	--enable-nls
%{?bcond_off_athena:#}%{__make} vim
%{?bcond_off_athena:#}mv -f vim gvim.athena

%{?bcond_off_motif:#}%{__make} distclean
%{?bcond_off_motif:#}%configure \
	--enable-max-features \
	--enable-gui=motif \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-rubyinterp \
	--enable-multibyte \
	--enable-cscope \
	--enable-fontset \
	--disable-gpm \
	--without-gnome \
	--enable-nls
%{?bcond_off_motif:#}%{__make} vim
%{?bcond_off_motif:#}mv -f vim gvim.motif

%{?bcond_off_gtk:#}%{__make} distclean
%{?bcond_off_gtk:#}%configure \
	--enable-max-features \
	--enable-gui=gtk \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-rubyinterp \
	--disable-gpm \
	--enable-cscope \
	--enable-fontset \
	--enable-nls
%{?bcond_off_gtk:#}%{__make} vim
%{?bcond_off_gtk:#}mv -f vim gvim.gtk

%{?bcond_off_gnome:#}%{__make} distclean
%{?bcond_off_gnome:#}%configure \
	--enable-max-features \
	--enable-gui=gnome \
	--with-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-rubyinterp \
	--disable-gpm \
	--enable-cscope \
	--enable-fontset \
	--enable-nls
%{?bcond_off_gnome:#}%{__make} vim
%{?bcond_off_gnome:#}mv -f vim gvim.gnome

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_var}/lib/vim,%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim} \
	$RPM_BUILD_ROOT{%{_prefix}/X11R6/bin,%{_applnkdir}/Development/Editors}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_bindir}/*

%{!?bcond_off_static:install src/vim.ncurses	$RPM_BUILD_ROOT%{_bindir}/vim}
%{?bcond_off_static:install src/vim.ncurses	$RPM_BUILD_ROOT/bin/vi}
%{!?bcond_off_static:install src/vim.static	$RPM_BUILD_ROOT/bin/vi}
%{?bcond_off_static:ln -sf /bin/vi		$RPM_BUILD_ROOT%{_bindir}/vim}
install src/xxd.static				$RPM_BUILD_ROOT/bin/xxd
install src/vimtutor				$RPM_BUILD_ROOT%{_bindir}/vimtutor

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/*.1

install runtime/doc/vim.1 $RPM_BUILD_ROOT%{_mandir}/man1
install runtime/doc/xxd.1 $RPM_BUILD_ROOT%{_mandir}/man1

install runtime/doc/vimtutor.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ex.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rview.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rvim.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vi.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1

mv -f $RPM_BUILD_ROOT%{_datadir}/vim/v*/vimrc_example.vim $RPM_BUILD_ROOT%{_sysconfdir}/vim/vimrc
mv -f $RPM_BUILD_ROOT%{_datadir}/vim/v*/gvimrc_example.vim $RPM_BUILD_ROOT%{_sysconfdir}/vim/gvimrc

ln -sf vim $RPM_BUILD_ROOT%{_bindir}/rvim
ln -sf vi  $RPM_BUILD_ROOT/bin/ex
ln -sf vi  $RPM_BUILD_ROOT/bin/view
ln -sf vi  $RPM_BUILD_ROOT/bin/rview

%{!?bcond_off_athena:install src/gvim.athena	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.athena}
%{!?bcond_off_motif: install src/gvim.motif	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.motif}
%{!?bcond_off_gtk:   install src/gvim.gtk	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.gtk}
%{!?bcond_off_gnome: install src/gvim.gnome	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.gnome}

%{!?bcond_off_gtk:ln -sf gvim.gtk		$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim}
%{!?bcond_off_gtk:ln -sf gvim			$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/rgvim}
%{!?bcond_off_gtk:ln -sf gvim			$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gview}
%{!?bcond_off_gtk:ln -sf gvim			$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/rgview}

%{!?bcond_off_athena:install %{SOURCE4}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?bcond_off_motif: install %{SOURCE5}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?bcond_off_gtk:   install %{SOURCE6} 	$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?bcond_off_gnome: install %{SOURCE7}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}

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
%dir %{_sysconfdir}/vim
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/gvimrc

%dir %{_var}/lib/vim

%dir %{_datadir}/vim
%dir %{_datadir}/vim/v*
%{_datadir}/vim/v*/doc
%{_datadir}/vim/v*/ftplugin
%{_datadir}/vim/v*/indent
%{_datadir}/vim/v*/keymap
%dir %{_datadir}/vim/v*/lang
%{_datadir}/vim/v*/lang/README*
%lang(af) %{_datadir}/vim/v*/lang/*af*
%lang(cs) %{_datadir}/vim/v*/lang/*cs*
%lang(de) %{_datadir}/vim/v*/lang/*de*
%lang(es) %{_datadir}/vim/v*/lang/es
%lang(es) %{_datadir}/vim/v*/lang/*es_es*
%lang(es) %{_datadir}/vim/v*/lang/*spanish*
%lang(fr) %{_datadir}/vim/v*/lang/*fr*
%lang(hu) %{_datadir}/vim/v*/lang/*hu*
%lang(nl) %{_datadir}/vim/v*/lang/*nl*
%lang(it) %{_datadir}/vim/v*/lang/*it*
%lang(ja) %{_datadir}/vim/v*/lang/*ja*
%lang(ko) %{_datadir}/vim/v*/lang/*ko*
%lang(pl) %{_datadir}/vim/v*/lang/*pl*
%lang(zh_TW) %{_datadir}/vim/v*/lang/*zh*
%{_datadir}/vim/v*/macros
%{_datadir}/vim/v*/plugin
%{_datadir}/vim/v*/syntax
%{_datadir}/vim/v*/tutor
%{_datadir}/vim/v*/*.vim

%{_mandir}/man1/vim.*
%{_mandir}/man1/rvim.*

%{!?bcond_off_athena:%files -n gvim-athena}
%{!?bcond_off_athena:%defattr(644,root,root,755)}
%{!?bcond_off_athena:%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.athena}
%{!?bcond_off_athena:%{_applnkdir}/Development/Editors/gvim-athena.desktop}

%{!?bcond_off_motif:%files -n gvim-motif}
%{!?bcond_off_motif:%defattr(644,root,root,755)}
%{!?bcond_off_motif:%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.motif}
%{!?bcond_off_motif:%{_applnkdir}/Development/Editors/gvim-motif.desktop}

%{!?bcond_off_gtk:%files -n gvim-gtk}
%{!?bcond_off_gtk:%defattr(644,root,root,755)}
%{!?bcond_off_gtk:%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.gtk}
%{!?bcond_off_gtk:%attr(755,root,root) %{_prefix}/X11R6/bin/rgvim}
%{!?bcond_off_gtk:%attr(755,root,root) %{_prefix}/X11R6/bin/rgview}
%{!?bcond_off_gtk:%attr(755,root,root) %verify(not link) %{_prefix}/X11R6/bin/gvim}
%{!?bcond_off_gtk:%{_applnkdir}/Development/Editors/gvim-gtk.desktop}

%{!?bcond_off_gnome:%files -n gvim-gnome}
%{!?bcond_off_gnome:%defattr(644,root,root,755)}
%{!?bcond_off_gnome:%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.gnome}
%{!?bcond_off_gnome:%{_applnkdir}/Development/Editors/gvim-gnome.desktop}
