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


def compute_f(x, initial_condition):
    return eval(initial_condition)


def compute_matrix(L, delta_x, T, delta_t, beta, boundary_1, boundary_2, initial_condition):
    sigma = beta * delta_t / (delta_x ** 2)
    N = int(L / delta_x)
    M = int(T / delta_t)

    x = []
    for i in range(int(N) + 1):
        x.append(i * delta_x)

    t = []
    for i in range(int(M) + 1):
        t.append(i * delta_t)

    const_matrix = (1 + 2 * sigma) * np.identity(int(N - 1))
    for i in range(1, int(N) - 1):
        const_matrix[i - 1][i] = -sigma
        const_matrix[i][i - 1] = -sigma

    const_matrix = inv(const_matrix)
    const_vect = np.zeros((int(N - 1), 1))
    const_vect[0] = boundary_1
    const_vect[int(N - 1) - 1] = boundary_2

    u0 = np.zeros((int(N - 1), 1))
    for i in range((int(N - 1))):
        u0[i] = compute_f(((i + 1) * delta_x), initial_condition)

    u = []
    u.append(u0)

    for i in range(int(M)):
        u.append(np.dot(const_matrix, (u[i] + sigma * const_vect)))

    bigU = np.zeros((int(N) + 1, int(M) + 1))

    for k in range(int(M + 1)):
        for i in range(1, int(N)):
            bigU[i, k] = u[k][i - 1]

    for i in range(int(M) + 1):
        bigU[0, i] = boundary_1  # one end
        bigU[int(N), i] = boundary_2

    return bigU


def plot_heatmap(L, delta_x, T, delta_t, beta, boundary_1, boundary_2, initial_condition, resolution=500):
    bigU = compute_matrix(L, delta_x, T, delta_t, beta,
                          boundary_1, boundary_2, initial_condition)
    print(bigU.shape)
    plt.figure()
    sns.heatmap(bigU)
    print("here")
    plt.ylabel("x")
    plt.xlabel("t")

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


def plot_3D(L, delta_x, T, delta_t, beta, boundary_1, boundary_2, initial_condition, resolution=500):
    bigU = compute_matrix(L, delta_x, T, delta_t, beta,
                          boundary_1, boundary_2, initial_condition)
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
    ha.plot_surface(X.T, T.T, bigU, color="red")
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
