# TODO:
# - some nice icon
# - SECURITY: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=289560
#
# Conditional build:
%bcond_without	static		# don't build static version
%bcond_without	athena		# don't build Athena Widgets-based gvim
%bcond_without	motif		# don't build Motif-based gvim
%bcond_without	gtk		# don't build GTK+-based gvim support
%bcond_without	gnome		# don't build GNOME-based gvim support
%bcond_without	kde		# don't build kvim
%bcond_with	perl		# with Perl interp
%bcond_with	python		# with Python interp
%bcond_with	ruby		# with Ruby interp
%bcond_with	tcl		# with Tcl interp
%bcond_with	bonobo		# with bonobo component (breaks other things)
%bcond_without	selinux		# without selinux support
%bcond_without	ispell		# don't build vim.ispell
%bcond_without	home_etc	# without home_etc support
#
%define		_ver		7.0
%define		_patchlevel	148

Summary:	Vi IMproved - a Vi clone
Summary(de.UTF-8):   VIsual editor iMproved
Summary(es.UTF-8):   Editor visual incrementado
Summary(fr.UTF-8):   Editeur VIM : VIsual editor iMproved
Summary(pl.UTF-8):   Vi IMproved - klon edytora Vi
Summary(pt_BR.UTF-8):   Editor visual incrementado
Summary(ru.UTF-8):   Visual editor IMproved - Единственно Правильный Редактор :)
Summary(tr.UTF-8):   Gelişmiş bir vi sürümü
Summary(uk.UTF-8):   Visual editor IMproved - Єдино Вірний Редактор :)
Name:		vim
Version:	%{_ver}
Release:	0.%{_patchlevel}.1
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/vim/unstable/snapshot/%{name}-%{_ver}%{_patchlevel}.zip
# Source0-md5:	63609a2653b49411899575444e1c4cc1
#Source1:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{_ver}-lang.tar.gz
# Source1-md5:	5395c4dacbf1c5008b22c4b86794e8a7
#Source2:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{_ver}-extra.tar.gz
# Source2-md5:	6e4bd6c8122bcb9dc576514bdb52484e
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source4-md5:	bc4d1e115ca506ad7751b9bd2b773a7f
Source5:	http://freenux.org/kvim/kvim-runtime-6.2.14.tar.bz2
# Source5-md5:	6f633e79bcf5f35918bb0bff6850a971
Source6:	http://skawina.eu.org/mikolaj/usr_doc_pl.zip
# Source6-md5:	ff96284b1c913d55cf0877839b34d490
Source10:	g%{name}-athena.desktop
Source11:	g%{name}-motif.desktop
Source12:	g%{name}-gtk.desktop
Source13:	g%{name}-gnome.desktop
Source14:	%{name}.desktop
# http://www.vim.org/scripts/script.php?script_id=1120
Source15:	php.vim
# http://www.vim.org/scripts/script.php?script_id=415 (1.13)
Source16:	zenburn.vim
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-ispell.patch
Patch4:		%{name}-ispell-axp.patch
Patch5:		%{name}-%{name}rc.patch
Patch6:		%{name}-no_libelf.patch
Patch7:		%{name}-egrep.patch
Patch8:		k%{name}-desktop.patch
Patch9:		%{name}-specsyntax.patch
Patch10:	%{name}-specsyntax-pld.patch
Patch11:	%{name}-bonobo.patch
Patch12:	%{name}-home_etc.patch
#Patch12:	%{name}-dynamic_python.patch
Patch13:	%{name}-selinux.patch
Patch14:	%{name}-specsyntax4.patch
Patch15:	%{name}-po.patch
Patch16:	%{name}-filetype_vim-perl_tests.patch
Patch17:	%{name}-pl.po.patch
Patch18:	%{name}-po-syntax.patch
Patch19:	%{name}-modprobe.patch

Patch99:	http://www.opensky.ca/gnome-vim/vim-patches/%{name}-bonobo-20040115.patch
Patch999:	http://freenux.org/vim/%{name}2kvim-6.3b.diff.bz2
URL:		http://www.vim.org/
%{?with_athena:BuildRequires:	XFree86-devel}
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.2.1}
%{?with_kde:BuildRequires:	kdelibs-devel >= 9:3.0.0}
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.2.0.1}
%{?with_selinux:BuildRequires:	libselinux-devel}
%{?with_motif:BuildRequires:	openmotif-devel}
BuildRequires:	ncurses-devel
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python:BuildRequires:	python-devel}
%{?with_ruby:BuildRequires:	ruby}
%{?with_tcl:BuildRequires:	tcl-devel}
%if %{with bonobo}
BuildRequires:	libgnomeui-devel >= 2.2.0.1
BuildRequires:	ORBit2-devel
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	nautilus-devel >= 2.2.0
%endif
%if %{with static}
BuildRequires:	acl-static
BuildRequires:	attr-static
BuildRequires:	glibc-static
%{?with_selinux:BuildRequires:	libselinux-static}
BuildRequires:	ncurses-static
%else
Provides:	%{name}-static = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-static
%endif
BuildRequires:	unzip
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Obsoletes:	vim-enhanced
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# that's example script
%define		_noautoreq	'/bin/csh'

