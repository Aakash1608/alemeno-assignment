import cv2
from PIL import Image
import math
import numpy as np

def read_image(buffer, flags):
    # this function reads the in memory image we get from the api request
    bytes_as_np_array = np.frombuffer(buffer.read(), dtype=np.uint8)
    return cv2.imdecode(bytes_as_np_array, flags)

def crop_image(img):
    # following function crops the image to remove access part(the part below final color block) of strip that doesnt have any test info
    height, width = img.shape[:2]
    img_crop = img[ 0 : math.floor(0.65*height), 0 : width]
    return img_crop

def strip_edges(img_crop):
    # function detects the strip rectangle and gives the left and right value of the edge 
    h_crop, w_crop = img_crop.shape[:2]
    img_gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(src=img_gray, ksize=(3, 5), sigmaX=0.5)
    img_edge = cv2.Canny(img_blur, 10, 250)

    # finding the points on left and right of edge detection
    find_left = False

    left_val = 0
    while not find_left:
        if img_edge[math.floor(h_crop/2), left_val] == 255:
            find_left = True
            break
        left_val += 1

    find_right = False
    right_val = w_crop-1
    while not find_right:
        if img_edge[math.floor(h_crop/2), right_val] == 255:
            find_right = True
            break
        right_val -= 1

    return left_val, right_val

def cvtBGR2RGB(color_val):
    temp = color_val[0]
    color_val[0] = color_val[2]
    color_val[2] = temp
    return color_val
def strip_detection(img):
    img = read_image(img, cv2.IMREAD_COLOR)
    img_crop = crop_image(img)
    h_crop, w_crop = img_crop.shape[:2]

    left_val, right_val = strip_edges(img_crop)

    h_one = 0
    h_ini = math.floor(h_crop/10)
    h_increment = h_ini
    w_init = math.floor((right_val+left_val)/2)

    color_val_dict={}
    color_key_arr=['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    for i in range(10):
        temp_img = img_crop[h_one : h_ini, 0 : w_crop]
        color_val = temp_img[math.floor((h_ini-h_one)/2), w_init]
        cvt_color_val = cvtBGR2RGB(color_val)
        color_obj = {color_key_arr[i]: cvt_color_val}
        color_val_dict.update(color_obj)
        h_one = h_ini
        h_ini += h_increment
    return color_val_dict