
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
    user_timeline = api.get_user_timeline(screen_name='uxmovement')
    rate_limit = api.rate_limit(['statuses'])
    tweet_list = []
    c=0
    while True:
        for i in user_timeline:
            id = i['id']
            tweet = i['text'].encode('ascii','ignore')
            if tweet not in tweet_list:
                tweet_list.append((tweet.lower(),id))    #ignore is for non ascii character
        max_id = tweet_list[-1][1]
        c+=1
        user_timeline=api.get_user_timeline(screen_name='uxmovement',max_id=max_id)
        if c==10:
            break
    d={}
    
    for tweet,i in zip(tweet_list,range(len(tweet_list))):
        print str(i) + "----->" + tweet[0]
        sp = tweet[0].split()
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
    word_list=[]
    for k,v in d.iteritems():
        t = (v,k)
        word_list.append(t)
        if v > mx:
          key = k
          mx=v



    word_list.sort()
    for i in word_list:
        print i
        print "--------------"
    print "---------------------------maxxxx-------------"
    print key,mx
