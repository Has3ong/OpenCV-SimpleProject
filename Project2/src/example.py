import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os


def create_rgb(i):
    x = np.array(cm.tab10(i))[:3]*255
    return tuple(x)

def mouse_callback(event, x, y, flags, param):
    global marks_updated
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image, (x, y), 10, (current_marker), -1)
        cv2.circle(window, (x, y), 10, colors[current_marker], -1)
        marks_updated = True

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(__BASE_DIR__ + '/small_coastal.jpg')

window = np.copy(image)

marker_image = np.zeros(image.shape[:2], dtype=np.int32)
segments = np.zeros(image.shape, dtype=np.uint8)

colors = []
for i in range(10):
    colors.append(create_rgb(i))

n_markers = 10
current_marker = 1
marks_updated = False

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

while True:
    cv2.imshow('Segments', segments)
    cv2.imshow('Image', window)

    k = cv2.waitKey(1)

    if k == 27:
        break

    elif k == ord('c'):
        window = image.copy()
        marker_image = np.zeros(image.shape[0:2], dtype=np.int32)
        segments = np.zeros(image.shape, dtype=np.uint8)

    elif k > 0 and chr(k).isdigit():

        current_marker = int(chr(k))

    if marks_updated:

        marker_image_copy = marker_image.copy()
        cv2.watershed(image, marker_image_copy)

        segments = np.zeros(image.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            segments[marker_image_copy == (color_ind)] = colors[color_ind]

        marks_updated = False

cv2.destroyAllWindows()