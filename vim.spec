#
# Conditional build:
%bcond_without static # without static version
%bcond_without athena # without Athena Widgets-based gvim
%bcond_without motif  # without Motif-based gvim
%bcond_without gtk    # without gtk+-based gvim support
%bcond_without gnome  # without gnome-based gvim support
%bcond_with    perl   # with perl interp
%bcond_with    python # with python interp
%bcond_with    ruby   # with ruby interp
%bcond_with    tcl    # with tcl interp
%bcond_with    bonobo # with bonobo patch (doesn't work at the moment)
#
%define		_ver		6.2
%define		_patchlevel	211

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
Release:	1
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
Source10:	g%{name}-athena.desktop
Source11:	g%{name}-motif.desktop
Source12:	g%{name}-gtk.desktop
Source13:	g%{name}-gnome.desktop
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-ispell.patch
Patch4:		%{name}-ispell-axp.patch
Patch5:		%{name}-vimrc.patch
Patch6:		%{name}-no_libelf.patch
Patch7:		%{name}-egrep.patch
Patch8:		%{name}-spec-fix.patch
Patch9:		%{name}-specsyntax.patch
Patch10:	%{name}-specsyntax-pld.patch
Patch11:	%{name}-bonobo.patch
Patch12:	%{name}-home_etc.patch
#Patch12:	%{name}-dynamic_python.patch
Patch13:	%{name}-selinux.patch

