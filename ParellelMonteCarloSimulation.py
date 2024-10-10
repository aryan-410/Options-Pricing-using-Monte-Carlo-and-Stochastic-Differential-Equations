from numba import njit, prange
import numpy as np

@njit(parallel=True)
def parallel_asset_paths(S0, r, sigma, dt, M, N):
    S = np.zeros((N, M + 1))
    S[:, 0] = S0
    for t in prange(1, M + 1):
        Z = np.random.standard_normal(N)
        S[:, t] = S[:, t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)
    return S
