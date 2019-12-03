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


class basicProblem(EuclideanOptimizable):
    def __init__(self):
        super().__init__(2)
        self.nconstraints = 0
        self.nineqconstraints = 2

    def x0(self):
        return [1.5, 2.25]

    def J(self, x):
        return x[1]+0.3*x[0]

    def dJ(self, x):
        return [0.3, 1]

    def H(self, x):
        return [-x[1]+1.0/x[0], -(3-x[0]-x[1])]

    def dH(self, x):
        return [[-1.0/x[0]**2, -1], [1, 1]]


params = {'alphaC': 1, 'debug': 0,
          'alphaJ': 1, 'dt': 0.1, 'maxtrials': 1}
resultsEqualized = nlspace_solve(EqualizedOptimizable(basicProblem()), params)
resultsEqualized['x'] = [list(x[0])+list(x[1])
                         for x in resultsEqualized['x']]

results = nlspace_solve(basicProblem(), params)
print(f"Method of slack ended in {len(resultsEqualized['J'])} iterations.")
print(f"Nullspace method ended in {len(results['J'])} iterations.")

resultsCopy = results.copy()
for key in results:
    resultsCopy[key] = results[key].copy()[:100]
input("\nWill test restarting, press any key")
resultsNew = nlspace_solve(basicProblem(), params, resultsCopy)

print("\nResults after restart:")
for key in resultsNew:
    print("{0:<10} before restart: \t".format(key), len(results[key]),
          " \t after restart:\t", len(resultsNew[key]))

print("")
print("Optimum :")
print(results['x'][-1])
print("Comparison with restarting : ")
print(resultsNew['x'][-1])
if with_plot:
    drawProblem(basicProblem(), XLIM=[0.2, 2.8], YLIM=[0.2, 2.8],
                resolution=200)
    drawData(resultsEqualized, 'EQUALIZED', 'green', x0=True)
    drawData(results, 'NLSPACE', 'blue')

    plt.figure()
    drawMuls(results, 'NLSPACE')
    plt.legend()

    plt.figure()
    drawJ(results)
    drawJ(resultsEqualized, 'EQUALIZED', linestyle='--')
    plt.legend()

    plt.show()

input("\nWill run basic problem 2. Press any key")
if with_plot:
    plt.close('all')


# BASIC PROBLEM2
class basicProblem2(EuclideanOptimizable):
    def __init__(self):
        super().__init__(2)
        self.nineqconstraints = 2
        self.nconstraints = 0

    def x0(self):
        return [1.5, 2.25]

    def J(self, x):
        return (x[0]-2)**2+(x[1]-2)**2

    def dJ(self, x):
        return [2*(x[0]-2), 2*(x[1]-2)]

    def H(self, x):
        return [-x[1]+1.0/x[0], -(3-x[0]-x[1])]

    def dH(self, x):
        return [[-1.0/x[0]**2, -1], [1, 1]]


options = {'alphaC': 0.2, 'alphaJ': 1, 'dt': 0.1}
resultsEqualized = nlspace_solve(
    EqualizedOptimizable(basicProblem2()), options)
resultsEqualized['x'] = [list(x[0])+list(x[1])
                         for x in resultsEqualized['x']]
if with_plot:
    drawData(resultsEqualized, 'EQUALIZED', 'green', loc='lower left', x0=True)

results = nlspace_solve(basicProblem2(), options)
print("")
print("Optimum :")
print(results['x'][-1])
print(f"Method of slack ended in {len(resultsEqualized['J'])} iterations.")
print(f"Nullspace method ended in {len(results['J'])} iterations.")
if with_plot:
    drawProblem(basicProblem2(), XLIM=[0.04, 3], YLIM=[
                0.2, 2.7], resolution=200)
    drawData(results, 'NLSPACE', 'blue', loc='lower left')

    plt.figure()
    drawMuls(results, 'NLSPACE')
    plt.legend()

    plt.figure()
    drawJ(results)
    drawJ(resultsEqualized, 'EQUALIZED', linestyle='--')
    plt.legend()

    plt.figure()
    drawC(results)
    drawC(resultsEqualized, 'EQUALIZED', linestyle='--')
    plt.legend()

input("\nWill run parab problem. Press any key")
# PARAB PROBLEM
if with_plot:
    plt.close('all')


class parabProblem(EuclideanOptimizable):
    def __init__(self):
        super().__init__(2)
        self.nconstraints = 0
        self.nineqconstraints = 2

    def x0(self):
        return [3, 3]

    def J(self, x):
        return x[1]**2+(x[0]+3)**2

    def dJ(self, x):
        return [2*(x[0]+3), 2*x[1]]

    def H(self, x):
        return [-x[0]**2+x[1], -x[1]-x[0]-2]

    def dH(self, x):
        return [[-2*x[0], 1], [-1, -1]]


options = {'alphaC': 0.2, 'alphaJ': 1,  'dt': 0.1}
resultsEqualized = nlspace_solve(EqualizedOptimizable(parabProblem()), options)
resultsEqualized['x'] = [list(x[0])+list(x[1])
                         for x in resultsEqualized['x']]
if with_plot:
    drawProblem(parabProblem(), XLIM=[-3.5, 5], YLIM=[-1.3, 3.2])
    drawData(resultsEqualized, 'EQUALIZED',
             'green', loc='lower right', x0=True)

results = nlspace_solve(parabProblem(), options)
print("")
print("Optimum :")
print(results['x'][-1])
print(f"Method of slack ended in {len(resultsEqualized['J'])} iterations.")
print(f"Nullspace method ended in {len(results['J'])} iterations.")
if with_plot:
    drawData(results, 'NLSPACE', 'blue', loc='lower right')

    plt.figure()
    drawMuls(results, 'NLSPACE')
    plt.legend()

    plt.figure()
    drawJ(results)
    drawJ(resultsEqualized, 'EQUALIZED', linestyle='--')
    plt.legend()

    plt.figure()
    drawC(results)
    drawC(resultsEqualized, 'EQUALIZED', linestyle='--')
    plt.legend()

    plt.show()
input("Press any key")
