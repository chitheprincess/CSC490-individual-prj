import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
from numpy.linalg import inv
from io import BytesIO
import base64
import os
import time
import glob
from math import pi


def compute_f(x, f_x):
    return eval(f_x)


def compute_g(x, g_x):
    return eval(g_x)


def compute_matrix(L, delta_x, T, delta_t, c, f_x, g_x, boundary_1, boundary_2):
    sigma = (c * delta_t / (delta_x)) ** 2
    N = L / delta_x
    M = T / delta_t

    initial_cond = np.zeros(int(N + 1))
    for i in range(int(N + 1)):
        initial_cond[i] = compute_f((i * delta_x), f_x)

    u_neg = np.zeros(int(N + 1))
    u_neg[0] = initial_cond[0]
    u_neg[int(N)] = boundary_2
    for i in range(1, int(N)):
        u_neg[i] = initial_cond[i] - delta_t * compute_g((i * delta_x), g_x) + sigma * (
            initial_cond[i - 1] - 2*initial_cond[i] + initial_cond[i + 1]) / 2

    const_matrix = (2 - 2 * sigma) * np.identity(int(N + 1))
    const_matrix[0][0] = 0
    const_matrix[int(N)][int(N)] = 0
    for i in range(1, int(N)):
        const_matrix[i][i - 1] = sigma
        const_matrix[i][i + 1] = sigma

    u = []
    u.append(u_neg)
    u.append(initial_cond)

    for i in range(1, int(M + 1)):
        u_prev = np.copy(u[i - 1])
        u_prev[0] = -boundary_1
        u_prev[int(N)] = -boundary_2
        u.append(np.dot(const_matrix, u[i]) - u_prev)

    bigU = np.zeros((int(N) + 1, int(M) + 1))

    for k in range(int(M + 1)):
        for i in range(int(N + 1)):
            bigU[i, k] = u[k + 1][i]

    return bigU


def plot_3D_wave(L, delta_x, T, delta_t, c, f_x, g_x, boundary_1, boundary_2, resolution=500):
    bigU = compute_matrix(L, delta_x, T, delta_t, c, f_x,
                          g_x, boundary_1, boundary_2)
    N = int(L / delta_x)
    M = int(T / delta_t)

    x = []
    for i in range(int(N)+1):
        x.append(i*delta_x)

    t = []
    for i in range(int(M)+1):
        t.append(i*delta_t)

    hf = plt.figure()
    ha = hf.add_subplot(111, projection='3d')

    # `plot_surface` expects `x` and `y` data to be 2D
    X, T = np.meshgrid(x, t)
    ha.plot_surface(X.T, T.T, bigU)
    ha.set_xlabel("x", fontsize=20)
    ha.set_ylabel("t", fontsize=20)
    ha.set_zlabel("u", fontsize=20)

    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile
