#
# Conditional build:
%bcond_without	static		# don't build static version
%bcond_without	athena		# don't build Athena Widgets-based gvim
%bcond_without	motif		# don't build Motif-based gvim
%bcond_without	gtk		# don't build GTK+-based gvim support
%bcond_without	gnome		# don't build GNOME-based gvim support
%bcond_without	heavy		# don't build heavy (full-featured GTK+-based gvim/vim)
%bcond_without	perl		# without Perl interp
%bcond_without	python		# without Python interp
%bcond_with	ruby		# with Ruby interp
%bcond_with	tcl		# with Tcl interp
%bcond_without	selinux		# without selinux support
%bcond_without	home_etc	# without home_etc support
#
%define		ver		7.1
%define		patchlevel	305

# cflags get changed while configuring
%undefine	configure_cache
#
Summary:	Vi IMproved - a Vi clone
Summary(de.UTF-8):	VIsual editor iMproved
Summary(es.UTF-8):	Editor visual incrementado
Summary(fr.UTF-8):	Editeur VIM : VIsual editor iMproved
Summary(pl.UTF-8):	Vi IMproved - klon edytora Vi
Summary(pt_BR.UTF-8):	Editor visual incrementado
Summary(ru.UTF-8):	Visual editor IMproved - Единственно Правильный Редактор :)
Summary(tr.UTF-8):	Gelişmiş bir vi sürümü
Summary(uk.UTF-8):	Visual editor IMproved - Єдино Вірний Редактор :)
Name:		vim
Version:	%{ver}.%{patchlevel}
Release:	2
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/vim/unix/%{name}-%{ver}.tar.bz2
# Source0-md5:	44c6b4914f38d6f9aa959640b89da329
Source1:	ftp://ftp.vim.org/pub/vim/extra/%{name}-%{ver}-lang.tar.gz
# Source1-md5:	144aa049ba70621acf4247f0459f3ee7
Source2:	ftp://ftp.vim.org/pub/vim/extra/%{name}-%{ver}-extra.tar.gz
# Source2-md5:	605cc7ae31bcc9d7864bb0bb6025f55d
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	bc4d1e115ca506ad7751b9bd2b773a7f
Source4:	http://skawina.eu.org/mikolaj/usr_doc_pl.zip
# Source4-md5:	ff96284b1c913d55cf0877839b34d490
Source10:	g%{name}-athena.desktop
Source11:	g%{name}-motif.desktop
Source12:	g%{name}-gtk.desktop
Source13:	g%{name}-gnome.desktop
Source14:	%{name}.desktop
# syntax files
# http://www.vim.org/scripts/script.php?script_id=1491 (0.7.5)
Source20:	javascript.vim
Source21:	nagios.vim
# http://www.vim.org/scripts/script.php?script_id=447 (20040206)
Source22:	exim.vim
# http://www.vim.org/scripts/script.php?script_id=1571 (0.9.7)
Source23:	php.vim
# color schemes
# http://www.vim.org/scripts/script.php?script_id=415 (1.15)
Source30:	zenburn.vim
# http://www.vim.org/scripts/script.php?script_id=92 (1.0)
Source31:	borland.vim
# http://www.vim.org/scripts/download_script.php?src_id=7799 (1.2.5)
Source32:	oceandeep.vim
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-%{name}rc.patch
Patch4:		%{name}-no_libelf.patch
Patch5:		%{name}-egrep.patch
Patch6:		%{name}-awk.patch
Patch7:		%{name}-filetype_vim-perl_tests.patch
Patch8:		%{name}-apache.patch
Patch9:		%{name}-po-syntax.patch
Patch10:	%{name}-modprobe.patch
Patch11:	%{name}-doubleparenthesis.patch
Patch12:	%{name}-syntax-fstab.patch
Patch13:	010_all_%{name}-6.3-vixie.patch
Patch14:	013_all_%{name}-7.0-cron-vars-79981.patch
Patch15:	020_all_%{name}-7.0-fstab-tmpfs-size.patch
Patch16:	021_all_%{name}-7.0-fstab-bogus-errors.patch
Patch17:	024_all_%{name}-6.3-bash-83565.patch
Patch18:	027_all_%{name}-7.0-automake-substitutions-93378.patch
Patch19:	%{name}-smarty.patch
Patch20:	%{name}-tutor-lessdeps.patch
Patch21:	%{name}-nagios.patch
Patch22:	%{name}-filetypes.patch
Patch23:	%{name}-man_installation.patch
Patch102:	%{name}-gtkfilechooser.patch
Patch104:	%{name}-home_etc.patch
Patch105:	%{name}-autopaste.patch
Patch106:	%{name}-ft-cron.patch
%patchset_source -f ftp://ftp.vim.org/pub/editors/vim/patches/7.1/7.1.%03g 1 %{patchlevel}
URL:		http://www.vim.org/
%{?with_athena:BuildRequires:	XFree86-devel}
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
%if %{with gtk} || %{with heavy} 
BuildRequires:	gtk+2-devel >= 2:2.6.0
%endif
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.2.0.1}
%if %{with selinux} || %{with heavy}
BuildRequires:	libselinux-devel
%endif
BuildRequires:	ncurses-devel
%{?with_motif:BuildRequires:	openmotif-devel}
%if %{with perl} || %{with heavy}
BuildRequires:	perl-devel
%endif
%if %{with python} || %{with heavy}
BuildRequires:	python-devel >= 2.5
%endif
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
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Provides:	vi-editor
Provides:	vi
Obsoletes:	vim-enhanced
Obsoletes:	vim-ispell
Obsoletes:	vim-plugin-multvals
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
Summary(pl.UTF-8):	W pełni funkcjonalna wersja Vim-a
Group:		Appplications/Editors/Vim

