import cv2 as cv
import numpy as np
from typing import Tuple

def is_grayscale(img: np.ndarray) -> bool:

    if img.ndim == 2 or (img.ndim == 3 and img.shape[2] == 1):
        return True

    return False

def convert_to_grayscale(img: np.ndarray) -> np.ndarray:

    if is_grayscale(img):

        gray = img if img.ndim == 2 else img[:, :, 0]

    else:

        B = img[:, :, 0].astype(np.float32)
        G = img[:, :, 1].astype(np.float32)
        R = img[:, :, 2].astype(np.float32)

        gray = 0.114 * B + 0.587 * G + 0.299 * R

    gray = gray[:, :, None]

    return gray.astype(np.float32)

def convert_to_lab(img: np.ndarray) -> np.ndarray:

    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    return lab.astype(np.float32)

def to_grayscale_or_lab(img: np.ndarray) -> Tuple[np.ndarray, bool]:

    if is_grayscale(img):

        gray_img = convert_to_grayscale(img)

        return gray_img, False

    else:

        lab_img = convert_to_lab(img)

        return lab_img, True