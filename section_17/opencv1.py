import cv2

img = cv2.imread('images/galaxy.jpg', 0)

print type(img)
print img           # actual numpy data
print img.shape     # shape of numpy array tuple-3
print img.ndim      # image dimensions
print (img.shape[1]/2, img.shape[0]/2)      # resized tuple.

resized_image = cv2.resize(img, (img.shape[1]/2, img.shape[0]/2))     # resize interpolates values and spits out an image.

cv2.imshow('Galaxy', resized_image)

cv2.waitKey(0)  #wait, in milliseconds
cv2.destroyAllWindows()

cv2.imwrite('images/galaxy_resize.jpg', resized_image)