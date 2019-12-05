import numpy as np
from numpy import pi


def diffMatrix(M, method):

    D = np.zeros((M, M))
    if method == 'fourier':
        delta = 2 * pi / M

        for i in range(M):
            for j in range(M):
                if M % 2 == 0:
                    if i == j:
                        D[i, j] = - pi ** 2 / (3 * delta ** 2) - 1 / 6
                    else:
                        D[i, j] = -(-1) ** (i - j) * .5 * np.sin((i - j) * delta / 2) ** (-2)
                else:
                    if i == j:
                        D[i, j] = - pi ** 2 / (3 * delta ** 2) - 1 / 12
                    else:
                        D[i, j] = -(-1) ** (i - j) * .5 * (np.sin((i - j) * delta / 2) ** (-1)) \
                                       * (np.tan((i - j) * delta / 2) ** (-1))
        D = (delta ** 2) * D
    elif method == 'finite':
        D = -2 * np.eye(M) + np.eye(M, k=1) + np.eye(M, k=-1)

    return D

class SCSA:

    def __init__(self, D, signal, h=1, auto=True):
        self.signal = signal
        self.M = len(signal)
        self.h = h
        self.reconstructed = np.zeros(self.M)
        self.D = D
        self.eig = np.zeros(self.M)
        self.mse = 0

        if auto:
            self.reconstruct()

    def reconstruct(self):
        I = np.diag(self.signal - np.min(self.signal))
        H = -(self.h**2)*self.D - I

        self.eig, func = np.linalg.eig(H)

        indx = self.eig.argsort()
        self.eig = self.eig[indx]
        func = np.real(func[:, indx])
        self.km = np.sqrt(-np.real(self.eig[self.eig <= 0]))
        self.psi = func[:, self.eig <= 0]

        for i in range(len(self.km)):
            self.reconstructed += 4*self.h*self.km[i]*np.square(func[:, i])

        self.reconstructed = self.reconstructed + np.min(self.signal)

        self.mse = np.square(self.signal - self.reconstructed).mean()

    def writeEigToTxt(self, path):
        f = open(path, 'w+')
        f.write("h = " + str(self.h) + '\n')
        for i in range(len(self.eig)):
            f.write(str(self.eig[i]) + '\n')
        f.close()

    def writePsiToCsv(self, path):
        f = open(path, 'w+')
        for i in range(len(self.psi[0, :])):
            if i == (len(self.psi[0, :]) - 1):
                f.write("Psi_" + str(i) + "\n")
            else:
                f.write("Psi_" + str(i) + ",")

        for j in range(len(self.psi[:, 0])):
            for i in range(len(self.psi[0, :])):
                if i == (len(self.psi[0, :]) - 1):
                    f.write(str(self.psi[j, i]) + "\n")
                else:
                    f.write(str(self.psi[j, i]) + ",")

        f.close()
