"""
This script allows you to
1. training Fasttext Model
2. predict the validation model
Before started, please set working directory to /Script
"""
import os
import fasttext
import pandas as pd
import numpy as np
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.snowball import SnowballStemmer
from f_prepare_text import *
from f_ml_text_clean import *
lemmatizer = WordNetLemmatizer()
snow_stemmer = SnowballStemmer(language='english')
stop_words = set(stopwords.words('english'))
# we don't want single letter, so remove those words
single_words = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'}
stop_words = stop_words.difference(single_words)
pd.set_option('mode.chained_assignment', None)

#------------------------------------------------------------------
# Clean the training data, and convert it to suit fasttext
#------------------------------------------------------------------
curr_dir = os.getcwd()
temp_dir = curr_dir.replace('Script','Temp')
input_dir = curr_dir.replace('Script','Input')

training_df = Preparing_Fastext_Training(no_super=True)
training_df.to_csv(temp_dir + "/training_cleaned.csv", index=False, header=False)

# here use above csv filename
write_text("training_cleaned.csv")




#------------------------------------------------------------------
# clean the validation data
#------------------------------------------------------------------
# read the data
validation = pd.read_csv(input_dir + "/validation.csv")
# clean the title text
validation['PROJECT_TITLE'] = validation['PROJECT_TITLE'].apply(clean)
# tokenize the cleaned text
validation["PROJECT_TITLE_roots"]=np.nan
validation['PROJECT_TITLE_roots']=validation['PROJECT_TITLE'].apply(simplify)
    

#------------------------------------------------------------------
# model training and prediction
#------------------------------------------------------------------
# detail about the package refers to https://fasttext.cc/docs/en/python-module.html#usage-overview
model = fasttext.train_supervised(temp_dir + "/training_cleaned.txt", lr=.5, epoch=5, wordNgrams=2, loss='ova')

# model prediction    
validation['predicted'] = validation['PROJECT_TITLE_roots'].apply(lambda x: model.predict(x, k=-1, threshold=0.8)[0])

# recover the label back to disease
validation['predicted'] = validation['predicted'].astype(str)
validation['predicted'] = validation['predicted'].apply(recover)


# if you just want the predicted result you can stop here!

#------------------------------------------------------------------
# How well is the model doing?
#------------------------------------------------------------------

# first we clean the validation true label
validation['nih_cat_adjusted'] = validation['NIH_SPENDING_CATS'].apply(lambda x: cat_sepration(x, raw_to_i2, i2_disease_no_super, i2_disease, no_super))
validation['nih_cat_adjusted'] = validation['nih_cat_adjusted'].apply(lambda x: x.split(' '))
validation['nih_cat_adjusted'] = validation['nih_cat_adjusted'].apply(lambda x: [a.replace("__label__", "") for a in x])
validation['nih_cat_adjusted'] = validation['nih_cat_adjusted'].apply(lambda x: [a.replace("_", " ") for a in x])
validation['nih_cat_adjusted'] = validation['nih_cat_adjusted'].apply(set)
validation['nih_cat_adjusted'] = validation['nih_cat_adjusted'].apply(lambda x: x.difference({""}))

# then we convert predicted label to set
validation['predicted'] = validation['predicted'].apply(lambda x: x.split(', '))
validation['predicted'] = validation['predicted'].apply(lambda x: [a.replace(",", "") for a in x])
validation['predicted'] = validation['predicted'].apply(set)
validation['predicted'] = validation['predicted'].apply(lambda x: x.difference({""}))

validation['overlap'] = validation.apply(lambda x: x['predicted'].intersection(x['nih_cat_adjusted']), axis=1)

# then we can use some general ML stat to measure the performance























