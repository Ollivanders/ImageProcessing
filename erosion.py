#######################################
# Filename: erosion.py                #
# Author: Oliver Baxandall            #
# Date created: 29 / 10 / 2017        #
# Date last modified: 18 / 11 / 2017  #
# Python Version: 2.7.14              #
#######################################

import cv2  # imports the opencv library
import numpy as np
import sys
import dilation as dilate  # imports the dilation function

""" 
Function that creates a new image and turns it into a eroded version of the input.
Erosion is where a shape/kernel with an origin at its centre is defined and ran through the image. The minimum
grayscale value that is found in the kernel is then allocated to the new dilated image. It is therefore the opposite of
dilation. This function therefore creates a complement of the orignal image first and the runs the dilation function
on the complement image, then finds the complement of that result. This is equivalent to erosion. The new image is then
created.
"""


# ---------------------------------------------------------------------------------------------------------------------


def erode(img):
    if not img is None:  # if no image is passed, no process is taken place and an error is printed to the command line
        h, w = np.shape(img)  # allocates the height and width of the image to the variables "h" and "w" respectively
        new_image = np.zeros((h, w), np.uint8)  # defines an image with coordinates 0 with the same size as the original

        # Iterate through the image pixel by pixel with {py, px} indicating the coordinates for the Kernels origin
        for py in range(0, h):
            for px in range(0, w):
                img[px, py] = 255 - img[px, py]
                # creates a complement image by subtracting the grayscale value from the max value

        new_image = dilate.dilate(img)  # dilates the complement image and allocates it to new_image
        for py in range(0, h):
            for px in range(0, w):
                new_image[px, py] = 255 - new_image[px, py]  # creates the complements of the dilatied image

        return new_image

    else:
        print(
            "No image file successfully loaded.")  # printed to tell the user that the image was not loaded


# ---------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":  # avoided when an instance is created in other classes, only runs when file is run
    # Run when the script is run on the command line
    input_image = sys.argv[1]  # allocates the second String after python to the identity input_image
    output_image = sys.argv[2]  # allocates the third String after python to the identity input_image
    image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)  # reads the input image and allocates to the variable image
    cv2.imwrite(output_image, erode(image))  # calls the dilation function on image and writes it to a file with
    # output_image name
