from __future__ import absolute_import
from __future__ import print_function
import six
__author__ = 'a_medelyan'

import rake
import operator
import io
import pandas as pd

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file


# ## run on the beauty and soup
'''
surveys=pd.read_excel("Bar_soup.xlsx",header=0)
healthy_skin=""
how_know_healthy=""
how_get_healthy=""
how_maintain=""
how_concerned=""
for i in range(len(surveys)):
    healthy_skin=healthy_skin+" "+surveys.iloc[i,1]
    how_know_healthy=how_know_healthy+" "+surveys.iloc[i,2]
    how_get_healthy=how_get_healthy+" "+surveys.iloc[i,3]
    how_maintain=how_maintain+" "+surveys.iloc[i,4]
    how_concerned=how_concerned+" "+surveys.iloc[i,5]

#keywords_healthy=rake_object.run(healthy_skin,0.8)
#top_10_keyword=keywords_healthy[0:10]
#for keyword in keywords_healthy:
#    print("Keywords: ",keyword[0], "Score: ",keyword[1],"Counts: ",keyword[2])
with open('healthy_skin.txt',"w") as out:
    out.write(healthy_skin)
with open('how_know_healthy.txt',"w") as hout:
    hout.write(how_know_healthy)
with open('how_get_healthy.txt',"w") as gout:
    gout.write(how_get_healthy)
with open('how_maintain_healthy.txt',"w") as mout:
    mout.write(how_maintain)
with open('how_concerned.txt',"w") as cout:
    cout.write(how_concerned)
'''
#2. run on RAKE on a given text
sample_file = io.open("healthy_skin.txt", 'r',encoding="iso-8859-1")
text = sample_file.read()
rake_object = rake.Rake(stoppath)
keywords = rake_object.run(text,0.8)
# # 3. print results
print("Keywords Score: ", keywords['keywords_score'])
print("Keywords counts: ",keywords['keywords_counts'] )
print("Stem Counts: ", keywords['stem_counts'])

print("----------")
# # EXAMPLE TWO - BEHIND THE SCENES (from https://github.com/aneesha/RAKE/rake.py)

#1. initialize RAKE by providing a path to a stopwords file
'''
rake_object = rake.Rake(stoppath,3,4,2,1,1,2)

text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
       "of a system of linear Diophantine equations, no strict inequations, and not strict inequations are considered. " \
       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
       "systems and systems of mixed types. Not a lot of linear equations are considered"

sample_file = io.open("healthy_skin.txt", 'r',encoding="iso-8859-1")
text = sample_file.read()
print("Finish Reading Text")
freq_trade_off=0.8
top_n=20
'''
# sentence_list_raw = rake.split_sentences(text)
# sentence_list=rake.spell_check(sentence_list_raw)
# stopwordlist=rake.load_stop_words(stoppath)
# stop_words_pattern = rake.build_stop_word_regex(stopwordlist)
# print("Start detecting negation")
# sentence_list_neg_melt = rake.handle_neg_list(sentence_list)
# print("Start Lemmatizing")
# sentence_list_lemma=rake.lemmatize_sentence_list(sentence_list_neg_melt)
# ## new step for extracting common word phrases like body wash
# #sentence_list_group_words=group_words(sentence_list_neg_melt)
# print("start generating candidate")
# phrase_list_lemma = rake.generate_candidate_keywords(sentence_list_lemma, stop_words_pattern, stopwordlist,
#                                                  1, 5, 1, 1,2)
# print("stemming candidate")
# final_list, phrase_list_stem, track_stem = rake.stem_candidate_keywords(phrase_list_lemma)
# print("calculate keyphrase stem metrics")
# stem_word_scores,keyphrase_stem_counts,keyphrase_stem_frequency = rake.calculate_stem_metrics(phrase_list_stem, freq_trade_off)
# print("calculate keyphrase lemma metrics")
# lemma_word_scores,keyphrase_lemma_counts,keyphrase_lemma_frequency=rake.calculate_word_metrics(phrase_list_lemma,freq_trade_off)
# keyphrase_candidates_score = rake.generate_lemma_keyphrase_scores(phrase_list_lemma, lemma_word_scores)
# return_list={}
# sorted_keywords = sorted(six.iteritems(keyphrase_candidates_score), key=operator.itemgetter(1), reverse=True)
# top_n_keywords=sorted_keywords[0:top_n]
# keywords_score=[]
# keywords_counts=[]
# keywords_freq=[]
# for pair in top_n_keywords:
#      keywords_score.append((pair[0],pair[1]))
#      keywords_counts.append((pair[0],keyphrase_lemma_counts[pair[0]]))
#      keywords_freq.append((pair[0],keyphrase_lemma_frequency[pair[0]]))
#
# sorted_stem = sorted(six.iteritems(stem_word_scores), key=operator.itemgetter(1), reverse=True)
# top_n_stem = sorted_stem[0:top_n]
# stem_score = []
# stem_counts = []
# stem_freq = []
# for pair in top_n_stem:
#        stem_score.append((pair[0], pair[1]))
#        stem_counts.append((pair[0], keyphrase_stem_counts[pair[0]]))
#        stem_freq.append([pair[0], keyphrase_stem_frequency[pair[0]]])
# return_list['keywords_score']=keywords_score
# return_list['keywords_counts']=keywords_counts
# return_list['keywords_freq']=keywords_freq
# return_list['stem_score']=stem_score
# return_list['stem_counts']=stem_counts
# return_list['stem_freq']=stem_freq
#
# print("keywords_score: ", return_list['keywords_score'] )
# print("keywords_count: ", return_list['keywords_counts'])
# print("Stem counts: ",return_list['stem_counts'])

