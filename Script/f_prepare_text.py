"""
This script prepare the traing and validation (or data for prediction) sample
"""
import pandas as pd
import numpy as np
import nltk
import os
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
import csv
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.snowball import SnowballStemmer
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

# set working directory to script!
curr_dir = os.getcwd()
temp_dir = curr_dir.replace('Script','Temp')
input_dir = curr_dir.replace('Script','Input')


# detail about how we create NIH_disease_cleaning can refer to f_raw_to_intermediate_step2
raw_to_intermediate_step2 = pd.read_csv(input_dir + '/NIH_disease_cleaning.csv')
raw_to_i2 = raw_to_intermediate_step2.set_index('NIH_SPENDING_CATS')['Intermediate_step2'].to_dict()



# For each Intermediate_Step2 we construct (1. if diseases 2. if super-cats)
manual_crosswalk = pd.read_excel(input_dir + '/NIH_disease_crosswalk.xlsx',index_col=0)
i2_disease = set(manual_crosswalk.loc[manual_crosswalk['Diseases']==1,'Intermediate_step2'])
i2_disease_no_super = set(manual_crosswalk.loc[(manual_crosswalk['Diseases']==1)&(manual_crosswalk['Supercategory']!=1),'Intermediate_step2'])





def Preparing_Fastext_Training(no_super=True):
    # read training data: text + label
    training_df = pd.read_csv(input_dir + '/training.csv')
    
    # create a new column to put tokenized text (help improve prediction)
    training_df['PROJECT_TITLE_roots'] = ""            
      
    # clean the text
    training_df['PROJECT_TITLE'] = training_df['PROJECT_TITLE'].apply(clean)
    
    # tokenize title
    training_df['PROJECT_TITLE_roots'] = training_df['PROJECT_TITLE'].apply(simplify)
    
    # prepare labels 
    training_df['nih_cat_adjusted'] = training_df['NIH_SPENDING_CATS'].apply(lambda x: cat_sepration(x, raw_to_i2, i2_disease_no_super, i2_disease, no_super))
            
    return training_df[['PROJECT_TITLE_roots','nih_cat_adjusted']]


# this function convert above csv file to txt ---> so that you can do fasttext model!

def write_text(csv_name):
    file_name_txt = csv_name.replace('csv', 'txt')
    txt_file = open(temp_dir+'/' + file_name_txt, "w", encoding="utf-8") # create empty txt
    with open(temp_dir + '/' + csv_name, "r", encoding="utf-8") as csvFile:
        #Read CSV
        readCsv = csv.reader(csvFile)
        for row in readCsv:
            #Get Values and manupilate in the file.write
            row1 = ' '.join([i for i in row]) 
            row1 = row1.replace(",", " ") 
            #Write CSV you need format it to string if the value is an int
            txt_file.write(row1+'\n') # ie after each line go to new line
            
    #You Must Close the FIle after writing it.
    txt_file.close()
    
    return print('Training TXT is ready!')
















