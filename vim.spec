#
# Conditional build:
%bcond_without	static		# don't build static version
%bcond_without	athena		# don't build Athena Widgets-based gvim
%bcond_without	motif		# don't build Motif-based gvim
%bcond_without	gtk		# don't build GTK+-based gvim support
%bcond_without	gnome		# don't build GNOME-based gvim support
%bcond_without	heavy		# don't build heavy (full-featured GNOME-based gvim/vim)
%bcond_without	gui		# don't build any GUI
%bcond_without	light		# don't build light (minimal, ncurses, but not static)
%bcond_with	perl		# with Perl interp in vim package
%bcond_with	python		# with Python interp in vim package
%bcond_with	ruby		# with Ruby interp in vim package
%bcond_with	tcl		# with Tcl interp
%bcond_without	selinux		# without selinux support
%bcond_without	home_etc	# without home_etc support

%if %{without gui}
%undefine	with_athena
%undefine	with_motif
%undefine	with_gtk
%undefine	with_gnome
%endif

# Command to check for latest patch:
# wget ftp://ftp.vim.org/pub/editors/vim/patches/7.4/MD5SUMS -O sources
# tail -n1 sources | awk '{print $2}'
# VCS Commits: https://code.google.com/p/vim/source/browse/

%define		ver		7.4
%define		patchlevel	884
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
Version:	%{ver}.%{patchlevel}
Release:	%{rel}
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/vim/unix/%{name}-%{ver}.tar.bz2
# Source0-md5:	607e135c559be642f210094ad023dc65
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	bc4d1e115ca506ad7751b9bd2b773a7f
Source2:	http://skawina.eu.org/mikolaj/usr_doc_pl.zip
# Source2-md5:	ff96284b1c913d55cf0877839b34d490
Source10:	g%{name}-athena.desktop
Source11:	g%{name}-motif.desktop
Source12:	g%{name}-gtk.desktop
Source13:	g%{name}-gnome.desktop
Source14:	%{name}.desktop
Source15:	update-source.sh
# syntax files
# http://www.vim.org/scripts/script.php?script_id=1491 (0.7.5)
Source20:	javascript.vim
# http://www.vim.org/scripts/script.php?script_id=447 (20040206)
Source22:	exim.vim
# color schemes
# http://www.vim.org/scripts/script.php?script_id=415 (1.15)
Source30:	zenburn.vim
# http://www.vim.org/scripts/script.php?script_id=92 (1.0)
Source31:	borland.vim
# http://www.vim.org/scripts/script.php?script_id=368 (1.2.5)
Source32:	oceandeep.vim
# http://www.vim.org/scripts/script.php?script_id=1464 (2.6.3)
Source33:	moria.vim
%patchset_source -f ftp://ftp.vim.org/pub/editors/vim/patches/%{ver}/%{ver}.%03g 1 %{patchlevel}
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-no_libelf.patch
Patch4:		%{name}-egrep.patch
Patch5:		%{name}-awk.patch
Patch6:		%{name}-filetype_vim-perl_tests.patch
Patch7:		%{name}-apache.patch
Patch8:		%{name}-po-syntax.patch
Patch9:		%{name}-modprobe.patch
Patch10:	%{name}-doubleparenthesis.patch
Patch11:	%{name}-syntax-fstab.patch
Patch12:	010_all_%{name}-6.3-vixie.patch
Patch13:	013_all_%{name}-7.0-cron-vars-79981.patch
Patch14:	020_all_%{name}-7.0-fstab-tmpfs-size.patch
Patch15:	021_all_%{name}-7.0-fstab-bogus-errors.patch
Patch17:	027_all_%{name}-7.0-automake-substitutions-93378.patch
Patch18:	%{name}-smarty.patch
Patch19:	%{name}-tutor-lessdeps.patch
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
Patch33:	%{name}-locales.patch
Patch34:	%{name}-rtdir.patch
Patch35:	%{name}-ft-mib.patch
Patch36:	%{name}-ft-lib-udevrules.patch
Patch37:	%{name}-ft-mysql.patch
Patch38:	%{name}-ft-gyp.patch
Patch39:	%{name}-revert-7.4.165-noundo.patch
URL:		http://www.vim.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	gpm-devel
%if "%{pld_release}" == "ac"
%{?with_athena:BuildRequires:	XFree86-devel}
BuildRequires:	gettext-devel
%else
BuildRequires:	gettext-tools
%{?with_athena:BuildRequires:	xorg-lib-libXaw-devel}
%endif
%if %{with gtk} || %{with heavy}
BuildRequires:	gtk+2-devel >= 2:2.6.0
%endif
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.2.0.1}
%if %{with selinux} || %{with heavy}
BuildRequires:	libselinux-devel
%endif
%{?with_motif:BuildRequires:	motif-devel}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%if %{with perl} || %{with heavy}
BuildRequires:	perl-devel
%endif
%if %{with python} || %{with heavy}
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%endif
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.426
%if %{with ruby} || %{with heavy}
BuildRequires:	ruby-devel
%endif
%if %{with tcl} || %{with heavy}
BuildRequires:	tcl-devel
%endif
Obsoletes:	kvim
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
Obsoletes:	vim-minimal
Obsoletes:	vim-static
%endif
BuildRequires:	unzip
Suggests:	%{name}-rt = %{epoch}:%{version}-%{release}
Provides:	vi-editor
Provides:	vi
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-enhanced
Obsoletes:	vim-ispell
Obsoletes:	vim-plugin-multvals
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
Obsoletes:	vim-enhanced
Obsoletes:	vim-ispell
Obsoletes:	vim-plugin-multvals

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
Obsoletes:	vim-enhanced
Obsoletes:	vim-ispell
Obsoletes:	vim-plugin-multvals

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
Obsoletes:	vim-minimal

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
Obsoletes:	gvim-bonobo
Obsoletes:	vim-common
Obsoletes:	vim-syntax-gitcommit
Obsoletes:	vim-syntax-upstart
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	gzip
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
Obsoletes:	vim-X11

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
Obsoletes:	vim-X11

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
Obsoletes:	vim-X11

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
Obsoletes:	vim-X11

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
Requires(post,postun):	gtk+2
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	%{name}-rt-extras = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
Provides:	vim-editor = %{epoch}:%{version}-%{release}
Obsoletes:	vim-X11

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
%setup -q -n %{name}74

