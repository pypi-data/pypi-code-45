"""
Create experimental environment for vivado HLS 
"""

import logging
from os import chdir
from pathlib import Path
import shutil
import tempfile

from plumbum import local

from . import compedit
from . import vivado_report as vrpt

class TmpDirManager:
    def __init__(self, destruct=True):
        logger = logging.getLogger("vrs_log")
        self.destruct = destruct
        self.work_dir = Path.cwd()
        self.path = Path(tempfile.mkdtemp())
        logger.info("Creating temporary directory in {}".format(self.path))
        logger.debug("work_dir : {}".format(self.work_dir))
        logger.debug("self_destruct : {}".format(self.destruct))

    def __enter__(self):
        logging.getLogger("vrs_log").debug("Changing current dir to {}".format(self.path)) 
        chdir(self.path)

    def __exit__(self, _, __, ___):
        logger = logging.getLogger("vrs_log")
        logger.debug("leaving temporary dir and switching to {}".format(self.work_dir))
        chdir(self.work_dir)
        if self.destruct:
            logger.debug("Removing temporary directory")
            shutil.rmtree(self.path)
        pass

def generate_script(vivado_script, clock_period, standard, comp_name, defines, includes, part):
    with vivado_script.open("w") as o:
        logger = logging.getLogger("vrs_log")
        logger.debug("Starting generation of tcl script")
        o.write("open_project vivado_hls_synthesis\n")
        o.write("set_top {}\n".format(comp_name))
        includes_str = "" if includes is None else " ".join(
            ["-I{}".format(s) for s in includes]
        )
        if defines is None:
            def_str = ""
        else:
            def_str = " ".join(["-D{}={}".format(k, v) for k,v in defines.items()])
        o.write('add_files comp.cpp -cflags "-std={} {} {}"\n'.format(
                standard, 
                includes_str, 
                def_str
            )
        )
        o.write('open_solution "solution"\n')
        o.write('set_part {{{}}} -tool vivado\n'.format(part)) 
        o.write('create_clock -period {} -name default\n'.format(
                clock_period
        ))
        o.write('csynth_design\n')
        o.write('export_design -flow impl -rtl vhdl -format ip_catalog\n')

def run_script(vivado_script):
    vivado_hls = local["vivado_hls"]
    vivado_hls(str(vivado_script))


def experiment(comp_path, 
               comp_name, 
               exp_name, 
               clock_period,
               part,
               standard,
               includes = None, 
               defines = None, 
               keep_env = False,
               depth_constraint = None
            ):
    logger = logging.getLogger("vrs_log")
    logger.info("Experiment: {}".format(exp_name))
    comp = Path(comp_path).resolve()
    if not comp.exists():
        raise FileNotFounError("Error when starting experiment: component file"
                               "{} does not exist".format(comp))
    logger.info("Found component file {}".format(comp))
    with TmpDirManager(not keep_env):
        comp_copy = Path("comp.cpp")
        compedit.decorate_comp(comp, comp_copy, depth_constraint)
        logger.debug("Adding pragma decoration")

        vivado_script = Path("vivado_script.tcl")
        generate_script(vivado_script, 
                        clock_period, 
                        standard,
                        comp_name, 
                        defines,
                        includes, 
                        part
                       )
        run_script(vivado_script)
        vivado_hls_rpt = Path(
                "./vivado_hls_synthesis/solution/syn/report/{}_csynth.xml".format(comp_name)
            ).resolve()
        syn_res = vrpt.parse_syn_report(vivado_hls_rpt)
        vivado_report = Path(
                "./vivado_hls_synthesis/solution/impl/report/vhdl/{}_export.xml".format(comp_name)
            ).resolve()
        impl_res = vrpt.parse_impl_report(vivado_report)
    return {"syn" : syn_res, "impl" : impl_res}


