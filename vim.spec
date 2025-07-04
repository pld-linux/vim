#
# Conditional build:
%bcond_without	static		# static version
%bcond_without	athena		# Athena Widgets-based gvim
%bcond_without	motif		# Motif-based gvim
%bcond_without	gtk		# GTK+-based gvim support
%bcond_without	gtk3		# use GTK+ 2.x instead of 3.x
%bcond_without	gnome		# GNOME-based gvim support
%bcond_without	heavy		# heavy (full-featured GNOME-based gvim/vim)
%bcond_without	gui		# any GUI
%bcond_without	light		# light (minimal, ncurses, but not static)
%bcond_without	x11		# vimx (non-GUI with X11 clipboard support)
%bcond_with	lua		# Lua interp in vim package
%bcond_with	perl		# Perl interp in vim package
%bcond_with	python		# Python 2 interp in vim package
%bcond_with	python3		# Python 3 interp in vim package
%bcond_with	ruby		# Ruby interp in vim package
%bcond_with	tcl		# Tcl interp
%bcond_with	x		# X11 support
%bcond_without	selinux		# SELinux support
%bcond_without	home_etc	# home_etc support

%if %{without gui}
%undefine	with_athena
%undefine	with_motif
%undefine	with_gtk
%undefine	with_gnome
%endif

# Command to check for latest patch:
# wget ftp://ftp.vim.org/pub/editors/vim/patches/8.0/MD5SUMS -O - | tail -n1 | awk '{print $2}'
# VCS Commits: https://github.com/vim/vim/commits/master

%define		ver		9.1.1453
%define		rel		1
Summary:	Vi IMproved - a Vi clone
Summary(de.UTF-8):	VIsual editor iMproved
Summary(es.UTF-8):	Editor visual incrementado
Summary(fr.UTF-8):	Editeur VIM : VIsual editor iMproved
Summary(hu.UTF-8):	Vi IMproved - a Vi szerkesztő bővítése
Summary(pl.UTF-8):	Vi IMproved - klon edytora Vi
Summary(pt_BR.UTF-8):	Editor visual incrementado
Summary(ru.UTF-8):	Visual editor IMproved - Единственно Правильный Редактор :)
Summary(tr.UTF-8):	Gelişmiş bir vi sürümü
Summary(uk.UTF-8):	Visual editor IMproved - Єдино Вірний Редактор :)
Name:		vim
Version:	%{ver}
# keep macro for release, otherwise people tend to increment Epoch instead
Release:	%{rel}
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
#TODO:	https://github.com/vim/vim/archive/v%{ver}/%{name}-%{ver}.tar.gz
Source0:	https://github.com/vim/vim/archive/v%{ver}.tar.gz
# Source0-md5:	8517249bc5d0bf835a7f01035220e281
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	bc4d1e115ca506ad7751b9bd2b773a7f
Source2:	http://skawina.eu.org/mikolaj/usr_doc_pl.zip
# Source2-md5:	ff96284b1c913d55cf0877839b34d490
Source15:	update-source.sh
# syntax files
# http://www.vim.org/scripts/script.php?script_id=1491 (0.7.7)
Source20:	javascript.vim
# http://www.vim.org/scripts/script.php?script_id=447 (20040206)
Source22:	exim.vim
# color schemes
# http://www.vim.org/scripts/script.php?script_id=415 (2.21)
Source30:	zenburn.vim
# http://www.vim.org/scripts/script.php?script_id=92 (1.0)
Source31:	borland.vim
# http://www.vim.org/scripts/script.php?script_id=368 (1.2.5)
Source32:	oceandeep.vim
# http://www.vim.org/scripts/script.php?script_id=1464 (2.6.5)
Source33:	moria.vim
Patch0:		%{name}-sysconfdir.patch

Patch2:		%{name}-paths.patch

Patch5:		%{name}-awk.patch
Patch6:		%{name}-filetype_vim-perl_tests.patch
Patch7:		%{name}-apache.patch
Patch8:		%{name}-po-syntax.patch

Patch10:	%{name}-doubleparenthesis.patch
Patch11:	%{name}-syntax-fstab.patch

Patch14:	020_all_%{name}-7.0-fstab-tmpfs-size.patch
Patch15:	021_all_%{name}-7.0-fstab-bogus-errors.patch
Patch17:	027_all_%{name}-7.0-automake-substitutions-93378.patch
Patch18:	%{name}-smarty.patch

Patch20:	%{name}-nagios.patch
Patch21:	%{name}-filetypes.patch
Patch22:	%{name}-man_installation.patch
Patch23:	%{name}-vimrc.patch
Patch24:	%{name}-syntax-exports.patch
Patch25:	sudoers-include.patch
Patch26:	%{name}-home_etc.patch
Patch27:	%{name}-autopaste.patch
Patch28:	%{name}-ft-cron.patch
Patch29:	%{name}-phpscript.patch
Patch30:	%{name}-pam.patch
Patch32:	%{name}-localedir.patch

Patch34:	%{name}-rtdir.patch
Patch35:	%{name}-ft-mib.patch

Patch38:	%{name}-ft-gyp.patch
Patch39:	%{name}-revert-7.4.165-noundo.patch
Patch40:	desktop.patch
Patch41:	%{name}-lua.patch
URL:		http://www.vim.org/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	gpm-devel
%if "%{pld_release}" == "ac"
%if %{with athena} || %{with x11} || %{with x}
BuildRequires:	XFree86-devel
%endif
BuildRequires:	gettext-devel
%else
BuildRequires:	gettext-tools
%{?with_athena:BuildRequires:	xorg-lib-libXaw-devel}
%if %{with x11} || %{with gui} || %{with x}
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
%endif
%endif
BuildRequires:	grep
%if %{with gtk} || %{with heavy}
BuildRequires:	gdk-pixbuf2-devel >= 2.31
%if %{with gtk3}
BuildRequires:	gtk+3-devel >= 3.0
%else
BuildRequires:	gtk+2-devel >= 2:2.6.0
%endif
%endif
%if %{with gnome} || %{with heavy}
BuildRequires:	libcanberra-devel
%endif
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.2.0.1}
%if %{with selinux} || %{with heavy}
BuildRequires:	libselinux-devel
%endif
BuildRequires:	libsodium-devel
%if %{with lua} || %{with heavy}
BuildRequires:	lua52-devel >= 5.2
%endif
%{?with_motif:BuildRequires:	motif-devel}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%if %{with perl} || %{with heavy}
BuildRequires:	perl-devel
%endif
%if %{with python} || %{with heavy}
BuildRequires:	python-devel >= 1:2.3
%endif
%if %{with python3} || %{with heavy}
BuildRequires:	python3-devel
%endif
%if %{with python} || %{with python3} || %{with heavy}
BuildRequires:	rpm-pythonprov
%endif
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.718
%if %{with ruby} || %{with heavy}
BuildRequires:	ruby-devel >= 1.6.0
%endif
%if %{with tcl} || %{with heavy}
BuildRequires:	tcl-devel >= 8.0
%endif
Obsoletes:	kvim < 4:7.0
%if %{with static}
BuildRequires:	acl-static
BuildRequires:	attr-static
BuildRequires:	glibc-static
%{?with_selinux:BuildRequires:	libselinux-static}
BuildRequires:	ncurses-static
%else
Provides:	%{name}-static = %{epoch}:%{version}-%{release}
Obsoletes:	elvis-static
Obsoletes:	nvi
Obsoletes:	vi
Obsoletes:	vim-minimal < 5.6
Obsoletes:	vim-static < %{epoch}:%{version}-%{release}
%endif
BuildRequires:	unzip
Suggests:	%{name}-rt = %{epoch}:%{version}-%{release}
Provides:	vi-editor
Provides:	vi
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-enhanced < 5.6
Obsoletes:	vim-ispell < 4:7.0
Obsoletes:	vim-ncurses < 5.6
Obsoletes:	vim-plugin-multvals < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# configure redefines it to =1
%define		filterout_cpp	-D_FORTIFY_SOURCE=[0-9]*
%define		filterout_c		-Wp,-D_FORTIFY_SOURCE=2