# official patches
# patches 7.4.802, 7.4.809 do not apply
# 7.4.802 does not apply and 7.4.809 attempts to revert 7.4.802
%patchset_patch 1 801
%patchset_patch 803 808
%patchset_patch 810 %{patchlevel}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p0
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch17 -p0
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%{?with_home_etc:%patch26 -p1}

# autopaste patch - automatically switch to paste mode
# when `really fast typing' situation happens
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1

cp -p %{SOURCE20} runtime/syntax
cp -p %{SOURCE22} runtime/syntax
cp -p %{SOURCE30} runtime/colors
cp -p %{SOURCE31} runtime/colors
cp -p %{SOURCE32} runtime/colors

%{__unzip} -qd runtime/doc %{SOURCE2}

# remove unsupported locales
%{__rm} src/po/zh_{CN,TW}.UTF-8.po
%{__rm} runtime/lang/menu_zh_{cn,tw}.utf-8.vim

# fix nb/no
%{__mv} src/po/n{o,b}.po
%{__mv} runtime/tutor/tutor.n{o,b}
%{__mv} runtime/tutor/tutor.n{o,b}.utf-8
%{__mv} runtime/lang/menu_n{o,b}.latin1.vim
%{__mv} runtime/lang/menu_n{o,b}.utf-8.vim
%{__mv} runtime/lang/menu_n{o,b}_no.latin1.vim
%{__mv} runtime/lang/menu_n{o,b}_no.utf-8.vim

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
		--%{!?with_perl:dis}%{?with_perl:en}able-perlinterp \
		--%{!?with_python:dis}%{?with_python:en}able-pythoninterp \
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
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-rubyinterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-multibyte \
	--disable-nls

LDFLAGS="%{rpmldflags}"
%endif

%if %{with light}
build vim.light \
	--disable-gui \
	--without-x \
	--with-features=small \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-rubyinterp \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-nls
%endif

build vim.ncurses \
	--disable-gui \
	--without-x \
	--with-features=huge

build vimx \
	--disable-gui \
	--with-x \
	--with-features=huge

%if %{with athena}
build gvim.athena \
	--with-features=huge \
	--enable-gui=athena \
	--with-x \
	--enable-fontset \
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
	--disable-gpm \
	--without-gnome

%endif

%if %{with gtk}
build gvim.gtk \
	--with-features=huge \
	--enable-gui=gtk2 \
	--enable-gtk2-check \
	--with-x \
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
	--enable-perlinterp \
	--enable-pythoninterp \
	--enable-rubyinterp \
	--enable-tclinterp \
	--disable-gpm

build gvim.heavy \
	--with-features=huge \
	--enable-gui=gnome2 \
	--enable-gtk2-check \
	--enable-gnome-check \
	--with-x \
	--enable-perlinterp \
	--enable-pythoninterp \
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

# not supported locales added by 7.3.764 or later
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cs.cp1250
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ja.sjis
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ja.euc-jp
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pl.UTF-8
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pl.cp1250
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ru.cp1251
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sk.cp1250
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/uk.cp1251
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/zh_CN.cp936

%find_lang %{name}

# use compressed docs, see :help gzip-helpfile
%{__gzip} -9 $RPM_BUILD_ROOT%{_datadir}/vim/doc/*.txt
%{__sed} -i -e 's=\(\t.*\.txt\)\t=\1.gz\t=' $RPM_BUILD_ROOT%{_datadir}/vim/doc/tags

%{__gzip} -9 $RPM_BUILD_ROOT%{_datadir}/vim/doc/*.??x
%{__sed} -i -e 's=\(\t.*\.plx\)\t=\1.gz\t=' $RPM_BUILD_ROOT%{_datadir}/vim/doc/tags-pl

%{__rm} $RPM_BUILD_ROOT%{_bindir}/*

%if %{with static}
install -p src/bin/vim.ncurses	$RPM_BUILD_ROOT%{_bindir}/vim
install -p src/bin/vim.static	$RPM_BUILD_ROOT/bin/vi
%else
install -p src/bin/vim.ncurses	$RPM_BUILD_ROOT/bin/vi
ln -sf /bin/vi		$RPM_BUILD_ROOT%{_bindir}/vim
%endif
install -p src/bin/vimx	$RPM_BUILD_ROOT%{_bindir}/vimx
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

cp -p %{SOURCE14}	$RPM_BUILD_ROOT%{_desktopdir}

%if %{with athena}
install -p src/bin/gvim.athena	$RPM_BUILD_ROOT%{_bindir}/gvim.athena
cp -p %{SOURCE10}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with motif}
install -p src/bin/gvim.motif	$RPM_BUILD_ROOT%{_bindir}/gvim.motif
cp -p %{SOURCE11}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gnome}
install -p src/bin/gvim.gnome	$RPM_BUILD_ROOT%{_bindir}/gvim.gnome
cp -p %{SOURCE13}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gtk}
install -p src/bin/gvim.gtk	$RPM_BUILD_ROOT%{_bindir}/gvim.gtk
ln -sf gvim.gtk		$RPM_BUILD_ROOT%{_bindir}/gvim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/eview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/evim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gvimdiff
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgvim
cp -p %{SOURCE12}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with heavy}
install -p src/bin/vim.heavy	$RPM_BUILD_ROOT%{_bindir}
install -p src/bin/gvim.heavy	$RPM_BUILD_ROOT%{_bindir}
%endif
%if %{with light}
install -p src/bin/vim.light	$RPM_BUILD_ROOT%{_bindir}
%endif

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p runtime/vim48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/vim.png

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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rvim
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/vimdiff
%{_mandir}/man1/rvim.1*
%{_mandir}/man1/vimdiff.1*
%lang(fi) %{_mandir}/fi/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/vimdiff.1*
%lang(id) %{_mandir}/id/man1/rvim.1*
%lang(id) %{_mandir}/id/man1/vim.1*
%lang(it) %{_mandir}/it/man1/rvim.1*
%lang(it) %{_mandir}/it/man1/vim.1*
%lang(it) %{_mandir}/it/man1/vimdiff.1*
%lang(ja) %{_mandir}/ja/man1/rvim.1*
%lang(ja) %{_mandir}/ja/man1/vim.1*
%lang(ja) %{_mandir}/ja/man1/vimdiff.1*
%lang(pl) %{_mandir}/pl/man1/rvim.1*
%lang(pl) %{_mandir}/pl/man1/vim.1*
%lang(pl) %{_mandir}/pl/man1/vimdiff.1*
%lang(ru) %{_mandir}/ru/man1/rvim.1*
%lang(ru) %{_mandir}/ru/man1/vim.1*
%lang(ru) %{_mandir}/ru/man1/vimdiff.1*
%{_desktopdir}/%{name}.desktop

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
%doc %{_datadir}/vim/autoload/README.txt

%dir %{_datadir}/vim/ftdetect

%dir %{_datadir}/vim/ftplugin
%doc %{_datadir}/vim/ftplugin/README.txt
%{_datadir}/vim/ftplugin/*.vim
%{_datadir}/vim/ftplugin/logtalk.dict

%dir %{_datadir}/vim/indent
%doc %{_datadir}/vim/indent/README.txt
%{_datadir}/vim/indent/*.vim

%dir %{_datadir}/vim/keymap
%doc %{_datadir}/vim/keymap/README.txt
%{_datadir}/vim/keymap/*.vim

%dir %{_datadir}/vim/plugin
%doc %{_datadir}/vim/plugin/README.txt

%dir %{_datadir}/vim/syntax
%doc %{_datadir}/vim/syntax/README.txt
%{_datadir}/vim/syntax/*.vim

%dir %{_datadir}/vim/colors
%doc %{_datadir}/vim/colors/README.txt
%{_datadir}/vim/colors/*.vim

%dir %{_datadir}/vim/lang
%doc %{_datadir}/vim/lang/README*

%lang(af) %{_datadir}/vim/lang/menu_af*
%lang(ca) %{_datadir}/vim/lang/menu_ca*
%lang(cs) %{_datadir}/vim/lang/menu_cs*
%lang(cs) %{_datadir}/vim/lang/menu_*czech*
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
%lang(fi) %{_mandir}/fi/man1/vim.1*
%lang(fr) %{_mandir}/fr/man1/vim.1*
%{_pixmapsdir}/vim.png

# plugins in base -rt package
%{_datadir}/vim/autoload/gzip.vim
%{_datadir}/vim/plugin/gzip.vim
%{_datadir}/vim/plugin/matchparen.vim

%files rt-extras
%defattr(644,root,root,755)
%{_datadir}/vim/plugin/*.vim
%{_datadir}/vim/autoload/*.vim
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
%{_datadir}/vim/doc/*.txt.gz

# Polish
%lang(pl) %{_datadir}/vim/doc/*.plx.gz

%files tutor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%dir %{_datadir}/vim/tutor
%dir %{_datadir}/vim/tutor/tutor

%{_datadir}/vim/tutor/README.txt
%{_datadir}/vim/tutor/tutor.vim
%{_datadir}/vim/tutor/tutor.utf-8
%lang(el) %{_datadir}/vim/tutor/README.el.cp737.txt
%lang(el) %{_datadir}/vim/tutor/README.el.txt

%lang(de) %{_datadir}/vim/tutor/tutor.bar
%lang(de) %{_datadir}/vim/tutor/tutor.bar.utf-8
%lang(ca) %{_datadir}/vim/tutor/tutor.ca
%lang(ca) %{_datadir}/vim/tutor/tutor.ca.utf-8
%lang(cs) %{_datadir}/vim/tutor/tutor.cs
%lang(cs) %{_datadir}/vim/tutor/tutor.cs.cp1250
%lang(cs) %{_datadir}/vim/tutor/tutor.cs.utf-8
%lang(de) %{_datadir}/vim/tutor/tutor.de
%lang(de) %{_datadir}/vim/tutor/tutor.de.utf-8
%lang(el) %{_datadir}/vim/tutor/tutor.el
%lang(el) %{_datadir}/vim/tutor/tutor.el.cp737
%lang(el) %{_datadir}/vim/tutor/tutor.el.utf-8
%lang(eo) %{_datadir}/vim/tutor/tutor.eo
%lang(eo) %{_datadir}/vim/tutor/tutor.eo.utf-8
%lang(es) %{_datadir}/vim/tutor/tutor.es
%lang(es) %{_datadir}/vim/tutor/tutor.es.utf-8
%lang(fr) %{_datadir}/vim/tutor/tutor.fr
%lang(fr) %{_datadir}/vim/tutor/tutor.fr.utf-8
%lang(hr) %{_datadir}/vim/tutor/tutor.hr
%lang(hr) %{_datadir}/vim/tutor/tutor.hr.cp1250
%lang(hr) %{_datadir}/vim/tutor/tutor.hr.utf-8
%lang(hu) %{_datadir}/vim/tutor/tutor.hu
%lang(hu) %{_datadir}/vim/tutor/tutor.hu.cp1250
%lang(hu) %{_datadir}/vim/tutor/tutor.hu.utf-8
%lang(it) %{_datadir}/vim/tutor/tutor.it
%lang(it) %{_datadir}/vim/tutor/tutor.it.utf-8
%lang(ja) %{_datadir}/vim/tutor/tutor.ja.euc
%lang(ja) %{_datadir}/vim/tutor/tutor.ja.sjis
%lang(ja) %{_datadir}/vim/tutor/tutor.ja.utf-8
%lang(ko) %{_datadir}/vim/tutor/tutor.ko.euc
%lang(ko) %{_datadir}/vim/tutor/tutor.ko.utf-8
%lang(nl) %{_datadir}/vim/tutor/tutor.nl
%lang(nl) %{_datadir}/vim/tutor/tutor.nl.utf-8
%lang(nb) %{_datadir}/vim/tutor/tutor.nb
%lang(nb) %{_datadir}/vim/tutor/tutor.nb.utf-8
%lang(pl) %{_datadir}/vim/tutor/tutor.pl
%lang(pl) %{_datadir}/vim/tutor/tutor.pl.cp1250
%lang(pl) %{_datadir}/vim/tutor/tutor.pl.utf-8
%lang(pt) %{_datadir}/vim/tutor/tutor.pt
%lang(pt) %{_datadir}/vim/tutor/tutor.pt.utf-8
%lang(ru) %{_datadir}/vim/tutor/tutor.ru
%lang(ru) %{_datadir}/vim/tutor/tutor.ru.cp1251
%lang(ru) %{_datadir}/vim/tutor/tutor.ru.utf-8
%lang(sk) %{_datadir}/vim/tutor/tutor.sk
%lang(sk) %{_datadir}/vim/tutor/tutor.sk.cp1250
%lang(sk) %{_datadir}/vim/tutor/tutor.sk.utf-8
%lang(sv) %{_datadir}/vim/tutor/tutor.sv
%lang(sv) %{_datadir}/vim/tutor/tutor.sv.utf-8
%lang(tr) %{_datadir}/vim/tutor/tutor.tr.iso9
%lang(tr) %{_datadir}/vim/tutor/tutor.tr.utf-8
%lang(vi) %{_datadir}/vim/tutor/tutor.vi.utf-8
%lang(zh_CN) %{_datadir}/vim/tutor/tutor.zh_cn.utf-8
%lang(zh_TW) %{_datadir}/vim/tutor/tutor.zh.big5
%lang(zh_TW) %{_datadir}/vim/tutor/tutor.zh.euc
%lang(zh_TW) %{_datadir}/vim/tutor/tutor.zh.utf-8
%lang(zh_TW) %{_datadir}/vim/tutor/tutor.zh_tw.utf-8

%{_mandir}/man1/vimtutor.1*
%lang(fr) %{_mandir}/fr/man1/vimtutor.1*
%lang(it) %{_mandir}/it/man1/vimtutor.1*
%lang(ja) %{_mandir}/ja/man1/vimtutor.1*
%lang(pl) %{_mandir}/pl/man1/vimtutor.1*
%lang(ru) %{_mandir}/ru/man1/vimtutor.1*

%files -n vimx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimx

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
%{_mandir}/man1/gvi*
%{_mandir}/man1/rgv*
%lang(fi) %{_mandir}/fi/man1/gvi*
%lang(fi) %{_mandir}/fi/man1/rgv*
%lang(fr) %{_mandir}/fr/man1/eview.1*
%lang(fr) %{_mandir}/fr/man1/evim.1*
%lang(fr) %{_mandir}/fr/man1/gvi*
%lang(fr) %{_mandir}/fr/man1/rgv*
%lang(id) %{_mandir}/id/man1/gvi*
%lang(id) %{_mandir}/id/man1/rgv*
%lang(it) %{_mandir}/it/man1/eview.1*
%lang(it) %{_mandir}/it/man1/evim.1*
%lang(it) %{_mandir}/it/man1/gvi*
%lang(it) %{_mandir}/it/man1/rgv*
%lang(ja) %{_mandir}/ja/man1/eview.1*
%lang(ja) %{_mandir}/ja/man1/evim.1*
%lang(ja) %{_mandir}/ja/man1/gvi*
%lang(ja) %{_mandir}/ja/man1/rgv*
%lang(pl) %{_mandir}/pl/man1/eview.1*
%lang(pl) %{_mandir}/pl/man1/evim.1*
%lang(pl) %{_mandir}/pl/man1/gvi*
%lang(pl) %{_mandir}/pl/man1/rgv*
%lang(ru) %{_mandir}/ru/man1/eview.1*
%lang(ru) %{_mandir}/ru/man1/evim.1*
%lang(ru) %{_mandir}/ru/man1/gvi*
%lang(ru) %{_mandir}/ru/man1/rgv*
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
