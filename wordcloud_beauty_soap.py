from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS
# Read the whole text.
text = open('rating_5.txt').read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
cloud_mask = np.array(Image.open("cloud.png"))

stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=200, mask=cloud_mask,
               stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file("rating_5.png")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(cloud_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()