#
# Conditional build:
%bcond_without	static	# without static version
%bcond_without	athena	# without Athena Widgets-based gvim
%bcond_without	motif	# without Motif-based gvim
%bcond_without	gtk	# without gtk+-based gvim support
%bcond_without	gnome	# without gnome-based gvim support
%bcond_without	kde	# kvim:)
%bcond_with	perl	# with perl interp
%bcond_with	python	# with python interp
%bcond_with	ruby	# with ruby interp
%bcond_with	tcl	# with tcl interp
%bcond_with	bonobo	# with bonobo component (breaks other things)
%bcond_without  selinux # without selinux
%bcond_without	ispell	# disable vim.ispell
#
%define		_ver		6.2
%define		_patchlevel	498

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
Version:	%{_ver}.%{_patchlevel}
Release:	2
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{_ver}.tar.bz2
# Source0-md5:	c49d360bbd069d00e2a57804f2a123d9
Source1:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{_ver}-lang.tar.gz
# Source1-md5:	aa0079938f636d08be71078933477d8b
Source2:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{_ver}-extra.tar.gz
# Source2-md5:	db0db37baea01874867d8d2414db104c
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source4-md5:	bc4d1e115ca506ad7751b9bd2b773a7f
Source5:	http://freenux.org/kvim/kvim-runtime-6.2.14.tar.bz2
# Source5-md5:	6f633e79bcf5f35918bb0bff6850a971
Source10:	g%{name}-athena.desktop
Source11:	g%{name}-motif.desktop
Source12:	g%{name}-gtk.desktop
Source13:	g%{name}-gnome.desktop
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-ispell.patch
Patch4:		%{name}-ispell-axp.patch
Patch5:		%{name}-%{name}rc.patch
Patch6:		%{name}-no_libelf.patch
Patch7:		%{name}-egrep.patch
Patch8:		%{name}-spec-fix.patch
Patch9:		%{name}-specsyntax.patch
Patch10:	%{name}-specsyntax-pld.patch
Patch11:	%{name}-bonobo.patch
Patch12:	%{name}-home_etc.patch
#Patch12:	%{name}-dynamic_python.patch
Patch13:	%{name}-selinux.patch
Patch14:	%{name}-specsyntax4.patch
Patch15:	%{name}-po.patch
Patch16:	%{name}-filetype_vim-perl_tests.patch

Patch99:	http://www.opensky.ca/gnome-vim/vim-patches/%{name}-bonobo-20040115.patch
Patch101:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.001-100.gz
Patch201:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.101-200.gz
Patch301:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.201-300.gz
Patch401:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.301-400.gz
Patch501:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.401
Patch502:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.402
Patch503:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.403
Patch504:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.404
Patch505:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.405
Patch506:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.406
Patch507:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.407
Patch508:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.408
Patch509:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.409
Patch510:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.410
Patch511:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.411
Patch512:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.412
Patch513:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.413
Patch514:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.414
Patch515:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.415
Patch516:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.416
Patch517:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.417
Patch518:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.418
Patch519:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.419
Patch520:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.420
Patch521:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.421
Patch522:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.422
Patch523:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.423
Patch524:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.424
Patch525:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.425
Patch526:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.426
Patch527:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.427
Patch528:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.428
Patch529:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.429
Patch530:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.430
Patch531:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.431
Patch532:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.432
Patch533:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.433
Patch534:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.434
Patch535:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.435
Patch536:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.436
Patch537:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.437
Patch538:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.438
Patch539:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.439
Patch540:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.440
Patch541:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.441
Patch542:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.442
Patch543:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.443
Patch544:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.444
Patch545:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.445
Patch546:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.446
Patch547:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.447
Patch548:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.448
Patch549:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.449
Patch550:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.450
Patch551:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.451
Patch552:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.452
Patch553:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.453
Patch554:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.454
Patch555:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.455
Patch556:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.456
Patch557:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.457
Patch558:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.458
Patch559:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.459
Patch560:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.460
Patch561:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.461
Patch562:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.462
Patch563:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.463
Patch564:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.464
Patch565:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.465
Patch566:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.466
Patch567:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.467
Patch568:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.468
Patch569:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.469
Patch570:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.470
Patch571:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.471
Patch572:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.472
Patch573:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.473
Patch574:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.474
Patch575:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.475
Patch576:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.476
Patch577:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.477
Patch578:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.478
Patch579:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.479
Patch580:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.480
Patch581:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.481
Patch582:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.482
Patch583:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.483
Patch584:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.484
Patch585:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.485
Patch586:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.486
Patch587:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.487
Patch588:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.488
Patch589:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.489
Patch590:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.490
Patch591:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.491
Patch592:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.492
Patch593:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.493
Patch594:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.494
Patch595:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.495
Patch596:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.496
Patch597:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.497
Patch598:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.498
Patch999:	http://freenux.org/vim/%{name}2kvim-6.2.490.diff.bz2
URL:		http://www.vim.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2.2.1}
%{?with_kde:BuildRequires:	kdelibs-devel >= 9:3.0.0}
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.2.0.1}
%{?with_selinux:BuildRequires:	libselinux-devel}
%{?with_motif:BuildRequires:	motif-devel}
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
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Obsoletes:	vim-enhanced
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# that's example script
%define		_noautoreq	'/bin/csh'

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
Obsoletes:	elvis-static
Obsoletes:	nvi
Obsoletes:	vi
Obsoletes:	vim-minimal

