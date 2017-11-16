import pandas as pd

#plotly.tools.set_credentials_file(username='ya2366', api_key='NsBnrxY3Pt2oYtTIA6t1')
reviews=pd.read_excel("Beauty_review.xlsx")
import matplotlib.pyplot as plt
import numpy as np

rating_1=reviews.loc[reviews['overall'] == 1]
rating_2=reviews.loc[reviews['overall'] == 2]
rating_3=reviews.loc[reviews['overall'] == 3]
rating_4=reviews.loc[reviews['overall'] == 4]
rating_5=reviews.loc[reviews['overall'] == 5]

rating_1_str=""
rating_2_str=""
rating_3_str=""
rating_4_str=""
rating_5_str=""
for i in range(len(rating_1)):
    rating_1_str=rating_1_str+" "+rating_1.iloc[i,5]

for i in range(len(rating_2)):
    rating_2_str=rating_2_str+" "+rating_2.iloc[i,5]

for i in range(len(rating_3)):
    rating_3_str=rating_3_str+" "+rating_3.iloc[i,5]
for i in range(len(rating_4)):
    rating_4_str=rating_4_str+" "+rating_4.iloc[i,5]
for i in range(len(rating_5)):
    rating_5_str=rating_5_str+" "+rating_5.iloc[i,5]
#keywords_healthy=rake_object.run(healthy_skin,0.8)
#top_10_keyword=keywords_healthy[0:10]
#for keyword in keywords_healthy:
#    print("Keywords: ",keyword[0], "Score: ",keyword[1],"Counts: ",keyword[2])
with open('rating_1.txt',"w") as out:
    out.write(rating_1_str)
with open('rating_2.txt',"w") as hout:
    hout.write(rating_2_str)
with open('rating_3.txt',"w") as gout:
    gout.write(rating_3_str)
with open('rating_4.txt',"w") as mout:
    mout.write(rating_4_str)
with open('rating_5.txt',"w") as cout:
    cout.write(rating_5_str)