%description heavy
This package provides full featured version of Vim, which includes
support for Perl, Python, Ruby and Tcl scripting.

%description heavy -l pl.UTF-8
Pakiet ten dostarcza w pełni funkcjonalną wersję Vim-a, czyli
zawierającą wsparcie dla skryptowania w językach Perl, Python, Ruby oraz
Tcl.

%package static
Summary:	Statically linked Vim
Summary(pl.UTF-8):	Statycznie skonsolidowany Vim
Group:		Applications/Editors/Vim
Provides:	vi-editor
Provides:	vi
Obsoletes:	elvis-static
Obsoletes:	nvi
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

%package rt
Summary:	Vim runtime files
Summary(cs.UTF-8):	Soubory nezbytné pro libovolný editor ViM
Summary(da.UTF-8):	Fælles filer som er nødvendige for enhver version af VIM editoren
Summary(de.UTF-8):	Die von allen Versionen des VIM-Editors benötigten gemeinsamen Dateien
Summary(es.UTF-8):	Ficheros comunes a todas las versiones de VIM
Summary(fr.UTF-8):	Fichiers communs indispensables pour toute version de l'éditeur VIM
Summary(id.UTF-8):	File umum yang dibutuhkan oleh semua versi editor VIM
Summary(is.UTF-8):	Grunnskrár sem allar útgáfur VIM ritilsins þurfa á að halda
Summary(it.UTF-8):	File comuni necessari per tutte le versioni dell'editor VIM
Summary(ja.UTF-8):	すべてのバージョンの VIM エディタで必要とされる共通ファイル
Summary(nb.UTF-8):	Felles filer som er nødvendige for enhver versjon av VIM editoren
Summary(pl.UTF-8):	Pliki przydatne edytorowi Vim
Summary(pt.UTF-8):	Os ficheiros comuns necessários para qualquer versão do editor VIM
Summary(ru.UTF-8):	Файлы, требуемые для любой версии редактора vim
Summary(sk.UTF-8):	Spoločné súbory potrebné pre všetky verzie editoru VIM
Summary(sl.UTF-8):	Skupne datoteke, potrebne s katerokoli različico urejevalnika VIM
Summary(sv.UTF-8):	De gemensamma filerna som behövs av alla versioner av redigeraren VIM
Summary(uk.UTF-8):	Файли, потрібні для будь-якої версії редактору vim
Summary(zh_CN.UTF-8):	任何版本的 VIM 编辑器所需的公用文件。
Group:		Applications/Editors/Vim
# for hicolor icons
Requires:	hicolor-icon-theme
Requires:	vim-plugin-securemodelines
Requires:	vim-syntax-spec
# mktemp is for vimtutor
Requires:	mktemp
Obsoletes:	gvim-bonobo
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

