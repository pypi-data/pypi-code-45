"""
Define how to iterate over synthesis
"""

from pathlib import Path
import logging

from . import vivado_exp

class csv_handler:
    def __init__(self, filename):
        self.file = Path(filename).resolve()
        with self.file.open("w") as f:
            f.write("version, cycles, II, estimated_period, "
                    "real_period, Slices, LUT, FF, DSP, BRAM, SRL\n") 

    def handle(self, record):
        syn = record["syn"]
        impl = record["impl"]
        with self.file.open('a') as f:
            f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(
                syn['Vivado_HLS_Version'],
                syn['Pipeline_Depth'],
                syn['II'],
                syn['estimated_period'],
                impl['timing'],
                impl['Slices'],
                impl['LUT'],
                impl['FF'],
                impl['DSP'],
                impl['BRAM'],
                impl['SRL'])
            )

def minimize_latency(
        comp_path,
        comp_name,
        exp_prefix,
        clock_period,
        part,
        standard,
        includes,
        defines,
        handlers,
        keep_envs = False
    ):
    logger = logging.getLogger("vrs_log")
    handler = logging.FileHandler("{}.log".format(exp_prefix), "w")
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.info("{} : Trying to minimize latency for top level component {} " 
                "described in {}".format(exp_prefix, comp_name, comp_path))
    
    logger.info("Starting without latency constraint")
    ret = vivado_exp.experiment(comp_path, comp_name, exp_prefix+"_base",
                                clock_period, part, standard, includes,
                                defines, keep_envs)

    constraint = float(clock_period)

    for h in handlers:
        h.handle(ret)
    timing = float(ret['impl']['timing'])
    cycles = int(ret['syn']['Pipeline_Depth'])
    logger.info("Baseline result : {} cycles at a clock period of "
                "{}ns".format(cycles, timing))
    timings = {cycles : timing}
    up = cycles
    cur_best = cycles
    cur_best_timing = timing
    low = 1
    while up > low + 1:
        mid = low +  (up - low) // 2
        logger.info("Running the experiment with a pipeline depth constraint "
                    "of {}".format(mid))
        ret = vivado_exp.experiment(comp_path, comp_name,
                                    exp_prefix+"_{}".format(mid),
                                clock_period, part, standard, includes,
                                defines, keep_envs, mid)
        for h in handlers:
            h.handle(ret)
        timing = float(ret['impl']['timing'])
        cycles = int(ret['syn']['Pipeline_Depth'])
        timings[cycles] = timing
        logger.info("Result : {} cycles of {} ns".format(cycles, timing)) 
        if timing <= constraint:
            up = mid
            cur_best = cycles
            cur_best_timing = timing
        else:
            low = mid
        logger.info("New interval : [{},{}]".format(low, up))
    logger.removeHandler(handler)
    
    best = up if (low == 1 or timings[low] > constraint) else low
    best_timing = timing[best]

    return best, best_timing
