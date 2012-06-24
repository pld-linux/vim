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
Summary(ru):	Visual editor IMproved - ����������� ���������� �������� :)
Summary(tr):	Geli�mi� bir vi s�r�m�
Summary(uk):	Visual editor IMproved - ����� ������ �������� :)
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
Obsoletes:	vi
Obsoletes:	vim-minimal

%description static
Text editor similar to Vi. This version is built with minimal feature
and is installed in /bin as a rescue tool. The installation of this
package is STRONGLY recommended.

%description static -l pl
Edytor tekstu podobny do Vi. Ta wersja zosta�a zlinkowana statycznie i
posiada minimaln� ilo�� dodatk�w. Jest instalowana w /bin jako
narz�dzie dla administratora. Instalacja tego pakietu jest MOCNO
zalecana, mo�e on pom�c Ci uratowa� system w czasie awarii.

%description static -l ru
����� vim-static ������������� ������������� vim ��� /bin/vi, ���
������ ��� ������� ���� ����� ������������ ������ �������� ��������
�������.

%description static -l uk
����� vim-static ���������� Ҧ������ vim �� /bin/vi, �� ������ ���
������� ��צ�� ��Ħ, ���� ���������� Ԧ���� �������� ������� �������.

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
Summary(no):	Felles filer som er n�dvendige for enhver versjon av VIM editoren
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
Requires:	%{name}-rt = %{version}
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
Requires:	%{name}-rt = %{version}
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

%package -n gvim-gtk
Summary:	Vim for X Window built with gtk
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki GTK
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{version}
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
Summary:	Vim for X Window built with gnome
Summary(pl):	Vim dla X Window korzystaj�cy z biblioteki GNOME
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{version}
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
