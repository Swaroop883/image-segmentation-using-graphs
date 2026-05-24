import numpy as np

def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

class UnionFind:
    def __init__(self, n: int, features: np.ndarray = None):

        self.parent = np.arange(n, dtype=np.int32)

        self.rank = np.zeros(n, dtype=np.int16)

        self.size = np.ones(n, dtype=np.int32)

        self.int_diff = np.zeros(n, dtype=np.float32)

        self.feature_sum = None

        if features is not None:

            self.feature_sum = features.reshape(-1, features.shape[-1]).copy()

    def find(self, x: int) -> int:

        root = x

        while self.parent[root] != root:
            root = self.parent[root]

        while self.parent[x] != x:
            p = self.parent[x]
            self.parent[x] = root
            x = p

        return root

    def _union_sets(self, ra: int, rb: int, w: float):

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        self.size[ra] += self.size[rb]

        self.int_diff[ra] = max(self.int_diff[ra], self.int_diff[rb], w)

        if self.feature_sum is not None:
            self.feature_sum[ra] += self.feature_sum[rb]

    def union_by_mean_similarity(self, a: int, b: int, w: float, threshold_mean: float) -> bool:

        if self.feature_sum is None:
            return False

        ra, rb = self.find(a), self.find(b)

        if ra == rb:
            return False

        mean_a = self.feature_sum[ra] / self.size[ra]
        mean_b = self.feature_sum[rb] / self.size[rb]

        w_mean = distance(mean_a, mean_b)

        if w_mean > threshold_mean:
            return False

        self._union_sets(ra, rb, w)

        return True
    def union_by_fh_algorithm(self, a: int, b: int, w: float, k: float) -> bool:
        
        ra, rb = self.find(a), self.find(b)

        
        if ra == rb:
            return False

        
        tau_a = self.int_diff[ra] + (k / self.size[ra])
        tau_b = self.int_diff[rb] + (k / self.size[rb])

        
        if w > min(tau_a, tau_b):
            return False

        
        self._union_sets(ra, rb, w)

        return True

    def force_union(self, a: int, b: int, w: float):

        ra, rb = self.find(a), self.find(b)

        if ra == rb:
            return False

        self._union_sets(ra, rb, w)

        return True