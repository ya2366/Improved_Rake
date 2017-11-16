import pandas as pd
import nltk
from nltk.corpus import wordnet

synonyms = []
word=("glow")
for syn in wordnet.synsets("glow"):
    for l in syn.lemmas():
        if l.name()!= word:
            synonyms.append(l.name())
        if l.antonyms():
            synonyms.append('no_'+l.antonyms()[0].name())


print(set(synonyms))
'''
from nltk.parse.stanford import StanfordDependencyParser
path_to_jar = '/Users/yutingan/stanford-parser-full-2017-06-09/stanford-parser.jar'
path_to_models_jar = '/Users/yutingan/stanford-parser-full-2017-06-09/stanford-parser-3.8.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

result = dependency_parser.raw_parse('Healthy skin has no itchiness, no flaky or blemishes and glowing')
dep = result.__next__()
dependency=[]
word_to_negate=[]
for row in list(dep.triples()):
    relation=[row[0][0],row[0][1],row[1],row[2][0],row[2][1]]
    dependency.append(relation)
df=pd.DataFrame(dependency,columns=['first_word','first_tag','relation','second_word','second_tag'])
print(df)
if 'neg' in list(df['relation']):
    after_no=df[df['second_word']=='no']['first_word']
    print(after_no)
    for word in list(after_no):
        word_to_negate.append(word)
        if not df[df['first_word']==word][df['second_word']=='or'][df['relation']=='cc'].empty:
             for relation_word in list(df[df['first_word']==word][df['relation']=='conj']['second_word']):
                 word_to_negate.append(relation_word)

print(word_to_negate)
'''