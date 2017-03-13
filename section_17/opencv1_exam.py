# exercise / exam
# loop through files in the 'images' folder and create smaller versions of each

import cv2
import glob
import os

images = glob.glob('images/*.jpg')

for i in images:

    filename = os.path.basename(i)
    # open the file
    file = cv2.imread(i, -1)

    # resize the file
    resized = cv2.resize(file, (file.shape[1]/3, file.shape[0]/3))

    # show the file
    cv2.imshow(i, resized)


    # wait until keypress
    cv2.waitKey(0)

    # destroy all windows
    cv2.destroyAllWindows()

    # write to file
    cv2.imwrite('images/'+'resized_' + filename, resized)
