# coding=utf-8
# @Time: 2023/8/11 15:29
# @Author: liyang
# @File: wordCloud.py
# @Software: PyCharm

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import sqlite3

# 1.准备词云所需的文字
con = sqlite3.connect('movieTop250.db')
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

# 2.分词
cut = jieba.cut(text)
words = [word for word in cut if len(word) > 1]  # 仅保留长度大于1的词语
string = ' '.join(words)
print(len(string))

# 3.创建遮罩
img = Image.open(r'.\static\assets\img\tree.jpg')  # 打开遮罩图片
img_array = np.array(img)  # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(string)

# 4.绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 是否显示坐标轴

# plt.show()  # 显示生成的词云图片
# 5.输出词云图片到文件
plt.savefig(r'.\static\assets\img\wordCloud.jpg', dpi=200)