%description
Text editor similar to Vi. Important improvements: multiple windows,
multi-level undo, block highliting, folding, and many other.

%description -l cs.UTF-8
ViM je nový a vylepšený editor vycházející z klasického editoru vi. Vi
byl prvním celoobrazovkovým editorem pro Unix a je stále velmi
populární. ViM je obohacený funkcemi jako: podpora více oken,
víceúrovňové undo, zvýrazňování bloků a řadu dalších užitečných
funkcí.

%description -l de.UTF-8
Der Visual-Editor iMproved ist ein aktualisierter und erweiterter Klon
des vi-Editors, der mit praktisch allen UN*X-Systemen ausgeliefert
wird. Er bringt mehrere Fenster, mehrstufige Widerrufen-Funktion,
Block-Markierung und viele weitere Zusatzfunktionen im Vergleich zum
Standard-vi-Programm.

%description -l es.UTF-8
El editor Visual Mejorado es una versión actualizada y con nuevas
características adicionales del mundialmente famoso 'vi' que acompaña
prácticamente todos los sistemas UN*X. Posibilita trabajar con
múltiples ventanas, varios niveles de deshacer, bloques enfatizados, y
otras muchas características del 'vi'.

%description -l fr.UTF-8
L'éditeur VIsuel aMélioré est un clone mis à jour et doté de
caractéristiques supplémentaires de l'éditeur « vi » fourni avec
pratiquement tous les systèmes UN*X. Il ajoute les fenêtres
mutltiples, l'annulation a plusieurs niveaux, la mise en évidence des
blocs et autres caractéristiques au vi de base.

%description -l id.UTF-8
VIM (VIsual editor iMproved) adalah versi vi editor yang sudah
diupdate dan ditambah kemampuannya. Vi adalah editor untuk UNIX yang
pertama yang menggunakan layar, dan sekarang masih sangat populer. VIM
mengembangkan vi dengan menambah kemampuan baru seperti: multiple
windows, multi-level undo, block highlighting, dll.

%description -l is.UTF-8
VIM (VIsual editor iMproved) er uppfærð og endurbætt útgáfa af vi
ritlinum. Vi var fyrsti skjá-ritillinn fyrir UNIX og er enn mjög
vinsæll. VIM gerist föðurbetrungur með nýjum möguleikum líkt og
gluggakerfi, iðrun og yfirbót (e: multi-level undo), blokkarvali og
fleira.

%description -l it.UTF-8
VIM (Vi IMproved) è una versione aggiornata e perfezionata dell'editor
vi. Vi è stato il primo editor per UNIX realmente basato su video ed è
ancora molto diffuso. VIM perfeziona vi aggiungendo nuove funzioni:
finestre multiple, funzione \"annulla\" multilivello, evidenziazione
dei blocchi e altro.

%description -l pl.UTF-8
Edytor tekstu podobny do Vi. Ważne ulepszenia: możliwość pracy w wielu
oknach, wielopoziomowa opcja 'cofnij', bloki, podświetlanie składni,
folding i wiele innych.

%description -l pt_BR.UTF-8
O editor Vim (Vi Enhanced) é um versão atualizada e com novas
características do mundialmente famoso 'vi' que acompanha praticamente
todos os sistemas UN*X. Ele possibilita trabalhar com múltiplas
janelas, vários níveis de desfazer, blocos enfatizados, e muitas
outras características do 'vi'.

%description -l ru.UTF-8
VIsual editor iMproved - это обновленный и значительно улучшенный клон
редактора vi, который поставляется практически со всеми
UN*X-системами. В этой версии есть многоуровневый откат, выделение
блоков, синтаксическая подсветка и много другого...

%description -l sk.UTF-8
VIM (VIsual editor iMproved) je novšia a vylepšená verzia editoru vi.
Vi bol prvým skutočne obrazovkovo orientovaným editorom pre UNIX a
stále je veľmi populárny. VIM má oproti vi vylepšenia ako: prácu s
viacerými oknami, viacnásobné undo, zvýrazňovanie blokov textu a iné.

%description -l sv.UTF-8
VIM (Vi IMproved) är en uppdaterad och förbättrad version av
redigeraren vi. Vi var den första riktiga skärmbaserade redigeraren
till UNIX, och är fortfarande väldigt populär. VIM förbättrar vi med
nya finesser: flera fönster, flernivå ångra, blockmarkering och mer
ändå.

