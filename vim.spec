#
# Conditional build:
# _without_static	- without static version
# _without_athena	- without Athena Widgets-based gvim. DOESN'T WORK.
# _without_motif	- without Motif-based gvim
# _without_gtk		- without gtk+-based gvim support
# _without_gnome	- without gnome-based gvim support
# _with_ispell		- with spell checking (non-standard feature; disables RIGHTLEFT and FKMAP)
# _with_perl		- with perl interp
# _with_python		- with python interp
# _with_ruby		- with ruby interp
# _with_tcl		- with tcl interp

## %define		_ver		6.0
## %define		_patchlevel	208

Summary:	Vi IMproved - a Vi clone
Summary(de):	VIsual editor iMproved
Summary(es):	Editor visual incrementado
Summary(fr):	Editeur VIM : VIsual editor iMproved
Summary(pl):	Vi IMproved - klon edytora Vi
Summary(pt_BR):	Editor visual incrementado
Summary(ru):	Visual editor IMproved - Единственно Правильный Редактор :)
Summary(tr):	GeliЧmiЧ bir vi sЭrЭmЭ
Summary(uk):	Visual editor IMproved - ╢дино В╕рний Редактор :)
Name:		vim
Version:	6.1
Release:	1
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{version}-lang.tar.gz
Source2:	g%{name}-athena.desktop
Source3:	g%{name}-motif.desktop
Source4:	g%{name}-gtk.desktop
Source5:	g%{name}-gnome.desktop
#packed from	ftp://ftp.vim.org/pub/editors/vim/patches/6.0.*
## Source6:	%{name}-patches-%{_ver}.%{_patchlevel}.tar.bz2
Source7:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-ispell.patch
Patch4:		%{name}-ispell-axp.patch
URL:		http://www.vim.org/
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
%{!?_without_athena:BuildRequires:	Xaw3d-devel}
%{!?_without_gnome:BuildRequires:	esound-devel}
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_gtk:BuildRequires:		gtk+-devel}
%{!?_without_motif:BuildRequires:	motif-devel}
%{!?_without_static:BuildRequires:	glibc-static}
%{!?_without_static:BuildRequires:	ncurses-static}
%{?_with_perl:BuildRequires:		perl-devel}
%{?_with_python:BuildRequires:		python-devel}
%{?_with_ruby:BuildRequires:		ruby}
%{?_with_tcl:BuildRequires:		tcl-devel}
Requires:	%{name}-rt = %{version}
%{?_without_static:Requires:	%{name}-static = %{version}}
Obsoletes:	vim-enhanced
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text editor similar to Vi. Important improvements: multiple windows,
multi-level undo, block highliting, folding, and many other.

%description -l cs
ViM je novЩ a vylep╧enЩ editor vychАzejМcМ z klasickИho editoru vi. Vi
byl prvnМm celoobrazovkovЩm editorem pro Unix a je stАle velmi
populАrnМ. ViM je obohacenЩ funkcemi jako: podpora vМce oken,
vМceЗrovРovИ undo, zvЩrazРovАnМ blokЫ a Ьadu dal╧Мch u╬iteХnЩch
funkcМ.

%description -l de
Der Visual-Editor iMproved ist ein aktualisierter und erweiterter Klon
des vi-Editors, der mit praktisch allen UN*X-Systemen ausgeliefert
wird. Er bringt mehrere Fenster, mehrstufige Widerrufen-Funktion,
Block-Markierung und viele weitere Zusatzfunktionen im Vergleich zum
Standard-vi-Programm.

%description -l es
El editor Visual Mejorado es una versiСn actualizada y con nuevas
caracterМsticas adicionales del mundialmente famoso 'vi' que acompaЯa
prАcticamente todos los sistemas UN*X. Posibilita trabajar con
mЗltiples ventanas, varios niveles de deshacer, bloques enfatizados, y
otras muchas caracterМsticas del 'vi'.

%description -l fr
L'Иditeur VIsuel aMИliorИ est un clone mis Ю jour et dotИ de
caractИristiques supplИmentaires de l'Иditeur ╚ vi ╩ fourni avec
pratiquement tous les systХmes UN*X. Il ajoute les fenЙtres
mutltiples, l'annulation a plusieurs niveaux, la mise en Иvidence des
blocs et autres caractИristiques au vi de base.

%description -l id
VIM (VIsual editor iMproved) adalah versi vi editor yang sudah
diupdate dan ditambah kemampuannya. Vi adalah editor untuk UNIX yang
pertama yang menggunakan layar, dan sekarang masih sangat populer. VIM
mengembangkan vi dengan menambah kemampuan baru seperti: multiple
windows, multi-level undo, block highlighting, dll.

