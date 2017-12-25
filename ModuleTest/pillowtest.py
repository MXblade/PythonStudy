#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('../files/image/dog.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 应用模糊滤镜
im = im.filter(ImageFilter.BLUR)
# 把缩放后的图像用jpeg格式保存:
im.save('../files/image/dog2thumbnail.jpg', 'jpeg')