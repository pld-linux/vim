" Filename:    spec.vim
" Purpose:     Vim syntax file
" Language:    SPEC: Build/install scripts for Linux RPM packages
" Maintainer:  Donovan Rebbechi elflord@pegasus.rutgers.edu
" URL:	       http://pegasus.rutgers.edu/~elflord/vim/syntax/spec.vim
" Last Change: Tue Oct  3 17:35:15 BRST 2000 <aurelio@conectiva.com.br>

" For version 5.x: Clear all syntax items
" For version 6.x: Quit when a syntax file was already loaded
if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

syn sync minlines=1000

syn match specSpecialChar contained '[][!$()\\|>^;:]'
syn match specColon       contained ':'
syn match specPercent     contained '%'

syn match specVariables   contained '\$\h\w*' contains=specSpecialVariablesNames,specSpecialChar
syn match specVariables   contained '\${\w*}' contains=specSpecialVariablesNames,specSpecialChar

syn match specMacroIdentifier contained '%\h\w*' contains=specMacroNameLocal,specMacroNameOther,specPercent
"syn match specMacroIdentifier contained '%{\w*}' contains=specMacroNameLocal,specMacroNameOther,specPercent,specSpecialChar
syn region specMacroIdentifier oneline matchgroup=Special start='%{' skip='\\}' end='}' contains=specMacroNameLocal,specMacroNameOther,specPercent,specSpecialChar
syn match specBcond contained '%{with\(out\)\?\s\+[a-zA-Z0-9_-]\+}'

syn match specSpecialVariables contained '\$[0-9]\|\${[0-9]}'
syn match specCommandOpts      contained '\s\(-\w\+\|--\w[a-zA-Z0-9_-]\+\)'ms=s+1
syn match specComment '^\s*#.*$'


syn case match


" matches with no highlight
syn match specNoNumberHilite 'X11\|X11R6\|[a-zA-Z]*\.\d\|[a-zA-Z][-/]\d'
syn match specManpageFile '[a-zA-Z]\.1'

" Day, Month and most used license acronyms
syn keyword specLicense contained GPL LGPL BSD MIT GNU
syn keyword specWeekday contained Mon Tue Wed Thu Fri Sat Sun
syn keyword specMonth   contained Jan Feb Mar Apr Jun Jul Aug Sep Oct Nov Dec
syn keyword specMonth   contained January February March April May June July August September October November December

" #, @, www
syn match specNumber '\(^-\=\|[ \t]-\=\|-\)[0-9.-]*[0-9]'
syn match specEmail contained "<\=\<[A-Za-z0-9_.-]\+@\([A-Za-z0-9_-]\+\.\)\+[A-Za-z]\+\>>\="
syn match specURL      contained '\<\(\(https\{0,1}\|ftp\)://\|\(www[23]\{0,1}\.\|ftp\.\)\)[A-Za-z0-9._/~:,#?=-]\+\>'
syn match specURLMacro contained '\<\(\(https\{0,1}\|ftp\)://\|\(www[23]\{0,1}\.\|ftp\.\)\)[A-Za-z0-9._/~:,#%{}-]\+\>' contains=specMacroIdentifier

" TODO take specSpecialVariables out of the cluster for the sh* contains (ALLBUT)
" Special system directories
syn match specListedFilesPrefix contained '/\(usr\|local\|opt\|X11R6\|X11\)/'me=e-1
syn match specListedFilesBin    contained '/s\=bin/'me=e-1
syn match specListedFilesLib    contained '/\(lib\|include\)/'me=e-1
syn match specListedFilesDoc    contained '/\(man\d*\|doc\|info\)\>'
syn match specListedFilesEtc    contained '/etc/'me=e-1
syn match specListedFilesShare  contained '/share/'me=e-1
syn cluster specListedFiles contains=specListedFilesBin,specListedFilesLib,specListedFilesDoc,specListedFilesEtc,specListedFilesShare,specListedFilesPrefix,specVariables,specSpecialChar

