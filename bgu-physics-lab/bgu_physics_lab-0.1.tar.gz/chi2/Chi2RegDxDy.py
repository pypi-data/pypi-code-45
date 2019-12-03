import matplotlib.pyplot as plt
# from matplotlib.offsetbox import AnchoredText
import matplotlib
import numpy
import iminuit
# from iminuit import Minuit, describe
# from iminuit.util import make_func_code
# import numpy as np


class Chi2RegDxDy:  # This class is like Chi2Regression but takes into account dx
    def __init__(self, model, x, y, dx, dy):
        self.model = model  # model predicts y value for given x value
        self.x = numpy.array(x)  # the x values
        self.y = numpy.array(y)  # the y values
        self.dx = numpy.array(dx)  # the x-axis uncertainties
        self.dy = numpy.array(dy)  # the y-axis uncertainties
        self.func_code = iminuit.util.make_func_code(iminuit.describe(self.model)[1:])
        self.h = (x[-1] - x[
            0]) / 10000  # this is the step size for the numerical calculation of the df/dx = last value in x (x[-1]) - first value in x (x[0])/10000

    def __call__(self, *par):  # par are a variable number of model parameters
        self.ym = self.model(self.x, *par)
        df = (self.model(self.x + self.h, *par) - self.ym) / self.h  # the derivative df/dx at point x is taken as [f(x+h)-f(x)]/h
        chi2 = sum(((self.y - self.ym) ** 2) / (self.dy ** 2 + (df * self.dx) ** 2))  # chi2 is now Sum of: f(x)-y)^2/(uncert_y^2+(df/dx*uncert_x)^2)
        return chi2

    def show(self, optimizer, x_title="X", y_title="Y", goodness_loc=2):
        self.par = optimizer.parameters
        self.fit_arg = optimizer.fitarg
        self.chi2 = optimizer.fval
        self.ndof = len(self.x) - len(self.par)
        self.chi_ndof = self.chi2 / self.ndof
        self.par_values = []
        self.par_error = []
        text = ""
        for _ in (self.par):
            self.par_values.append(self.fit_arg[_])
            self.par_error.append(self.fit_arg["error_" + _])
            text += "%s = %0.4f \u00B1 %0.4f \n" % (_, self.fit_arg[_], self.fit_arg["error_" + _])
        text = text + "\u03C7\u00B2 /ndof = %0.4f(%0.4f/%d)" % (self.chi_ndof, self.chi2, self.ndof)
        self.y_fit = self.model(self.x, *self.par_values)
        plt.rc("font", size=16, family="Times New Roman")
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_axes([0, 0, 1, 1])
        # ax.plot(self.x,self.y_fit)
        ax.plot(self.x, self.y_fit)  # I think we want to
        ax.scatter(self.x, self.y, c="red")
        # ax.errorbar(self.x, self.y, self.dy, self.dy,fmt='none',ecolor='red', capsize=3) typo here I think!(?)
        ax.errorbar(self.x, self.y, self.dy, self.dx, fmt='none', ecolor='red', capsize=3)
        ax.set_xlabel(x_title, fontdict={"size": 21})
        ax.set_ylabel(y_title, fontdict={"size": 21})
        anchored_text = matplotlib.offsetbox.AnchoredText(text, loc=goodness_loc)
        ax.add_artist(anchored_text)
        plt.grid(True)