%description -l tr.UTF-8
Standart vi metin düzenleyicisinin gelişmiş hali; daha fazla komut,
birden fazla pencere desteği ve blok işaretleme yetenekleri içerir.

%description -l uk.UTF-8
VIsual editor iMproved - це оновлений та значно поліпшений клон
редактора vi, який поставляється практично зі всіма UN*X-системами. В
цій версії є багаторівневий відкат, виділення блоків, синтаксична
підсвітка та багато іншого...

%package -n xxd
Summary:	Utility to convert files to hexdump or do the reverse
Summary(pl.UTF-8):   Narzędzie do zamiany plików na postać szesnastkową i odwrotnie
Group:		Applications/Editors/Vim

%description -n xxd
xxd creates a hex dump of a given file or standard input. It can also
convert a hex dump back to its original binary form. Like uuencode and
uudecode it allows the transmission of binary data in a `mail-safe'
ASCII representation, but has the advantage of decoding to standard
output. Moreover, it can be used to perform binary file patching.

%description -n xxd -l pl.UTF-8
xxd tworzy szesnastkowy zapis pliku podanego na standardowe wejście.
Może także przekonwertować taki zapis na oryginalną, binarną postać.
Podobnie jak uuencode i uudecode pozwala na przesyłanie danych
binarnych w postaci ASCII, ale ma możliwość dekodowania na standardowe
wyjście. Co więcej, może być użyty do modyfikowania plików binarnych.

%package static
Summary:	Statically linked Vim
Summary(pl.UTF-8):   Statycznie skonsolidowany Vim
Group:		Applications/Editors/Vim
Provides:	vi
Obsoletes:	elvis-static
Obsoletes:	nvi
Obsoletes:	vi
Obsoletes:	vim-minimal

%description static
Text editor similar to Vi. This version is built with minimal feature
and is installed in /bin as a rescue tool. The installation of this
package is STRONGLY recommended.

%description static -l pl.UTF-8
Edytor tekstu podobny do Vi. Ta wersja została skonsolidowana
statycznie i posiada minimalną ilość dodatków. Jest instalowana w /bin
jako narzędzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, może on pomóc Ci uratować system w czasie awarii.

%description static -l ru.UTF-8
Пакет vim-static устанавливает разновидность vim как /bin/vi, что
удобно для запуска даже когда смонтирована только корневая файловая
система.

%description static -l uk.UTF-8
Пакет vim-static встановлює різновид vim як /bin/vi, що зручно для
запуску навіть тоді, коли змонтована тільки корньова файлова система.

%package ispell
Summary:	Vim with ispell support
Summary(pl.UTF-8):   Vim z wsparciem dla ispella
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Conflicts:	ispell < 3.2.06
Conflicts:	ispell-pl < 20021127-2

%description ispell
Text editor similar to Vi. This version is built with ispell support.

%description ispell -l pl.UTF-8
Edytor tekstu podobny do Vi. Ta wersja została skompilowana ze
wsparciem dla ispella.

%package rt
Summary:	Vim runtime files
Summary(cs.UTF-8):   Soubory nezbytné pro libovolný editor ViM
Summary(da.UTF-8):   Fælles filer som er nødvendige for enhver version af VIM editoren
Summary(de.UTF-8):   Die von allen Versionen des VIM-Editors benötigten gemeinsamen Dateien
Summary(es.UTF-8):   Ficheros comunes a todas las versiones de VIM
Summary(fr.UTF-8):   Fichiers communs indispensables pour toute version de l'éditeur VIM
Summary(id.UTF-8):   File umum yang dibutuhkan oleh semua versi editor VIM
Summary(is.UTF-8):   Grunnskrár sem allar útgáfur VIM ritilsins þurfa á að halda
Summary(it.UTF-8):   File comuni necessari per tutte le versioni dell'editor VIM
Summary(ja.UTF-8):   すべてのバージョンの VIM エディタで必要とされる共通ファイル
Summary(nb.UTF-8):   Felles filer som er nødvendige for enhver versjon av VIM editoren
Summary(pl.UTF-8):   Pliki przydatne edytorowi Vim
Summary(pt.UTF-8):   Os ficheiros comuns necessários para qualquer versão do editor VIM
Summary(ru.UTF-8):   Файлы, требуемые для любой версии редактора vim
Summary(sk.UTF-8):   Spoločné súbory potrebné pre všetky verzie editoru VIM
Summary(sl.UTF-8):   Skupne datoteke, potrebne s katerokoli različico urejevalnika VIM
Summary(sv.UTF-8):   De gemensamma filerna som behövs av alla versioner av redigeraren VIM
Summary(uk.UTF-8):   Файли, потрібні для будь-якої версії редактору vim
Summary(zh_CN.UTF-8):   任何版本的 VIM 编辑器所需的公用文件。
Group:		Applications/Editors/Vim
Requires:	mktemp
Requires:	which
Obsoletes:	vim-common

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for Vim. If you want to take advantage of Vim more
powerful features, you should install this package.

%description rt -l cs.UTF-8
Tento balíček obsahuje společné soubory pro všechny další balíčky s
vim.

%description rt -l da.UTF-8
The vim-rt package contains files which every VIM binary will need in
order to run.

%description rt -l de.UTF-8
Das Paket vim-rt enthält Dateien, die jede VIM-Binärdatei für die
Ausführung benötigt.

%description rt -l es.UTF-8
The vim-rt package contains files which every VIM binary will need in
order to run.

%description rt -l fr.UTF-8
Le paquetage vim-rt contient des fichiers dont chaque fichier binaire
VIM a besoin pour fonctionner.

%description rt -l id.UTF-8
Package vim-rt berisi file yang dibutuhkan semua versi VIM agar bisa
berjalan.

%description rt -l is.UTF-8
vim-rt pakkinn inniheldur skrár sem allar VIM keyrsluskrárnar þurfa
til að keyra.

%description rt -l it.UTF-8
Il pacchetto vim-rt contiene i file necessari a ogni binario di VIM
per poter funzionare.

%description rt -l pl.UTF-8
W tym pakiecie znajdziesz dokumentację, makra, pliki konfiguracyjne i
strony podręcznika dla edytora Vim. Jeżeli chcesz korzystać z
zaawansowanych możliwości Vima, powinieneś zainstalować ten pakiet.

%description rt -l pt.UTF-8
O pacote vim-rt contém os ficheiros que todos os executáveis do VIM
irão necessitar para correr.

%description rt -l ru.UTF-8
Пакет vim-rt содержит файлы (например, файлы справки), которые нужны
для работы любой программы vim.

%description rt -l sk.UTF-8
Balík vim-rt obsahuje súbory, ktoré bude potrebovať pre správnu
funkciu každá verzia editoru VIM.

%description rt -l sv.UTF-8
Paketet vim-rt innehåller filer som alla VIM-binärer behöver för att
köra.

%description rt -l uk.UTF-8
Пакет vim-rt містить файли (наприклад, файли довідки), котрі потрібні
для роботи будь-якої програми vim.

%package -n gvim-athena
Summary:	Vim for X Window built with Athena
Summary(pl.UTF-8):   Vim dla X Window korzystający z biblioteki Athena
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-athena
The classic Unix text editor now also under X Window System! This
version is built with Athena Widget Set.

%description -n gvim-athena -l pl.UTF-8
Wersja edytora Vim pracująca w środowisku X Window z wykorzystaniem
biblioteki Athena Widget Set.

%description -n gvim-athena -l ru.UTF-8
Этот пакет представляет собой версию VIM, собранную с библиотеками
Athena Widget Set, что позволяет запускать VIM как приложение X Window
System - с полностью графическим интерфейсом и поддержкой мыши.

%description -n gvim-athena -l uk.UTF-8
Цей пакет містить версію VIM, зібрану з бібліотеками Athena Widget
Set, що дозволяє запускати VIM як прикладну програму X Window System -
з повністю графічним інтерфейсом та підтримкою миші.

%package -n gvim-motif
Summary:	Vim for X Window built with Motif
Summary(pl.UTF-8):   Vim dla X Window korzystający z biblioteki Motif
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-motif
The classic Unix text editor now also under X Window System! This
version is built with Motif.

%description -n gvim-motif -l pl.UTF-8
Wersja edytora Vim pracująca w środowisku X Window z wykorzystaniem
biblioteki Motif.

%description -n gvim-motif -l ru.UTF-8
Этот пакет представляет собой версию VIM, собранную с библиотеками
Motif, что позволяет запускать VIM как приложение X Window System - с
полностью графическим интерфейсом и поддержкой мыши.

%description -n gvim-motif -l uk.UTF-8
Цей пакет містить версію VIM, зібрану з бібліотеками Motif, що
дозволяє запускати VIM як прикладну програму X Window System - з
повністю графічним інтерфейсом та підтримкою миші.

%package -n kvim
Summary:	Vim for X Window built with KDE
Summary(pl.UTF-8):   Vim dla X Window korzystający z biblioteki KDE
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n kvim
The classic Unix text editor now also under X Window System! This
version is built with KDE.

%description -n kvim -l pl.UTF-8
Wersja edytora Vim pracująca w środowisku X Window z wykorzystaniem
biblioteki KDE.

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl.UTF-8):   Vim dla X Window korzystający z biblioteki GTK
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This
version is built with GTK.

%description -n gvim-gtk -l pl.UTF-8
Wersja edytora Vim pracująca w środowisku X Window z wykorzystaniem
biblioteki GTK.

%description -n gvim-gtk -l ru.UTF-8
Этот пакет представляет собой версию VIM, собранную с библиотеками
GTK, что позволяет запускать VIM как приложение X Window System - с
полностью графическим интерфейсом и поддержкой мыши. Просто скажите
'gvim'...

%description -n gvim-gtk -l uk.UTF-8
Цей пакет містить версію VIM, зібрану з бібліотеками GTK, що дозволяє
запускати VIM як прикладну програму X Window System - з повністю
графічним інтерфейсом та підтримкою миші. Просто скажіть 'gvim'...

%package -n gvim-gnome
Summary:	Vim for X Window built with GNOME
Summary(pl.UTF-8):   Vim dla X Window korzystający z biblioteki GNOME
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gnome
The classic Unix text editor now also under X Window System! This
version is build with GNOME.

%description -n gvim-gnome -l pl.UTF-8
Wersja edytora Vim pracująca w środowisku X Window z wykorzystaniem
bibliotek GNOME.

%description -n gvim-gnome -l ru.UTF-8
Этот пакет представляет собой версию VIM, собранную с библиотеками
GNOME, что позволяет запускать VIM как приложение X Window System - с
полностью графическим интерфейсом и поддержкой мыши.

%description -n gvim-gnome -l uk.UTF-8
Цей пакет містить версію VIM, зібрану з бібліотеками GNOME, що
дозволяє запускати VIM як прикладну програму X Window System - з
повністю графічним інтерфейсом та підтримкою миші.

%package -n gvim-bonobo
Summary:	Vim for X Window built as bonobo component
Summary(pl.UTF-8):   Vim dla X Window zbudowany jako element bonobo
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-bonobo
The classic Unix text editor now also under X Window System! This
version is build as bonobo component.

%description -n gvim-bonobo -l pl.UTF-8
Wersja edytora Vim pracująca w środowisku X Window, zbudowana jako
element bonobo.

%prep
%setup -q -c -a5

# kvim
#%patch999 -p1

%patch0 -p1
%{?with_bonobo:%patch99 -p1}
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%ifarch alpha
%patch4 -p1
%endif
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#%patch10 -p1
%{?with_bonobo:%patch11 -p1}
%{?with_home_etc:%patch12 -p1}
%{?with_selinux:%patch13 -p1}
#%patch14 -p1
#%patch15 -p1
%patch16 -p1
#%patch17 -p1
#%patch18 -p1
%patch19 -p0 -b .modprobe

install %{SOURCE15} runtime/indent
install %{SOURCE16} runtime/colors

%build
cd src
%{__autoconf}
# needed to prevent deconfiguring
cp -f configure auto

install -d bin

%if %{with bonobo}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--with-features=huge \
	--enable-gui=gnome2 \
	--enable-bonobo \
	--enable-gtk2-check \
	--enable-gnome-check \
	--with-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	--disable-gpm \
	--enable-cscope \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim-component vim-factory Vim_Control.server
mv vim-component vim-factory Vim_Control.server bin/
%endif

%if %{with static}
%{__make} distclean
LDFLAGS="%{rpmldflags} -static"
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-rubyinterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-multibyte \
	%{?with_bonobo:--disable-bonobo} \
	--with-features=small \
	--with-tlib=tinfo \
	--disable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim \
	SPELL_OBJ=
mv -f vim bin/vim.static
LDFLAGS="%{rpmldflags}"
%endif

%{__make} distclean
%configure \
	--disable-gui \
	--without-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	%{?with_bonobo:--disable-bonobo} \
	--enable-cscope \
	--enable-gpm \
	--with-features=huge \
	--enable-multibyte \
	--with-tlib=ncurses \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim \
	SPELL_OBJ=
mv -f vim bin/vim.ncurses
%if %{with ispell}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--disable-gui \
	--without-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	%{?with_bonobo:--disable-bonobo} \
	--enable-cscope \
	--enable-gpm \
	--with-features=huge \
	--enable-multibyte \
	--with-tlib=ncurses \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/vim.ispell
%endif
%if %{with kde}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--with-features=huge \
	--enable-gui=kde \
	--with-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	%{?with_bonobo:--disable-bonobo} \
	--enable-cscope \
	--with-qt-dir=%{_prefix} \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libs=%{_libdir} \
	--enable-fontset \
	--disable-gpm \
	--without-gnome \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--enable-kde-toolbar \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/kvim
%endif

%if %{with athena}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--with-features=huge \
	--enable-gui=athena \
	--with-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	%{?with_bonobo:--disable-bonobo} \
	--enable-cscope \
	--enable-fontset \
	--disable-gpm \
	--without-gnome \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.athena
%endif


%if %{with motif}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--with-features=huge \
	--enable-gui=motif \
	--with-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	%{?with_bonobo:--disable-bonobo} \
	--enable-multibyte \
	--enable-cscope \
	--enable-fontset \
	--disable-gpm \
	--without-gnome \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.motif
%endif

%if %{with gtk}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--with-features=huge \
	--enable-gui=gtk2 \
	--enable-gtk2-check \
	--with-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	%{?with_bonobo:--disable-bonobo} \
	--disable-gpm \
	--enable-cscope \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.gtk
%endif

%if %{with gnome}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--with-features=huge \
	--enable-gui=gnome2 \
	%{?with_bonobo:--disable-bonobo} \
	--enable-gtk2-check \
	--enable-gnome-check \
	--with-x \
	%{!?with_perl:--disable-perlinterp} \
	%{?with_perl:--enable-perlinterp} \
	%{!?with_python:--disable-pythoninterp} \
	%{?with_python:--enable-pythoninterp} \
	%{!?with_ruby:--disable-rubyinterp} \
	%{?with_ruby:--enable-rubyinterp} \
	%{!?with_tcl:--disable-tclinterp} \
	%{?with_tcl:--enable-tclinterp} \
	--disable-gpm \
	--enable-cscope \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.gnome
%endif


%{__make} xxd/xxd languages

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/*

%if %{with static}
install -m755 src/bin/vim.ncurses	$RPM_BUILD_ROOT%{_bindir}/vim
install -m755 src/bin/vim.static	$RPM_BUILD_ROOT/bin/vi
%else
install -m755 src/bin/vim.ncurses	$RPM_BUILD_ROOT/bin/vi
ln -sf /bin/vi		$RPM_BUILD_ROOT%{_bindir}/vim
%endif
%if %{with ispell}
install -m755 src/bin/vim.ispell	$RPM_BUILD_ROOT%{_bindir}/vim.ispell
%endif
install -m755 src/xxd/xxd	$RPM_BUILD_ROOT%{_bindir}/xxd
install -m755 src/vimtutor	$RPM_BUILD_ROOT%{_bindir}/vimtutor

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

install %{SOURCE14}	$RPM_BUILD_ROOT%{_desktopdir}

%if %{with athena}
install -m755 src/bin/gvim.athena	$RPM_BUILD_ROOT%{_bindir}/gvim.athena
install %{SOURCE10}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with motif}
install -m755 src/bin/gvim.motif	$RPM_BUILD_ROOT%{_bindir}/gvim.motif
install %{SOURCE11}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gnome}
install -m755 src/bin/gvim.gnome	$RPM_BUILD_ROOT%{_bindir}/gvim.gnome
install %{SOURCE13}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gtk}
install -m755 src/bin/gvim.gtk	$RPM_BUILD_ROOT%{_bindir}/gvim.gtk
ln -sf gvim.gtk		$RPM_BUILD_ROOT%{_bindir}/gvim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgvim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgview
install %{SOURCE12}	$RPM_BUILD_ROOT%{_desktopdir}
%endif

%if %{with kde}
install -m755 src/bin/kvim $RPM_BUILD_ROOT%{_bindir}/kvim
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,22x22}/actions
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{32x32,48x48,64x64}/apps
install runtime/hi16-action-make.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions
install runtime/hi22-action-make.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/actions
install runtime/kvim32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/kvim.png
install runtime/kvim48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/kvim.png
install runtime/kvim64x64.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/kvim.png
install runtime/KVim.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kvim
install runtime/kde-tips $RPM_BUILD_ROOT%{_datadir}/apps/kvim/tips
%endif

# Bonobo
%if %{with bonobo}
install -d $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
install src/bin/Vim_Control.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
install -m755 src/bin/vim-{component,factory} $RPM_BUILD_ROOT%{_bindir}
%endif

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
unzip -d $RPM_BUILD_ROOT%{_datadir}/vim/v*/doc %{SOURCE6}

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/{doc,{after/,}{syntax,ftdetect,plugin,ftplugin}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/rvim
%{_desktopdir}/%{name}.desktop

%if %{with static}
%files static
%defattr(644,root,root,755)
%endif
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*

%{_mandir}/man1/vi.1*
%{_mandir}/man1/ex.1*
%{_mandir}/man1/view.1*
%{_mandir}/man1/rview.1*
%lang(fi) %{_mandir}/fi/man1/vi.1*
%lang(fi) %{_mandir}/fi/man1/ex.1*
%lang(fi) %{_mandir}/fi/man1/view.1*
%lang(fi) %{_mandir}/fi/man1/rview.1*
%lang(fr) %{_mandir}/fr/man1/vi.1*
%lang(fr) %{_mandir}/fr/man1/ex.1*
%lang(fr) %{_mandir}/fr/man1/view.1*
%lang(fr) %{_mandir}/fr/man1/rview.1*
%lang(id) %{_mandir}/id/man1/vi.1*
%lang(id) %{_mandir}/id/man1/ex.1*
%lang(id) %{_mandir}/id/man1/view.1*
%lang(id) %{_mandir}/id/man1/rview.1*
%lang(it) %{_mandir}/it*/man1/ex.1*
%lang(it) %{_mandir}/it*/man1/view.1*
%lang(it) %{_mandir}/it*/man1/rview.1*
%lang(pl) %{_mandir}/pl/man1/vi.1*
%lang(pl) %{_mandir}/pl/man1/ex.1*
%lang(pl) %{_mandir}/pl/man1/view.1*
%lang(pl) %{_mandir}/pl/man1/rview.1*
%lang(ru) %{_mandir}/ru*/man1/ex.1*
%lang(ru) %{_mandir}/ru*/man1/view.1*
%lang(ru) %{_mandir}/ru*/man1/rview.1*

%if %{with ispell}
%files ispell
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim.ispell
%endif

%files -n xxd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxd
%{_mandir}/man1/xxd.1*
%lang(fr) %{_mandir}/fr/man1/xxd.1*
%lang(it) %{_mandir}/it*/man1/xxd.1*
%lang(ru) %{_mandir}/ru*/man1/xxd.1*

%files rt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%dir %{_sysconfdir}/vim
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/gvimrc

%dir %{_datadir}/vim
%dir %{_datadir}/vim/v*
%dir %{_datadir}/vim/v*/doc
%doc %{_datadir}/vim/v*/doc/*.txt
%lang(pl) %doc %{_datadir}/vim/v*/doc/*.plx
%attr(755,root,root) %{_datadir}/vim/v*/doc/*.pl
%verify(not size mtime md5) %{_datadir}/vim/v*/doc/tags
%lang(pl) %verify(not size mtime md5) %{_datadir}/vim/v*/doc/tags-pl
%{_datadir}/vim/v*/ftplugin
%{_datadir}/vim/v*/indent
%{_datadir}/vim/v*/keymap
%dir %{_datadir}/vim/v*/lang
%doc %{_datadir}/vim/v*/lang/README*

# just add after/ and ftdetect/ separately, other dirs catched by glob above
%{_datadir}/vim/vimfiles/after
%{_datadir}/vim/vimfiles/ftdetect

%lang(af) %{_datadir}/vim/v*/lang/af
%lang(ca) %{_datadir}/vim/v*/lang/ca
%lang(en_GB) %{_datadir}/vim/v*/lang/en_GB
%lang(cs) %{_datadir}/vim/v*/lang/cs
%lang(de) %{_datadir}/vim/v*/lang/de
%lang(es) %{_datadir}/vim/v*/lang/es
%lang(fr) %{_datadir}/vim/v*/lang/fr
%lang(ga) %{_datadir}/vim/v*/lang/ga
%lang(it) %{_datadir}/vim/v*/lang/it
%lang(ja) %{_datadir}/vim/v*/lang/ja*
%lang(ko) %{_datadir}/vim/v*/lang/ko
%lang(pl) %{_datadir}/vim/v*/lang/pl
%lang(ru) %{_datadir}/vim/v*/lang/ru
%lang(sk) %{_datadir}/vim/v*/lang/sk
%lang(sv) %{_datadir}/vim/v*/lang/sv
%lang(nb) %{_datadir}/vim/v*/lang/no
#%lang(tr) %{_datadir}/vim/v*/lang/tr
%lang(uk) %{_datadir}/vim/v*/lang/uk
%lang(vi) %{_datadir}/vim/v*/lang/vi
%lang(zh_CN) %{_datadir}/vim/v*/lang/zh_CN*
%lang(zh_TW) %{_datadir}/vim/v*/lang/zh_TW*

%lang(af) %{_datadir}/vim/v*/lang/menu_af*
%lang(ca) %{_datadir}/vim/v*/lang/menu_ca*
%lang(cs) %{_datadir}/vim/v*/lang/menu_cs*
%lang(cs) %{_datadir}/vim/v*/lang/menu_*czech*
%lang(de) %{_datadir}/vim/v*/lang/menu_de*
%lang(de) %{_datadir}/vim/v*/lang/menu_*german*
%lang(es) %{_datadir}/vim/v*/lang/menu_es*
%lang(es) %{_datadir}/vim/v*/lang/menu_*spanish*
%lang(en_GB) %{_datadir}/vim/v*/lang/menu_en_gb*
%lang(en_GB) %{_datadir}/vim/v*/lang/menu_*english*
%lang(fr) %{_datadir}/vim/v*/lang/menu_fr*
%lang(hu) %{_datadir}/vim/v*/lang/menu_hu*
%lang(it) %{_datadir}/vim/v*/lang/menu_it*
%lang(ja) %{_datadir}/vim/v*/lang/menu_ja*
%lang(ko) %{_datadir}/vim/v*/lang/menu_ko*
%lang(nl) %{_datadir}/vim/v*/lang/menu_nl*
%lang(nb) %{_datadir}/vim/v*/lang/menu_no*
%lang(pl) %{_datadir}/vim/v*/lang/menu_pl*
%lang(pl) %{_datadir}/vim/v*/lang/menu_*polish*
%lang(pt) %{_datadir}/vim/v*/lang/menu_pt*
%lang(ru) %{_datadir}/vim/v*/lang/menu_ru*
%lang(sk) %{_datadir}/vim/v*/lang/menu_sk*
%lang(sk) %{_datadir}/vim/v*/lang/menu_*slovak*
%lang(sr) %{_datadir}/vim/v*/lang/menu_sr*
%lang(sv) %{_datadir}/vim/v*/lang/menu_sv*
%lang(uk) %{_datadir}/vim/v*/lang/menu_uk*
%lang(vi) %{_datadir}/vim/v*/lang/menu_vi*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh.cp936*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh.gb2312*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh_cn*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_*chinese*gb*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh.cp950*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh.big5*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh_tw*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_*taiwan*

%lang(en_GB) %{_datadir}/vim/v*/spell/en.*.spl

%{_datadir}/vim/v*/macros
%{_datadir}/vim/v*/plugin
%{_datadir}/vim/v*/print
%{_datadir}/vim/v*/syntax
%{_datadir}/vim/v*/tools
%{_datadir}/vim/v*/tutor
%{_datadir}/vim/v*/colors
%{_datadir}/vim/v*/compiler
%{_datadir}/vim/v*/autoload
%{_datadir}/vim/v*/*.vim

%{_mandir}/man1/vim*
%{_mandir}/man1/rvim.*
%lang(fi) %{_mandir}/fi/man1/vim*
%lang(fi) %{_mandir}/fi/man1/rvim.*
%lang(fi) %{_mandir}/fi/man1/gvi*
%lang(fi) %{_mandir}/fi/man1/rgv*
%lang(fr) %{_mandir}/fr/man1/vim*
%lang(fr) %{_mandir}/fr/man1/rvim.*
%lang(fr) %{_mandir}/fr/man1/gvi*
%lang(fr) %{_mandir}/fr/man1/rgv*
%lang(id) %{_mandir}/id/man1/vim*
%lang(id) %{_mandir}/id/man1/rvim.*
%lang(id) %{_mandir}/id/man1/gvi*
%lang(id) %{_mandir}/id/man1/rgv*
%lang(it) %{_mandir}/it*/man1/vim*
%lang(pl) %{_mandir}/pl/man1/vim*
%lang(pl) %{_mandir}/pl/man1/rvim.*
%lang(pl) %{_mandir}/pl/man1/gvi*
%lang(pl) %{_mandir}/pl/man1/rgv*
%lang(ru) %{_mandir}/ru*/man1/vim*

%if %{with athena}
%files -n gvim-athena
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvim.athena
%{_desktopdir}/gvim-athena.desktop
%endif

%if %{with motif}
%files -n gvim-motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvim.motif
%{_desktopdir}/gvim-motif.desktop
%endif

%if %{with kde}
%files -n kvim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvim
%{_desktopdir}/kde/KVim.desktop
%{_iconsdir}/hicolor/*/apps/kvim.png
%{_iconsdir}/hicolor/*/actions/*make*.png
%{_datadir}/apps/kvim
%endif


%if %{with gtk}
%files -n gvim-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvim.gtk
%attr(755,root,root) %{_bindir}/rgvim
%attr(755,root,root) %{_bindir}/rgview
%attr(755,root,root) %verify(not link) %{_bindir}/gvim
%{_desktopdir}/gvim-gtk.desktop
%endif

%if %{with gnome}
%files -n gvim-gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvim.gnome
%{_desktopdir}/gvim-gnome.desktop
%endif

%if %{with bonobo}
%files -n gvim-bonobo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim-component
%attr(755,root,root) %{_bindir}/vim-factory
%{_libdir}/bonobo/servers/*
%endif