%description static
Text editor similar to Vi. This version is built with minimal feature
and is installed in /bin as a rescue tool. The installation of this
package is STRONGLY recommended.

%description static -l pl
Edytor tekstu podobny do Vi. Ta wersja zostaЁa skonsolidowana
statycznie i posiada minimaln╠ ilo╤Ф dodatkСw. Jest instalowana w /bin
jako narzЙdzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, mo©e on pomСc Ci uratowaФ system w czasie awarii.

%description static -l ru
Пакет vim-static устанавливает разновидность vim как /bin/vi, что
удобно для запуска даже когда смонтирована только корневая файловая
система.

%description static -l uk
Пакет vim-static встановлю╓ р╕зновид vim як /bin/vi, що зручно для
запуску нав╕ть тод╕, коли змонтована т╕льки корньова файлова система.

%package ispell
Summary:	Vim with ispell support
Summary(pl):	Vim z wsparciem dla ispella
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Conflicts:	ispell < 3.2.06
Conflicts:	ispell-pl < 20021127-2

%description ispell
Text editor similar to Vi. This version is built with ispell support.

%description ispell -l pl
Edytor tekstu podobny do Vi. Ta wersja zostaЁa skompilowana ze
wsparciem dla ispella.

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
Summary(nb):	Felles filer som er nЬdvendige for enhver versjon av VIM editoren
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
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
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

%package -n kvim
Summary:	Vim for X Window built with KDE
Summary(pl):	Vim dla X Window korzystaj╠cy z biblioteki KDE
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n kvim
The classic Unix text editor now also under X Window System! This
version is built with KDE.

%description -n kvim -l pl
Wersja edytora Vim pracuj╠ca w ╤rodowisku X Window z wykorzystaniem
biblioteki KDE.

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj╠cy z biblioteki GTK
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
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

%package -n gvim-bonobo
Summary:	Vim for X Window built as bonobo component
Summary(pl):	Vim dla X Window zbudowany jako element bonobo
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-bonobo
The classic Unix text editor now also under X Window System! This
version is build as bonobo component.

%description -n gvim-bonobo -l pl
Wersja edytora Vim pracuj╠ca w ╤rodowisku X Window, zbudowana jako
element bonobo.

%prep
%setup -q -b1 -b2 -a5 -n %{name}%(echo %{_ver} | tr -d .)
# official patches
# cumulative
%patch101 -p0
%patch201 -p0
%patch301 -p0
%patch401 -p0

# single
%patch501 -p0
%patch502 -p0
%patch503 -p0
%patch504 -p0
%patch505 -p0
%patch506 -p0
%patch507 -p0
%patch508 -p0
%patch509 -p0
%patch510 -p0
%patch511 -p0
%patch512 -p0
%patch513 -p0
%patch514 -p0
%patch515 -p0
%patch516 -p0
%patch517 -p0
%patch518 -p0
%patch519 -p0
%patch520 -p0
%patch521 -p0
%patch522 -p0
%patch523 -p0
%patch524 -p0
%patch525 -p0
%patch526 -p0
%patch527 -p0
%patch528 -p0
%patch529 -p0
%patch530 -p0
%patch531 -p0
%patch532 -p0
%patch533 -p0
%patch534 -p0
%patch535 -p0
%patch536 -p0
%patch537 -p0
%patch538 -p0
%patch539 -p0
%patch540 -p0
%patch541 -p0
%patch542 -p0
%patch543 -p0
%patch544 -p0
%patch545 -p0
%patch546 -p0
%patch547 -p0
%patch548 -p0
%patch549 -p0
%patch550 -p0
%patch551 -p0
%patch552 -p0
%patch553 -p0
%patch554 -p0
%patch555 -p0
%patch556 -p0
%patch557 -p0
%patch558 -p0
%patch559 -p0
%patch560 -p0
%patch561 -p0
%patch562 -p0
%patch563 -p0
%patch564 -p0
%patch565 -p0
%patch566 -p0
%patch567 -p0
%patch568 -p0
%patch569 -p0
%patch570 -p0
%patch571 -p0
%patch572 -p0
%patch573 -p0
%patch574 -p0
%patch575 -p0
%patch576 -p0
%patch577 -p0
%patch578 -p0
%patch579 -p0
%patch580 -p0
%patch581 -p0
%patch582 -p0
%patch583 -p0
%patch584 -p0
%patch585 -p0
%patch586 -p0
%patch587 -p0
%patch588 -p0
%patch589 -p0
%patch590 -p0
%patch591 -p0
%patch592 -p0
%patch593 -p0
%patch594 -p0
%patch595 -p0
#%patch596 -p0
%patch597 -p0
%patch598 -p0

