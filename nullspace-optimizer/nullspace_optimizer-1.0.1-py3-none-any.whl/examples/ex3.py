# Copyright 2018-2019 CNRS, Ecole Polytechnique and Safran.
#
# This file is part of nullspace_optimizer.
#
# nullspace_optimizer is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# nullspace_optimizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# A copy of the GNU General Public License is included below.
# For further information, see <http://www.gnu.org/licenses/>.

from nullspace_optimizer import *
import numpy as np
try:
    import matplotlib.cm as cm
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt
    from nullspace_optimizer.examples.draw import *
    with_plot = True
    plt.ion()
except Exception:
    with_plot = False


class unconstrainedProblem(EuclideanOptimizable):
    def __init__(self):
        super().__init__(2)
        self.nconstraints = 0
        self.nineqconstraints = 0

    def x0(self):
        return [1.5, 2.25]

    def J(self, x):
        return x[1]**2+0.1*x[0]**2

    def dJ(self, x):
        return [0.2*x[0], 2*x[1]]


params = {'alphaC': 1, 'debug': 0,
          'alphaJ': 1, 'dt': 1, 'maxtrials': 1}

results = nlspace_solve(unconstrainedProblem(), params)
print(f"Nullspace method ended in {len(results['J'])} iterations.")

print("")
print("Optimum :")
print(results['x'][-1])
if with_plot:
    drawProblem(unconstrainedProblem(), XLIM=[-3, 3], YLIM=[-3, 3],
                resolution=200)
    drawData(results, 'NLSPACE', 'blue')

    plt.figure()
    drawJ(results)
    plt.legend()

    plt.show()

input("\nPress any key")
if with_plot:
    plt.close('all')
