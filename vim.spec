# TODO:
# - some nice icon
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
%define		_ver		6.3
%define		_patchlevel	047

Summary:	Vi IMproved - a Vi clone
Summary(de):	VIsual editor iMproved
Summary(es):	Editor visual incrementado
Summary(fr):	Editeur VIM : VIsual editor iMproved
Summary(pl):	Vi IMproved - klon edytora Vi
Summary(pt_BR):	Editor visual incrementado
Summary(ru):	Visual editor IMproved - ����������� ���������� �������� :)
Summary(tr):	Geli�mi� bir vi s�r�m�
Summary(uk):	Visual editor IMproved - ����� ������ �������� :)
Name:		vim
Version:	%{_ver}.%{_patchlevel}
Release:	3
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/editors/vim/unix/%{name}-%{_ver}.tar.bz2
# Source0-md5:	821fda8f14d674346b87e3ef9cb96389
Source1:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{_ver}-lang.tar.gz
# Source1-md5:	5395c4dacbf1c5008b22c4b86794e8a7
Source2:	ftp://ftp.vim.org/pub/editors/vim/extra/%{name}-%{_ver}-extra.tar.gz
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
Patch101:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.001
Patch102:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.002
Patch103:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.003
Patch104:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.004
Patch105:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.005
Patch106:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.006
Patch107:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.007
Patch108:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.008
Patch109:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.009
Patch110:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.010
Patch111:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.011
Patch112:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.012
Patch113:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.013
Patch114:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.014
Patch115:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.015
Patch116:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.016
Patch117:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.017
Patch118:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.018
Patch119:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.019
Patch120:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.020
Patch121:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.021
Patch122:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.022
Patch123:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.023
Patch124:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.024
Patch125:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.025
Patch126:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.026
Patch127:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.027
Patch128:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.028
Patch129:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.029
Patch130:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.030
Patch131:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.031
Patch132:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.032
Patch133:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.033
Patch134:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.034
Patch135:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.035
Patch136:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.036
Patch137:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.037
Patch138:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.038
Patch139:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.039
Patch140:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.040
Patch141:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.041
Patch142:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.042
Patch143:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.043
Patch144:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.044
Patch145:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.045
Patch146:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.046
Patch147:	ftp://ftp.vim.org/pub/editors/vim/patches/6.3/6.3.047
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

%description -l cs
ViM je nov� a vylep�en� editor vych�zej�c� z klasick�ho editoru vi. Vi
byl prvn�m celoobrazovkov�m editorem pro Unix a je st�le velmi
popul�rn�. ViM je obohacen� funkcemi jako: podpora v�ce oken,
v�ce�rov�ov� undo, zv�raz�ov�n� blok� a �adu dal��ch u�ite�n�ch
funkc�.

%description -l de
Der Visual-Editor iMproved ist ein aktualisierter und erweiterter Klon
des vi-Editors, der mit praktisch allen UN*X-Systemen ausgeliefert
wird. Er bringt mehrere Fenster, mehrstufige Widerrufen-Funktion,
Block-Markierung und viele weitere Zusatzfunktionen im Vergleich zum
Standard-vi-Programm.

%description -l es
El editor Visual Mejorado es una versi�n actualizada y con nuevas
caracter�sticas adicionales del mundialmente famoso 'vi' que acompa�a
pr�cticamente todos los sistemas UN*X. Posibilita trabajar con
m�ltiples ventanas, varios niveles de deshacer, bloques enfatizados, y
otras muchas caracter�sticas del 'vi'.

%description -l fr
L'�diteur VIsuel aM�lior� est un clone mis � jour et dot� de
caract�ristiques suppl�mentaires de l'�diteur � vi � fourni avec
pratiquement tous les syst�mes UN*X. Il ajoute les fen�tres
mutltiples, l'annulation a plusieurs niveaux, la mise en �vidence des
blocs et autres caract�ristiques au vi de base.

%description -l id
VIM (VIsual editor iMproved) adalah versi vi editor yang sudah
diupdate dan ditambah kemampuannya. Vi adalah editor untuk UNIX yang
pertama yang menggunakan layar, dan sekarang masih sangat populer. VIM
mengembangkan vi dengan menambah kemampuan baru seperti: multiple
windows, multi-level undo, block highlighting, dll.

%description -l is
VIM (VIsual editor iMproved) er uppf�r� og endurb�tt �tg�fa af vi
ritlinum. Vi var fyrsti skj�-ritillinn fyrir UNIX og er enn mj�g
vins�ll. VIM gerist f��urbetrungur me� n�jum m�guleikum l�kt og
gluggakerfi, i�run og yfirb�t (e: multi-level undo), blokkarvali og
fleira.