# that's example script
%define		_noautoreq	'/bin/csh'

# cflags get changed while configuring
%undefine	configure_cache

%description
Text editor similar to Vi. Important improvements: multiple windows,
multi-level undo, block highliting, folding, and many other.

%description -l cs.UTF-8
VIM je nový a vylepšený editor vycházející z klasického editoru vi. Vi
byl prvním celoobrazovkovým editorem pro Unix a je stále velmi
populární. VIM je obohacený funkcemi jako: podpora více oken,
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

%description -l hu.UTF-8
A Vi-hez hasonló texteditor. Néhány fontos bővítés: ablakkezelés,
többszintű undo, blokk kiemelés, kódrészletek összecsukása, és még sok
más...

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
finestre multiple, funzione "annulla" multilivello, evidenziazione dei
blocchi e altro.

%description -l pl.UTF-8
Edytor tekstu podobny do Vi. Ważne ulepszenia: możliwość pracy w wielu
oknach, wielopoziomowa opcja 'cofnij', bloki, podświetlanie składni,
folding i wiele innych.

%description -l pt.UTF-8
O VIM (VIsual editor iMproved) é uma versão melhorada e actualizada do
editor vi. O vi foi o primeiro verdadeiro editor baseado em ecrã para
o UNIX, e ainda é muito popular. O VIM melhora o vi acrescentando
novas potencialidades: janelas múltiplas, anulação multi-nível, realce
de blocos e mais.

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
Summary(pl.UTF-8):	Narzędzie do zamiany plików na postać szesnastkową i odwrotnie
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

%package heavy
Summary:	Full featured build of Vim
Summary(hu.UTF-8):	A Vim teljeskörű szolgáltatásait nyújtó verzió
Summary(pl.UTF-8):	W pełni funkcjonalna wersja Vima
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Provides:	vi-editor
Provides:	vi
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-enhanced < 5.6
Obsoletes:	vim-ispell < 4:7.0
Obsoletes:	vim-ncurses < 5.6
Obsoletes:	vim-plugin-multvals < 1.1

%description heavy
This package provides full featured version of Vim, which includes
support for Perl, Python, Ruby and Tcl scripting.

%description heavy -l hu.UTF-8
Ez a csomag a Vim teljeskörű szolgáltatásait nyújtó verzióját
tartalmazza, amelyben benne van a Perl, Python, Ruby és Tcl támogatás.

%description heavy -l pl.UTF-8
Pakiet ten dostarcza w pełni funkcjonalną wersję Vima, czyli
zawierającą obsługę skryptów w językach Perl, Python, Ruby oraz Tcl.

%package light
Summary:	Minimal build of Vim
Summary(pl.UTF-8):	Minimalna wersja vima
Group:		Applications/Editors/Vim
Provides:	vi-editor
Provides:	vi
Provides:	vim-editor = %{epoch}:%{version}-%{release}

%description light
This package provides light featured version of Vim.

%description light -l pl.UTF-8
Pakiet ten dostarcza minimalną wersję Vima.

%package -n vimx
Summary:	Vi IMproved - a Vi clone
Summary(pl.UTF-8):	Vi IMproved - klon edytora Vi
Group:		X11/Applications/Editors
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Provides:	vi-editor
Provides:	vi
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-enhanced < 5.6
Obsoletes:	vim-ispell < 4:7.0
Obsoletes:	vim-plugin-multvals < 1.1

%description -n vimx
This package provides console version of Vim, with support for basic
X11 features like system clipboard.

%description -n vimx -l pl.UTF-8
Pakiet ten dostarcza konsolową wersję Vima, posiadającą wsparcie dla
podstawowych funckcji X11, takich jak systemowy schowek.

%package static
Summary:	Statically linked Vim
Summary(hu.UTF-8):	A Vim statikus verziója
Summary(pl.UTF-8):	Statycznie skonsolidowany Vim
Group:		Applications/Editors/Vim
Provides:	vi-editor
Provides:	vi
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	elvis-static
Obsoletes:	nvi
Obsoletes:	vim-minimal < 5.6

%description static
Text editor similar to Vi. This version is built with minimal feature
and is installed in /bin as a rescue tool. The installation of this
package is STRONGLY recommended.

%description static -l hu.UTF-8
Vi-hez hasonló text editor. Ez a verzió a legminimálisabb
szolgáltatásokat nyújtja, és a /bin könyvtárba települ, mint egy mentő
eszköz. Ennek a csomagnak a telepítése ERŐSEN javallott.

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

%package rt
Summary:	Vim runtime files
Summary(cs.UTF-8):	Soubory nezbytné pro libovolný editor VIM
Summary(da.UTF-8):	Fælles filer som er nødvendige for enhver version af VIM editoren
Summary(de.UTF-8):	Die von allen Versionen des VIM-Editors benötigten gemeinsamen Dateien
Summary(es.UTF-8):	Ficheros comunes a todas las versiones de VIM
Summary(fr.UTF-8):	Fichiers communs indispensables pour toute version de l'éditeur VIM
Summary(hu.UTF-8):	A Vim futásidejű fájljai
Summary(id.UTF-8):	File umum yang dibutuhkan oleh semua versi editor VIM
Summary(is.UTF-8):	Grunnskrár sem allar útgáfur VIM ritilsins þurfa á að halda
Summary(it.UTF-8):	File comuni necessari per tutte le versioni dell'editor VIM
Summary(ja.UTF-8):	すべてのバージョンの VIM エディタで必要とされる共通ファイル
Summary(nb.UTF-8):	Felles filer som er nødvendige for enhver versjon av VIM editoren
Summary(pl.UTF-8):	Pliki przydatne dla edytora Vim
Summary(pt.UTF-8):	Os ficheiros comuns necessários para qualquer versão do editor VIM
Summary(ru.UTF-8):	Файлы, требуемые для любой версии редактора vim
Summary(sk.UTF-8):	Spoločné súbory potrebné pre všetky verzie editoru VIM
Summary(sl.UTF-8):	Skupne datoteke, potrebne s katerokoli različico urejevalnika VIM
Summary(sv.UTF-8):	De gemensamma filerna som behövs av alla versioner av redigeraren VIM
Summary(uk.UTF-8):	Файли, потрібні для будь-якої версії редактору vim
Summary(zh_CN.UTF-8):	任何版本的 VIM 编辑器所需的公用文件。
Group:		Applications/Editors/Vim
Requires:	rpm-whiteout >= 1.3
Requires:	vim-plugin-securemodelines
Obsoletes:	gvim-bonobo < 4:7.1.063
Obsoletes:	vim-common < 5.6
Obsoletes:	vim-syntax-docker < 1.10.1
Obsoletes:	vim-syntax-gitcommit < 2
Obsoletes:	vim-syntax-golang <= 1.3.3-1
Obsoletes:	vim-syntax-lxc-docker <= 0.9.0-1
Obsoletes:	vim-syntax-nginx <= 0.3.3-2
Obsoletes:	vim-syntax-upstart < 1.4
BuildArch:	noarch

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for Vim. If you want to take advantage of Vim more
powerful features, you should install this package.