%description -l is
VIM (VIsual editor iMproved) er uppfФrП og endurbФtt ЗtgАfa af vi
ritlinum. Vi var fyrsti skjА-ritillinn fyrir UNIX og er enn mjЖg
vinsФll. VIM gerist fЖПurbetrungur meП nЩjum mЖguleikum lМkt og
gluggakerfi, iПrun og yfirbСt (e: multi-level undo), blokkarvali og
fleira.

%description -l it
VIM (Vi IMproved) Х una versione aggiornata e perfezionata dell'editor
vi. Vi Х stato il primo editor per UNIX realmente basato su video ed Х
ancora molto diffuso. VIM perfeziona vi aggiungendo nuove funzioni:
finestre multiple, funzione \"annulla\" multilivello, evidenziazione
dei blocchi e altro.

%description -l pl
Edytor tekstu podobny do Vi. Wa©ne ulepszenia: mo©liwo╤Ф pracy w wielu
oknach, wielopoziomowa opcja 'cofnij', bloki, pod╤wietlanie skЁadni,
folding i wiele innych.

%description -l ja
O VIM (VIsual editor iMproved) И uma versЦo melhorada e actualizada do
editor vi. O vi foi o primeiro verdadeiro editor baseado em ecrЦ para
o UNIX, e ainda И muito popular. O VIM melhora o vi acrescentando
novas potencialidades: janelas mЗltiplas, anulaГЦo multi-nМvel, realce
de blocos e mais.

%description -l pt_BR
O editor Vim (Vi Enhanced) И um versЦo atualizada e com novas
caracterМsticas do mundialmente famoso 'vi' que acompanha praticamente
todos os sistemas UN*X. Ele possibilita trabalhar com mЗltiplas
janelas, vАrios nМveis de desfazer, blocos enfatizados, e muitas
outras caracterМsticas do 'vi'.

%description -l ru
VIsual editor iMproved - это обновленный и значительно улучшенный клон
редактора vi, который поставляется практически со всеми
UN*X-системами. В этой версии есть многоуровневый откат, выделение
блоков, синтаксическая подсветка и много другого...

%description -l sk
VIM (VIsual editor iMproved) je nov╧ia a vylep╧enА verzia editoru vi.
Vi bol prvЩm skutoХne obrazovkovo orientovanЩm editorom pre UNIX a
stАle je ve╣mi populАrny. VIM mА oproti vi vylep╧enia ako: prАcu s
viacerЩmi oknami, viacnАsobnИ undo, zvЩrazРovanie blokov textu a inИ.

%description -l sv
VIM (Vi IMproved) Дr en uppdaterad och fЖrbДttrad version av
redigeraren vi. Vi var den fЖrsta riktiga skДrmbaserade redigeraren
till UNIX, och Дr fortfarande vДldigt populДr. VIM fЖrbДttrar vi med
nya finesser: flera fЖnster, flernivЕ Еngra, blockmarkering och mer
ДndЕ.

%description -l tr
Standart vi metin dЭzenleyicisinin geliЧmiЧ hali; daha fazla komut,
birden fazla pencere desteПi ve blok iЧaretleme yetenekleri iГerir.

%description -l uk
VIsual editor iMproved - це оновлений та значно пол╕пшений клон
редактора vi, який поставля╓ться практично з╕ вс╕ма UN*X-системами. В
ц╕й верс╕╖ ╓ багатор╕вневий в╕дкат, вид╕лення блок╕в, синтаксична
п╕дсв╕тка та багато ╕ншого...

%package -n xxd
Summary:	Utility to convert files to hexdump or do the reverse
Summary(pl):	NarzЙdzie do zamiany plikСw na postaФ szesnastkow╠ i odwrotnie
Group:		Applications/Editors/Vim

