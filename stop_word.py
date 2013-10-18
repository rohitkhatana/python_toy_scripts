
from twitter_complete import *
import re



#reading stop words from file
def get_stopWord(fd):
    l=[]
    for line in fd:
        line = line[:-1]
        l.append(line)
    return l

if __name__=="__main__":

    url_pat =   r'http+s?\:\/\/[a-zA-Z0-9]+\..+'
    '''
    resp = urllib.urlopen(a)
    print resp.getcode()
    200
    print resp.url

    '''
    
    fd = open('stop_words.txt','r')
    stop_word=[]
    stop_word=get_stopWord(fd)
    


    consumer_secret= 'hHWxrOaZ3e1P9q44q6t0tNLvHZXucKETg2CGuchsmRc'
    consumer_key= 'kgIpenTTZcD7wD9dnOOxPQ'
    
    oauth_token= '283990956-UTpDslfO4N7oBBpz0aaOIH7qAu0es2qHv7ocape7'
    oauth_token_secret= 'cHOMQHSKH5foZTsOWucSRhpnKsXzOI0PuFHKElLFI'
    
    #rohit
    oauth_token = '838203445-AOC6HFdUCZfAswXKVQQpdyCJImHoloyFVr1qZVSd'
    oauth_token_secret= 'v93GUHb2zoR8bNYzrN81Ns36hzaC8KgBTYGO3cGM'
    api = Api(consumer_key, consumer_secret,
              oauth_token, oauth_token_secret)
    #patio11 = software developer blogger
    #user_list = api.get_user_search('patio11')
    user_timeline = api.get_user_timeline(screen_name='rohitkhatana3')
    rate_limit = api.rate_limit(['statuses'])
    tweet_list = []
    for i in user_timeline :
        tweet = i['text'].encode('ascii','ignore')
        tweet_list.append(tweet.lower())    #ignore is for non ascii character
         
    d={}
    print tweet_list
    for tweet in tweet_list:
        sp = tweet.split()
        for word in sp:
            '''for i in range(len(word)):
                if word[i].isalnum() or ord(word[i]) == 35  or ord(word[i]) == 64:    
                    temp += word[i]
            '''
            if not word[len(word)-1].isalnum():
                word=word[:-1]
            if word not in stop_word:
                if word not in d:
                    d[word] = 1
                else:
                    d[word]+=1




    mx=0
    key=''
    for k,v in d.iteritems():
        print k,v
        if v > mx:
          key = k
          mx=v




        print "--------max------"
    print key,mx
