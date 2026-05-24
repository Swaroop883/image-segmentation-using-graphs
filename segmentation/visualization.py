import numpy as np

def random_color_segments(labels: np.ndarray) -> np.ndarray:

    H, W = labels.shape

    n_labels = labels.max() + 1

    rng = np.random.default_rng(42)

    palette = rng.integers(
        0,
        255,
        size=(n_labels, 3),
        dtype=np.uint8
    )

    out = palette[labels]

    return out