%package spell-en
Summary:	English dictionaries for VIMspell
Summary(pl.UTF-8):	Angielskie słowniki dla VIMspella
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}

%description spell-en
English dictionaries for VIMspell.

%description spell-en -l pl.UTF-8
Angielskie słowniki dla VIMspella.

%package -n gvim-athena
Summary:	Vim for X Window built with Athena
Summary(pl.UTF-8):	Vim dla X Window korzystający z biblioteki Athena
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
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
Summary(pl.UTF-8):	Vim dla X Window korzystający z biblioteki Motif
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
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

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl.UTF-8):	Vim dla X Window korzystający z biblioteki GTK
Group:		Applications/Editors/Vim
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
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
Summary(pl.UTF-8):	Vim dla X Window korzystający z biblioteki GNOME
Group:		Applications/Editors/Vim
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
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

%package -n gvim-heavy
Summary:	Full featured build of Vim with X-window support
Summary(pl.UTF-8):	W pełni funkcjonalna wersja Vim-a ze wsparciem dla X-window
Group:		Appplications/Editors/Vim
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	gvim
Provides:	vi-editor
Obsoletes:	vim-X11

%description -n gvim-heavy
This package provides full featured version of Vim, which includes
support for Perl, Python, Ruby and Tcl scripting, as well as GTK+2 GUI.

%description heavy -l pl.UTF-8
Pakiet ten dostarcza w pełni funkcjonalną wersję Vim-a, czyli
zawierającą wsparcie dla skryptowania w językach Perl, Python, Ruby oraz
Tcl jak również GUI GTK+2.

%prep
%setup -q -n %{name}71 -b1 -b2

# official patches
%patchset_patch 1 %{patchlevel}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p0
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p0
%patch18 -p0
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

# home etc
%{?with_home_etc:%patch104 -p1}

# autopaste patch - automatically switch to paste mode 
# when`really fast typing' situation happens
%patch105 -p1

%patch106 -p1

install %{SOURCE20} runtime/syntx
install %{SOURCE21} runtime/syntax
install %{SOURCE22} runtime/syntax
install %{SOURCE23} runtime/syntax
install %{SOURCE30} runtime/colors
install %{SOURCE31} runtime/colors

%build
cd src
%{__autoconf}
# needed to prevent deconfiguring
cp -f configure auto

install -d bin

%if %{with static}
%{__make} distclean
LDFLAGS="%{rpmldflags} -static"
%configure \
	--disable-gui \
	--without-x \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-rubyinterp \
	%{!?with_selinux:--disable-selinux} \
	--disable-tclinterp \
	--disable-cscope \
	--disable-gpm \
	--disable-multibyte \
	--with-features=small \
	--with-tlib="ncurses -ltinfo" \
	--disable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim

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
	--enable-cscope \
	--enable-gpm \
	--with-features=huge \
	--enable-multibyte \
	--with-tlib="ncurses -ltinfo" \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim

mv -f vim bin/vim.ncurses

%if %{with athena}
%{__make} distclean
%configure \
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
	--enable-cscope \
	--enable-fontset \
	--disable-gpm \
	--without-gnome \
	--with-tlib="ncurses -ltinfo" \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.athena
