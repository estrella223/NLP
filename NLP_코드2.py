from wordcloud import WordCloud, STOPWORDS    # -------------------------------------------
import numpy as np    # ------------------------------------
from PIL import Image    # ------------------------------------
import matplotlib.pyplot as plt    # ------------------------------------


text = open('apple.txt', encoding='UTF8').read()
text = text.replace('HAN', 'Han')
text = text.replace("LUKE'S", 'Luke')

mask = np.array(Image.open('apple.png'))
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords,
               margin=5, random_state=1).generate(text)
              # margin은 여백?
              # if random object is given, this ti used for generating random numbers
default_colors = wc.to_array()    # convert to array for recoloring

import random
def grey_color_func(word, font_size, position, orientation,
                    random_state = None, **kwargs):
    return 'hsl(0, 100%%, %d%%)' % random.randint(60, 100)
          # hsl(색상, 채도, 명도)
          # 색상 0=red, 120=green, 240=blue. 0~360까지 가능
          # 채도 0%는 회색, 100%는 풀걸러
          # 명도 0%는 블랙, 100%는 화이트

plt.figure(figsize=(12, 12))
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation='bilinear')
plt.axis('off')
plt.show()