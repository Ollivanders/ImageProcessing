#######################################
# Filename: dilation.py               #
# Author: Oliver Baxandall            #
# Date created: 29 / 10 / 2017        #
# Date last modified: 18 / 11 / 2017  #
# Python Version: 2.7.14              #
#######################################

import cv2  # imports the opencv library
import numpy as np
import sys

""" 
Function that creates a new image and turns it into a dilated version of the input.
Dilation is where a shape/kernel with an origin at its centre is defined and ran through the image. The maximum
grayscale value that is found in the kernel is then allocated to the new dilated image
This function uses a square kernel of size 5x5.
"""

# =====================================================================================================================


def dilate(img):
    if not img is None:  # if no image is passed, no process is taken place and an error is printed to the command line
        h, w = np.shape(img)  # allocates the height and width of the image to the variables "h" and "w" respectively
        new_image = np.zeros((h, w), np.uint8)  # defines an image with coordinates 0 with the same size as the original

        # Iterate through the image pixel by pixel with {py, px} indicating the coordiantes for the Kernels origin
        for py in range(0, h):
            for px in range(0, w):
                # Defines 5x5 square for the Kernel by 2 corners
                # c1 is the top left corner and c2 is the bottom left
                c1 = [px - 2, py - 2]
                c2 = [px + 3, py + 3]
                # since python loops end at the final value, the bottom left corner is 1 coordinate larger either side
                # in order to properly define the kernel for the loops

                # if the kernel goes over the border of the image, the kernel corners are replaced with the corner of
                # the image that is breached in order to stop a border effect from damaging the process
                if not py - 2 >= 0:
                    c1[1] = 0
                if not py + 3 <= h:
                    c2[1] = h
                if not px - 2 >= 0:
                    c1[0] = 0
                if not px + 3 <= w:
                    c2[0] = w

                max_value = -1  # lower than actually possible so the pixel value will always be larger from the start
                # loops through the kernel and identifies the largest pixel value within it
                for ky in range(c1[1], c2[1]):
                    for kx in range(c1[0], c2[0]):
                        if img[kx, ky] > max_value:
                            max_value = img[kx, ky]

                new_image[px, py] = max_value  # assigns the largest pixel value to the orign{px,py} in the new_image
        return new_image  # wants the new image is processed, the new image is returned

    else:
        print("No image file successfully loaded.")  # printed to tell the user that the image was not loaded

# ===================================================================================================================


if __name__ == "__main__":  # avoided when an instance is created in other classes, only runs when file is run
    # Run when the script is run on the command line
    input_image = sys.argv[1]  # allocates the second String after python to the identity input_image
    output_image = sys.argv[2]  # allocates the third String after python to the identity input_image
    image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)  # reads the input image and allocates to the variable image
    cv2.imwrite(output_image, dilate(image))  # calls the dilation function on image and writes it to a file with
    # output_image name
