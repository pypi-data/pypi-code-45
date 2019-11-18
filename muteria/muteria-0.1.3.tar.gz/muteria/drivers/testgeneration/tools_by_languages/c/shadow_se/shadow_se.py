
from __future__ import print_function
import os
import sys
import glob
import shutil
import logging
import re

import muteria.common.fs as common_fs
import muteria.common.mix as common_mix
import muteria.common.matrices as common_matrices

import muteria.controller.explorer as fd_structure
import muteria.drivers.criteria as criteria

from muteria.repositoryandcode.codes_convert_support import CodeFormats
from muteria.drivers.testgeneration.base_testcasetool import BaseTestcaseTool
from muteria.drivers.testgeneration.testcases_info import TestcasesInfoObject
from muteria.drivers import DriversUtils

from muteria.repositoryandcode.callback_object import DefaultCallbackObject

from muteria.drivers.testgeneration.tools_by_languages.c.klee.klee \
                                                    import TestcasesToolKlee

ERROR_HANDLER = common_mix.ErrorHandler

class TestcasesToolShadowSE(TestcasesToolKlee):
    """ Make sure to set the path to binarydir in user customs to use this
        The path to binary should be set to the path to the shadow 
        directory. in Shadow VM, it should be '/home/shadowvm/shadow'
    """
    def __init__(self, *args, **kwargs):
        TestcasesToolKlee.__init__(self, *args, **kwargs)
        ERROR_HANDLER.assert_true(self.custom_binary_dir is not None, \
                        "Custom binary dir must be set for shadow", __file__)
        self.shadow_folder_path = os.sep.join(\
                                    os.path.abspath(self.custom_binary_dir)\
                                    .split(os.sep)[:-3])
        self.llvm_29_compiler_path = os.path.join(self.shadow_folder_path, \
                                    "kleeDeploy/llvm-2.9/Release+Asserts/bin")
        self.llvm_gcc_path = os.path.join(self.shadow_folder_path, \
                                'kleeDeploy/llvm-gcc4.2-2.9-x86_64-linux/bin')
        self.wllvm_path = os.path.join(self.shadow_folder_path, \
                                            'kleeDeploy/whole-program-llvm')
        self.klee_change_locs_list_file = os.path.join(self.tests_working_dir,\
                                                    "klee_change_locs.json")
    #~ def __init__()

    # SHADOW override
    def _get_default_params(self):
        bool_params = {
            '-ignore-solver-failures': None,
            '-allow-external-sym-calls': True, #None,
            '-posix-runtime': True, #None,
            '-dump-states-on-halt': True, #None,
            #'-only-output-states-covering-new': True 
            '--zest': True,
            '--shadow': True,
            '-emit-all-errors': True,
            '-no-std-out': True,
            '-shadow-allow-allocs': True,
            '-watchdog': True,
            '-shadow-replay-standalone': False,
        }
        key_val_params = {
            #'-output-dir': self.tests_storage_dir,
            #'-solver-backend': None,
            '-search': None,
            '-max-memory': None,
            '-max-time': self.config.TEST_GENERATION_MAXTIME,
            '-libc': 'uclibc',
            '-use-shadow-version': 'product',
            '-program-name': None, #TODO: CHeck importance
        }
        return bool_params, key_val_params
    #~ def _get_default_params()
    
    # SHADOW override
    def _get_sym_args(self):
        # sym args
        default_sym_args = [] #['-sym-arg', '5']
        klee_sym_args = default_sym_args

        #klee_sym_args = default_sym_args
        #uc = self.config.get_tool_user_custom()
        #if uc is not None:
        #    post_bc_cmd = uc.POST_TARGET_CMD_ORDERED_FLAGS_LIST
        #    if post_bc_cmd is not None:
        #        klee_sym_args = []
        #        for tup in post_bc_cmd:
        #            klee_sym_args += list(tup)
        return klee_sym_args
    #~ def _get_sym_args()

    # SHADOW should override
    def _get_back_llvm_compiler(self):
        return "llvm-gcc" #'clang'
    #~ def _get_back_llvm_compiler()

    # SHADOW should override
    def _get_back_llvm_compiler_path(self):
        return self.llvm_29_compiler_path 
    #~ def _get_back_llvm_compiler_path()

    # SHADOW should override
    def _call_generation_run(self, runtool, args):
        # Delete any klee-out-*
        for d in os.listdir(self.tests_working_dir):
            if d.startswith('klee-out-'):
                shutil.rmtree(os.path.join(self.tests_working_dir, d))

        call_shadow_wrapper_file = os.path.join(self.tests_working_dir, \
                                                                "shadow_wrap")
        
        test_list = list(self.code_builds_factory.repository_manager\
                                                        .get_dev_tests_list())
        devtest_toolalias = self.parent_meta_tool.get_devtest_toolalias()

        # Get list of klee_change, klee_get_true/false locations.
        klee_change_stmts = []
        
        get_lines_callback_obj = self.GetLinesCallbackObject()
        get_lines_callback_obj.set_pre_callback_args(self.code_builds_factory\
                                    .repository_manager.revert_src_list_files)
        get_lines_callback_obj.set_post_callback_args(klee_change_stmts)

        pre_ret, post_ret = self.code_builds_factory.repository_manager\
                                    .custom_read_access(get_lines_callback_obj)
        ERROR_HANDLER.assert_true(pre_ret == \
                                common_mix.GlobalConstants.COMMAND_SUCCESS,\
                                                    "pre failed", __file__)
        ERROR_HANDLER.assert_true(post_ret == \
                                common_mix.GlobalConstants.COMMAND_SUCCESS,\
                                                    "post failed", __file__)

        ERROR_HANDLER.assert_true(len(klee_change_stmts) > 0, \
                        "No klee_change statement in the sources", __file__)

        # Filter only tests that cover those locations, 
        # if there is stmt coverage matrix 
        stmt_cov_mat_file = self.head_explorer.get_file_pathname(\
                            fd_structure.CRITERIA_MATRIX[criteria.TestCriteria\
                                                        .STATEMENT_COVERAGE])
        cov_tests = None
        if os.path.isfile(stmt_cov_mat_file):
            stmt_cov_mat = common_matrices.ExecutionMatrix(\
                                                    filename=stmt_cov_mat_file)
            meta_stmts = list(stmt_cov_mat.get_keys())
            tool_aliases = set()
            for meta_stmt in meta_stmts:
                alias, stmt = DriversUtils.reverse_meta_element(meta_stmt)
                tool_aliases.add(alias)
            klee_change_meta_stmts = []
            for alias in tool_aliases:
                klee_change_meta_stmts += [\
                                    DriversUtils.make_meta_element(e, alias) \
                                                    for e in klee_change_stmts]
            klee_change_meta_stmts = list(set(meta_stmts) & \
                                                set(klee_change_meta_stmts))

            cov_tests = set()
            if len(klee_change_meta_stmts) > 0:
                for _, t in stmt_cov_mat.query_active_columns_of_rows(\
                                row_key_list=klee_change_meta_stmts).items():
                    cov_tests |= set(t)
            #else:
            #    ERROR_HANDLER.assert_true(len(klee_change_meta_stmts) > 0, \
            #                            "No test covers the patch", __file__)

        # tests will be generated in the same dir that has the input .bc file
        os.mkdir(self.tests_storage_dir)

        # obtain candidate tests
        cand_testpair_list = []
        for test in test_list:
            meta_test = DriversUtils.make_meta_element(test, devtest_toolalias)
            if cov_tests is not None and meta_test not in cov_tests:
                continue 
            cand_testpair_list.append((test, meta_test))

        # Adjust the max-time in args
        ## locate max-time
        if len(cand_testpair_list) > 0:
            for i, v in enumerate(args):
                if v in ('-max-time', '--max-time'):
                    args[i+1] = \
                        str(max(1, float(args[i+1]) / len(cand_testpair_list)))
                    break
                elif v.startswith('-max-time=') or v.startswith('--max-time='):
                    pre, tmp = v.split('=')
                    tmp = str(max(1, float(tmp) / len(cand_testpair_list)))
                    args[i] = pre + '=' + str(tmp)

        # Set the wrapper
        with open(call_shadow_wrapper_file, 'w') as wf:
            wf.write('#! /bin/bash\n\n')
            wf.write('ulimit -s unlimited\n')
            wf.write(' '.join(['exec', runtool] + args + ['"${@:1}"']) + '\n')
        os.chmod(call_shadow_wrapper_file, 0o775)

        # run test
        exes, _ = self.code_builds_factory.repository_manager\
                                                .get_relative_exe_path_map()
        ERROR_HANDLER.assert_true(len(exes) == 1, \
                                            "Must have a single exe", __file__)
        exe_path_map = {e: call_shadow_wrapper_file for e in exes}
        env_vars = {}
        for test, meta_test in cand_testpair_list:
            self.parent_meta_tool.execute_testcase(meta_test, exe_path_map, \
                                        env_vars, with_output_summary=False)

            # copy the klee out
            test_out = os.path.join(self.tests_storage_dir, \
                                                    test.replace(os.sep, '_'))
            os.mkdir(test_out)
            for d in glob.glob(self.tests_working_dir+"/klee-out-*"):
                # make sure we can do anything with it
                self._dir_chmod777(d)
                shutil.move(d, test_out)
            ERROR_HANDLER.assert_true(len(list(os.listdir(test_out))) > 0, \
                                "Shadow generated no test for tescase: "+test,\
                                                                    __file__)
            if os.path.islink(os.path.join(self.tests_working_dir, \
                                                                'klee-last')):
                os.unlink(os.path.join(self.tests_working_dir, 'klee-last'))

        # store klee_change locs
        common_fs.dumpJSON(klee_change_stmts, self.klee_change_locs_list_file)
    #~ def _call_generation_run()

    class GetLinesCallbackObject(DefaultCallbackObject):
        def before_command(self):
            revert_src_func = self.pre_callback_args
            revert_src_func()
            return common_mix.GlobalConstants.COMMAND_SUCCESS
        #~ def before_command()

        def after_command(self):
            if self.op_retval == common_mix.GlobalConstants.COMMAND_FAILURE:
                return common_mix.GlobalConstants.COMMAND_FAILURE
            m_regex = re.compile('({}|{}|{})'.format('klee_change', \
                                            'klee_get_true', 'klee_get_false'))
            matched_lines = set()
            for src in self.source_files_to_objects:
                with open(os.path.join(self.repository_rootdir, src)) as f:
                    for lnum, line in enumerate(f):
                        if m_regex.search(line) is not None:
                            matched_lines.add(DriversUtils.make_meta_element(\
                                                            str(lnum+1), src))
            ret_lines = self.post_callback_args
            ret_lines.extend(matched_lines)
            return common_mix.GlobalConstants.COMMAND_SUCCESS
        #~ def after_command()
    #~ class CopyCallbackObject

    # SHADOW should override
    def _get_testexec_extra_env_vars(self, testcase):
        return None # TODO: get test env and return
    #~ def _get_testexec_extra_env_vars()

    def _do_generate_tests (self, exe_path_map, \
                                        code_builds_factory, max_time=None):
        env_path_bak = os.environ['PATH']
        os.environ['PATH'] = os.pathsep.join([self.llvm_gcc_path, \
                                         self.wllvm_path, os.environ['PATH']])

        super(TestcasesToolShadowSE, self)._do_generate_tests(\
                                        exe_path_map, \
                                        code_builds_factory, max_time=max_time)

        os.environ['PATH'] = env_path_bak
    #~ def _do_generate_tests ()
#~ class TestcasesToolShadowSE
