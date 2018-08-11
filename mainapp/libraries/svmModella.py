import os
import numpy as np

from sklearn.model_selection import KFold, train_test_split,cross_val_score

from sklearn import svm
import nltk

from sklearn import metrics

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pickle
from wordcloud import WordCloud

#importing dataset to data frame
# df = pd.read_csv('Real_Deal_Export.csv')
#
#
#
# #labels array
# text_data = df["description"]
# label_data = df["Label"]
# print  (text_data.shape)
# datashape = (text_data.shape)
# #print text_data
# #Clean and prep description Data
#
#
#
#
# #Split Train and test dataset...X is text_data, Y is label_data
# #random state is like a seed value that ensures that same results are derived regardless of the machine running the process
# #text_data_train, text_data_test, label_data_train, label_data_test = train_test_split(text_data, label_data, random_state=1, train_size=0.75,test_size=0.25)
#
# #Vectorization
# vectorizer = TfidfVectorizer(stop_words='english')
#
# #learn the vocab of the training data
# # text_data_train_transform = vectorizer.fit(text_data_train)
#
# # #transform train data into a document-term matrix
# #text_data_train_transform = vectorizer.fit_transform(text_data_train)
# #
# text_data_transform = vectorizer.fit(text_data)
#
# text_data_transform = vectorizer.transform(text_data)
#
#
# #transform test data into a document-term matrix
#text_data_test_transform = vectorizer.transform(text_data_test)

# print  len(vectorizer.get_feature_names())

# #convert sparse matrix to dense matrix
# #sparse matrix is probably better to feed into the model than dense matrix
# #print text_data_train.toarray()

# print pd.DataFrame(text_data_train_transform.toarray(), columns=
#                   vectorizer.get_feature_names())

#print vectorizer.get_feature_names()






#Support Vector machines
# svm = svm.LinearSVC()
# # svm.fit(text_data_train_transform,label_data_train)
# label_prediction_class = svm.predict(text_data_test_transform)
#
# # print label_prediction_class
#
# #Cross validation using kfold method so as to get more accurate scores on out-of-sample data
# # scoring attributes: accuracy,f1,recall, average_precision,precision,roc_auc
# scores = cross_val_score(svm, text_data_transform, label_data, cv=10, scoring='roc_auc')
#
#
#
#
# #test accuracy
# print('SVM accuracy ')
# # print metrics.accuracy_score(label_data_test,label_prediction_class)
#
# print scores
# print scores.mean()
#
#
# #Write to CSV file
# print 'writing Cyber Relevant Data to csv file...'
# # result = label_prediction_class
#
# cyber_related_description = []
# cyber_related_label= []
# cyber_related_add_time = []
# #
# # print result
#
#
# #
# # print 'related'
# # print (cyber_related_label)
#
# # print text_data_test.iloc[0]
# # print text_data_test.iloc[2]
#
#
#
# # print len(text_data_test)
#
# #for x in result:
# # classified_output =   pd.DataFrame(data={ "Description":text_data_test,"Label":result})
#
# # cyber_relevant = classified_output[classified_output.Label == 1 ]
#
#
#
# # print (cyber_relevant)
#
#
# # classified_output.to_csv('Classifed Output.csv')
# #cyber_relevant.to_csv('Cyber Relevant_RealDeal.csv')
# print ('Output Stored in CSV file')
#
#
#
#
# #LDA Analysis


