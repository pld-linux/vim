" Vim syntax file
" Filename:	nagios.vim
" Language:     Nagios template object configuration file
" Maintainer:	Lance Albertson <ramereth@gentoo.org>
" Orginal Author: Ava Arachne Jarvis <ajar@katanalynx.dyndns.org>
" URL:          http://dev.gentoo.org/~ramereth/vim/syntax/nagios.vim
"  * previous URL appears to be dead
" Version:	0.1
" Last Change:  2005 Jan 4


if !exists("main_syntax")
  if version < 600
    syntax clear
  elseif exists("b:current_syntax")
    finish
  endif

  let main_syntax = 'nagios'
endif

if version >= 600
  setlocal iskeyword=_,-,A-Z,a-z,48-57
else
endif

syn match nagiosComment '#.*'

syn match nagiosConstant '\<[0-9]\+%\?\>'
syn match nagiosConstant '\<[a-z]\>'

syn region nagiosString  start=+"+ end=+"+ contains=nagiosMacro
syn region nagiosString  start=+'+ end=+'+ contains=nagiosMacro

syn keyword nagiosSpecial  name register use

syn match nagiosDef 'define[ \t]\+\(\(host\|service\)extinfo\|host\|service\|timeperiod\|contact\|command\)'
syn match nagiosDef 'define[ \t]\+\(host\|contact\|service\)group'
syn match nagiosDef 'define[ \t]\+\(service\|host\)dependency'
syn match nagiosDef 'define[ \t]\+\(service\|host\|hostgroup\)escalation'

syn match nagiosMacro  '\$CONTACT\(NAME\|ALIAS\|EMAIL\|PAGER\)\$'
syn match nagiosMacro  '\$HOST\(NAME\|ALIAS\|ADDRESS\|STATE\|OUTPUT\|PERFDATA\|STATETYPE\|EXECUTIONTIME\)\$'
syn match nagiosMacro  '\$\(ARG\|USER\)\([1-9]\|[1-2][0-9]\|3[0-2]\)\$'
syn match nagiosMacro  '\$SERVICE\(DESC\|STATE\|OUTPUT\|PERFDATA\|LATENCY\|EXECUTIONTIME\|STATETYPE\)\$'
syn match nagiosMacro  '\$\(OUTPUT\|PERFDATA\|EXECUTIONTIME\|LATENCY\)\$'
syn match nagiosMacro  '\$NOTIFICATION\(TYPE\|NUMBER\)\$'
syn match nagiosMacro  '\$\(\(SHORT\|LONG\)\?DATETIME\|DATE\|TIME\|TIMET\)\$'
syn match nagiosMacro  '\$LASTSTATECHANGE\$'
syn match nagiosMacro  '\$ADMIN\(EMAIL\|PAGER\)\$'
syn match nagiosMacro  '\$\(SERVICE\|HOST\)ATTEMPT\$'
syn match nagiosMacro  '\$LAST\(HOST\|SERVICE\)CHECK\$'

syn region nagiosDefBody start='{' end='}' contains=nagiosDirective,nagiosMacro,nagiosConstant,nagiosString,nagiosSpecial transparent

syn keyword nagiosDirective  active_checks_enabled address alias check_command
syn keyword nagiosDirective  check_freshness check_period checks_enabled check_interval
syn keyword nagiosDirective  command_line command_name
syn keyword nagiosDirective  contact_groups contact_name contactgroup_name
syn keyword nagiosDirective  dependent_host_name dependent_service_description
syn keyword nagiosDirective  email event_handler event_handler_enabled
syn keyword nagiosDirective  execution_failure_criteria first_notification execution_failure_options
syn keyword nagiosDirective  flap_detection_enabled freshness_threshold failure_prediction_enabled
syn keyword nagiosDirective  friday high_flap_threshold host_name
syn keyword nagiosDirective  host_notification_commands
syn keyword nagiosDirective  host_notification_options
syn keyword nagiosDirective  host_notification_period hostgroup_name servicegroup_name hostgroups servicegroups
syn keyword nagiosDirective  is_volatile last_notification
syn keyword nagiosDirective  low_flap_threshold max_check_attempts
syn keyword nagiosDirective  members monday normal_check_interval
syn keyword nagiosDirective  notification_failure_criteria notification_failure_options
syn keyword nagiosDirective  notification_interval notification_options
syn keyword nagiosDirective  notification_period notifications_enabled
syn keyword nagiosDirective  obsess_over_service pager parallelize_check
syn keyword nagiosDirective  parents passive_checks_enabled
syn keyword nagiosDirective  process_perf_data retain_nonstatus_information
syn keyword nagiosDirective  retain_status_information retry_check_interval
syn keyword nagiosDirective  saturday service_description
syn keyword nagiosDirective  service_notification_commands
syn keyword nagiosDirective  service_notification_options
syn keyword nagiosDirective  service_notification_period stalking_options
syn keyword nagiosDirective  sunday thursday timeperiod_name tuesday wednesday
syn keyword nagiosDirective  icon_image icon_image_alt vrml_image statusmap_image
syn keyword nagiosDirective  notes notes_url 2d_coords 3d_coords obsess_over_host inherits_parent

hi link nagiosComment Comment
hi link nagiosConstant Number
hi link nagiosDef Statement
hi link nagiosDirective Define
hi link nagiosMacro Macro
hi link nagiosString String
hi link nagiosSpecial Special
