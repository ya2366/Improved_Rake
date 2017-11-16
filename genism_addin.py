from gensim.models import Phrases
from gensim.models.phrases import Phraser
import rake
import pandas as pd
import re
data=pd.read_excel("Beauty_review.xlsx")
reviews=data['reviewText']
train_list=[]
for review in reviews:
    one_sentence=re.sub(u'[^0-9|a-z|A-Z]'," ",review)
    words=one_sentence.split(" ")
    words_clean=[i for i in words if i != ""]
    train_list.append(words_clean)
## train a bigram phrase model
phrases = Phrases(train_list,min_count=5,threshold=10.0)
bigram  = Phraser(phrases)
# stoppath = "SmartStoplist.txt"
# # 1. initialize RAKE by providing a path to a stopwords file
# rake_object = rake.Rake(stoppath)