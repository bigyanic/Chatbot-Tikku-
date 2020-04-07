 # Meet Pybot: your friend

import nltk
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import random
import string
f=open('exam.txt','r',errors = 'ignore')

checkpoint = "./chatbot_weights.ckpt"
raw=f.read()
raw=raw.lower()# converts to lowercase
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words


sent_tokens[:2]


word_tokens[:5]



lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_Ans = ["My name is Tikku.","My name is Tikku i can help you in examination related issues.","Im tikku :) ","My name is tikku.I am happy to solve your examination related queries :) "]
GREETING_INPUTS = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("what is your work ?","what is your work","what can you do?","what you can do.")
Basic_Ans = "I can help you with examinaton related issues,about Examination related rules,informations and many more."
Basic_Om = ("when will exam start","when will exam begin.","when will exam start in lpu ","when will exam start in lpu?","when will exam start in lpu?","","when will exam begin in lpu.")
Basic_AnsM = ["Please refer UMS for detail,goto Examination details section and you will find details of start of exam."]


# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans

# Checking for Basic_QM
def basicM(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)
        
# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"Sorry! i am unable to understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


def chat(user_response):
    user_response=user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False

            return "You are welcome.."
        elif(basicM(user_response)!=None):
            return basicM(user_response)
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):

                return
            elif(greeting(user_response)!=None):

                return greeting(user_response)
            elif(user_response.find("What is your name") != -1 or user_response.find("What is your name?") != -1 or user_response.find("who are you") != -1 or user_response.find("Who are you?") != -1):
                return IntroduceMe(user_response)
            elif(basic(user_response)!=None):
                return basic(user_response)
            else:

                return response(user_response)
                sent_tokens.remove(user_response)
                
    else:
        flag=False

        return "Bye! take care.."
        
        

