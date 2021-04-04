import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
from numpy.linalg import inv
from io import BytesIO
import base64


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
    sns.set()
    sns.heatmap(bigU)
    plt.ylabel("x")
    plt.xlabel("t")

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png