%endif


%if %{with motif}
%{__make} distclean
%configure \
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
	--enable-multibyte \
	--enable-cscope \
	--enable-fontset \
	--disable-gpm \
	--without-gnome \
	--with-tlib="ncurses -ltinfo" \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.motif
%endif

%if %{with gtk}
%{__make} distclean
%configure \
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
	--disable-gpm \
	--enable-cscope \
	--with-tlib="ncurses -ltinfo" \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.gtk
%endif

%if %{with gnome}
%{__make} distclean
%configure \
	--with-features=huge \
	--enable-gui=gnome2 \
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
	--with-tlib="ncurses -ltinfo" \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.gnome
%endif

# vim.heavy / gvim.heavy
%if %{with heavy}
%{__make} distclean
%configure \
	--with-features=huge \
	--disable-gui \
	--without-x \
	--enable-perlinterp \
	--enable-pythoninterp \
	--enable-rubyinterp \
	--enable-tclinterp \
	--disable-gpm \
	--enable-cscope \
	--with-tlib="ncurses -ltinfo" \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/vim.heavy

%{__make} distclean
%configure \
	--with-features=huge \
	--enable-gui=gnome2 \
	--enable-gtk2-check \
	--enable-gnome-check \
	--with-x \
	--enable-perlinterp \
	--enable-pythoninterp \
	--enable-rubyinterp \
	--enable-tclinterp \
	--disable-gpm \
	--enable-cscope \
	--with-tlib="ncurses -ltinfo" \
	--enable-nls \
	--with-modifiedby="PLD Linux Distribution" \
	--with-compiledby="PLD Linux Distribution"

%{__make} vim
mv -f vim bin/gvim.heavy
%endif


%{__make} xxd/xxd languages

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/*

%if %{with static}
install src/bin/vim.ncurses	$RPM_BUILD_ROOT%{_bindir}/vim
install src/bin/vim.static	$RPM_BUILD_ROOT/bin/vi
%else
install src/bin/vim.ncurses	$RPM_BUILD_ROOT/bin/vi
ln -sf /bin/vi		$RPM_BUILD_ROOT%{_bindir}/vim
%endif
install src/xxd/xxd	$RPM_BUILD_ROOT%{_bindir}/xxd
install src/vimtutor	$RPM_BUILD_ROOT%{_bindir}/vimtutor

# Moved into patch
#
# rm -f $RPM_BUILD_ROOT%{_mandir}/man1/*.1
# install runtime/doc/vim.1 $RPM_BUILD_ROOT%{_mandir}/man1
# install runtime/doc/xxd.1 $RPM_BUILD_ROOT%{_mandir}/man1
# install runtime/doc/vimtutor.1 $RPM_BUILD_ROOT%{_mandir}/man1
# echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ex.1
# echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rview.1
# echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rvim.1
# echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1

echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vi.1
echo ".so vim.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1

# not supported directories
rm -rf $RPM_BUILD_ROOT%{_mandir}/??.*/

mv -f $RPM_BUILD_ROOT%{_datadir}/vim/v*/vimrc_example.vim $RPM_BUILD_ROOT%{_sysconfdir}/vim/vimrc
mv -f $RPM_BUILD_ROOT%{_datadir}/vim/v*/gvimrc_example.vim $RPM_BUILD_ROOT%{_sysconfdir}/vim/gvimrc

ln -sf vim $RPM_BUILD_ROOT%{_bindir}/eview
ln -sf vim $RPM_BUILD_ROOT%{_bindir}/evim
ln -sf vim $RPM_BUILD_ROOT%{_bindir}/rvim
ln -sf vim $RPM_BUILD_ROOT%{_bindir}/vimdiff
ln -sf vi  $RPM_BUILD_ROOT/bin/ex
ln -sf vi  $RPM_BUILD_ROOT/bin/view
ln -sf vi  $RPM_BUILD_ROOT/bin/rview