def trainn_model(file):
    # from sklearn import svm
    # import pandas as pd


    df = pd.read_csv(file)

    df = df.drop_duplicates(subset=['name', 'description'], keep=False)

    df = df.fillna(value=50)
    # labels array
    text_data = df["description"]
    label_data = df["Label"]

    stopwords_file = open("search stopwords.txt", "r")
    stopwords_list = stopwords_file.read().splitlines()
    # Vectorization
    # vectorizer = TfidfVectorizer(stop_words=stopwords_list)
    vectorizer = TfidfVectorizer(stop_words=stopwords_list, token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b')

    # learn the vocab of the training data
    #text_data_train_transform = vectorizer.fit(text_data_train)

    # #transform train data into a document-term matrix
    # text_data_train_transform = vectorizer.fit_transform(text_data_train)
    #
    text_data_transform = vectorizer.fit(text_data)

    text_data_transform = vectorizer.transform(text_data)

    # print vectorizer.get_feature_names()
    #This can be used to get the most occuring words in the feature set
    # OR/AND get the words with the highest TFIDF scores

    # Support Vector machines

    ctiSvmModel = svm.LinearSVC()
    ctiSvmModel.fit(text_data_transform,label_data)


    #Saving Vectorizer
    vectorizer_pkl = open('vectorizer.pkl','wb')
    pickle.dump(vectorizer,vectorizer_pkl)
    vectorizer_pkl.close()

    #Saving the Model using pickle
    ctiSvmModel_pkl = open('ctiSvmModel.pkl','wb')
    pickle.dump(ctiSvmModel,ctiSvmModel_pkl)
    ctiSvmModel_pkl.close()


    return 'Data Trained Succesfully and Serialized'



def runModel(file):

    df = pd.read_csv(file)

    # Remove duplicate listings , keep = false means drop all duplicates
    df = df.drop_duplicates(subset=['name', 'description'], keep=False)


    df = df.fillna(value=50)
    text_data = df["description"]
    text_data = text_data.drop_duplicates()


    vectorizer_pkld = open('vectorizer3.pkl','rb')
    vectorizer = pickle.load(vectorizer_pkld)
    vectorizer_pkld.close()

    text_data_transform = vectorizer.transform(text_data.values.astype('U'))

    ctiSvmModel_pkld = open('ctiSvmModel3.pkl','rb')
    ctiSvmModel = pickle.load(ctiSvmModel_pkld)
    ctiSvmModel_pkld.close()

    result = ctiSvmModel.predict(text_data_transform)

    classified_output =   pd.DataFrame(data={ "Description":text_data,"Label":result})

    cyber_relevant = classified_output[classified_output.Label == 1 ]

    return cyber_relevant

def extractTopics(corpus,market_name,top_n):

    # df = pd.read_csv('Cyber Relevant_Oasis.csv')
    #
    # df.drop_duplicates(subset=['description'], keep=False)
    #
    # df = df.fillna(value=50)

    # text_data = df["Description"]

    text_data = corpus

    stopwords_file = open("search stopwords.txt", "r")
    stopwords_list = stopwords_file.read().splitlines()

    # vectorizer = TfidfVectorizer(stop_words=stopwords_list)
    #unicode and igonore cases
    vectorizer = TfidfVectorizer(stop_words=stopwords_list, token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b')

    vectorizer.fit_transform(text_data)
#Sorting the TFIDF scores from the lowest(higher frequency) to the highest
    index = np.argsort(vectorizer.idf_)[::1]
    features = vectorizer.get_feature_names()
    top_n = top_n


    top_features = [features[i] for i in index[:top_n]]
    # print(top_features)
    # print((vectorizer.vocabulary_))

    # vectorizer = TfidfVectorizer(stop_words=stopwords_list)
    #
    # text_data_transform = vectorizer.fit_transform(text_data.values.astype('U'))


    wc = WordCloud(
        relative_scaling=1.0,
        background_color='#f6f6f6',
        width = 800,
        height = 600,
        stopwords=stopwords_list,  # set or space-separated string
    ).generate(''.join(text_data))

    if market_name == 'agora':
        wc.to_file('mainapp/static/agora_wc.png')
    elif market_name == 'real_deal':
        wc.to_file('mainapp/static/real_deal_wc.png')
    elif market_name == 'hansa':
        wc.to_file('mainapp/static/hansa_wc.png')
    elif market_name == 'valhala':
        wc.to_file('mainapp/static/valhala_wc.png')
    elif market_name == 'tochka':
        wc.to_file('mainapp/static/tochka_wc.png')
    elif market_name == 'alpha_bay':
        wc.to_file('mainapp/static/alpha_bay_wc.png')
    elif market_name == 'evo':
        wc.to_file('mainapp/static/evo_wc.png')
    elif market_name == 'dream_market':
        wc.to_file('mainapp/static/dream_market_wc.png')
    elif market_name == 'adm':
        wc.to_file('mainapp/static/adm_wc.png')
    elif market_name == 'oasis':
        wc.to_file('mainapp/static/oasis_wc.png')

    return top_features

def getWordCloud(market_name):
    word_cloud_path =''
    if market_name == 'agora':
        #retreiving the file by its name alone
        word_cloud_path = 'agora_wc.png'
    elif market_name == 'real_deal':
        #retreiving the file by its name alone
        word_cloud_path = 'real_deal_wc.png'
    elif market_name == 'hansa':
        #retreiving the file by its name alone
        word_cloud_path = 'hansa_wc.png'
    elif market_name == 'valhala':
        #retreiving the file by its name alone
        word_cloud_path = 'valhala_wc.png'
    elif market_name == 'tochka':
        #retreiving the file by its name alone
        word_cloud_path = 'tochka_wc.png'
    elif market_name == 'alpha_bay':
        #retreiving the file by its name alone
        word_cloud_path = 'alpha_bay_wc.png'
    elif market_name == 'evo':
        #retreiving the file by its name alone
        word_cloud_path = 'evo_wc.png'
    elif market_name == 'dream_market':
        #retreiving the file by its name alone
        word_cloud_path = 'dream_market_wc.png'
    elif market_name == 'adm':
        #retreiving the file by its name alone
        word_cloud_path = 'adm_wc.png'
    elif market_name == 'oasis':
        #retreiving the file by its name alone
        word_cloud_path = 'oasis_wc.png'

    return word_cloud_path

# def getTopFetures(corpus):
#     text_data = corpus
    # stopwords_file = open("search stopwords.txt", "r")
    # stopwords_list = stopwords_file.read().splitlines()