" specComands
syn match   specConfigure  contained '\./configure'
syn match   specTarCommand contained '\<tar\s\+[cxvpzjf]\{,5}\s*'
syn match   specMacro contained '%\(\(group\|user\)\(add\|remove\)\|banner\|service\|addusertogroup\|\(\(nsplugin\|apache_config\)_\(un\)\?install\)\|depmod\|py_o\?comp\)'
" XXX don't forget to update specScriptArea when updating specMacro
syn keyword specCommandSpecial contained root
syn keyword specCommand		contained make xmkmf mkdir chmod find sed rm strip moc echo grep ls rm mv mkdir chown install cp pwd cat tail then else elif cd gzip rmdir ln eval export touch unzip bzip2
syn cluster specCommands contains=specCommand,specTarCommand,specConfigure,specCommandSpecial,specMacro

" frequently used rpm env vars
syn keyword specSpecialVariablesNames contained RPM_BUILD_ROOT RPM_BUILD_DIR RPM_SOURCE_DIR RPM_OPT_FLAGS LDFLAGS CC CC_FLAGS CPPNAME CFLAGS CXX CXXFLAGS CPPFLAGS

" valid macro names from /usr/lib/rpm/macros
syn keyword specMacroNameOther contained buildroot buildsubdir debugcflags debuginfocflags date distribution disturl ix86 x8664
syn keyword specMacroNameOther contained kgcc kgcc_package name nil optflags packager perl_archlib perl_privlib perl_sitearch
syn keyword specMacroNameOther contained perl_sitelib perl_vendorarch perl_vendorlib py_sitedir py_sitescriptdir release
syn keyword specMacroNameOther contained rpmcflags rpmcxxflags rpmldflags tmpdir vendor version epoch php_pear_dir
syn keyword specMacroNameOther contained requires_eq requires_releq_kernel_up requires_releq_kernel_smp releq_kernel_up releq_kernel_smp __kernel_ver
syn keyword specMacroNameOther contained requires_php_extension requires_zend_extension pear_package_setup pear_package_install
syn match   specMacroNameOther contained '\<\(PATCH\|SOURCE\)\d*\>'

" valid _macro names from /usr/lib/rpm/macros
syn keyword specMacroNameLocal contained _aclocaldir _applnkdir _arch _binary_payload _bindir _build _build_arch _build_alias
syn keyword specMacroNameLocal contained _build_cpu _builddir _build_os _buildshell _buildsubdir _build_vendor _bzip2bin _datadir
syn keyword specMacroNameLocal contained _dbpath _dbpath_rebuild _defaultdocdir _desktopdir _docdir _examplesdir _excludedocs _kdedocdir
syn keyword specMacroNameLocal contained _exec_prefix _fixgroup _fixowner _fixperms _fontsdir _ftpport _ftpproxy _gnu _gpg_name
syn keyword specMacroNameLocal contained _gpg_path _gtkdocdir _gzipbin _host _host_alias _host_cpu _host_os _host_vendor
syn keyword specMacroNameLocal contained _httpport _httpproxy _iconsdir _includedir _infodir _initrddir _install_langs
syn keyword specMacroNameLocal contained _install_script_path _instchangelog _javaclasspath _javadir _javadocdir _kernelsrcdir
syn keyword specMacroNameLocal contained _kernel_ver _kernel_ver_str _langpatt _lib _libdir _libexecdir _localstatedir _mandir
syn keyword specMacroNameLocal contained _netsharedpath _oldincludedir _omf_dest_dir _os _package_version _pgpbin _pgp_name
syn keyword specMacroNameLocal contained _pgp_path _pixmapsdir _pkgconfigdir _prefix _preScriptEnvironment _provides _rpmdir
syn keyword specMacroNameLocal contained _rpmfilename _sbindir _sharedstatedir _signature _smp_mflags _sourcedir _source_payload
syn keyword specMacroNameLocal contained _specdir _srcrpmdir _sysconfdir _target _target_alias _target_cpu _target_os _target_platform
syn keyword specMacroNameLocal contained _target_vendor _target_base_arch _timecheck _tmppath _topdir _usr _usrsrc _var _vendor
syn keyword specMacroNameLocal contained __cxx __cc __make __perl __libtoolize __autopoint __aclocal __autoconf __automake __autoheader __gettextize __sed


