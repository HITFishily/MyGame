# -*- coding: utf-8 -*-
from PIL import Image,ImageFont,ImageDraw
import os

text = u'''虽然使用 TrueType 字体比使用位图字体更灵活，但是它渲染速度较慢，
并且更改标签的属性(字体，大小)是一项非常消耗性能的操作。
如果您需要具有相同属性的多个 Label 对象，那可以创建一个 TTFConfig 对象来统一配置，
TTFConfig 对象允许你设置所有标签的共同属性。"
'''
im = Image.new("RGB", (1920, 1080), (147, 213, 220))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype('font.TTF', 30)
dr.text((10, 440), text, font=font, fill="#000000")
#im.show()
im.save('1.png')