# kvim
%patch999 -p1

%patch0 -p1
%{?with_bonobo:%patch99 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%ifarch alpha
%patch4 -p1
%endif
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%{?with_bonobo:%patch11 -p1}
%patch12 -p1
%{?with_selinux:%patch13 -p1}
%patch14 -p1
%patch15 -p1
%patch16 -p1

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
install -m755 src/bin/kvim  $RPM_BUILD_ROOT%{_bindir}/kvim
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,22x22}/actions
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{32x32,48x48,64x64}/apps
install runtime/hi16-action-make.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions
install runtime/hi22-action-make.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/actions
install runtime/kvim32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/kvim.png
install runtime/kvim48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/kvim.png
install runtime/kvim64x64.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/kvim.png
install runtime/KVim.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde
echo "Categories=Qt;KDE;Utility;TextEditor" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/KVim.desktop
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/rvim

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
%lang(pl) %{_mandir}/pl/man1/vi.1*
%lang(pl) %{_mandir}/pl/man1/ex.1*
%lang(pl) %{_mandir}/pl/man1/view.1*
%lang(pl) %{_mandir}/pl/man1/rview.1*

%if %{with ispell}
%files ispell
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim.ispell
%endif

%files -n xxd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxd
%{_mandir}/man1/xxd.1*

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
%attr(755,root,root) %{_datadir}/vim/v*/doc/*.pl
%verify(not size mtime md5) %{_datadir}/vim/v*/doc/tags
%{_datadir}/vim/v*/ftplugin
%{_datadir}/vim/v*/indent
%{_datadir}/vim/v*/keymap
%dir %{_datadir}/vim/v*/lang
%doc %{_datadir}/vim/v*/lang/README*

%lang(af) %{_datadir}/vim/v*/lang/af
%lang(en_GB) %{_datadir}/vim/v*/lang/en_GB
%lang(cs) %{_datadir}/vim/v*/lang/cs
%lang(de) %{_datadir}/vim/v*/lang/de
%lang(es) %{_datadir}/vim/v*/lang/es
%lang(fr) %{_datadir}/vim/v*/lang/fr
%lang(it) %{_datadir}/vim/v*/lang/it
%lang(ja) %{_datadir}/vim/v*/lang/ja*
%lang(ko) %{_datadir}/vim/v*/lang/ko
%lang(pl) %{_datadir}/vim/v*/lang/pl
%lang(sk) %{_datadir}/vim/v*/lang/sk
%lang(nb) %{_datadir}/vim/v*/lang/no
#%lang(tr) %{_datadir}/vim/v*/lang/tr
%lang(uk) %{_datadir}/vim/v*/lang/uk
%lang(zh_CN) %{_datadir}/vim/v*/lang/zh_CN*
%lang(zh_TW) %{_datadir}/vim/v*/lang/zh_TW*

%lang(af) %{_datadir}/vim/v*/lang/menu_af_af*
%lang(cs) %{_datadir}/vim/v*/lang/menu_cs_cz*
%lang(de) %{_datadir}/vim/v*/lang/menu_de_de*
%lang(es) %{_datadir}/vim/v*/lang/menu_es_es*
%lang(en_GB) %{_datadir}/vim/v*/lang/menu_en_gb*
%lang(fr) %{_datadir}/vim/v*/lang/menu_fr_fr*
%lang(hu) %{_datadir}/vim/v*/lang/menu_hu_hu*
%lang(it) %{_datadir}/vim/v*/lang/menu_it_it*
%lang(ja) %{_datadir}/vim/v*/lang/menu_ja_jp*
%lang(ko) %{_datadir}/vim/v*/lang/menu_ko_kr*
%lang(nl) %{_datadir}/vim/v*/lang/menu_nl_nl*
%lang(nb) %{_datadir}/vim/v*/lang/menu_no_no*
%lang(pl) %{_datadir}/vim/v*/lang/menu_pl_pl*
%lang(pt) %{_datadir}/vim/v*/lang/menu_pt_br*
%lang(sk) %{_datadir}/vim/v*/lang/menu_sk_sk*
%lang(sr) %{_datadir}/vim/v*/lang/menu_sr_yu*
%lang(uk) %{_datadir}/vim/v*/lang/menu_uk_ua*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh_cn*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh_tw*

%{_datadir}/vim/v*/macros
%{_datadir}/vim/v*/plugin
%{_datadir}/vim/v*/print
%{_datadir}/vim/v*/syntax
%{_datadir}/vim/v*/tools
%{_datadir}/vim/v*/tutor
%{_datadir}/vim/v*/colors
%{_datadir}/vim/v*/compiler
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
%lang(it) %{_mandir}/it/man1/vim*
%lang(pl) %{_mandir}/pl/man1/vim*
%lang(pl) %{_mandir}/pl/man1/rvim.*
%lang(pl) %{_mandir}/pl/man1/gvi*
%lang(pl) %{_mandir}/pl/man1/rgv*

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
