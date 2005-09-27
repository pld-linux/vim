" Vim filetype plugin file
" Language: RPM spec file
" Author:   Elan Ruusamäe <glen@pld-linux.org>
" Copyright:    Copyright (c) 2005 PLD Linux
" Licence:  GPL
"
" This sets up filetype specific options for RPM spec files.

setlocal tw=70

map <F8> :!rpmbuild -bb %<CR>