install %{SOURCE14}	$RPM_BUILD_ROOT%{_desktopdir}

%if %{with athena}
install src/bin/gvim.athena	$RPM_BUILD_ROOT%{_bindir}/gvim.athena
install %{SOURCE10}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with motif}
install src/bin/gvim.motif	$RPM_BUILD_ROOT%{_bindir}/gvim.motif
install %{SOURCE11}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gnome}
install src/bin/gvim.gnome	$RPM_BUILD_ROOT%{_bindir}/gvim.gnome
install %{SOURCE13}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gtk}
install src/bin/gvim.gtk	$RPM_BUILD_ROOT%{_bindir}/gvim.gtk
ln -sf gvim.gtk		$RPM_BUILD_ROOT%{_bindir}/gvim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gvimdiff
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgvim
install %{SOURCE12}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with heavy}
install src/bin/vim.heavy	$RPM_BUILD_ROOT%{_bindir}
install src/bin/gvim.heavy	$RPM_BUILD_ROOT%{_bindir}
%endif

install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install runtime/vim16x16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/vim.png
install runtime/vim32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/vim.png
install runtime/vim48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/vim.png

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

unzip -qd $RPM_BUILD_ROOT%{_datadir}/vim/v*/doc %{SOURCE4}

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/{doc,{after/,}{compiler,ftdetect,ftplugin,indent,plugin,spell,syntax}}
> $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/doc/tags

# separate package
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/vim71/{ftplugin,syntax}/spec.vim

# no autodeps
chmod a-x $RPM_BUILD_ROOT%{_datadir}/vim/vim71/doc/vim2html.pl
chmod a-x $RPM_BUILD_ROOT%{_datadir}/vim/vim71/tools/shtags.pl
chmod a-x $RPM_BUILD_ROOT%{_datadir}/vim/vim71/tools/pltags.pl
chmod a-x $RPM_BUILD_ROOT%{_datadir}/vim/vim71/tools/efm_perl.pl
chmod a-x $RPM_BUILD_ROOT%{_datadir}/vim/vim71/tools/efm_filter.pl

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
%attr(755,root,root) %{_bindir}/eview
%attr(755,root,root) %{_bindir}/evim
%attr(755,root,root) %{_bindir}/rvim
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/vimdiff
%{_mandir}/man1/eview.1*
%{_mandir}/man1/evim.1*
%{_mandir}/man1/rvim.1*
%{_mandir}/man1/vimdiff.1*
%lang(fi) %{_mandir}/fi/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/eview.1*
%lang(fr) %{_mandir}/fr/man1/evim.1*
%lang(fr) %{_mandir}/fr/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/vimdiff.1*
%lang(id) %{_mandir}/id/man1/rvim.1*
%lang(it) %{_mandir}/it/man1/eview.1*
%lang(it) %{_mandir}/it/man1/evim.1*
%lang(it) %{_mandir}/it/man1/rvim.1*
%lang(it) %{_mandir}/it/man1/vimdiff.1*
%lang(pl) %{_mandir}/pl/man1/eview.1*
%lang(pl) %{_mandir}/pl/man1/evim.1*
%lang(pl) %{_mandir}/pl/man1/rvim.1*
%lang(pl) %{_mandir}/pl/man1/vimdiff.1*
%lang(ru) %{_mandir}/ru/man1/eview.1*
%lang(ru) %{_mandir}/ru/man1/evim.1*
%lang(ru) %{_mandir}/ru/man1/rvim.1*
%lang(ru) %{_mandir}/ru/man1/vimdiff.1*
%{_desktopdir}/%{name}.desktop

%if %{with static}
%files static
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
#%lang(it) %{_mandir}/it/man1/vi.1*
%lang(it) %{_mandir}/it/man1/ex.1*
%lang(it) %{_mandir}/it/man1/view.1*
%lang(it) %{_mandir}/it/man1/rview.1*
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
%lang(pl) %{_mandir}/pl/man1/xxd.1*
%lang(ru) %{_mandir}/ru/man1/xxd.1*