Patch99:	http://www.opensky.ca/gnome-vim/patches/vim-bonobo-20030726.patch
Patch101:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.001
Patch102:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.002
Patch103:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.003
Patch104:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.004
Patch105:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.005
Patch106:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.006
Patch107:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.007
Patch108:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.008
Patch109:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.009
Patch110:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.010
Patch111:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.011
Patch112:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.012
Patch113:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.013
Patch114:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.014
Patch115:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.015
Patch116:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.016
Patch117:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.017
Patch118:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.018
Patch119:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.019
Patch120:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.020
Patch121:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.021
Patch122:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.022
Patch123:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.023
Patch124:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.024
Patch125:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.025
Patch126:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.026
Patch127:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.027
Patch128:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.028
Patch129:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.029
Patch130:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.030
Patch131:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.031
Patch132:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.032
Patch133:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.033
Patch134:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.034
Patch135:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.035
Patch136:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.036
Patch137:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.037
Patch138:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.038
Patch139:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.039
Patch140:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.040
Patch141:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.041
Patch142:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.042
Patch143:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.043
Patch144:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.044
Patch145:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.045
Patch146:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.046
Patch147:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.047
Patch148:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.048
Patch149:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.049
Patch150:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.050
Patch151:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.051
Patch152:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.052
Patch153:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.053
Patch154:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.054
Patch155:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.055
Patch156:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.056
Patch157:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.057
Patch158:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.058
Patch159:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.059
Patch160:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.060
Patch161:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.061
Patch162:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.062
Patch163:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.063
Patch164:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.064
Patch165:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.065
Patch166:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.066
Patch167:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.067
Patch168:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.068
Patch169:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.069
Patch170:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.070
Patch171:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.071
Patch172:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.072
Patch173:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.073
Patch174:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.074
Patch175:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.075
Patch176:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.076
Patch177:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.077
Patch178:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.078
Patch179:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.079
Patch180:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.080
Patch181:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.081
Patch182:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.082
Patch183:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.083
Patch184:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.084
Patch185:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.085
Patch186:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.086
Patch187:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.087
Patch188:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.088
Patch189:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.089
Patch190:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.090
Patch191:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.091
Patch192:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.092
Patch193:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.093
Patch194:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.094
Patch195:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.095
Patch196:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.096
Patch197:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.097
Patch198:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.098
Patch199:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.099
Patch200:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.100
Patch201:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.101
Patch202:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.102
Patch203:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.103
Patch204:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.104
Patch205:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.105
Patch206:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.106
Patch207:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.107
Patch208:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.108
Patch209:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.109
Patch210:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.110
Patch211:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.111
Patch212:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.112
Patch213:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.113
Patch214:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.114
Patch215:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.115
Patch216:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.116
Patch217:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.117
Patch218:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.118
Patch219:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.119
Patch220:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.120
Patch221:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.121
Patch222:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.122
Patch223:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.123
Patch224:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.124
Patch225:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.125
Patch226:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.126
Patch227:       ftp://ftp.vim.org/pub/editors/vim/patches/6.2.127
Patch228:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.128
Patch229:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.129
Patch230:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.130
Patch231:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.131
Patch232:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.132
Patch233:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.133
Patch234:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.134
Patch235:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.135
Patch236:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.136
Patch237:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.137
Patch238:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.138
Patch239:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.139
Patch240:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.140
Patch241:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.141
Patch242:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.142
Patch243:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.143
Patch244:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.144
Patch245:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.145
Patch246:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.146
Patch247:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.147
Patch248:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.148
Patch249:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.149
Patch250:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.150
Patch251:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.151
Patch252:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.152
Patch253:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.153
Patch254:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.154
Patch255:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.155
Patch256:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.156
Patch257:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.157
Patch258:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.158
Patch259:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.159
Patch260:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.160
Patch261:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.161
Patch262:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.162
Patch263:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.163
Patch264:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.164
Patch265:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.165
Patch266:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.166
Patch267:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.167
Patch268:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.168
Patch269:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.169
Patch270:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.170
Patch271:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.171
Patch272:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.172
Patch273:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.173
Patch274:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.174
Patch275:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.175
Patch276:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.176
Patch277:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.177
Patch278:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.178
Patch279:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.179
Patch280:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.180
Patch281:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.181
Patch282:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.182
Patch283:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.183
Patch284:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.184
Patch285:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.185
Patch286:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.186
Patch287:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.187
Patch288:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.188
Patch289:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.189
Patch290:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.190
Patch291:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.191
Patch292:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.192
Patch293:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.193
Patch294:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.194
Patch295:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.195
Patch296:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.196
Patch297:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.197
Patch298:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.198
Patch299:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.199
Patch300:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.200
Patch301:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.201
Patch302:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.202
Patch303:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.203
Patch304:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.204
Patch305:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.205
Patch306:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.206
Patch307:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.207
Patch308:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.208
Patch309:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.209
Patch310:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.210
Patch311:	ftp://ftp.vim.org/pub/editors/vim/patches/6.2.211
URL:		http://www.vim.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2.2.1}
BuildRequires:	ncurses-devel
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.2.0.1}
BuildRequires:	libselinux-devel
%{?with_motif:BuildRequires:	motif-devel}
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python:BuildRequires:	python-devel}
%{?with_ruby:BuildRequires:	ruby}
%{?with_tcl:BuildRequires:	tcl-devel}
%if %{with bonobo}
BuildRequires:	ORBit2-devel
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	nautilus-devel >= 2.2.0
%endif
%if %{with static}
BuildRequires:	acl-static
BuildRequires:	attr-static
BuildRequires:	glibc-static
BuildRequires:	libselinux-static
BuildRequires:	ncurses-static
%else
Provides:	%{name}-static = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-static
%endif
Requires:	%{name}-rt = %{epoch}:%{version}
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
Requires:	%{name}-rt = %{epoch}:%{version}
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
Requires:	%{name}-rt = %{epoch}:%{version}
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
Requires:	%{name}-rt = %{epoch}:%{version}
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
Requires:	%{name}-rt = %{epoch}:%{version}
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
Requires:	%{name}-rt = %{epoch}:%{version}
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
%setup -q -b1 -b2 -n %{name}%(echo %{_ver} | tr -d .)
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
%patch148 -p0
%patch149 -p0
%patch150 -p0
%patch151 -p0
%patch152 -p0
%patch153 -p0
%patch154 -p0
%patch155 -p0
%patch156 -p0
%patch157 -p0
%patch158 -p0
%patch159 -p0
%patch160 -p0
%patch161 -p0
%patch162 -p0
%patch163 -p0
%patch164 -p0
%patch165 -p0
%patch166 -p0
%patch167 -p0
%patch168 -p0
%patch169 -p0
%patch170 -p0
%patch171 -p0
%patch172 -p0
%patch173 -p0
%patch174 -p0
%patch175 -p0
%patch176 -p0
%patch177 -p0
%patch178 -p0
%patch179 -p0
%patch180 -p0
%patch181 -p0
%patch182 -p0
%patch183 -p0
%patch184 -p0
%patch185 -p0
%patch186 -p0
%patch187 -p0
%patch188 -p0
%patch189 -p0
%patch190 -p0
%patch191 -p0
%patch192 -p0
%patch193 -p0
%patch194 -p0
%patch195 -p0
%patch196 -p0
%patch197 -p0
%patch198 -p0
%patch199 -p0
%patch200 -p0
%patch201 -p0
%patch202 -p0
%patch203 -p0
%patch204 -p0
%patch205 -p0
%patch206 -p0
%patch207 -p0
%patch208 -p0
%patch209 -p0
%patch210 -p0
%patch211 -p0
%patch212 -p0
%patch213 -p0
%patch214 -p0
%patch215 -p0
%patch216 -p0
%patch217 -p0
%patch218 -p0
%patch219 -p0
%patch220 -p0
%patch221 -p0
%patch222 -p0
%patch223 -p0
%patch224 -p0
%patch225 -p0
%patch226 -p0
%patch227 -p0
%patch228 -p0
%patch229 -p0
%patch230 -p0
%patch231 -p0
%patch232 -p0
%patch233 -p0
%patch234 -p0
%patch235 -p0
%patch236 -p0
%patch237 -p0
%patch238 -p0
%patch239 -p0
%patch240 -p0
%patch241 -p0
%patch242 -p0
%patch243 -p0
%patch244 -p0
%patch245 -p0
%patch246 -p0
%patch247 -p0
%patch248 -p0
%patch249 -p0
%patch250 -p0
%patch251 -p0
%patch252 -p0
%patch253 -p0
%patch254 -p0
%patch255 -p0
%patch256 -p0
%patch257 -p0
%patch258 -p0
%patch259 -p0
%patch260 -p0
%patch261 -p0
%patch262 -p0
%patch263 -p0
%patch264 -p0
%patch265 -p0
%patch266 -p0
%patch267 -p0
%patch268 -p0
%patch269 -p0
%patch270 -p0
%patch271 -p0
%patch272 -p0
%patch273 -p0
%patch274 -p0
%patch275 -p0
%patch276 -p0
%patch277 -p0
%patch278 -p0
%patch279 -p0
%patch280 -p0
%patch281 -p0
%patch282 -p0
%patch283 -p0
%patch284 -p0
%patch285 -p0
%patch286 -p0
%patch287 -p0
%patch288 -p0
%patch289 -p0
%patch290 -p0
%patch291 -p0
%patch292 -p0
%patch293 -p0
%patch294 -p0
%patch295 -p0
%patch296 -p0
%patch297 -p0
%patch298 -p0
%patch299 -p0
%patch300 -p0
%patch301 -p0
%patch302 -p0
%patch303 -p0
%patch304 -p0
%patch305 -p0
%patch306 -p0
%patch307 -p0
%patch308 -p0
%patch309 -p0
%patch310 -p0
%patch311 -p0

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
%patch13 -p1

