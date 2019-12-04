#-*- coding: utf-8 -*-
"""Setuplib subcommand 'ENUMERATE'.
Enumerate available commands based on 'pkt_resources'.
Supports parameters and filters.
"""
from __future__ import absolute_import
from __future__ import print_function

import sys
import os
import re
import traceback

import distutils.cmd

import pkg_resources

import yapydata.datatree.datatree as datatree
import setuplib

__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "239b0bf7-674a-4f53-a646-119f591af806"

__version__ = "01.01.005"

__product_family__ = "setuplib"
__product__ = "setuplib"
__product_component__ = "list_enty_points"


class SetuplibCommandsxError(setuplib.SetuplibError):
    """Error on setuplib calls.
    """
    pass


class SetupListEntryPointsX(distutils.cmd.Command):
    """List available entry points."""

    description = 'List available entry points.'
    user_options = [
        ('debug',                 'd',  "Raises degree of debug traces of current context. Supports repetition. "
                                        "Each raises the debug verbosity level of the context by one."),
        ('exit',                  'e',  "Exit after command 'setuplib' immediately, ignore following. "
                                        "Default := off."),
        ('filter=',               None, "Define a filter, for details refer to the manual. "
                                        "Default: ''"),
        ('format=',               'f',  "Define display format. "
                                        "See '--format=help. "
                                        "Default: 'name,module_name,dist.egg_info:::fname'"),
        ('group=',                'g',  "Set group for scan, '--group=none' scans all, "
                                        "'--group=console_scripts' displays all console scripts, "
                                        "etc. "
                                        "For current list: '--group=help', similar to '--list-groups'. "
                                        "See 'PyPA.io'."
                                        "Default: 'distutils.commands'"),
        ('ignore-missing',        'i',  "Ignore errors due to missing components, and continue. "
                                        " For example in case of missing an optional. "
                                        "Default: False. "),
        ('layout=',               None, "Define display layout. "
                                        "See '--format=help'. "
                                        "Default: table"),
        ('list-groups',           None, "Lists all scanned groups. "
                                        "Is shortcut for the '--format' option, "
                                        "refer to the manuals for additional details. "
                                        "Default: names only."
                                        ),
        ('long',                  'l',  "List long format, similar to shell command 'ls -l'. "
                                        "Default: off"),
        ('quiet',                 'q',  "Suppress display including warnings. Display error messages only."
                                        "Default: off"),
        ('search-path',           'P',  "Set the search path for requested resources. "
                                        "Default: 'sys.path'"),
        ('sort=',                 None, "Sort a specified field number. "
                                        "Default: 0"),
        ('verbose',               'v',  "Raises verbosity of current context. Supports repetition. "
                                        "Each raises the command verbosity level of the context by one. "
                                        "The value is defined by the global option defined in "
                                        "'Distribution'. "
                                        "Refer to the manuals for the special behaviour when used as "
                                        "either a global option(start 'verbose=1'), "
                                        "or as a command context option(start 'verbose=0'). "
                                        "Default:=1."),
    ]


    def initialize_options(self):
        """Define the API entrypoints and data of the command 'list'.
        
        REMARK: verbose and debug are encapsulated/hidden by distutils.

        """
        self.alias = None
        self.at_once = None
        self.debug = None
        self.exit = None
        self.filter = None
        self.format = None
        self.group = None
        self.ignore_missing = None
        self.layout = None
        self.long = None
        self.list_groups = None
        self.quiet = None
        self.search_path = None
        self.sort = None
        self.verbose = None

    def finalize_options(self):
        """Initializae the API of 'lis'. 
        """

        # quick-and-dirty hack to resolve the inconsistency of
        # global and local verbose values of distutils
        try:
            # The context option is actually not set by the framework,
            # instead the global option is reset and intialized to
            # the number of occurances and passes to the initialization
            # of the memeber 'self.verbose'.
            # Thus the poll fails, while the value is already set via the framework.
            # See code distutils.dist.Distribution.
            # Anyhow...keeping it as a reminder.
            _v_opts = self.distribution.get_option_dict('setuplib')['verbose'][1]
            if _v_opts:
                self.verbose += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            pass

        # global and local verbose values of distutils
        try:
            # See verbose for description of the global option quiet.
            # See code distutils.dist.Distribution.
            _q_opts = self.distribution.get_option_dict('setuplib')['quiet'][1]
            if _q_opts:
                self.quiet += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            if self.quiet == None:
                self.quiet = 0
            pass


        # debug
        if self.debug == None:
            self.debug = 0


        if self.ignore_missing == None:
            self.ignore_missing = False

        if self.exit == None:
            self.exit = False
            
        if self.long == None:
            self.long = 0

        if self.sort == None:
            self.sort = 0

        if self.list_groups != None:
            self.list_groups = True

        if self.group == None:
            # allow pre-selection of a set of groups, e.g. regular expression
            if not self.list_groups:
                self.group = 'distutils.commands'
        elif self.group.lower() == 'none':
            self.group = None


        if self.layout == None:
            self.layout = 'table'  # list, table, xml, json, yaml
        elif self.layout == 'help':
            print()
            print("Current layouts are: list, table")
            print("Soon available:      csv, ini, json, .properties, xml, yaml")
            print()
            sys.exit(0)

        if self.format == None:
            self.format = 'name,module_name,dist.egg_info:::fname'
        elif self.format.lower() == 'help':
            print("format := (list | table | csl | xml | json | yaml)")
            sys.exit(0)

        # set the internal format representation for the request - or default
        _format = []
        for _f in self.format.split(','):
            _fx = _f.split(':')
            if len(_fx) == 0:
                continue
            elif _fx[0] and len(_fx) == 1:
                _format.append([_fx[0], 0, 'auto', ''])
            elif len(_fx) < 5:
                _rec = [_fx[0], 0, 'auto', '',]

                if _fx[1]:
                    _rec[1] = int(_fx[1]) 

                if _fx[2]:
                    if _fx[2].lower() not in (
                            'cl', 'cr', 'clip', 'auto',
                        ):
                        raise SetuplibCommandsxError(
                                "parameter error:%s - %s - in: %s" %(
                                str(_fx[2]),
                                str(_f),
                                str(self.format),
                                )
                            )

                    _rec[2] = _fx[2].lower()

                if _fx[3]:
                    # optional special format, passed untouched
                    _rec[3] = _fx[3] 

                if _rec[1] or int(_rec[1]) == 0:
                    # force auto
                    _rec[2] = 'auto'
                
                _format.append(_rec)

            else:
                raise SetuplibCommandsxError(
                        "parameter error: %s - in: %s" %(
                        str(_f),
                        str(self.format),
                        )
                    )
        self.format = _format

        # for now reminder only
        if self.filter == None:
            self.filter = None

        #
        # assemble parameter for the external class
        #
        self.task = {
            "alias": self.alias,
            "debug": self.debug,
            "exit": self.exit,
            "format": self.format,
            "filter": self.filter,
            "group": self.group,
            "ignore_missing": self.ignore_missing,
            "layout": self.layout,
            "list_groups": self.list_groups,
            "long": self.long,
            "quiet": self.quiet,
            "search_path": self.search_path,
            "sort": self.sort,
            "verbose": self.verbose,
            }


        if self.at_once:
            _m = MyDistributionData(self.distribution, self.task)
            _m.enumerate(self.task)
            _m.print()
            sys.exit(0)

    def run(self):
        """Creates documents.
        Calls the defined and activated wrapper scripts.
        """
        _m = MyDistributionData(self.distribution, self.task)
        _m.enumerate(self.task)

        _m.print()
        
