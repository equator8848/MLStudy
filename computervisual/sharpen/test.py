# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 15:34
# @Author  : Equator

import cv2
from computervisual.sharpen.sobel import sobel_filter
from computervisual.visual.compare import img_compare
import matplotlib.pyplot as plt


def test_color():
    img = cv2.imread('../images/ironman.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    (r, g, b) = cv2.split(img)
    bH = sobel_filter(b)
    gH = sobel_filter(g)
    rH = sobel_filter(r)
    output_img = cv2.merge((rH, gH, bH), )  # 通道合成
    img_maps = {}
    img_maps['source'] = img
    img_maps['output'] = output_img
    img_compare(img_maps)


def test_gray():
    img = cv2.imread('../images/ironman.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output_img = sobel_filter(gray)
    img_maps = {}
    img_maps['source'] = gray
    img_maps['output'] = output_img
    plt.title('img_compare')
    i = 1
    for key in img_maps:
        plt.subplot(len(img_maps), 1, i)
        plt.imshow(img_maps[key], cmap='gray')
        i = i + 1
    plt.show()


def test_color_merge():
    img = cv2.imread('../images/ironman.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    (r, g, b) = cv2.split(img)
    bH = (b + sobel_filter(b)) / 2
    gH = (g + sobel_filter(g)) / 2
    rH = (r + sobel_filter(r)) / 2
    output_img = cv2.merge((rH, gH, bH), )  # 通道合成
    img_maps = {}
    img_maps['source'] = img
    img_maps['output'] = output_img
    img_compare(img_maps)


if __name__ == '__main__':
    test_gray()