%files rt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%dir %{_sysconfdir}/vim
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vim/gvimrc

%dir %{_datadir}/vim
%dir %{_datadir}/vim/v*
%dir %{_datadir}/vim/v*/doc
%doc %{_datadir}/vim/v*/doc/*.txt
%lang(pl) %doc %{_datadir}/vim/v*/doc/*.plx
%attr(755,root,root) %{_datadir}/vim/v*/doc/*.pl
%verify(not md5 mtime size) %{_datadir}/vim/v*/doc/tags
%lang(pl) %verify(not md5 mtime size) %{_datadir}/vim/v*/doc/tags-pl
%{_datadir}/vim/v*/ftplugin
%{_datadir}/vim/v*/indent
%{_datadir}/vim/v*/keymap
%dir %{_datadir}/vim/v*/lang
%doc %{_datadir}/vim/v*/lang/README*

# just add after/ and ftdetect/ separately, other dirs caught by globs above or below
%{_datadir}/vim/vimfiles/after
%{_datadir}/vim/vimfiles/ftdetect

%lang(af) %{_datadir}/vim/v*/lang/menu_af*
%lang(af) %{_datadir}/vim/v*/lang/af/
%lang(ca) %{_datadir}/vim/v*/lang/menu_ca*
%lang(ca) %{_datadir}/vim/v*/lang/ca/
%lang(cs) %{_datadir}/vim/v*/lang/menu_cs*
%lang(cs) %{_datadir}/vim/v*/lang/menu_*czech*
%lang(cs) %{_datadir}/vim/v*/lang/cs/
%lang(de) %{_datadir}/vim/v*/lang/menu_de*
%lang(de) %{_datadir}/vim/v*/lang/menu_*german*
%lang(de) %{_datadir}/vim/v*/lang/de/
%lang(en_GB) %{_datadir}/vim/v*/lang/menu_en_gb*
%lang(en_GB) %{_datadir}/vim/v*/lang/menu_*english*
%lang(en_GB) %{_datadir}/vim/v*/lang/en_GB/
%lang(es) %{_datadir}/vim/v*/lang/menu_es*
%lang(es) %{_datadir}/vim/v*/lang/menu_*spanish*
%lang(es) %{_datadir}/vim/v*/lang/es/
%lang(fr) %{_datadir}/vim/v*/lang/menu_fr*
%lang(fr) %{_datadir}/vim/v*/lang/fr/
%lang(ga) %{_datadir}/vim/v*/lang/ga/
%lang(hu) %{_datadir}/vim/v*/lang/menu_hu*
%lang(it) %{_datadir}/vim/v*/lang/menu_it*
%lang(it) %{_datadir}/vim/v*/lang/it/
%lang(ja) %{_datadir}/vim/v*/lang/menu_ja*
%lang(ja) %{_datadir}/vim/v*/lang/ja/
%lang(ko) %{_datadir}/vim/v*/lang/menu_ko*
%lang(ko) %{_datadir}/vim/v*/lang/ko/
%lang(nl) %{_datadir}/vim/v*/lang/menu_nl*
%lang(nb) %{_datadir}/vim/v*/lang/menu_no*
%lang(nb) %{_datadir}/vim/v*/lang/no/
%lang(pl) %{_datadir}/vim/v*/lang/menu_pl*
%lang(pl) %{_datadir}/vim/v*/lang/menu_*polish*
%lang(pl) %{_datadir}/vim/v*/lang/pl/
%lang(pt) %{_datadir}/vim/v*/lang/menu_pt*
%lang(ru) %{_datadir}/vim/v*/lang/menu_ru*
%lang(ru) %{_datadir}/vim/v*/lang/ru/
%lang(sk) %{_datadir}/vim/v*/lang/menu_sk*
%lang(sk) %{_datadir}/vim/v*/lang/menu_*slovak*
%lang(sk) %{_datadir}/vim/v*/lang/sk/
%lang(sl) %{_datadir}/vim/v*/lang/menu_sl_si*
%lang(sr) %{_datadir}/vim/v*/lang/menu_sr*
%lang(sv) %{_datadir}/vim/v*/lang/menu_sv*
%lang(sv) %{_datadir}/vim/v*/lang/sv/
%lang(uk) %{_datadir}/vim/v*/lang/menu_uk*
%lang(uk) %{_datadir}/vim/v*/lang/uk/
%lang(vi) %{_datadir}/vim/v*/lang/menu_vi*
%lang(vi) %{_datadir}/vim/v*/lang/vi/
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh.cp936*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh.gb2312*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh_cn*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_*chinese*gb*
%lang(zh_CN) %{_datadir}/vim/v*/lang/zh_CN/
%lang(zh_CN) %{_datadir}/vim/v*/lang/zh_CN.UTF-8/
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh.cp950*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh.big5*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh_tw*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_*taiwan*
%lang(zh_TW) %{_datadir}/vim/v*/lang/zh_TW/
%lang(zh_TW) %{_datadir}/vim/v*/lang/zh_TW.UTF-8/

