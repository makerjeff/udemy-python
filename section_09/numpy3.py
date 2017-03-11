'''Learning how to index, slice, and iterate through arrays.'''

import numpy as np
import cv2

im_gray = cv2.imread('../smallgray.png', 0)     # 0 = grayscale, 1 = BGR, -1 unaltered
print im_gray[0:2, 2:4]                         # gets a small subsection of an image. can probably an ROI from this.
