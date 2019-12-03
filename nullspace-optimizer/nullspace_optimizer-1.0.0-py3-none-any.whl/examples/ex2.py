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
try:
    import matplotlib.pyplot as plt
    from nullspace_optimizer.examples.draw import drawProblem, drawData
    with_plot = True
except Exception:
    with_plot = False


class problemeSimple2(EuclideanOptimizable):
    def __init__(self, xinit):
        super().__init__(n=2)
        self.xinit = xinit

        self.nconstraints = 0
        self.nineqconstraints = 2

    def x0(self):
        return self.xinit

    def J(self, x):
        return x[0]

    def G(self, x):
        return []

    def H(self, x):
        return [0.5**2-x[0]**2-x[1]**2,
                -x[0]-1]

    def dJ(self, x):
        return [1, 0]

    def dG(self, x):
        return []

    def dH(self, x):
        return [[-2*x[0], -2*x[1]],
                [-1, 0]]


problem1 = problemeSimple2(xinit=[1.25, 0])
problem2 = problemeSimple2(xinit=[0, -1.2])
problem3 = problemeSimple2(xinit=[1, 0.3])
problem4 = problemeSimple2(xinit=[0.7, -0.2])
problem5 = problemeSimple2(xinit=[-1.3, 1])

optParams = {'dt': 0.01, 'alphaC': 1, 'alphaJ': 1, 'maxtrials': 1, 'debug': -1}
results1 = nlspace_solve(problem1, optParams)
results2 = nlspace_solve(problem2, optParams)
results3 = nlspace_solve(problem3, optParams)
results4 = nlspace_solve(problem4, optParams)
results5 = nlspace_solve(problem5, optParams)

if with_plot:
    plt.ion()
    drawProblem(problemeSimple2([0, 0]), [-1.5, 1.5], [-1.5, 1.5])
    drawData(results1, None, 'C0', x0=True, xfinal=True)
    drawData(results2, None, 'C1', x0=True, xfinal=True)
    drawData(results3, None, 'C2', x0=True, xfinal=True)
    drawData(results4, None, 'C3', x0=True, xfinal=True)
    drawData(results5, None, 'C4', x0=True, xfinal=True)
    plt.gca().get_legend().remove()
    plt.show()
input("Press any key")