" ------------------------------------------------------------------------------
" here's is all the spec sections definitions: PreAmble, Description, Package,
"   Scripts, Files and Changelog

" One line macros - valid in all ScriptAreas
" tip: remember do include new items on specScriptArea's skip section
syn region specSectionMacroArea oneline matchgroup=specSectionMacro start='^%\(\(un\)\?define\|dump\|trace\|patch\d*\|setup\|configure2_13\|configure\|GNUconfigure\|find_lang\|makeinstall\|bcond_with\(out\)\?\|include\)\>' end='$' contains=specCommandOpts,specMacroIdentifier,specSectionMacroBcondArea
syn region specSectionMacroBracketArea oneline matchgroup=specSectionMacro start='^%{\(configure2_13\|configure\|GNUconfigure\|find_lang\|makeinstall\)}' end='$' contains=specCommandOpts,specMacroIdentifier
syn region specSectionMacroBcondArea oneline matchgroup=specBlock start='%{!\??\(with\(out\)\?_[a-zA-Z0-9_]\+\|debug\):' skip='\\}' end='}' contains=ALLBUT,shCase

" %% Files Section %%
" TODO %config valid parameters: missingok\|noreplace
" TODO %verify valid parameters: \(not\)\= \(md5\|atime\|...\)
syn region specFilesArea matchgroup=specSection start='^%[Ff][Ii][Ll][Ee][Ss]\>' skip='%\(attrib\|defattr\|attr\|dir\|config\|docdir\|doc\|lang\|verify\|ghost\|exclude\|dev\|if\|else\|endif\)\>' end='^%[a-zA-Z]'me=e-2 contains=specFilesOpts,specFilesDirective,@specListedFiles,specComment,specCommandSpecial,specMacroIdentifier,specSectionMacroBcondArea,specIf
" tip: remember to include new items in specFilesArea above
syn match  specFilesDirective contained '%\(attrib\|defattr\|attr\|dir\|config\|docdir\|doc\|lang\|verify\|ghost\|exclude\|dev\)\>'

" valid options for certain section headers
syn match specDescriptionOpts contained '\s-[ln]\s*\a'ms=s+1,me=e-1
syn match specPackageOpts     contained    '\s-n\s*\w'ms=s+1,me=e-1
syn match specFilesOpts       contained    '\s-f\s*\w'ms=s+1,me=e-1


syn case ignore


" %% PreAmble Section %%
" Copyright and Serial were deprecated by License and Epoch
syn region specPreAmbleDeprecated oneline matchgroup=specError start='^\(Copyright\|Serial\)' end='$' contains=specEmail,specURL,specURLMacro,specLicense,specColon,specVariables,specSpecialChar,specMacroIdentifier
syn region specPreAmble oneline matchgroup=specCommand
	\ start='\(^\|\(^%{!\??\(with\(out\)\?_[a-zA-Z0-9_]\+\|debug\):\)\@<=\)\(Prereq\|Summary\|Name\|Version\|Packager\|Requires\|Icon\|URL\|Source\d*\|Patch\d*\|Prefix\|Packager\|Group\|License\|Release\|BuildRoot\|Distribution\|Vendor\|Provides\|ExclusiveArch\|ExcludeArch\|ExclusiveOS\|Obsoletes\|BuildArch\|BuildArchitectures\|BuildRequires\|BuildConflicts\|BuildPreReq\|Conflicts\|AutoRequires\|AutoReqProv\|AutoReq\|AutoProv\|Epoch\|NoSource\)'
	\ end='$\|}\@='
	\ contains=specEmail,specURL,specURLMacro,specLicense,specColon,specVariables,specSpecialChar,specMacroIdentifier,specSectionMacroBcondArea