%description -n xxd
xxd creates a hex dump of a given file or standard input. It can also
convert a hex dump back to its original binary form. Like uuencode and
uudecode it allows the transmission of binary data in a `mail-safe'
ASCII representation, but has the advantage of decoding to standard
output. Moreover, it can be used to perform binary file patching.

%description -n xxd -l pl
xxd tworzy szesnastkowy zapis pliku podanego na standardowe wej╤cie.
Mo©e tak©e przekonwertowaФ taki zapis na oryginaln╠, binarn╠ postaФ.
Podobnie jak uuencode i uudecode pozwala na przesyЁanie danych
binarnych w postaci ASCII, ale ma mo©liwo╤Ф dekodowania na standardowe
wyj╤cie. Co wiЙcej, mo©e byФ u©yty do modyfikowania plikСw binarnych.

%package static
Summary:	Statically linked Vim
Summary(pl):	Statycznie skonsolidowany Vim
Group:		Applications/Editors/Vim
Provides:	vi
Obsoletes:	vi
Obsoletes:	vim-minimal

%description static
Text editor similar to Vi. This version is built with minimal feature
and is installed in /bin as a rescue tool. The installation of this
package is STRONGLY recommended.

%description static -l pl
Edytor tekstu podobny do Vi. Ta wersja zostaЁa zlinkowana statycznie i
posiada minimaln╠ ilo╤Ф dodatkСw. Jest instalowana w /bin jako
narzЙdzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, mo©e on pomСc Ci uratowaФ system w czasie awarii.

%description static -l ru
Пакет vim-static устанавливает разновидность vim как /bin/vi, что
удобно для запуска даже когда смонтирована только корневая файловая
система.

%description static -l uk
Пакет vim-static встановлю╓ р╕зновид vim як /bin/vi, що зручно для
запуску нав╕ть тод╕, коли змонтована т╕льки корньова файлова система.

%package rt
Summary:	Vim runtime files
Summary(cs):	Soubory nezbytnИ pro libovolnЩ editor ViM
Summary(da):	FФlles filer som er nЬdvendige for enhver version af VIM editoren
Summary(de):	Die von allen Versionen des VIM-Editors benЖtigten gemeinsamen Dateien
Summary(es):	Ficheros comunes a todas las versiones de VIM
Summary(fr):	Fichiers communs indispensables pour toute version de l'Иditeur VIM
Summary(id):	File umum yang dibutuhkan oleh semua versi editor VIM
Summary(is):	GrunnskrАr sem allar ЗtgАfur VIM ritilsins Чurfa А aП halda
Summary(it):	File comuni necessari per tutte le versioni dell'editor VIM
Summary(ja):	╓╧╓ы╓ф╓н╔п║╪╔╦╔Г╔С╓н VIM ╔╗╔г╔ё╔©╓ги╛мв╓х╓╣╓Л╓К╤╕дл╔у╔║╔╓╔К
Summary(no):	Felles filer som er nЬdvendige for enhver versjon av VIM editoren
Summary(pl):	Pliki przydatne edytorowi Vim
Summary(pt):	Os ficheiros comuns necessАrios para qualquer versЦo do editor VIM
Summary(ru):	Файлы, требуемые для любой версии редактора vim
Summary(sk):	SpoloХnИ sЗbory potrebnИ pre v╧etky verzie editoru VIM
Summary(sl):	Skupne datoteke, potrebne s katerokoli razliХico urejevalnika VIM
Summary(sv):	De gemensamma filerna som behЖvs av alla versioner av redigeraren VIM
Summary(uk):	Файли, потр╕бн╕ для будь-яко╖ верс╕╖ редактору vim
Summary(zh_CN):	хн╨н╟Ф╠╬╣д VIM ╠Ю╪╜фВкЫпХ╣д╧╚сцнд╪Ч║ё
Group:		Applications/Editors/Vim
Requires:	mktemp
Requires:	which
Obsoletes:	vim-common

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for Vim. If you want to take advantage of Vim more
powerful features, you should install this package.

%description rt -l cs
Tento balМХek obsahuje spoleХnИ soubory pro v╧echny dal╧М balМХky s
vim.

%description rt -l da
The vim-rt package contains files which every VIM binary will need in
order to run.

%description rt -l de
Das Paket vim-rt enthДlt Dateien, die jede VIM-BinДrdatei fЭr die
AusfЭhrung benЖtigt.

%description rt -l es
The vim-rt package contains files which every VIM binary will need in
order to run.

%description rt -l fr
Le paquetage vim-rt contient des fichiers dont chaque fichier binaire
VIM a besoin pour fonctionner.

%description rt -l id
Package vim-rt berisi file yang dibutuhkan semua versi VIM agar bisa
berjalan.

%description rt -l is
vim-rt pakkinn inniheldur skrАr sem allar VIM keyrsluskrАrnar Чurfa
til aП keyra.

%description rt -l it
Il pacchetto vim-rt contiene i file necessari a ogni binario di VIM
per poter funzionare.

%description rt -l pl
W tym pakiecie znajdziesz dokumentacjЙ, makra, pliki konfiguracyjne i
strony podrЙcznika dla edytora Vim. Je©eli chcesz korzystaФ z
zaawansowanych mo©liwo╤ci Vima, powiniene╤ zainstalowaФ ten pakiet.

%description rt -l pt
O pacote vim-rt contИm os ficheiros que todos os executАveis do VIM
irЦo necessitar para correr.

%description rt -l ru
Пакет vim-rt содержит файлы (например, файлы справки), которые нужны
для работы любой программы vim.

%description rt -l sk
BalМk vim-rt obsahuje sЗbory, ktorИ bude potrebova╩ pre sprАvnu
funkciu ka╬dА verzia editoru VIM.

%description rt -l sv
Paketet vim-rt innehЕller filer som alla VIM-binДrer behЖver fЖr att
kЖra.

%description rt -l uk
Пакет vim-rt м╕стить файли (наприклад, файли дов╕дки), котр╕ потр╕бн╕
для роботи будь-яко╖ програми vim.

%package -n gvim-athena
Summary:	Vim for X Window built with Athena
Summary(pl):	Vim dla X Window korzystaj╠cy z biblioteki Athena
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-athena
The classic Unix text editor now also under X Window System! This
version is built with Athena Widget Set.

%description -n gvim-athena -l pl
Wersja edytora Vim pracuj╠ca w ╤rodowisku X Window z wykorzystaniem
biblioteki Athena Widget Set.

%description -n gvim-athena -l ru
Этот пакет представляет собой версию VIM, собранную с библиотеками
Athena Widget Set, что позволяет запускать VIM как приложение X Window
System - с полностью графическим интерфейсом и поддержкой мыши.

%description -n gvim-athena -l uk
Цей пакет м╕стить верс╕ю VIM, з╕брану з б╕бл╕отеками Athena Widget
Set, що дозволя╓ запускати VIM як прикладну програму X Window System -
з повн╕стю граф╕чним ╕нтерфейсом та п╕дтримкою миш╕.

%package -n gvim-motif
Summary:	Vim for X Window built with Motif
Summary(pl):	Vim dla X Window korzystaj╠cy z biblioteki Motif
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-motif
The classic Unix text editor now also under X Window System! This
version is built with Motif.

%description -n gvim-motif -l pl
Wersja edytora Vim pracuj╠ca w ╤rodowisku X Window z wykorzystaniem
biblioteki Motif.

%description -n gvim-motif -l ru
Этот пакет представляет собой версию VIM, собранную с библиотеками
Motif, что позволяет запускать VIM как приложение X Window System - с
полностью графическим интерфейсом и поддержкой мыши.

%description -n gvim-motif -l uk
Цей пакет м╕стить верс╕ю VIM, з╕брану з б╕бл╕отеками Motif, що
дозволя╓ запускати VIM як прикладну програму X Window System - з
повн╕стю граф╕чним ╕нтерфейсом та п╕дтримкою миш╕.

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj╠cy z biblioteki GTK
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This
version is built with GTK.

%description -n gvim-gtk -l pl
Wersja edytora Vim pracuj╠ca w ╤rodowisku X Window z wykorzystaniem
biblioteki GTK.

%description -n gvim-gtk -l ru
Этот пакет представляет собой версию VIM, собранную с библиотеками
GTK, что позволяет запускать VIM как приложение X Window System - с
полностью графическим интерфейсом и поддержкой мыши. Просто скажите
'gvim'...

%description -n gvim-gtk -l uk
Цей пакет м╕стить верс╕ю VIM, з╕брану з б╕бл╕отеками GTK, що дозволя╓
запускати VIM як прикладну програму X Window System - з повн╕стю
граф╕чним ╕нтерфейсом та п╕дтримкою миш╕. Просто скаж╕ть 'gvim'...

%package -n gvim-gnome
Summary:	Vim for X Window built with gnome
Summary(pl):	Vim dla X Window korzystaj╠cy z biblioteki GNOME
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{version}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gnome
The classic Unix text editor now also under X Window System! This
version is build with GNOME.

%description -n gvim-gnome -l pl
Wersja edytora Vim pracuj╠ca w ╤rodowisku X Window z wykorzystaniem
bibliotek GNOME.

%description -n gvim-gnome -l ru
Этот пакет представляет собой версию VIM, собранную с библиотеками
GNOME, что позволяет запускать VIM как приложение X Window System - с
полностью графическим интерфейсом и поддержкой мыши.

%description -n gvim-gnome -l uk
Цей пакет м╕стить верс╕ю VIM, з╕брану з б╕бл╕отеками GNOME, що
дозволя╓ запускати VIM як прикладну програму X Window System - з
повн╕стю граф╕чним ╕нтерфейсом та п╕дтримкою миш╕.

%prep
%setup -q -b1 -n %{name}%(echo %{version} | sed -e "s#\.##g")
## %setup -q -b1 -a6 -n %{name}%(echo %{_ver} | sed -e "s#\.##g")
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?_with_ispell:%patch3 -p1}
%ifarch alpha
%{?_with_ispell:%patch4 -p1}
%endif

## # these patches are to "extra" package which we don't need (nor use)
## rm -f patches/6.0.{027,048,053,064,070,073,093,106,107,115,116,117,119,123,121,122,125,135,161,162,164,165,179,186,188,205,207}
## # apply the rest of official patches
## for f in patches/6.0.* ; do
## 	echo "Applying official patch `basename $f` ..."
## 	patch -s -p0 < $f
## done

%build
cd src
autoconf
%configure \
	--disable-gui \
	--without-x \
	%{!?_with_perl:--disable-perlinterp} \
	%{?_with_perl:--enable-perlinterp} \
	%{!?_with_python:--disable-pythoninterp} \
	%{?_with_python:--enable-pythoninterp} \
	%{!?_with_ruby:--disable-rubyinterp} \
	%{?_with_ruby:--enable-rubyinterp} \
	%{!?_with_tcl:--disable-tclinterp} \
	%{?_with_tcl:--enable-tclinterp} \
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
	--disable-rubyinterp \
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
	%{!?_with_perl:--disable-perlinterp} \
	%{?_with_perl:--enable-perlinterp} \
	%{!?_with_python:--disable-pythoninterp} \
	%{?_with_python:--enable-pythoninterp} \
	%{!?_with_ruby:--disable-rubyinterp} \
	%{?_with_ruby:--enable-rubyinterp} \
	%{!?_with_tcl:--disable-tclinterp} \
	%{?_with_tcl:--enable-tclinterp} \
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
	%{!?_with_perl:--disable-perlinterp} \
	%{?_with_perl:--enable-perlinterp} \
	%{!?_with_python:--disable-pythoninterp} \
	%{?_with_python:--enable-pythoninterp} \
	%{!?_with_ruby:--disable-rubyinterp} \
	%{?_with_ruby:--enable-rubyinterp} \
	%{!?_with_tcl:--disable-tclinterp} \
	%{?_with_tcl:--enable-tclinterp} \
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
	%{!?_with_perl:--disable-perlinterp} \
	%{?_with_perl:--enable-perlinterp} \
	%{!?_with_python:--disable-pythoninterp} \
	%{?_with_python:--enable-pythoninterp} \
	%{!?_with_ruby:--disable-rubyinterp} \
	%{?_with_ruby:--enable-rubyinterp} \
	%{!?_with_tcl:--disable-tclinterp} \
	%{?_with_tcl:--enable-tclinterp} \
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
	%{!?_with_perl:--disable-perlinterp} \
	%{?_with_perl:--enable-perlinterp} \
	%{!?_with_python:--disable-pythoninterp} \
	%{?_with_python:--enable-pythoninterp} \
	%{!?_with_ruby:--disable-rubyinterp} \
	%{?_with_ruby:--enable-rubyinterp} \
	%{!?_with_tcl:--disable-tclinterp} \
	%{?_with_tcl:--enable-tclinterp} \
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
rm -f $RPM_BUILD_ROOT%{_bindir}/*

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

%{!?_without_athena:install %{SOURCE2}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?_without_motif: install %{SOURCE3}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?_without_gtk:   install %{SOURCE4}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}
%{!?_without_gnome: install %{SOURCE5}		$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors}

bzip2 -dc %{SOURCE7} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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
%lang(pl) %{_mandir}/pl/man1/vi.1*
%lang(pl) %{_mandir}/pl/man1/ex.1*
%lang(pl) %{_mandir}/pl/man1/view.1*
%lang(pl) %{_mandir}/pl/man1/rview.1*

%files rt
%defattr(644,root,root,755)
%doc vim2html.pl
%attr(755,root,root) %{_bindir}/vimtutor
%dir %{_sysconfdir}/vim
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vim/gvimrc

%dir %{_datadir}/vim
%dir %{_datadir}/vim/v*
%dir %{_datadir}/vim/v*/doc
%{_datadir}/vim/v*/doc/*.txt
%verify(not size mtime md5) %{_datadir}/vim/v*/doc/tags
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
%lang(fi) %{_mandir}/fi/man1/vim*
%lang(fi) %{_mandir}/fi/man1/rvim.*
%lang(fr) %{_mandir}/fr/man1/vim*
%lang(fr) %{_mandir}/fr/man1/rvim.*
%lang(id) %{_mandir}/id/man1/vim*
%lang(id) %{_mandir}/id/man1/rvim.*
%lang(it) %{_mandir}/it/man1/vim*
%lang(pl) %{_mandir}/pl/man1/vim*
%lang(pl) %{_mandir}/pl/man1/rvim.*

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