%description -l it
VIM (Vi IMproved) � una versione aggiornata e perfezionata dell'editor
vi. Vi � stato il primo editor per UNIX realmente basato su video ed �
ancora molto diffuso. VIM perfeziona vi aggiungendo nuove funzioni:
finestre multiple, funzione \"annulla\" multilivello, evidenziazione
dei blocchi e altro.

%description -l pl
Edytor tekstu podobny do Vi. Wa�ne ulepszenia: mo�liwo�� pracy w wielu
oknach, wielopoziomowa opcja 'cofnij', bloki, pod�wietlanie sk�adni,
folding i wiele innych.

%description -l ja
O VIM (VIsual editor iMproved) � uma vers�o melhorada e actualizada do
editor vi. O vi foi o primeiro verdadeiro editor baseado em ecr� para
o UNIX, e ainda � muito popular. O VIM melhora o vi acrescentando
novas potencialidades: janelas m�ltiplas, anula��o multi-n�vel, realce
de blocos e mais.

%description -l pt_BR
O editor Vim (Vi Enhanced) � um vers�o atualizada e com novas
caracter�sticas do mundialmente famoso 'vi' que acompanha praticamente
todos os sistemas UN*X. Ele possibilita trabalhar com m�ltiplas
janelas, v�rios n�veis de desfazer, blocos enfatizados, e muitas
outras caracter�sticas do 'vi'.

%description -l ru
VIsual editor iMproved - ��� ����������� � ����������� ���������� ����
��������� vi, ������� ������������ ����������� �� �����
UN*X-���������. � ���� ������ ���� �������������� �����, ���������
������, �������������� ��������� � ����� �������...

%description -l sk
VIM (VIsual editor iMproved) je nov�ia a vylep�en� verzia editoru vi.
Vi bol prv�m skuto�ne obrazovkovo orientovan�m editorom pre UNIX a
st�le je ve�mi popul�rny. VIM m� oproti vi vylep�enia ako: pr�cu s
viacer�mi oknami, viacn�sobn� undo, zv�raz�ovanie blokov textu a in�.

%description -l sv
VIM (Vi IMproved) �r en uppdaterad och f�rb�ttrad version av
redigeraren vi. Vi var den f�rsta riktiga sk�rmbaserade redigeraren
till UNIX, och �r fortfarande v�ldigt popul�r. VIM f�rb�ttrar vi med
nya finesser: flera f�nster, flerniv� �ngra, blockmarkering och mer
�nd�.

%description -l tr
Standart vi metin d�zenleyicisinin geli�mi� hali; daha fazla komut,
birden fazla pencere deste�i ve blok i�aretleme yetenekleri i�erir.

%description -l uk
VIsual editor iMproved - �� ��������� �� ������ ��̦������ ����
��������� vi, ���� �������Ѥ���� ��������� ڦ �Ӧ�� UN*X-���������. �
æ� ���Ӧ� � ������Ҧ������ צ����, ��Ħ����� ���˦�, �����������
Ц��צ��� �� ������ ������...

%package -n xxd
Summary:	Utility to convert files to hexdump or do the reverse
Summary(pl):	Narz�dzie do zamiany plik�w na posta� szesnastkow� i odwrotnie
Group:		Applications/Editors/Vim