" %% Description Section %%
syn region specDescriptionArea matchgroup=specSection start='^%description' end='^%'me=e-1 contains=specDescriptionOpts,specEmail,specURL,specNumber,specMacroIdentifier,specComment

" %% Package Section %%
syn region specPackageArea matchgroup=specSection start='^%package' end='^%'me=e-1 contains=specPackageOpts,specPreAmble,specComment

" %% Scripts Section %%
syn region specScriptArea matchgroup=specSection
	\ start='^%\(prep\|build\|install\|clean\|pre\|postun\|preun\|post\|triggerin\|triggerun\|triggerpostun\|pretrans\|posttrans\|verifyscript\)\>'
	\ skip='^%{\|^%\(define\|patch\d*\|configure2_13\|configure\|GNUconfigure\|setup\|find_lang\|makeinstall\|useradd\|groupadd\|addusertogroup\|banner\|service\|py_o\?comp\|\(\(nsplugin\|apache_config\)_\(un\)\?install\)\|depmod\)\>'
	\ end='^%'me=e-1
	\ contains=specSpecialVariables,specVariables,@specCommands,specVariables,shDo,shFor,shCaseEsac,specNoNumberHilite,specCommandOpts,shComment,shIf,specSpecialChar,specMacroIdentifier,specSectionMacroArea,specSectionMacroBracketArea,shOperator,shQuote1,shQuote2,specSectionMacroBcondArea
" XXX don't forget to update specMacro when updating specScriptArea

" %% Changelog Section %%
syn region specChangelogArea matchgroup=specSection start='^%changelog' end='^%'me=e-1
	\ contains=specEmail,specURL,specWeekday,specMonth,specNumber,specComment,specLicense,specRevision,specLogMessage,specLogError

syn match specRevision contained "^Revision [.0-9]\+  [/0-9]\+ [:0-9]\+  [a-zA-Z0-9]\+$"
syn region specLogMessage contained start="^[- ] " end="$" contains=specLogError,specURL,specEmail
syn match specLogError contained "%%"

" ------------------------------------------------------------------------------
" here's the shell syntax for all the Script Sections


syn case match


" sh-like comment style, only valid in script part
syn match shComment contained '#.*$'

syn region shQuote1 contained matchgroup=shQuoteDelim start=+'+ skip=+\\'+ end=+'+ contains=specMacroIdentifier
syn region shQuote2 contained matchgroup=shQuoteDelim start=+"+ skip=+\\"+ end=+"+ contains=specVariables,specMacroIdentifier,specSectionMacroBcondArea

syn match shOperator contained '[><|!&;]\|[!=]='
syn region shDo transparent matchgroup=specBlock start="\<do\>" end="\<done\>" contains=ALLBUT,shFunction,shDoError,shCase,specPreAmble,@specListedFiles

syn region specIf  matchgroup=specBlock start="%ifosf\|%ifos\|%ifnos\|%ifarch\|%ifnarch\|ifdef\|ifndef\|%if\|%else"  end='%endif'  contains=ALLBUT, specIfError, shCase

syn region shIf transparent matchgroup=specBlock start="\<if\>" end="\<fi\>" contains=ALLBUT,shFunction,shIfError,shCase,@specListedFiles

syn region shFor  matchgroup=specBlock start="\<for\>" end="\<in\>" contains=ALLBUT,shFunction,shInError,shCase,@specListedFiles