%description rt -l cs.UTF-8
Tento balíček obsahuje společné soubory pro všechny další balíčky s
vim.

%description rt -l de.UTF-8
Das Paket vim-rt enthält Dateien, die jede VIM-Binärdatei für die
Ausführung benötigt.

%description rt -l fr.UTF-8
Le paquetage vim-rt contient des fichiers dont chaque fichier binaire
VIM a besoin pour fonctionner.

%description rt -l hu.UTF-8
Ez a csomag makrókat, dokumentációt, nyelvi konfigurációt és kézikönyv
oldalakat tartalmaz Vim-hez. Ha ki akarod használni a Vim
lehetőségeit, érdemes telepítened ezt a csomagot.

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
W tym pakiecie znajdują się makra, pliki konfiguracyjne i strony
podręcznika dla edytora Vim. Aby korzystać z zaawansowanych możliwości
Vima, należy zainstalować ten pakiet.

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

%package rt-extras
Summary:	Vim runtime extra files
Summary(pl.UTF-8):	Dodatkowe pliki uruchomieniowe Vima
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description rt-extras
This package contains more runtime extra files, not really useful. If
you want to take full advantage of Vim more powerful features, you
should install this package.

%description rt-extras -l pl.UTF-8
Ten pakiet zawiera dodatkowe pliki uruchomieniowe, nie tak bardzo
przydatne. Aby korzystać ze wszystkich możliwości Vima, należy
zainstalować ten pakiet.

%package doc
Summary:	Context Vim documentation
Summary(pl.UTF-8):	Dokumentacja kontekstowa do Vima
Group:		Applications/Editors/Vim
Requires(post,postun):	/usr/bin/vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc
This package contains Vim documentation accessible from vim itself
using :help command.

%description doc -l pl.UTF-8
Ten pakiet zawiera dokumentację do Vima dostępną z poziomu samego vima
za pomocą polecenia :help.

%package spell-en
Summary:	English dictionaries for VIMspell
Summary(pl.UTF-8):	Angielskie słowniki dla VIMspella
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description spell-en
English dictionaries for VIMspell.

%description spell-en -l pl.UTF-8
Angielskie słowniki dla VIMspella.

%package tutor
Summary:	Vim tutorial
Summary(hu.UTF-8):	Vim tutorial
Summary(pl.UTF-8):	Samouczek do Vima
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	mktemp
Requires:	vim-editor = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tutor
This package contains Vim tutorial.

%description tutor -l hu.UTF-8
Ez a csomag a vimtutor-t tartalmazza, amely egy gyakorlat-orientált
bevezető a Vim-hez.

%description tutor -l pl.UTF-8
Ten pakiet zawiera samouczek do Vima.

%package -n gvim-athena
Summary:	Vim for X Window built with Athena
Summary(hu.UTF-8):	A Vim X Window verziója, az Athena felhasználásával
Summary(pl.UTF-8):	Vim dla X Window korzystający z biblioteki Athena
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-X11 < 5.6
Obsoletes:	vim-athena < 5.6

%description -n gvim-athena
The classic Unix text editor now also under X Window System! This
version is built with Athena Widget Set.

%description -n gvim-athena -l hu.UTF-8
A Vim X Window verziója, az Athena Widgetkészlet felhasználásával.

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
Summary:	Vim for X Window System built with Motif
Summary(hu.UTF-8):	A Vim X Window verziója, a Motif felhasználásával
Summary(pl.UTF-8):	Vim dla systemu X Window korzystający z biblioteki Motif
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	gvim-lesstif < 5.6-5
Obsoletes:	vim-X11 < 5.6
Obsoletes:	vim-lesstif < 5.6

%description -n gvim-motif
The classic Unix text editor now also under X Window System! This
version is built with Motif.

%description -n gvim-motif -l hu.UTF-8
A Vim X Window verziója, a Motif Widgetkészlet felhasználásával.

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

%package -n gvim-gtk
Summary:	Vim for X Window System built with GTK+
Summary(hu.UTF-8):	A Vim X Window verziója, a GTK+ felhasználásával
Summary(pl.UTF-8):	Vim dla systemu X Window korzystający z biblioteki GTK+
Group:		Applications/Editors/Vim
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	%{name}-rt-extras = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-X11 < 5.6
Obsoletes:	vim-gtk < 5.6

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This
version is built with GTK+.

%description -n gvim-gtk -l hu.UTF-8
A Vim X Window verziója, a GTK+ Widgetkészlet felhasználásával.

%description -n gvim-gtk -l pl.UTF-8
Wersja edytora Vim pracująca w środowisku X Window z wykorzystaniem
biblioteki GTK+.

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
Summary:	Vim for X Window System built with GNOME
Summary(hu.UTF-8):	A Vim X Window verziója, a GNOME felhasználásával
Summary(pl.UTF-8):	Vim dla systemu X Window korzystający z biblioteki GNOME
Group:		Applications/Editors/Vim
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	%{name}-rt-extras = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-X11 < 5.6

%description -n gvim-gnome
The classic Unix text editor now also under X Window System! This
version is build with GNOME.

%description -n gvim-gnome -l hu.UTF-8
A Vim X Window verziója, a GNOME felhasználásával.

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

%package -n gvim-heavy
Summary:	Full featured build of Vim with X Window support
Summary(hu.UTF-8):	A gvim legteljesebb verziója
Summary(pl.UTF-8):	W pełni funkcjonalna wersja Vima z interfejsem dla X Window
Group:		Applications/Editors/Vim
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	%{name}-rt-extras = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-X11 < 5.6

%description -n gvim-heavy
This package provides full featured version of Vim, which includes
support for Perl, Python, Ruby and Tcl scripting, as well as GTK+2
GUI.

