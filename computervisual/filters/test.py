# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 15:34
# @Author  : Equator
import cv2
from computervisual.filters.means_filter import means_filter
from computervisual.visual.compare import img_compare


def test_means_filter():
    img = cv2.imread('../images/ironman.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output_img = means_filter(gray, 3)
    img_maps = {}
    img_maps['source'] = gray
    img_maps['output'] = output_img
    img_compare(img_maps)


def test_color():
    img = cv2.imread('../images/ironman.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    (r, g, b) = cv2.split(img)
    bH = means_filter(b, 3)
    gH = means_filter(g, 3)
    rH = means_filter(r, 3)
    output_img = cv2.merge((rH, gH, bH), )  # 通道合成
    img_maps = {}
    img_maps['source'] = img
    img_maps['output'] = output_img
    img_compare(img_maps)


if __name__ == '__main__':
    test_color()