syn region shCaseEsac transparent matchgroup=specBlock start="\<case\>" matchgroup=NONE end="\<in\>"me=s-1 contains=ALLBUT,shFunction,shCaseError,@specListedFiles nextgroup=shCaseEsac
syn region shCaseEsac matchgroup=specBlock start="\<in\>" end="\<esac\>" contains=ALLBUT,shFunction,shCaseError,@specListedFilesBin
syn region shCase matchgroup=specBlock contained start=")"  end=";;" contains=ALLBUT,shFunction,shCaseError,shCase,@specListedFiles

syn sync match shDoSync       grouphere  shDo       "\<do\>"
syn sync match shDoSync       groupthere shDo       "\<done\>"
syn sync match shIfSync       grouphere  shIf       "\<if\>"
syn sync match shIfSync       groupthere shIf       "\<fi\>"
syn sync match specIfSync     grouphere  specIf     "%ifarch\|%ifos\|%ifnos"
syn sync match specIfSync     groupthere specIf     "%endIf"
syn sync match shForSync      grouphere  shFor      "\<for\>"
syn sync match shForSync      groupthere shFor      "\<in\>"
syn sync match shCaseEsacSync grouphere  shCaseEsac "\<case\>"
syn sync match shCaseEsacSync groupthere shCaseEsac "\<esac\>"

" Define the default highlighting.
" For version 5.7 and earlier: only when not done already
" For version 5.8 and later: only when an item doesn't have highlighting yet
if version >= 508 || !exists("did_spec_syntax_inits")
  if version < 508
    let did_spec_syntax_inits = 1
    command -nargs=+ HiLink hi link <args>
  else
    command -nargs=+ HiLink hi def link <args>
  endif

  "main types color definitions
  HiLink specSection			Structure
  HiLink specSectionMacro		Macro
  HiLink specWWWlink			PreProc
  HiLink specOpts			Operator

  "yes, it's ugly, but white is sooo cool
  if &background == "dark"
    hi def specGlobalMacro		ctermfg=white
  else
    HiLink specGlobalMacro		Identifier
  endif

  "sh colors
  HiLink shComment			Comment
  HiLink shIf				Statement
  HiLink shOperator			Special
  HiLink shQuote1			String
  HiLink shQuote2			String
  HiLink shQuoteDelim			Statement

  " spec colors
  HiLink specBlock			Function
  HiLink specBcond			Function
  HiLink specColon			Special
  HiLink specCommand			Statement
  HiLink specCommandOpts		specOpts
  HiLink specCommandSpecial		Special
  HiLink specComment			Comment
  HiLink specConfigure			specCommand
  HiLink specDate			String
  HiLink specDescriptionOpts		specOpts
  HiLink specEmail			specWWWlink
  HiLink specError			Error
  HiLink specFilesDirective		specSectionMacro
  HiLink specFilesOpts			specOpts
  HiLink specLicense			String
  HiLink specMacroNameLocal		specGlobalMacro
  HiLink specMacroNameOther		specGlobalMacro
  HiLink specManpageFile		NONE
  HiLink specMonth			specDate
  HiLink specNoNumberHilite		NONE
  HiLink specNumber			Number
  HiLink specPackageOpts		specOpts
  HiLink specPercent			Special
  HiLink specSpecialChar		Special
  HiLink specSpecialVariables		specGlobalMacro
  HiLink specSpecialVariablesNames	specGlobalMacro
  HiLink specTarCommand			specCommand
  HiLink specMacro			Macro
  HiLink specURL			specWWWlink
  HiLink specURLMacro			specWWWlink
  HiLink specVariables			Identifier
  HiLink specWeekday			specDate
  HiLink specListedFilesBin		Statement
  HiLink specListedFilesDoc		Statement
  HiLink specListedFilesEtc		Statement
  HiLink specListedFilesLib		Statement
  HiLink specListedFilesPrefix		Statement
  HiLink specListedFilesShare		Statement

  HiLink specRevision			Number
  HiLink specLogMessage			Identifier
  HiLink specLogError			Error

  delcommand HiLink
endif

let b:current_syntax = "spec"

" vim: ts=8