%description -n gvim-heavy -l hu.UTF-8
A gvim legteljesebb verziója, Perl, Python, Ruby és Tcl támogatással.

%description -n gvim-heavy -l pl.UTF-8
Pakiet ten dostarcza w pełni funkcjonalną wersję Vima, czyli
zawierającą obsługę skryptów w językach Perl, Python, Ruby oraz Tcl
jak również GUI GTK+2.

%prep
%setup -q

cp -p runtime/gvim.desktop gvim-athena.desktop
cp -p runtime/gvim.desktop gvim-gnome.desktop
cp -p runtime/gvim.desktop gvim-gtk.desktop
cp -p runtime/gvim.desktop gvim-motif.desktop

%patch -P0 -p1

%patch -P2 -p1

%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

%patch -P10 -p1
%patch -P11 -p1

%patch -P14 -p1
%patch -P15 -p1
%patch -P17 -p1
%patch -P18 -p1

%patch -P20 -p1
%patch -P21 -p1
%patch -P22 -p1
%patch -P23 -p1
%patch -P24 -p1
%patch -P25 -p1
%{?with_home_etc:%patch -P26 -p1}

# autopaste patch - automatically switch to paste mode
# when `really fast typing' situation happens
%patch -P27 -p1
%patch -P28 -p1
%patch -P29 -p1
%patch -P30 -p1
%patch -P32 -p1

%patch -P34 -p1
%patch -P35 -p1

%patch -P38 -p1
%patch -P39 -p1
%patch -P40 -p1
%patch -P41 -p1

cp -p %{SOURCE20} runtime/syntax
cp -p %{SOURCE22} runtime/syntax
cp -p %{SOURCE30} runtime/colors
cp -p %{SOURCE31} runtime/colors
cp -p %{SOURCE32} runtime/colors

%{__unzip} -qd runtime/doc %{SOURCE2}

# not info files but some binary files for Amiga:
# Amiga Workbench drawer icon
# Amiga Workbench project icon
# Amiga Workbench tool icon
find -name '*.info' | xargs rm -v

%build
cd src
%{__autoconf}
# needed to prevent deconfiguring
cp -f configure auto
install -d bin

build() {
	set -x
	local target=$1
	shift

	%configure \
%if "%{pld_release}" == "ac"
		--with-tlib="ncurses -ltinfo"
%else
		--with-tlib="ncursesw"
%endif

	%{__make} -j1 distclean
	# add common options, can override (disable) if needed with args
	%configure \
		--%{!?with_lua:dis}%{?with_lua:en}able-luainterp \
		--%{!?with_perl:dis}%{?with_perl:en}able-perlinterp \
		--%{!?with_python:dis}%{?with_python:en}able-pythoninterp \
		--%{!?with_python3:dis}%{?with_python3:en}able-python3interp \
		--%{!?with_ruby:dis}%{?with_ruby:en}able-rubyinterp \
		--%{!?with_tcl:dis}%{?with_tcl:en}able-tclinterp \
		%{!?with_selinux:--disable-selinux} \
		--enable-cscope \
		--enable-gpm \
		--enable-multibyte \
		--enable-nls \
%if "%{pld_release}" == "ac"
		--with-tlib="ncurses -ltinfo" \
%else
		--with-tlib="ncursesw" \
%endif
		--with-modified-by="PLD Linux Distribution" \
		--with-compiledby="PLD Linux Distribution" \
		"$@"

	%{__make} vim
	mv -f vim bin/$target
}

%if %{with static}
LDFLAGS="%{rpmldflags} -static"
build vim.static \
	--disable-gui \
	--without-x \
	--with-features=small \
	--disable-canberra \
	--disable-luainterp \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-python3interp \
	--disable-rubyinterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--enable-multibyte \
	--disable-nls

LDFLAGS="%{rpmldflags}"
%endif

%if %{with light}
build vim.light \
	--disable-gui \
	--without-x \
	--with-features=small \
	--disable-canberra \
	--disable-luainterp \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-python3interp \
	--disable-rubyinterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-nls
%endif

build vim.ncurses \
	--disable-gui \
	%{__with_without x} \
	--disable-canberra \
	--with-features=huge

%if %{with x11}
build vimx \
	--disable-gui \
	--with-x \
	--disable-canberra \
	--with-features=huge
%endif

%if %{with athena}
build gvim.athena \
	--with-features=huge \
	--enable-gui=athena \
	--with-x \
	--enable-fontset \
	--disable-canberra \
	--disable-gpm \
	--without-gnome

%endif

%if %{with motif}
build gvim.motif \
	--with-features=huge \
	--enable-gui=motif \
	--with-x \
	--enable-multibyte \
	--enable-fontset \
	--disable-canberra \
	--disable-gpm \
	--without-gnome

%endif

%if %{with gtk}
build gvim.gtk \
	--with-features=huge \
%if %{with gtk3}
	--enable-gui=gtk3 \
	--enable-gtk3-check \
%else
	--enable-gui=gtk2 \
	--enable-gtk2-check \
%endif
	--with-x \
	--disable-canberra \
	--disable-gpm

%endif

%if %{with gnome}
build gvim.gnome \
	--with-features=huge \
	--enable-gui=gnome2 \
	--enable-gtk2-check \
	--enable-gnome-check \
	--with-x \
	--disable-gpm

%endif

# vim.heavy / gvim.heavy
%if %{with heavy}
build vim.heavy \
	--with-features=huge \
	--disable-gui \
	--without-x \
	--enable-luainterp \
	--enable-perlinterp \
	--enable-pythoninterp \
	--enable-python3interp \
	--enable-rubyinterp \
	--enable-tclinterp \
	--disable-canberra \
	--disable-gpm

build gvim.heavy \
	--with-features=huge \
	--enable-gui=gnome2 \
	--enable-gtk2-check \
	--enable-gnome-check \
	--with-x \
	--enable-luainterp \
	--enable-perlinterp \
	--enable-pythoninterp \
	--enable-python3interp \
	--enable-rubyinterp \
	--enable-tclinterp \
	--disable-gpm
%endif

%{__make} xxd/xxd languages

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim/ftdetect} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# generic gvim from upstream, but we have bunch of subpackages
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/gvim.desktop

# fix nb/no
%{__mv} $RPM_BUILD_ROOT%{_datadir}/vim/tutor/tutor1.n{o,b}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/vim/tutor/tutor1.n{o,b}.utf-8
%{__mv} $RPM_BUILD_ROOT%{_datadir}/vim/lang/menu_n{o,b}.latin1.vim
%{__mv} $RPM_BUILD_ROOT%{_datadir}/vim/lang/menu_n{o,b}.utf-8.vim
%{__mv} $RPM_BUILD_ROOT%{_datadir}/vim/lang/menu_n{o,b}_no.latin1.vim
%{__mv} $RPM_BUILD_ROOT%{_datadir}/vim/lang/menu_n{o,b}_no.utf-8.vim

