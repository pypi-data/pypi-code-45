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
    from nullspace_optimizer.examples.draw import *
    with_plot = True
except Exception:
    with_plot = False


class problemeSimple(EuclideanOptimizable):
    def __init__(self, xinit):
        super().__init__(n=2)
        self.xinit = xinit

        self.nconstraints = 0
        self.nineqconstraints = 3

    def x0(self):
        return self.xinit

    def J(self, x):
        return (x[0]+1)**2+(x[1]+1)**2

    def G(self, x):
        return []

    def H(self, x):
        return [x[0]**2+x[1]**2-1**2,
                x[0]+x[1]-1,
                -x[1]-0.7]

    def dJ(self, x):
        return [2*(x[0]+1), 2*(x[1]+1)]

    def dG(self, x):
        return []

    def dH(self, x):
        return [[2*x[0], 2*x[1]],
                [1, 1],
                [0, -1]]


problem1 = problemeSimple(xinit=[1.25, 0])
problem2 = problemeSimple(xinit=[0, -1.2])
problem3 = problemeSimple(xinit=[1, -1])
problem4 = problemeSimple(xinit=[0.7, 1.2])
problem5 = problemeSimple(xinit=[-1, 1])

optParams = {'dt': 0.01, 'alphaC': 0.2,
             'alphaJ': 1, 'maxtrials': 1, 'debug': -1}
results1 = nlspace_solve(problem1, optParams)
results2 = nlspace_solve(problem2, optParams)
results3 = nlspace_solve(problem3, optParams)
results4 = nlspace_solve(problem4, optParams)
results5 = nlspace_solve(problem5, optParams)

if with_plot:
    plt.ion()
    drawProblem(problemeSimple([0, 0]), [-1.5, 1.5], [-1.5, 1.5])
    drawData(results1, 'x1', 'C0', x0=True, xfinal=True, initlabel=None)
    drawData(results2, 'x2', 'C1', x0=True, xfinal=True, initlabel=None)
    drawData(results3, 'x3', 'C2', x0=True, xfinal=True, initlabel=None)
    drawData(results4, 'x4', 'C3', x0=True, xfinal=True, initlabel=None)
    drawData(results5, 'x5', 'C4', x0=True, xfinal=True, initlabel=None)

    plt.figure()
    drawMuls(results1, 'x1')
    plt.legend()
    plt.title('Lagrange multipliers for trajectory x1')
    plt.show()
    plt.figure()
    drawMuls(results2, 'x2')
    plt.legend()
    plt.title('Lagrange multipliers for trajectory x2')
    plt.show()
input("Press any key")
