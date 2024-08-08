"""
This script provides functions clean title, abstract and label of the projects
"""
# necessary package
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



def clean(x):
    if pd.isna(x): # if nan
        return x
    else: # if not nan
        x = x.lower()
        x = x.replace("/", " ") # put a space so that both words on both sides are accounted separately
        x = x.replace('description','')
        x = x.replace('provided by applicant','')
        x = x.replace('[unreadable]' ,'')
        x = x.replace('abstract not provided' ,'')
        x = x.replace("(", "")
        x = x.replace(")", "")
        x = x.replace(",", "")
        x = x.replace("*", "")
        x = x.replace("'", "")
        x = x.replace("``", "")
        x = x.replace('"', "")
        x = x.replace("-", " ")  
        x = x.replace(".", "")   
        x = x.replace(":", "") 
        x = x.replace(";", "") 
        x = x.replace("?", "") 
        x = x.replace("!", "") 
        x = x.replace("#", "") 
        x = x.replace("$", "") 
        x = x.replace("%", "") 
        x = x.replace("applicant", "") 
        x = x.replace("project summary", "") 
        x = x.replace("summary", "") 
        x = x.replace("abstract", "")
        x = x.replace("project narrative", "") 
        x = x.replace("narrative", "") 
        x = x.replace("public health relevance", "") 
        x = x.lower() 
        return x
    
def simplify(x):
    #tokenize the words
    if pd.isna(x):
        return x
    else:
        word_tokens=nltk.word_tokenize(x)
        list_words = [w for w in word_tokens if not w.lower() in stop_words]
        # lemmatize words and put together again in a sentence
        x = ' '.join([lemmatizer.lemmatize(words) for words in list_words])
        return x



def cat_sepration(x, i2_dict, dset_ns, dset, no_super): 
   #for each proj, e.g. NIHCAT = [alzheimer; stem cell; heart disease]---->[__label__alzheimer __label__stem_cell __label__heart_disease]
    string_back=""
    list_words_incat=x.split(";") # split categories for same project
    for l in range(0,len(list_words_incat)): # drop empty spaces beginning and end of each cat
        list_words_incat[l]=list_words_incat[l].rstrip()
        list_words_incat[l]=list_words_incat[l].lstrip()
    list_words_incat = [i for i in list_words_incat if i] # drop null categories 
    # (1) convert categories into cleaned cat version, keep cleaned version only
    cat_needed = [i2_dict.get(i,"") for i in list_words_incat if i]
    # two set of diseases
    cat_ns = [i for i in cat_needed if i in dset_ns]    
    cat_ws = [i for i in cat_needed if i in dset] # drop if not disease
    if no_super == True:        
        cat_needed = list(set(cat_ns))   #drop duplicates
    elif no_super == False:        
        cat_needed = list(set(cat_ws))   #drop duplicates
    else:
        print('Please check no_super option is correct')
    # (2) attach label
    pref='__label__'
    for w in cat_needed:
        w = w.replace(' ','_')
        string_back=string_back+pref+w+" "    
    
    return string_back 


def recover(x):
    if x == "": # if nan
        return np.nan
    else: # if not nan
        x = x.replace("'", "") # put a space so that both words on both sides are accounted separately
        x = x.replace('"', "") 
        x = x.replace("(", "")
        x = x.replace(")", "")
        x = x.replace("__label__", "")
        x = x.replace("_", " ")
        return x