# remove unsupported locales
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ko.UTF-8
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/no
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/zh_CN.UTF-8
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/zh_TW.UTF-8
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cs.cp1250
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ja.sjis
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ja.euc-jp
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pl.UTF-8
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pl.cp1250
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ru.cp1251
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sk.cp1250
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/uk.cp1251
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/zh_CN.cp936
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/lang/menu_zh_{cn,tw}.utf-8.vim

%find_lang %{name}

%{__rm} $RPM_BUILD_ROOT%{_bindir}/*

%if %{with static}
install -p src/bin/vim.ncurses	$RPM_BUILD_ROOT%{_bindir}/vim
install -p src/bin/vim.static	$RPM_BUILD_ROOT/bin/vi
%else
install -p src/bin/vim.ncurses	$RPM_BUILD_ROOT/bin/vi
ln -sf /bin/vi		$RPM_BUILD_ROOT%{_bindir}/vim
%endif
%if %{with x11}
install -p src/bin/vimx	$RPM_BUILD_ROOT%{_bindir}/vimx
%endif
install -p src/xxd/xxd	$RPM_BUILD_ROOT%{_bindir}/xxd
install -p src/vimtutor	$RPM_BUILD_ROOT%{_bindir}/vimtutor

echo ".so man1/vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vi.1
echo ".so man1/vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1

# not supported directories
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/??.*/

mv -f $RPM_BUILD_ROOT{%{_datadir}/vim/vimrc_example.vim,%{_sysconfdir}/vim/vimrc}
mv -f $RPM_BUILD_ROOT{%{_datadir}/vim/gvimrc_example.vim,%{_sysconfdir}/vim/gvimrc}

ln -sf vim $RPM_BUILD_ROOT%{_bindir}/rvim
ln -sf vim $RPM_BUILD_ROOT%{_bindir}/vimdiff
ln -sf vi  $RPM_BUILD_ROOT/bin/ex
ln -sf vi  $RPM_BUILD_ROOT/bin/view
ln -sf vi  $RPM_BUILD_ROOT/bin/rview

%if %{with athena}
install -p src/bin/gvim.athena $RPM_BUILD_ROOT%{_bindir}/gvim.athena
cp -p gvim-athena.desktop $RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with motif}
install -p src/bin/gvim.motif $RPM_BUILD_ROOT%{_bindir}/gvim.motif
cp -p gvim-motif.desktop $RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gnome}
install -p src/bin/gvim.gnome $RPM_BUILD_ROOT%{_bindir}/gvim.gnome
cp -p gvim-gnome.desktop $RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gtk}
install -p src/bin/gvim.gtk	$RPM_BUILD_ROOT%{_bindir}/gvim.gtk
cp -p gvim-gtk.desktop $RPM_BUILD_ROOT%{_desktopdir}
ln -sf gvim.gtk		$RPM_BUILD_ROOT%{_bindir}/gvim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/eview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/evim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gvimdiff
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgvim
%endif
%if %{with heavy}
install -p src/bin/vim.heavy	$RPM_BUILD_ROOT%{_bindir}
install -p src/bin/gvim.heavy	$RPM_BUILD_ROOT%{_bindir}
%endif
%if %{with light}
install -p src/bin/vim.light	$RPM_BUILD_ROOT%{_bindir}
%endif

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT{%{_iconsdir}/hicolor/48x48/apps,%{_pixmapsdir}}/gvim.png

# locolor scheme no longer supported
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/locolor

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/{doc,{after/,}{compiler,ftdetect,ftplugin,indent,plugin,spell,syntax}}
> $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/doc/tags

# separate package
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/{ftplugin,syntax}/spec.vim

# unuseful
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/vim/tools
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/bugreport.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/spell/check_locales.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/spell/cleanadd.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/spell/fixdup.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/doc/vim2html.pl

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database

%postun
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%post -n gvim-athena
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database

%postun -n gvim-athena
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database

%post -n gvim-motif
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database

%postun -n gvim-motif
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database

%post -n gvim-gtk
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database
%update_icon_cache hicolor

%postun -n gvim-gtk
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database
%update_icon_cache hicolor

%post -n gvim-gnome
%update_desktop_database_post
%update_icon_cache hicolor

%postun -n gvim-gnome
%update_desktop_database_postun
%update_icon_cache hicolor

%post -n gvim-heavy
%update_icon_cache hicolor

%postun -n gvim-heavy
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rvim
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/vimdiff
%{_mandir}/man1/rvim.1*
%{_mandir}/man1/vimdiff.1*
%lang(da) %{_mandir}/da/man1/rvim.1*
%lang(da) %{_mandir}/da/man1/vimdiff.1*
%lang(de) %{_mandir}/de/man1/rvim.1*
%lang(fi) %{_mandir}/fi/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/vimdiff.1*
%lang(id) %{_mandir}/id/man1/rvim.1*
%lang(it) %{_mandir}/it/man1/rvim.1*
%lang(it) %{_mandir}/it/man1/vimdiff.1*
%lang(ja) %{_mandir}/ja/man1/rvim.1*
%lang(ja) %{_mandir}/ja/man1/vimdiff.1*
%lang(pl) %{_mandir}/pl/man1/rvim.1*
%lang(pl) %{_mandir}/pl/man1/vimdiff.1*
%lang(ru) %{_mandir}/ru/man1/rvim.1*
%lang(ru) %{_mandir}/ru/man1/vimdiff.1*
%lang(tr) %{_mandir}/tr/man1/rvim.1*
%lang(tr) %{_mandir}/tr/man1/vimdiff.1*
%{_desktopdir}/vim.desktop

%if %{with static}
%files static
%endif
%defattr(644,root,root,755)
%attr(755,root,root) /bin/ex
%attr(755,root,root) /bin/rview
%attr(755,root,root) /bin/vi
%attr(755,root,root) /bin/view
%{_mandir}/man1/vi.1*
%{_mandir}/man1/ex.1*
%{_mandir}/man1/view.1*
%{_mandir}/man1/rview.1*
%lang(da) %{_mandir}/da/man1/ex.1*
%lang(da) %{_mandir}/da/man1/rview.1*
%lang(da) %{_mandir}/da/man1/view.1*
%lang(de) %{_mandir}/de/man1/ex.1*
%lang(de) %{_mandir}/de/man1/rview.1*
%lang(de) %{_mandir}/de/man1/view.1*
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
#%lang(it) %{_mandir}/it/man1/vi.1*
%lang(it) %{_mandir}/it/man1/ex.1*
%lang(it) %{_mandir}/it/man1/view.1*
%lang(it) %{_mandir}/it/man1/rview.1*
%lang(ja) %{_mandir}/ja/man1/ex.1*
%lang(ja) %{_mandir}/ja/man1/view.1*
%lang(ja) %{_mandir}/ja/man1/rview.1*
%lang(pl) %{_mandir}/pl/man1/vi.1*
%lang(pl) %{_mandir}/pl/man1/ex.1*
%lang(pl) %{_mandir}/pl/man1/view.1*
%lang(pl) %{_mandir}/pl/man1/rview.1*
#%lang(ru) %{_mandir}/ru/man1/vi.1*
%lang(ru) %{_mandir}/ru/man1/ex.1*
%lang(ru) %{_mandir}/ru/man1/view.1*
%lang(ru) %{_mandir}/ru/man1/rview.1*
%lang(tr) %{_mandir}/tr/man1/ex.1*
%lang(tr) %{_mandir}/tr/man1/view.1*
%lang(tr) %{_mandir}/tr/man1/rview.1*