%build
cd src
%{__autoconf}
# needed to prevent deconfiguring
cp -f configure auto

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
mv -f vim vim.static
LDFLAGS="%{rpmldflags}"
%endif

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
mv -f vim vim.ncurses
%{__make} xxd/xxd

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
mv -f vim vim.ispell

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
mv -f vim gvim.athena
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
mv -f vim gvim.motif
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
mv -f vim gvim.gtk
%endif

%if %{with gnome}
%{__make} distclean
%configure \
	CFLAGS="%{rpmcflags} -DFEAT_SPELL_HL" \
	--with-features=huge \
	--enable-gui=gnome2 \
	%{?with_bonobo:--enable-bonobo} \
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
mv -f vim gvim.gnome
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/*

%if %{with static}
install src/vim.ncurses	$RPM_BUILD_ROOT%{_bindir}/vim
install src/vim.static	$RPM_BUILD_ROOT/bin/vi
%else
install src/vim.ncurses	$RPM_BUILD_ROOT/bin/vi
ln -sf /bin/vi		$RPM_BUILD_ROOT%{_bindir}/vim
%endif

install src/vim.ispell	$RPM_BUILD_ROOT%{_bindir}/vim.ispell
install src/xxd/xxd	$RPM_BUILD_ROOT%{_bindir}/xxd
install src/vimtutor	$RPM_BUILD_ROOT%{_bindir}/vimtutor

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
install src/gvim.athena	$RPM_BUILD_ROOT%{_bindir}/gvim.athena
install %{SOURCE10}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with motif}
install src/gvim.motif	$RPM_BUILD_ROOT%{_bindir}/gvim.motif
install %{SOURCE11}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gnome}
install src/gvim.gnome	$RPM_BUILD_ROOT%{_bindir}/gvim.gnome
install %{SOURCE13}	$RPM_BUILD_ROOT%{_desktopdir}
%endif
%if %{with gtk}
install src/gvim.gtk	$RPM_BUILD_ROOT%{_bindir}/gvim.gtk
ln -sf gvim.gtk		$RPM_BUILD_ROOT%{_bindir}/gvim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgvim
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/gview
ln -sf gvim		$RPM_BUILD_ROOT%{_bindir}/rgview
install %{SOURCE12}	$RPM_BUILD_ROOT%{_desktopdir}
%endif

# Bonobo
%if %{with bonobo}
install -d $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
install src/Vim_Control.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
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

%files ispell
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vim.ispell

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
%lang(no) %{_datadir}/vim/v*/lang/no
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
%lang(no) %{_datadir}/vim/v*/lang/menu_no_no*
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
%{?with_bonobo:%{_libdir}/bonobo/servers/*}
%endif
