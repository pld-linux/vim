#
# Conditional build:
# _without_static	- without static version
# _without_athena	- without Athena Widgets-based gvim. DOESN'T WORK.
# _without_motif	- without Motif-based gvim
# _without_gtk		- without gtk+-based gvim support
# _without_gnome	- without gnome-based gvim support
# _with_ispell		- with spell checking (non-standard feature; disables RIGHTLEFT and FKMAP)
#
Summary:	Vi IMproved - a Vi clone
Summary(de):	VIsual editor iMproved
Summary(fr):	editeur VIM : VIsual editor iMproved
Summary(pl):	Vi IMproved - klon edytora Vi
Summary(tr):	Geliþmiþ bir vi sürümü
Name:		vim
Version:	6.0
Release:	2
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Source0:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{version}-lang.tar.gz
#Source2:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{version}-extra.tar.gz
Source3:	g%{name}-athena.desktop
Source4:	g%{name}-motif.desktop
Source5:	g%{name}-gtk.desktop
Source6:	g%{name}-gnome.desktop
#packed from	ftp://ftp.vim.org/pub/editors/vim/patches/6.0.*
Source7:	%{name}-patches-6.0.101.tar.bz2
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-phphighlight.patch
Patch3:		%{name}-paths.patch
Patch4:		%{name}-ispell.patch
URL:		http://www.vim.org/
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
%{!?_without_athena:BuildRequires:	Xaw3d-devel}
%{!?_without_gnome:BuildRequires:	esound-devel}
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_gtk:BuildRequires:	gtk+-devel}
%{!?_without_motif:BuildRequires:	motif-devel}
%{!?_without_static:BuildRequires:	glibc-static}
%{!?_without_static:BuildRequires:	ncurses-static}
Requires:	%{name}-rt = %{version}
%{?_without_static:Requires:	%{name}-static = %{version}}
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
oknach, wielopoziomowa opcja 'cofnij', bloki, pod¶wietlanie sk³adni
i wiele innych.

%description -l tr
Standart vi metin düzenleyicisinin geliþmiþ hali; daha fazla komut,
birden fazla pencere desteði ve blok iþaretleme yetenekleri içerir.

%package -n xxd
Summary:	Utility to convert files to hexdump or do the reverse
Summary(pl):	Narzêdzie do zamiany plików na postaæ szesnastkow± i odwrotnie
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim

