"""
Simple test of injecting time-varying current into a cell

Andrew Davison, UNIC, CNRS
May 2009

"""

import os.path
import matplotlib.pyplot as plt
from pyNN.utility import get_script_args, normalized_filename
from pyNN.recording import safe_makedirs

simulator_name = get_script_args(1)[0]
exec("from pyNN.%s import *" % simulator_name)

setup()

#cell = create(IF_curr_exp(v_thresh=-55.0, tau_refrac=5.0))
cell = Population(1, IF_curr_exp(v_thresh=-55.0, tau_refrac=5.0, i_offset=0.2))
print("cell is a {}".format(type(cell)))
#current_source = StepCurrentSource(times=[50.0, 110.0, 150.0, 210.0],
#                                   amplitudes=[0.4, 0.6, -0.2, 0.2])
#cell.inject(current_source)

filename = normalized_filename("Results", "FakeStepCurrentSource", "pkl", simulator_name)
safe_makedirs(os.path.dirname(filename))
#record('v', cell, filename, annotations={'script_name': __file__})
cell.record('v')

cell.i_offset = 0.2  # 0.0
run(50.0)
cell.i_offset = 0.4
run(60.0)
cell.i_offset = 0.6
run(40.0)
cell.i_offset = -0.2
run(60.0)
cell.i_offset = 0.2
run(40.0)

data = cell.get_data()
vm = data.segments[0].analogsignals[0]
plt.plot(vm.times, vm)
plt.xlabel("time (ms)")
plt.ylabel("v (mV)")
plt.title(__name__)
plt.savefig(filename.replace(".pkl", ".png"))

end()