#         if self.task['list_groups']:
#             _m.print_groups()
#         
#         else:
#             _m.print()



class MyDistributionData(object):

    #: supported types of simple filter combination logic
    combinelogic = {
        'and': 0,   #: True if all match
        'or': 1,    #: True if any match
        'nand': 2,  #: True if not all matches
        'nor': 3,   #: True if none matches
        'xor': 4,   #: True if one only matches
    }

    def __init__(self, distribution, task):

        self.distribution = distribution 

        self.task = task
        
        #: simple flat cache of all extension points
        self.ep_cache = {}

        #: flat cache of all commands        
        self.cmd_ep = []

        #: flat cache of standard commands only - from setuptools(eventually distutils too)        
        self.cmd_std = []

        #: flat cache of local commands only - from setup()        
        self.cmd_local = []
        
        #: flat cache of extra - non-standard - commands from setuptools
        self.cmd_ext_setuptools = []

        #: flat cache of extra - non-standard - commands from distutils - eventually
        self.cmd_ext_distutils = []

        #: flat cache of extra - non-standard - commands from third-party        
        self.cmd_ext_misc = []

        #: flat cache of extra commands from setuplib        
        self.cmd_setuplib = []

    def enumerate(self, task):
        """Calls *pkg_resources* and caches the results.
        The cached data is queried later for details required
        by the extended list and display commands.
        
        The caching happens here only, which comprises the flat
        data cache of all entry points and the additional 
        categorized cache of selective sets for later selection
        filters.

        The centralized preparation of the data for later filtering
        eases the data handling significantly by moderate use of
        additional resources. 

        Args:
            self:
                The current instance of this class.

        Returns:
            Results in the member variable::

                self.ep_cache

            The content is a *dict* containing the iterated
            entry points with the *<ep>.name* as key.

        Raises:
            pass-through

        """
        _task = task
        if not _task:
            _task = self._task

        if (
                _task['group'] == None
                or _task['group'] in ('help',)
            ):
            self.ep_cache = list(pkg_resources.iter_entry_points(None))
            self.ep_cache = [list(x.values())[0] for x in self.ep_cache]

            #
            # the shortcut for help display only
            #
            if _task['group'] in ('help',):
                _groups = []
                for e in self.ep_cache:
                    _groups.extend(e.dist.get_entry_map().keys())
                
                print()
                print("Current groups:")
                print()
                for g in sorted(set(_groups)):
                    print("   " + str(g))
                print()

                sys.exit(0)

        else:
            self.ep_cache = list(pkg_resources.iter_entry_points(_task['group']))

        if _task['filter']:
            _filters = _task['filter'].split(';')
            _combine = 0

            _query_filters = []
            for _fx in _filters:
                if _fx.lower() in 'and':
                    _combine = 0
                    continue
                elif _fx.lower() == 'or':
                    _combine = 1
                    continue
                elif _fx.lower() == 'nand':
                    _combine = 2
                    continue
                elif _fx.lower() == 'nor':
                    _combine = 3
                    continue
                elif _fx.lower() == 'xor':
                    _combine = 4
                    continue