%dir %{_datadir}/vim/v*/spell
%{_datadir}/vim/v*/spell/cleanadd.vim
%lang(he) %{_datadir}/vim/v*/spell/he.*
%lang(yi) %{_datadir}/vim/v*/spell/yi.*

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

%{_mandir}/man1/rvim.1*
%{_mandir}/man1/vim.1*
%{_mandir}/man1/vimtutor.1*
%lang(fi) %{_mandir}/fi/man1/rvim.1*
%lang(fi) %{_mandir}/fi/man1/vim.1*
%lang(fr) %{_mandir}/fr/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/vim.1*
%lang(fr) %{_mandir}/fr/man1/vimtutor.1*
%lang(id) %{_mandir}/id/man1/vim.1*
%lang(it) %{_mandir}/it/man1/vim.1*
%lang(it) %{_mandir}/it/man1/vimtutor.1*
%lang(pl) %{_mandir}/pl/man1/vim.1*
%lang(pl) %{_mandir}/pl/man1/vimtutor.1*
%lang(ru) %{_mandir}/ru/man1/vim.1*
%lang(ru) %{_mandir}/ru/man1/vimtutor.1*
%{_iconsdir}/hicolor/16x16/apps/vim.png
%{_iconsdir}/hicolor/32x32/apps/vim.png
%{_iconsdir}/hicolor/48x48/apps/vim.png

%if %{with heavy}
%files heavy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim.heavy
%endif

%files spell-en
%defattr(644,root,root,755)
%{_datadir}/vim/v*/spell/en.*.*

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
%attr(755,root,root) %{_bindir}/gvimdiff
%attr(755,root,root) %{_bindir}/gview
%attr(755,root,root) %{_bindir}/rgvim
%attr(755,root,root) %{_bindir}/rgview
%attr(755,root,root) %verify(not link) %{_bindir}/gvim
%{_mandir}/man1/gvi*
%{_mandir}/man1/rgv*
%lang(fi) %{_mandir}/fi/man1/gvi*
%lang(fi) %{_mandir}/fi/man1/rgv*
%lang(fr) %{_mandir}/fr/man1/gvi*
%lang(fr) %{_mandir}/fr/man1/rgv*
%lang(id) %{_mandir}/id/man1/gvi*
%lang(id) %{_mandir}/id/man1/rgv*
%lang(it) %{_mandir}/it/man1/gvi*
%lang(it) %{_mandir}/it/man1/rgv*
%lang(pl) %{_mandir}/pl/man1/gvi*
%lang(pl) %{_mandir}/pl/man1/rgv*
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
