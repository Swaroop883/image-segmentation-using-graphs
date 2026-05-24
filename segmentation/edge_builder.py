import numpy as np

def build_edges(features: np.ndarray, connectivity: int = 8):

    H, W, C = features.shape

    idx = lambda r, c: r * W + c

    edges = []

    for r in range(H):

        for c in range(W):

            p_idx = idx(r, c)

            p_features = features[r, c, :]

            if c + 1 < W:

                w = np.sqrt(np.sum((p_features - features[r, c + 1, :]) ** 2))

                edges.append((w, p_idx, idx(r, c + 1)))

            if r + 1 < H:

                w = np.sqrt(np.sum((p_features - features[r + 1, c, :]) ** 2))

                edges.append((w, p_idx, idx(r + 1, c)))

            if connectivity == 8:

                if (r + 1 < H) and (c + 1 < W):

                    w = np.sqrt(np.sum((p_features - features[r + 1, c + 1, :]) ** 2))

                    edges.append((w, p_idx, idx(r + 1, c + 1)))

                if (r + 1 < H) and (c - 1 >= 0):

                    w = np.sqrt(np.sum((p_features - features[r + 1, c - 1, :]) ** 2))

                    edges.append((w, p_idx, idx(r + 1, c - 1)))

    edges.sort(key=lambda t: t[0])

    return edges