#                 elif _fx.lower() == 'not':
#                     _combine = 5
#                     continue

                _record_filter = _fx.split(":")
                if len(_record_filter) > 1:
                    # a filter requires fieldname and rule for the spanned column
                    _query_filters.append(
                        (_record_filter[0].split('.'), re.compile(_record_filter[1]))
                        )
                elif len(_record_filter) == 1:
                    # formal, even may not match at all...
                    _query_filters.append((_record_filter[0].split('.'), ''))

            if _task['debug'] > 0:
                print("DBG:input entry points:    " + str(len(self.ep_cache)))
            
            _all_filters = len(_query_filters)
            for epi in reversed(range(len(self.ep_cache))):
                _match_cnt = 0
                for _fpath,_fexpr in _query_filters:
            
                    try:
                        _v = datatree.DataTree(self.ep_cache[epi])(*_fpath, pysyn=True)
                        if not _fexpr:
                            _match_cnt += 1
                        elif _fexpr.search(str(_v)):
                            _match_cnt += 1

                    except datatree.YapyDataDataTreeOidError:
                        if _task['ignore_missing']:
                            break
                        else:
                            # fall through to filter logic
                            pass

                else:
                    if not (
                            (_combine == 0 and _match_cnt == _all_filters)    # and
                            or (_combine == 1 and _match_cnt > 0)             # or
                            or (_combine == 2 and _match_cnt < _all_filters)  # nand
                            or (_combine == 3 and _match_cnt == 0)            # nor
                            or (_combine == 4 and _match_cnt == 1)            # xor
                        ):
                        self.ep_cache.pop(epi)

        if _task['debug'] > 0:
            print("DBG:filtered entry points: " + str(len(self.ep_cache)))

        self.ep_index = {}
        idx = 0
        for e in self.ep_cache:
            self.ep_index[e.name] = idx
            idx += 1 

        return

    def print_groups(self, outlist, index, task):
        
        """Print '--list-groups' output based on pre-filtered data.
        Thus the complete set of filters processed in enumerate
        are applicable.
        """
        _t = self.task
        self.ep_cache = list(pkg_resources.iter_entry_points(self.task['group']))
        if self.task['group'] == None:
            self.ep_cache = [list(x.values())[0] for x in self.ep_cache]

        _groups = {}
        for e in self.ep_cache:
            _gmap = e.dist.get_entry_map()
            for k,v in _gmap.items():
                if not _groups.get(k):
                    _groups[k] = v
                else:
                    _groups[k].update(v)

            pass


        #
        # now print the list
        #
        
        if _t['layout'] == 'list':
            #self.print_list(_list, _index, _t)
            self.print_groups_list(_groups, index, self.task)
        elif _t['layout'] == 'xml':
            raise NotImplementedError("XML is not yet available")
        elif _t['layout'] == 'json':
            raise NotImplementedError("JSON is not yet available")
        elif _t['layout'] == 'yaml':
            raise NotImplementedError("yaml is not yet available")
        elif _t['layout'] == 'csv':
            raise NotImplementedError("csv is not yet available")
        elif _t['layout'] == 'table':
            self.print_groups_list(_groups, index, self.task)
            #self.print_table(_list, _index, _t)
        else:
            raise SetuplibCommandsxError(
                    "Unknown layout: " + str(_t['layout'])
                )
        
    
    def print_groups_list(self, outlist, index, task):
        """Print '--list-groups' output based on pre-filtered data.
        Thus the complete set of filters are applicable.
        """
        
        _adjust_level = self.task['long']
        

        print()
        print("Current groups:")
        print()
        _maxsize = 0
        
        if _adjust_level == 3:
            for k,v in sorted(outlist.items()):
                if self.task['long']:
                    for k1,v1 in sorted(v.items()):
                        if len(k1) > _maxsize:
                            _maxsize = len(k1)

        for k,v in sorted(outlist.items()):
            print("   " + str(k))
            if self.task['long']:
                if _adjust_level == 2:
                    _maxsize = 0
                    for k1,v1 in sorted(v.items()):
                        if len(k1) > _maxsize:
                            _maxsize = len(k1)

                for k1,v1 in sorted(v.items()):
                    # I do not want to estimate, whether the tuple v1.attr could contain more than 1...
                    # so simply trust the str(v1) here...
                    _v1 = re.sub(k1 + ' *= *', '', str(v1))
                    if _maxsize > 0:
                        _format = "      {0:"+ str(_maxsize) + "} = {1}"
                    else: 
                        _format = "      {0} = {1}"
                    print( _format.format(
                            str(k1),
                            str(_v1),
                        )
                    )
                print()

        print()
        sys.exit(0)
        
    def print(self):
        """Prints the requested data.

        The printout is again processed in two levels.
        - print:

            Prepares the record data for the appropriate format.

            Calls the inteface::

                self.print_<format>(outlist, index, task)
                
                outlist := The list of resulting keys within the *self.ep_cache*.
                
                index := The sprocessed/sorted list of *(<key>, #index)* mapping 
                         of utlist to *self.ep_cache*.
                
                task := The parameters of the current task.

            For example::

                self.print_table(outlist, index, task)

        - print_<format>:
            Prints out the records of the selcted output format.

        Uses object data from *self*.

        """

        _t = self.task
        
        print()
        if _t['group'] == None:
            print("entry points of resource group: None == all")
        else:
            print("entry points of resource group: " + str(_t['group']))
        
        if _t['filter']:
            print("applied filter:                 " + str(_t['filter']))

        print()
        
        if _t['sort'] == 0:
            _index = self.ep_index
            _list = sorted(_index)

        elif _t['sort'] == 1:
            _index = {}
            idx = 0
            _fname = {}
            for e in self.ep_cache:
                _fname[e.module_name] = (e.name, idx,)
                idx += 1 
            for x in sorted(_fname.keys()):
                _index[_fname[x][0]] = _fname[x][1] 
            _list = _index

        elif _t['sort'] != 0:
            # fieldnames
            _n = _t['sort']
            _nx = _n.split('.')
            
            _index = {}
            idx = 0
            _fname = {}
            _grp = _t['group'] == None
            
            for _e in self.ep_cache:
                _val = datatree.DataTree(_e)(*_nx, pysyn=True)
                try:
                    _item = _fname[_val]
                    _item.append((_e.name, idx,))
                except KeyError:
                    _fname[_val] = [(_e.name, idx,),]
                    
                idx += 1 
            
            for x in sorted(_fname.keys()):
                for xi in _fname[x]:
                    _index[xi[0]] = xi[1]
            _list = _index


        #
        # now print the list
        #

        if self.task['list_groups']:
            self.print_groups(_list, _index, _t)
        
        else:
            if _t['layout'] == 'list':
                self.print_list(_list, _index, _t)
            elif _t['layout'] == 'xml':
                raise NotImplementedError("XML is not yet available")
            elif _t['layout'] == 'json':
                raise NotImplementedError("JSON is not yet available")
            elif _t['layout'] == 'yaml':
                raise NotImplementedError("yaml is not yet available")
            elif _t['layout'] == 'csv':
                raise NotImplementedError("csv is not yet available")
            elif _t['layout'] == 'table':
                self.print_table(_list, _index, _t)
            else:
                raise SetuplibCommandsxError(
                        "Unknown layout: " + str(_t['layout'])
                    )

    def print_table(self, outlist, index, task):
        """Print table.
        """
        # REMINDER:for tests:_header = [['name', 0, 'keep'], ['module_name', 0, 'keep'], ['dist.key', 0, 'keep']]

        # import prepared format string
        _header = task['format']
        _layout = task['layout']

        # determine maximum column widths for each field
        for _e in self.ep_cache:
            for i in range(len(_header)):
                if _header[i][2] not in ('auto', ):
                    continue

                _nx = _header[i][0].split('.')
                
                try:
                    _val = datatree.DataTree(_e)(*_nx, pysyn=True)
                except datatree.YapyDataDataTreeOidError:
                    _val = ''

                if (
                        _header[i][3] and _header[i][3] == 'fname'
                        and not task['long']
                    ):
                    _val = os.path.basename(_val)
                elif (
                        _header[i][3] and _header[i][3] == 'abs'
                    ):
                    _val = os.path.abspath(_val)
                
                if len(str(_val)) >= _header[i][1]:  # in case of equal add the space
                    _header[i][1] = len(str(_val)) + 1
                elif len(_header[i][0]) >= _header[i][1]:  # in case of equal add the space
                    _header[i][1] = len(_header[i][0]) + 1

        _head = [x[0] for x in _header]
        _format = ''
        _tabsep = ''
        _l = len(_header)
        for i in range(_l):
            if _header[i][1] == 0 or i == _l - 1:
                _format +=  "{%d}"%(i)
            else:
                _format +=  "{%d:%d}"%(i, _header[i][1])
        
            _tabsep += '-' * _header[i][1]

        print(_format.format(*_head))
        print(_tabsep)
        
        _ign = task['ignore_missing']
        for x in outlist:
            try:
                _e = self.ep_cache[index[x]]
                _values = []
                for _f in range(len(_head)): 
                    _nx = _head[_f].split('.')
                    _len = _header[_f][1] - 1
                    _lx = _header[_f][2]
                    try:
                        _v = datatree.DataTree(_e)(*_nx, pysyn=True)
                        _lv = len(str(_v))

                        if (
                                _header[_f][3] and _header[_f][3] == 'fname'
                                and not task['long']
                            ):
                            _v = os.path.basename(_v)
                        elif (
                                _header[_f][3] and _header[_f][3] == 'abs'
                            ):
                            _v = os.path.abspath(_v)

                        
                        if _lv > _len:
                            if _lx == 'cl':
                                _v = str(_v)[-_len:]
                            elif _lx == 'cr':
                                _v = str(_v)[:_len]
                            elif _lx == 'clip':
                                #TODO:
                                pass
                            elif _lx == 'auto':
                                pass

                        _values.append(_v)
                        
                    except datatree.YapyDataDataTreeOidError as e:
                        if _ign:
                            # the assumingly most generic type
                            _values.append('')
                        else:
                            # einfo = sys.exc_info()
                            # traceback.print_tb(einfo[2])
                            traceback.print_exc()
                            print("\n\nHINT: You have selected a non-present path, use:\n"
                                  "\n      '--ignore-missing' / '-i'  to continue"
                                  "\n      '--filter'                 for the pre-selection of a valid set\n"
                                  )
                            sys.exit(1)

                            # for now it's enough
                            # Python2 
                            # raise(datatree.YapyDataDataTreeOidError, datatree.YapyDataDataTreeOidError(e), sys.exc_info()[2])
                            # Python3 
                            # raise datatree.YapyDataDataTreeOidError from e

                
                if _ign:
                    if ( _values and len(_values) > 1 ) or ''.join([str(x) for x in _values]):
                        print(_format.format(*[str(v) for v in _values]))
                    else:
                        continue
                else:
                    print(_format.format(*[str(v) for v in _values]))

            except AttributeError:  # as e:
                raise
            except KeyError:  # as e:
                raise

        print()
        
    def print_list(self, outlist, index, task):
        """Print list.
        """
        # import prepared format string
        _header = task['format']
        _layout = task['layout']

        _head = [x[0] for x in _header]
        _format = ''
        _commonprefix = 0
        for i in range(len(_header)):
            if _commonprefix < len(str(_header[i][0])):
                _commonprefix = len(str(_header[i][0])) + 1

        prewidth = 5
        
        _format =  "{0} {1:%d}: {2}"%(_commonprefix)
        _idxstr = ' ' * prewidth
        _prestr = "\n{0:%d}" % (prewidth)
        _idx = 0

        for x in outlist:
            try:
                for _f in range(len(_head)): 
                    if _f:
                        _pre =  _idxstr
                    else:
                        _pre = _prestr.format(_idx)
                        _idx += 1
                        
                    try:
                        _v = datatree.DataTree(self.ep_cache[index[x]])(
                                *_head[_f].split('.'), pysyn=True
                            )

                        if (
                                _header[_f][3] and _header[_f][3] == 'fname'
                                and not task['long']
                            ):
                            _v = os.path.basename(_v)
                        elif (
                                _header[_f][3] and _header[_f][3] == 'abs'
                            ):
                            _v = os.path.abspath(_v)

                        _x = _format.format(
                                    _pre,
                                    _head[_f],
                                    _v, 
                                ) 
                    except datatree.YapyDataDataTreeOidError:
                        if task['ignore_missing']:
                            _x = _format.format(
                                        _pre,
                                        _head[_f],
                                        '' 
                                    ) 
                        else:
                            raise

                    print(_x)

            except AttributeError:  # as e:
                raise
            except KeyError:  # as e:
                raise

        print()

            