#######################################
# Filename: closing.py                #
# Author: Oliver Baxandall            #
# Date created: 29 / 10 / 2017        #
# Date last modified: 18 / 11 / 2017  #
# Python Version: 2.7.14              #
#######################################

import cv2  # imports the opencv library
import sys
import erosion as erode  # imports the erosion function
import dilation as dilate  # imports the dilation function

""" 
Function that creates a new image and turns it into a closed version of the input.
Closing is when an image is dilated and then the resulting image is then eroded using a specified kernel size
This function uses the dilation and erosion classes established in the other files, which use a square kernel, size 5x5.
"""


# ---------------------------------------------------------------------------------------------------------------------


def close(img):
    if not img is None:  # if no image is passed, no process is taken place and an error is printed to the command line
        new_image = dilate.dilate(img)  # runs dilation on the input image and allocates it to new_image
        final_image = erode.erode(new_image)  # runs erosion on the new_image and allocates it to itself
        return final_image  # returns the new_image
    else:
        print("No image file successfully loaded.")


# ---------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":  # avoided when an instance is created in other classes, only runs when file is run
    # Run when the script is run on the command line
    input_image = sys.argv[1]  # allocates the second String after python to the identity input_image
    output_image = sys.argv[2]  # allocates the third String after python to the identity input_image
    image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)  # reads the input image and allocates to the variable image
    cv2.imwrite(output_image, close(image))  # calls the dilation function on image and writes it to a file with
    # output_image name