%description -n xxd
xxd creates a hex dump of a given file or standard input. It can also
convert a hex dump back to its original binary form. Like uuencode and
uudecode it allows the transmission of binary data in a `mail-safe'
ASCII representation, but has the advantage of decoding to standard
output. Moreover, it can be used to perform binary file patching.

%description -n xxd -l pl
xxd tworzy szesnastkowy zapis pliku podanego na standardowe wej¶cie.
Mo¿e tak¿e przekonwertowaæ taki zapis na oryginaln±, binarn± postaæ.
Podobnie jak uuencode i uudecode pozwala na przesy³anie danych
binarnych w postaci ASCII, ale ma mo¿liwo¶æ dekodowania na standardowe
wyj¶cie. Co wiêcej, mo¿e byæ u¿yty do modyfikowania plików binarnych.

%package static
Summary:	Statically linked Vim
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
Edytor tekstu podobny do Vi. Ta wersja zosta³a zlinkowana statycznie
i posiada minimaln± ilo¶æ dodatków. Jest instalowana w /bin jako
narzêdzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, mo¿e on pomóc Ci uratowaæ system w czasie awarii.

%package rt
Summary:	Vim runtime files
Summary(pl):	Pliki przydatne edytorowi Vim
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	mktemp
Requires:	which
Obsoletes:	vim-common

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for Vim. If you want to take advantage of Vim more
powerful features, you should install this package.

%description rt -l pl
W tym pakiecie znajdziesz dokumentacjê, makra, pliki konfiguracyjne i
strony podrêcznika dla edytora Vim. Je¿eli chcesz korzystaæ z
zaawansowanych mo¿liwo¶ci Vima, powiniene¶ zainstalowaæ ten pakiet.

%package -n gvim-athena
Summary:	Vim for X Window built with Athena
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki Athena
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
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem
biblioteki Athena Widget Set.

%package -n gvim-motif
Summary:	Vim for X Window built with Motif
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki Motif
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
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem
biblioteki Motif.

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki GTK
Group:		Applications/Editors/Vim
Group(de):	Applikationen/Editors/Vim
Group(pl):	Aplikacje/Edytory/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This
version is build with GTK.

%description -n gvim-gtk -l pl
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem
biblioteki GTK.

%package -n gvim-gnome
Summary:	Vim for X Window built with gnome
Summary(pl):	Vim dla X Window korzystaj±cy z biblioteki GNOME
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
Wersja edytora Vim pracuj±ca w ¶rodowisku X Window z wykorzystaniem
bibliotek GNOME.

%prep
%setup -q -b1 -a7 -n %{name}%(echo %{version} | sed -e "s#\.##g")
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{?_with_ispell:%patch4 -p1}

# these patches are to "extra" package which we don't need (nor use)
rm -f patches/6.0.{027,048,053,064,070,073,093}
# apply the rest of officual patches
for f in patches/6.0.* ; do
	echo "Applying official patch `basename $f` ..."
	patch -s -p0 < $f
done

%build
cd src
autoconf
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-rubyinterp \
	--enable-cscope \
	--enable-gpm \
	--with-features=huge \
	--enable-multibyte \
	--with-tlib=ncurses \
	--enable-nls

%{__make} vim
mv -f vim vim.ncurses

%{__make} xxd/xxd

%if %{!?_without_static:1}%{?_without_static:0}
%{__make} distclean
LDFLAGS="%{rpmldflags} -static"
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-multibyte \
	--with-features=small \
	--with-tlib=tinfo \
	--disable-nls

%{__make} vim
mv -f vim vim.static
%endif

%if %{!?_without_athena:1}%{?_without_athena:0}
%{__make} distclean
LDFLAGS="%{rpmldflags}"
%configure \
	--with-features=huge \
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
%{__make} vim
mv -f vim gvim.athena
%endif

%if %{!?_without_motif:1}%{?_without_motif:0}
%{__make} distclean
%configure \
	--with-features=huge \
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
%{__make} vim
mv -f vim gvim.motif
%endif

%if %{!?_without_gtk:1}%{?_without_gtk:0}
%{__make} distclean
%configure \
	--with-features=huge \
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
%{__make} vim
mv -f vim gvim.gtk
%endif

%if %{!?_without_gnome:1}%{?_without_gnome:0}
%{__make} distclean
%configure \
	--with-features=huge \
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
%{__make} vim
mv -f vim gvim.gnome
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim} \
	$RPM_BUILD_ROOT{%{_prefix}/X11R6/bin,%{_applnkdir}/Development/Editors}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_bindir}/*

%{!?_without_static:install src/vim.ncurses	$RPM_BUILD_ROOT%{_bindir}/vim}
%{?_without_static:install src/vim.ncurses	$RPM_BUILD_ROOT/bin/vi}
%{!?_without_static:install src/vim.static	$RPM_BUILD_ROOT/bin/vi}
%{?_without_static:ln -sf /bin/vi		$RPM_BUILD_ROOT%{_bindir}/vim}
install src/xxd/xxd				$RPM_BUILD_ROOT%{_bindir}/xxd
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

%{!?_without_athena:install src/gvim.athena	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.athena}
%{!?_without_motif: install src/gvim.motif	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.motif}
%{!?_without_gtk:   install src/gvim.gtk	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.gtk}
%{!?_without_gnome: install src/gvim.gnome	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim.gnome}

%{!?_without_gtk:ln -sf gvim.gtk		$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gvim}
%{!?_without_gtk:ln -sf gvim			$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/rgvim}
%{!?_without_gtk:ln -sf gvim			$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gview}
%{!?_without_gtk:ln -sf gvim			$RPM_BUILD_ROOT%{_prefix}/X11R6/bin/rgview}

%{!?_without_athena:install %{SOURCE3}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?_without_motif: install %{SOURCE4}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?_without_gtk:   install %{SOURCE5}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?_without_gnome: install %{SOURCE6}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/rvim

%files -n xxd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxd
%{_mandir}/man1/xxd.1*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*

%{_mandir}/man1/vi.1*
%{_mandir}/man1/ex.1*
%{_mandir}/man1/view.1*
%{_mandir}/man1/rview.1*

%files rt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%dir %{_sysconfdir}/vim
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/gvimrc

%dir %{_datadir}/vim
%dir %{_datadir}/vim/v*
%{_datadir}/vim/v*/doc
%{_datadir}/vim/v*/ftplugin
%{_datadir}/vim/v*/indent
%{_datadir}/vim/v*/keymap
%dir %{_datadir}/vim/v*/lang
%{_datadir}/vim/v*/lang/README*

%lang(af) %{_datadir}/vim/v*/lang/af
%lang(de) %{_datadir}/vim/v*/lang/de
%lang(es) %{_datadir}/vim/v*/lang/es
%lang(fr) %{_datadir}/vim/v*/lang/fr
%lang(it) %{_datadir}/vim/v*/lang/it
%lang(ja) %{_datadir}/vim/v*/lang/ja*
%lang(ko) %{_datadir}/vim/v*/lang/ko
%lang(pl) %{_datadir}/vim/v*/lang/pl
%lang(sk) %{_datadir}/vim/v*/lang/sk
#%lang(tr) %{_datadir}/vim/v*/lang/tr
%lang(uk) %{_datadir}/vim/v*/lang/uk
%lang(zh_CN) %{_datadir}/vim/v*/lang/zh_CN*
%lang(zh_TW) %{_datadir}/vim/v*/lang/zh_TW

%lang(af) %{_datadir}/vim/v*/lang/menu_af_af*
%lang(cs) %{_datadir}/vim/v*/lang/menu_cs_cz*
%lang(de) %{_datadir}/vim/v*/lang/menu_de_de*
%lang(es) %{_datadir}/vim/v*/lang/menu_es_es*
%lang(fr) %{_datadir}/vim/v*/lang/menu_fr_fr*
%lang(hu) %{_datadir}/vim/v*/lang/menu_hu_hu*
%lang(it) %{_datadir}/vim/v*/lang/menu_it_it*
%lang(jp) %{_datadir}/vim/v*/lang/menu_ja_jp*
%lang(ko) %{_datadir}/vim/v*/lang/menu_ko_kr*
%lang(nl) %{_datadir}/vim/v*/lang/menu_nl_nl*
%lang(pl) %{_datadir}/vim/v*/lang/menu_pl_pl*
%lang(sk) %{_datadir}/vim/v*/lang/menu_sk_sk*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh_cn*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh_tw*

%{_datadir}/vim/v*/macros
%{_datadir}/vim/v*/plugin
%{_datadir}/vim/v*/syntax
%{_datadir}/vim/v*/tutor
%{_datadir}/vim/v*/colors
%{_datadir}/vim/v*/compiler
%{_datadir}/vim/v*/*.vim
%{_datadir}/vim/v*/*.ps

%{_mandir}/man1/vim*
%{_mandir}/man1/rvim.*

%if %{!?_without_athena:1}%{?_without_athena:0}
%files -n gvim-athena
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.athena
%{_applnkdir}/Development/Editors/gvim-athena.desktop
%endif

%if %{!?_without_motif:1}%{?_without_motif:0}
%files -n gvim-motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.motif
%{_applnkdir}/Development/Editors/gvim-motif.desktop
%endif

%if %{!?_without_gtk:1}%{?_without_gtk:0}
%files -n gvim-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.gtk
%attr(755,root,root) %{_prefix}/X11R6/bin/rgvim
%attr(755,root,root) %{_prefix}/X11R6/bin/rgview
%attr(755,root,root) %verify(not link) %{_prefix}/X11R6/bin/gvim
%{_applnkdir}/Development/Editors/gvim-gtk.desktop
%endif

%if %{!?_without_gnome:1}%{?_without_gnome:0}
%files -n gvim-gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/gvim.gnome
%{_applnkdir}/Development/Editors/gvim-gnome.desktop
%endif