%files -n xxd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxd
%{_mandir}/man1/xxd.1*
%lang(fr) %{_mandir}/fr/man1/xxd.1*
%lang(it) %{_mandir}/it/man1/xxd.1*
%lang(ja) %{_mandir}/ja/man1/xxd.1*
%lang(pl) %{_mandir}/pl/man1/xxd.1*
%lang(ru) %{_mandir}/ru/man1/xxd.1*

%files rt -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vim
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vim/gvimrc

%dir %{_datadir}/vim
%dir %{_datadir}/vim/doc
%verify(not md5 mtime size) %{_datadir}/vim/doc/tags
%lang(pl) %verify(not md5 mtime size) %{_datadir}/vim/doc/tags-pl
%verify(not md5 mtime size) %{_datadir}/vim/vimfiles/doc/tags

%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/doc
%dir %{_datadir}/vim/vimfiles/after
%dir %{_datadir}/vim/vimfiles/after/compiler
%dir %{_datadir}/vim/vimfiles/after/ftdetect
%dir %{_datadir}/vim/vimfiles/after/ftplugin
%dir %{_datadir}/vim/vimfiles/after/indent
%dir %{_datadir}/vim/vimfiles/after/plugin
%dir %{_datadir}/vim/vimfiles/after/spell
%dir %{_datadir}/vim/vimfiles/after/syntax
%dir %{_datadir}/vim/vimfiles/compiler
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/ftplugin
%dir %{_datadir}/vim/vimfiles/indent
%dir %{_datadir}/vim/vimfiles/plugin
%dir %{_datadir}/vim/vimfiles/spell
%dir %{_datadir}/vim/vimfiles/syntax

