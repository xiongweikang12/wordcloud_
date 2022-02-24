import jieba
import numpy as np
from pathlib import Path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
from collections import Counter


def split_four_text(text):
    # split_four_text函数用于jieba分词并分隔为2个字为一组的内容。

    words = jieba.lcut(text)

    # 用Counter方法计算单词频率数
    count = Counter(words) #dict的形式 {content:count.....}
    most_count = count.most_common() #list(content,count) [('加缪',6)......()]内容，频数
    words_list = []

    for i in most_count:
        if len(i[0]) == 2:
            words_list.append(i[0])

    return words_list


def draw_wordcloud(text, image_mask, ):
    # draw_wordcloud函数以用户定义的模板轮廓图来显示中文词云。

    sanguo_mask = np.array(Image.open(image_mask))

    wordcloud = WordCloud(background_color='white', mask=sanguo_mask,
                          max_words=1000,max_font_size=100,min_font_size=2
                          # 如果不设置中文字体，可能会出现乱码
                          ,font_path='C:\Windows \Fonts \STXINGKA.TTF')

    wordcloud.generate(text)

    image_colors = ImageColorGenerator(sanguo_mask)

    plt.figure(figsize=(14, 8))

    # 创建左侧中文词云图
    plt.subplot(121)
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    wordcloud.to_file('最爱.png')
    plt.axis('off')

    # 创建右侧原图
    plt.subplot(122)
    plt.imshow(sanguo_mask, interpolation='bilinear')
    plt.axis('off')

    plt.show()

text_path=Path('加缪.txt')
with text_path.open(encoding='utf-8') as f:
    text_content=f.read()
    exsit_jia=split_four_text(text_content)
    draw_wordcloud(str(exsit_jia),image_mask='加缪-removebg-preview_好压看图.png')
