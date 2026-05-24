import cv2 as cv
import numpy as np
from typing import Tuple

from segmentation.color_utils import to_grayscale_or_lab
from segmentation.edge_builder import build_edges
from segmentation.union_find import UnionFind
from segmentation.visualization import random_color_segments

def segment_graph(img_bgr: np.ndarray,
                  min_size: int = 50,
                  connectivity: int = 8,
                  resize_to: int = 0,
                  mean_threshold: float = 20) -> Tuple[np.ndarray, np.ndarray]:

    orig_h, orig_w = img_bgr.shape[:2]

    img = img_bgr

    if resize_to and max(orig_h, orig_w) > resize_to:

        scale = resize_to / float(max(orig_h, orig_w))

        img = cv.resize(
            img_bgr,
            (int(orig_w * scale), int(orig_h * scale)),
            interpolation=cv.INTER_AREA
        )

    H, W = img.shape[:2]

    features, is_color = to_grayscale_or_lab(img)

    edges = build_edges(features, connectivity=connectivity)

    N = H * W

    uf = UnionFind(N, features=features)

    for w, u, v in edges:

        uf.union_by_mean_similarity(u, v, w, mean_threshold)

    for w, u, v in edges:

        ru, rv = uf.find(u), uf.find(v)

        if ru != rv and (uf.size[ru] < min_size or uf.size[rv] < min_size):

            uf.force_union(u, v, w)

    roots = np.fromiter((uf.find(i) for i in range(N)), dtype=np.int32)

    unique_roots, new_labels = np.unique(roots, return_inverse=True)

    labels = new_labels.reshape(H, W).astype(np.int32)

    vis = np.zeros_like(img, dtype=np.uint8)

    for lab in range(len(unique_roots)):

        mask = (labels == lab)

        if mask.any():

            mean_col = img[mask].mean(axis=0)

            vis[mask] = mean_col.astype(np.uint8)

    if (H, W) != (orig_h, orig_w):

        labels = cv.resize(
            labels,
            (orig_w, orig_h),
            interpolation=cv.INTER_NEAREST
        ).astype(np.int32)

        vis = cv.resize(
            vis,
            (orig_w, orig_h),
            interpolation=cv.INTER_NEAREST
        )

    return labels, vis