%description -n xxd
xxd creates a hex dump of a given file or standard input. It can also
convert a hex dump back to its original binary form. Like uuencode and
uudecode it allows the transmission of binary data in a `mail-safe'
ASCII representation, but has the advantage of decoding to standard
output. Moreover, it can be used to perform binary file patching.

%description -n xxd -l pl
xxd tworzy szesnastkowy zapis pliku podanego na standardowe wej�cie.
Mo�e tak�e przekonwertowa� taki zapis na oryginaln�, binarn� posta�.
Podobnie jak uuencode i uudecode pozwala na przesy�anie danych
binarnych w postaci ASCII, ale ma mo�liwo�� dekodowania na standardowe
wyj�cie. Co wi�cej, mo�e by� u�yty do modyfikowania plik�w binarnych.

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
Edytor tekstu podobny do Vi. Ta wersja zosta�a skonsolidowana
statycznie i posiada minimaln� ilo�� dodatk�w. Jest instalowana w /bin
jako narz�dzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, mo�e on pom�c Ci uratowa� system w czasie awarii.

%description static -l ru
����� vim-static ������������� ������������� vim ��� /bin/vi, ���
������ ��� ������� ���� ����� ������������ ������ �������� ��������
�������.

%description static -l uk
����� vim-static ���������� Ҧ������ vim �� /bin/vi, �� ������ ���
������� ��צ�� ��Ħ, ���� ���������� Ԧ���� �������� ������� �������.

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
Edytor tekstu podobny do Vi. Ta wersja zosta�a skompilowana ze
wsparciem dla ispella.

%package rt
Summary:	Vim runtime files
Summary(cs):	Soubory nezbytn� pro libovoln� editor ViM
Summary(da):	F�lles filer som er n�dvendige for enhver version af VIM editoren
Summary(de):	Die von allen Versionen des VIM-Editors ben�tigten gemeinsamen Dateien
Summary(es):	Ficheros comunes a todas las versiones de VIM
Summary(fr):	Fichiers communs indispensables pour toute version de l'�diteur VIM
Summary(id):	File umum yang dibutuhkan oleh semua versi editor VIM
Summary(is):	Grunnskr�r sem allar �tg�fur VIM ritilsins �urfa � a� halda
Summary(it):	File comuni necessari per tutte le versioni dell'editor VIM
Summary(ja):	���٤ƤΥС������� VIM ���ǥ�����ɬ�פȤ���붦�̥ե�����
Summary(nb):	Felles filer som er n�dvendige for enhver versjon av VIM editoren
Summary(pl):	Pliki przydatne edytorowi Vim
Summary(pt):	Os ficheiros comuns necess�rios para qualquer vers�o do editor VIM
Summary(ru):	�����, ��������� ��� ����� ������ ��������� vim
Summary(sk):	Spolo�n� s�bory potrebn� pre v�etky verzie editoru VIM
Summary(sl):	Skupne datoteke, potrebne s katerokoli razli�ico urejevalnika VIM
Summary(sv):	De gemensamma filerna som beh�vs av alla versioner av redigeraren VIM
Summary(uk):	�����, ���Ҧ�Φ ��� ����-��ϧ ���Ӧ� ��������� vim
Summary(zh_CN):	�κΰ汾�� VIM �༭������Ĺ����ļ���
Group:		Applications/Editors/Vim
Requires:	mktemp
Requires:	which
Obsoletes:	vim-common

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for Vim. If you want to take advantage of Vim more
powerful features, you should install this package.

%description rt -l cs
Tento bal��ek obsahuje spole�n� soubory pro v�echny dal�� bal��ky s
vim.

%description rt -l da
The vim-rt package contains files which every VIM binary will need in
order to run.

%description rt -l de
Das Paket vim-rt enth�lt Dateien, die jede VIM-Bin�rdatei f�r die
Ausf�hrung ben�tigt.

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
vim-rt pakkinn inniheldur skr�r sem allar VIM keyrsluskr�rnar �urfa
til a� keyra.

%description rt -l it
Il pacchetto vim-rt contiene i file necessari a ogni binario di VIM
per poter funzionare.

%description rt -l pl
W tym pakiecie znajdziesz dokumentacj�, makra, pliki konfiguracyjne i
strony podr�cznika dla edytora Vim. Je�eli chcesz korzysta� z
zaawansowanych mo�liwo�ci Vima, powiniene� zainstalowa� ten pakiet.

%description rt -l pt
O pacote vim-rt cont�m os ficheiros que todos os execut�veis do VIM
ir�o necessitar para correr.

%description rt -l ru
����� vim-rt �������� ����� (��������, ����� �������), ������� �����
��� ������ ����� ��������� vim.

%description rt -l sk
Bal�k vim-rt obsahuje s�bory, ktor� bude potrebova� pre spr�vnu
funkciu ka�d� verzia editoru VIM.

%description rt -l sv
Paketet vim-rt inneh�ller filer som alla VIM-bin�rer beh�ver f�r att
k�ra.

%description rt -l uk
����� vim-rt ͦ����� ����� (���������, ����� ��צ���), ���Ҧ ���Ҧ�Φ
��� ������ ����-��ϧ �������� vim.

%package -n gvim-athena
Summary:	Vim for X Window built with Athena
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki Athena
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-athena
The classic Unix text editor now also under X Window System! This
version is built with Athena Widget Set.

%description -n gvim-athena -l pl
Wersja edytora Vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki Athena Widget Set.

%description -n gvim-athena -l ru
���� ����� ������������ ����� ������ VIM, ��������� � ������������
Athena Widget Set, ��� ��������� ��������� VIM ��� ���������� X Window
System - � ��������� ����������� ����������� � ���������� ����.

%description -n gvim-athena -l uk
��� ����� ͦ����� ���Ӧ� VIM, ڦ����� � ¦�̦������� Athena Widget
Set, �� ������Ѥ ��������� VIM �� ��������� �������� X Window System -
� ���Φ��� ���Ʀ���� ����������� �� Ц�������� ��ۦ.

%package -n gvim-motif
Summary:	Vim for X Window built with Motif
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki Motif
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-motif
The classic Unix text editor now also under X Window System! This
version is built with Motif.

%description -n gvim-motif -l pl
Wersja edytora Vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki Motif.

%description -n gvim-motif -l ru
���� ����� ������������ ����� ������ VIM, ��������� � ������������
Motif, ��� ��������� ��������� VIM ��� ���������� X Window System - �
��������� ����������� ����������� � ���������� ����.

%description -n gvim-motif -l uk
��� ����� ͦ����� ���Ӧ� VIM, ڦ����� � ¦�̦������� Motif, ��
������Ѥ ��������� VIM �� ��������� �������� X Window System - �
���Φ��� ���Ʀ���� ����������� �� Ц�������� ��ۦ.

%package -n kvim
Summary:	Vim for X Window built with KDE
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki KDE
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n kvim
The classic Unix text editor now also under X Window System! This
version is built with KDE.

%description -n kvim -l pl
Wersja edytora Vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki KDE.

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki GTK
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gtk
The classic Unix text editor now also under X Window System! This
version is built with GTK.

%description -n gvim-gtk -l pl
Wersja edytora Vim pracuj�ca w �rodowisku X Window z wykorzystaniem
biblioteki GTK.

%description -n gvim-gtk -l ru
���� ����� ������������ ����� ������ VIM, ��������� � ������������
GTK, ��� ��������� ��������� VIM ��� ���������� X Window System - �
��������� ����������� ����������� � ���������� ����. ������ �������
'gvim'...

%description -n gvim-gtk -l uk
��� ����� ͦ����� ���Ӧ� VIM, ڦ����� � ¦�̦������� GTK, �� ������Ѥ
��������� VIM �� ��������� �������� X Window System - � ���Φ���
���Ʀ���� ����������� �� Ц�������� ��ۦ. ������ ���֦�� 'gvim'...

%package -n gvim-gnome
Summary:	Vim for X Window built with GNOME
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki GNOME
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv
Obsoletes:	vim-X11

%description -n gvim-gnome
The classic Unix text editor now also under X Window System! This
version is build with GNOME.

%description -n gvim-gnome -l pl
Wersja edytora Vim pracuj�ca w �rodowisku X Window z wykorzystaniem
bibliotek GNOME.

%description -n gvim-gnome -l ru
���� ����� ������������ ����� ������ VIM, ��������� � ������������
GNOME, ��� ��������� ��������� VIM ��� ���������� X Window System - �
��������� ����������� ����������� � ���������� ����.

%description -n gvim-gnome -l uk
��� ����� ͦ����� ���Ӧ� VIM, ڦ����� � ¦�̦������� GNOME, ��
������Ѥ ��������� VIM �� ��������� �������� X Window System - �
���Φ��� ���Ʀ���� ����������� �� Ц�������� ��ۦ.

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
Wersja edytora Vim pracuj�ca w �rodowisku X Window, zbudowana jako
element bonobo.

%prep
%setup -q -b1 -b2 -a5 -n %{name}%(echo %{_ver} | tr -d .)

# official patches
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0
%patch127 -p0
%patch128 -p0
%patch129 -p0
%patch130 -p0
%patch131 -p0
%patch132 -p0
%patch133 -p0
%patch134 -p0
%patch135 -p0
%patch136 -p0
%patch137 -p0
%patch138 -p0
%patch139 -p0
%patch140 -p0
%patch141 -p0
%patch142 -p0
%patch143 -p0
%patch144 -p0
%patch145 -p0
%patch146 -p0
%patch147 -p0

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
%{?with_home_etc:%patch12 -p1}
%{?with_selinux:%patch13 -p1}
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p0 -b .modprobe

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
%lang(pl) %doc %{_datadir}/vim/v*/doc/*.plx
%attr(755,root,root) %{_datadir}/vim/v*/doc/*.pl
%verify(not size mtime md5) %{_datadir}/vim/v*/doc/tags
%lang(pl) %verify(not size mtime md5) %{_datadir}/vim/v*/doc/tags-pl
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
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh.cp936*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh.gb2312*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_zh_cn*
%lang(zh_CN) %{_datadir}/vim/v*/lang/menu_*chinese*gb*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh.cp950*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh.big5*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_zh_tw*
%lang(zh_TW) %{_datadir}/vim/v*/lang/menu_*taiwan*

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