%{_datadir}/vim/*.vim

%dir %{_datadir}/vim/autoload
%{_datadir}/vim/autoload/*complete.vim
%doc %{_datadir}/vim/autoload/README.txt
%dir %{_datadir}/vim/autoload/dist
%{_datadir}/vim/autoload/dist/ft.vim
%{_datadir}/vim/autoload/dist/json.vim
%{_datadir}/vim/autoload/dist/man.vim
%{_datadir}/vim/autoload/dist/script.vim
%{_datadir}/vim/autoload/dist/vim.vim
%{_datadir}/vim/autoload/dist/vim9.vim
%{_datadir}/vim/autoload/dist/vimindent.vim

%dir %{_datadir}/vim/ftdetect

%dir %{_datadir}/vim/ftplugin
%doc %{_datadir}/vim/ftplugin/README.txt
%{_datadir}/vim/ftplugin/*.vim
%{_datadir}/vim/ftplugin/logtalk.dict

%dir %{_datadir}/vim/import
%dir %{_datadir}/vim/import/dist
%{_datadir}/vim/import/dist/vimhelp.vim
%{_datadir}/vim/import/dist/vimhighlight.vim

%dir %{_datadir}/vim/indent
%doc %{_datadir}/vim/indent/README.txt
%{_datadir}/vim/indent/*.vim

%dir %{_datadir}/vim/keymap
%doc %{_datadir}/vim/keymap/README.txt
%{_datadir}/vim/keymap/*.vim

%{_datadir}/vim/pack

%dir %{_datadir}/vim/plugin
%doc %{_datadir}/vim/plugin/README.txt

%{_datadir}/vim/syntax

%dir %{_datadir}/vim/colors
%doc %{_datadir}/vim/colors/README.txt
%{_datadir}/vim/colors/*.vim
%dir %{_datadir}/vim/colors/lists
%{_datadir}/vim/colors/lists/*.vim
%dir %{_datadir}/vim/colors/tools
%{_datadir}/vim/colors/tools/check_colors.vim

%dir %{_datadir}/vim/lang
%doc %{_datadir}/vim/lang/README*

%lang(af) %{_datadir}/vim/lang/menu_af*
%lang(ca) %{_datadir}/vim/lang/menu_ca*
%lang(cs) %{_datadir}/vim/lang/menu_cs*
%lang(cs) %{_datadir}/vim/lang/menu_*czech*
%lang(da) %{_datadir}/vim/lang/menu_da*
%lang(de) %{_datadir}/vim/lang/menu_de*
%lang(de) %{_datadir}/vim/lang/menu_*german*
%lang(en_GB) %{_datadir}/vim/lang/menu_en_gb*
%lang(en_GB) %{_datadir}/vim/lang/menu_*english*
%lang(eo) %{_datadir}/vim/lang/menu_eo.utf-8.vim
%lang(eo) %{_datadir}/vim/lang/menu_eo_eo.utf-8.vim
%lang(eo) %{_datadir}/vim/lang/menu_eo_xx.utf-8.vim
%lang(es) %{_datadir}/vim/lang/menu_es*
%lang(es) %{_datadir}/vim/lang/menu_*spanish*
%lang(fi) %{_datadir}/vim/lang/menu_fi.latin1.vim
%lang(fi) %{_datadir}/vim/lang/menu_fi.utf-8.vim
%lang(fi) %{_datadir}/vim/lang/menu_fi_fi.latin1.vim
%lang(fi) %{_datadir}/vim/lang/menu_fi_fi.utf-8.vim
%lang(fi) %{_datadir}/vim/lang/menu_finnish_finland.1252.vim
%lang(fr) %{_datadir}/vim/lang/menu_fr*
%lang(hu) %{_datadir}/vim/lang/menu_hu*
%lang(is) %{_datadir}/vim/lang/menu_is*
%lang(it) %{_datadir}/vim/lang/menu_it*
%lang(ja) %{_datadir}/vim/lang/menu_ja*
%lang(ko) %{_datadir}/vim/lang/menu_ko*
%lang(nl) %{_datadir}/vim/lang/menu_nl*
%lang(nb) %{_datadir}/vim/lang/menu_nb*
%lang(pl) %{_datadir}/vim/lang/menu_pl*
%lang(pl) %{_datadir}/vim/lang/menu_*polish*
%lang(pt) %{_datadir}/vim/lang/menu_pt*
%lang(ru) %{_datadir}/vim/lang/menu_ru*
%lang(sk) %{_datadir}/vim/lang/menu_sk*
%lang(sk) %{_datadir}/vim/lang/menu_*slovak*
%lang(sl) %{_datadir}/vim/lang/menu_sl_si*
%lang(sr) %{_datadir}/vim/lang/menu_sr*
%lang(sv) %{_datadir}/vim/lang/menu_sv*
%lang(tr) %{_datadir}/vim/lang/menu_tr*
%lang(uk) %{_datadir}/vim/lang/menu_uk*
%lang(vi) %{_datadir}/vim/lang/menu_vi*
%lang(zh_CN) %{_datadir}/vim/lang/menu_zh.cp936*
%lang(zh_CN) %{_datadir}/vim/lang/menu_zh.gb2312*
%lang(zh_CN) %{_datadir}/vim/lang/menu_zh_cn*
%lang(zh_CN) %{_datadir}/vim/lang/menu_*chinese*gb*
%lang(zh_TW) %{_datadir}/vim/lang/menu_zh.cp950*
%lang(zh_TW) %{_datadir}/vim/lang/menu_zh.big5*
%lang(zh_TW) %{_datadir}/vim/lang/menu_zh_tw*
%lang(zh_TW) %{_datadir}/vim/lang/menu_*taiwan*

%dir %{_datadir}/vim/spell
%{_datadir}/vim/spell/spell.vim
%lang(he) %{_datadir}/vim/spell/he.*
%lang(yi) %{_datadir}/vim/spell/yi.*

%{_mandir}/man1/vim.1*
%lang(da) %{_mandir}/da/man1/vim.1*
%lang(de) %{_mandir}/de/man1/vim.1*
%lang(fi) %{_mandir}/fi/man1/vim.1*
%lang(fr) %{_mandir}/fr/man1/vim.1*
%lang(id) %{_mandir}/id/man1/vim.1*
%lang(it) %{_mandir}/it/man1/vim.1*
%lang(ja) %{_mandir}/ja/man1/vim.1*
%lang(pl) %{_mandir}/pl/man1/vim.1*
%lang(ru) %{_mandir}/ru/man1/vim.1*
%lang(tr) %{_mandir}/tr/man1/vim.1*
%{_pixmapsdir}/gvim.png

# plugins in base -rt package
%{_datadir}/vim/autoload/gzip.vim
%{_datadir}/vim/plugin/gzip.vim
%{_datadir}/vim/plugin/matchparen.vim

%files rt-extras
%defattr(644,root,root,755)
%{_datadir}/vim/plugin/*.vim
%{_datadir}/vim/autoload/*.vim
%exclude %{_datadir}/vim/autoload/*complete.vim
%{_datadir}/vim/autoload/cargo
%{_datadir}/vim/autoload/rust
%{_datadir}/vim/autoload/xml
%{_datadir}/vim/compiler
%{_datadir}/vim/macros
%{_datadir}/vim/print

# plugins in base -rt package
%exclude %{_datadir}/vim/autoload/gzip.vim
%exclude %{_datadir}/vim/plugin/gzip.vim
%exclude %{_datadir}/vim/plugin/matchparen.vim

%files doc
%defattr(644,root,root,755)
# English
%{_datadir}/vim/doc/*.txt

# Polish
%lang(pl) %{_datadir}/vim/doc/*.plx

%files tutor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%dir %{_datadir}/vim/tutor
%{_datadir}/vim/tutor/tutor.tutor
%{_datadir}/vim/tutor/tutor.tutor.json
%{_datadir}/vim/tutor/tutor.vim
%{_datadir}/vim/tutor/tutor1
%{_datadir}/vim/tutor/tutor1.utf-8
%{_datadir}/vim/tutor/tutor2
%{_datadir}/vim/tutor/tutor2.utf-8
%{_datadir}/vim/tutor/en

%{_datadir}/vim/tutor/README.txt
%lang(el) %{_datadir}/vim/tutor/README.el.cp737.txt
%lang(el) %{_datadir}/vim/tutor/README.el.txt
%lang(ru) %{_datadir}/vim/tutor/README.ru.utf-8.txt

%lang(de) %{_datadir}/vim/tutor/tutor1.bar
%lang(de) %{_datadir}/vim/tutor/tutor1.bar.utf-8
%lang(bg) %{_datadir}/vim/tutor/tutor1.bg.utf-8
%lang(ca) %{_datadir}/vim/tutor/tutor1.ca
%lang(ca) %{_datadir}/vim/tutor/tutor1.ca.utf-8
%lang(cs) %{_datadir}/vim/tutor/tutor1.cs
%lang(cs) %{_datadir}/vim/tutor/tutor1.cs.cp1250
%lang(cs) %{_datadir}/vim/tutor/tutor1.cs.utf-8
%lang(da) %{_datadir}/vim/tutor/tutor1.da
%lang(da) %{_datadir}/vim/tutor/tutor1.da.utf-8
%lang(de) %{_datadir}/vim/tutor/tutor1.de
%lang(de) %{_datadir}/vim/tutor/tutor1.de.utf-8
%lang(el) %{_datadir}/vim/tutor/tutor1.el
%lang(el) %{_datadir}/vim/tutor/tutor1.el.cp737
%lang(el) %{_datadir}/vim/tutor/tutor1.el.utf-8
%lang(eo) %{_datadir}/vim/tutor/tutor1.eo
%lang(eo) %{_datadir}/vim/tutor/tutor1.eo.utf-8
%lang(es) %{_datadir}/vim/tutor/tutor1.es
%lang(es) %{_datadir}/vim/tutor/tutor1.es.utf-8
%lang(fr) %{_datadir}/vim/tutor/tutor1.fr
%lang(fr) %{_datadir}/vim/tutor/tutor1.fr.utf-8
%lang(gl) %{_datadir}/vim/tutor/tutor1.gl
%lang(gl) %{_datadir}/vim/tutor/tutor1.gl.utf-8
%lang(gl) %{_datadir}/vim/tutor/tutor2.gl
%lang(gl) %{_datadir}/vim/tutor/tutor2.gl.utf-8
%lang(hr) %{_datadir}/vim/tutor/tutor1.hr
%lang(hr) %{_datadir}/vim/tutor/tutor1.hr.cp1250
%lang(hr) %{_datadir}/vim/tutor/tutor1.hr.utf-8
%lang(hu) %{_datadir}/vim/tutor/tutor1.hu
%lang(hu) %{_datadir}/vim/tutor/tutor1.hu.cp1250
%lang(hu) %{_datadir}/vim/tutor/tutor1.hu.utf-8
%lang(it) %{_datadir}/vim/tutor/tutor1.it
%lang(it) %{_datadir}/vim/tutor/tutor1.it.utf-8
%lang(it) %{_datadir}/vim/tutor/tutor2.it
%lang(it) %{_datadir}/vim/tutor/tutor2.it.utf-8
%lang(it) %{_datadir}/vim/tutor/it
%lang(ja) %{_datadir}/vim/tutor/tutor1.ja.euc
%lang(ja) %{_datadir}/vim/tutor/tutor1.ja.sjis
%lang(ja) %{_datadir}/vim/tutor/tutor1.ja.utf-8
%lang(ko) %{_datadir}/vim/tutor/tutor1.ko
%lang(ko) %{_datadir}/vim/tutor/tutor1.ko.euc
%lang(ko) %{_datadir}/vim/tutor/tutor1.ko.utf-8
%lang(lt) %{_datadir}/vim/tutor/tutor1.lt.utf-8
%lang(lv) %{_datadir}/vim/tutor/tutor1.lv.utf-8
%lang(nl) %{_datadir}/vim/tutor/tutor1.nl
%lang(nl) %{_datadir}/vim/tutor/tutor1.nl.utf-8
%lang(nb) %{_datadir}/vim/tutor/tutor1.nb
%lang(nb) %{_datadir}/vim/tutor/tutor1.nb.utf-8
%lang(pl) %{_datadir}/vim/tutor/tutor1.pl
%lang(pl) %{_datadir}/vim/tutor/tutor1.pl.cp1250
%lang(pl) %{_datadir}/vim/tutor/tutor1.pl.utf-8
%lang(pt) %{_datadir}/vim/tutor/tutor1.pt
%lang(pt) %{_datadir}/vim/tutor/tutor1.pt.utf-8
%lang(ru) %{_datadir}/vim/tutor/tutor1.ru
%lang(ru) %{_datadir}/vim/tutor/tutor1.ru.cp1251
%lang(ru) %{_datadir}/vim/tutor/tutor1.ru.utf-8
%lang(ru) %{_datadir}/vim/tutor/tutor2.ru.utf-8
%lang(ru) %{_datadir}/vim/tutor/ru
%lang(sk) %{_datadir}/vim/tutor/tutor1.sk
%lang(sk) %{_datadir}/vim/tutor/tutor1.sk.cp1250
%lang(sk) %{_datadir}/vim/tutor/tutor1.sk.utf-8
%lang(sr) %{_datadir}/vim/tutor/tutor1.sr.cp1250
%lang(sr) %{_datadir}/vim/tutor/tutor1.sr.utf-8
%lang(sr) %{_datadir}/vim/tutor/tutor2.sr.utf-8
%lang(sr) %{_datadir}/vim/tutor/sr
%lang(sv) %{_datadir}/vim/tutor/tutor1.sv
%lang(sv) %{_datadir}/vim/tutor/tutor1.sv.utf-8
%lang(tr) %{_datadir}/vim/tutor/tutor1.tr.iso9
%lang(tr) %{_datadir}/vim/tutor/tutor1.tr.utf-8
%lang(uk) %{_datadir}/vim/tutor/tutor1.uk.utf-8
%lang(vi) %{_datadir}/vim/tutor/tutor1.vi.utf-8
%lang(zh_CN) %{_datadir}/vim/tutor/tutor1.zh_cn.utf-8
%lang(zh_TW) %{_datadir}/vim/tutor/tutor1.zh.big5
%lang(zh_TW) %{_datadir}/vim/tutor/tutor1.zh.euc
%lang(zh_TW) %{_datadir}/vim/tutor/tutor1.zh.utf-8
%lang(zh_TW) %{_datadir}/vim/tutor/tutor1.zh_tw.utf-8

%{_mandir}/man1/vimtutor.1*
%lang(da) %{_mandir}/da/man1/vimtutor.1*
%lang(fr) %{_mandir}/fr/man1/vimtutor.1*
%lang(it) %{_mandir}/it/man1/vimtutor.1*
%lang(ja) %{_mandir}/ja/man1/vimtutor.1*
%lang(pl) %{_mandir}/pl/man1/vimtutor.1*
%lang(ru) %{_mandir}/ru/man1/vimtutor.1*
%lang(tr) %{_mandir}/tr/man1/vimtutor.1*

%if %{with x11}
%files -n vimx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimx
%endif

%if %{with heavy}
%files heavy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim.heavy
%endif

%if %{with light}
%files light
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim.light
%endif

%files spell-en
%defattr(644,root,root,755)
%{_datadir}/vim/spell/en.*.*

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

%if %{with gtk}
%files -n gvim-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvim.gtk
%attr(755,root,root) %verify(not link) %{_bindir}/gvim
%attr(755,root,root) %{_bindir}/eview
%attr(755,root,root) %{_bindir}/evim
%attr(755,root,root) %{_bindir}/gview
%attr(755,root,root) %{_bindir}/gvimdiff
%attr(755,root,root) %{_bindir}/rgview
%attr(755,root,root) %{_bindir}/rgvim
%{_mandir}/man1/eview.1*
%{_mandir}/man1/evim.1*
%{_mandir}/man1/gview.1*
%{_mandir}/man1/gvim.1*
%{_mandir}/man1/gvimdiff.1*
%{_mandir}/man1/rgview.1*
%{_mandir}/man1/rgvim.1*
%lang(da) %{_mandir}/da/man1/gvi*.1*
%lang(da) %{_mandir}/da/man1/rgv*.1*
%lang(de) %{_mandir}/de/man1/gvi*.1*
%lang(de) %{_mandir}/de/man1/rgv*.1*
%lang(fi) %{_mandir}/fi/man1/gvi*.1*
%lang(fi) %{_mandir}/fi/man1/rgv*.1*
%lang(fr) %{_mandir}/fr/man1/eview.1*
%lang(fr) %{_mandir}/fr/man1/evim.1*
%lang(fr) %{_mandir}/fr/man1/gvi*.1*
%lang(fr) %{_mandir}/fr/man1/rgv*.1*
%lang(id) %{_mandir}/id/man1/gvi*.1*
%lang(id) %{_mandir}/id/man1/rgv*.1*
%lang(it) %{_mandir}/it/man1/eview.1*
%lang(it) %{_mandir}/it/man1/evim.1*
%lang(it) %{_mandir}/it/man1/gvi*.1*
%lang(it) %{_mandir}/it/man1/rgv*.1*
%lang(ja) %{_mandir}/ja/man1/eview.1*
%lang(ja) %{_mandir}/ja/man1/evim.1*
%lang(ja) %{_mandir}/ja/man1/gvi*.1*
%lang(ja) %{_mandir}/ja/man1/rgv*.1*
%lang(pl) %{_mandir}/pl/man1/eview.1*
%lang(pl) %{_mandir}/pl/man1/evim.1*
%lang(pl) %{_mandir}/pl/man1/gvi*.1*
%lang(pl) %{_mandir}/pl/man1/rgv*.1*
%lang(ru) %{_mandir}/ru/man1/eview.1*
%lang(ru) %{_mandir}/ru/man1/evim.1*
%lang(ru) %{_mandir}/ru/man1/gvi*.1*
%lang(ru) %{_mandir}/ru/man1/rgv*.1*
%lang(tr) %{_mandir}/tr/man1/eview.1*
%lang(tr) %{_mandir}/tr/man1/evim.1*
%lang(tr) %{_mandir}/tr/man1/gvi*.1*
%lang(tr) %{_mandir}/tr/man1/rgv*.1*
%{_desktopdir}/gvim-gtk.desktop
%endif

%if %{with gnome}
%files -n gvim-gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvim.gnome
%{_desktopdir}/gvim-gnome.desktop
%endif

%if %{with heavy}
%files -n gvim-heavy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvim.heavy
%endif
