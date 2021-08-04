import pickle, json,os,time
from functions import slow,clear,path

def save_data():
    while True:
        text, response = [],[]
        
        tag = input('\ntag ( empty to exit ) > ') or 'close'
        if tag == 'close':
            break

        while True:
            texts = input('text ( empty to skip to next ) > ') or 'done'
            if texts == 'done':
                break
            text.append(texts)
            
        while True:
            responses = input('responses ( empty to skip to next ) > ') or 'done'
            if responses == 'done':
                break
            response.append(responses)
            
        action = input('action ( empty for False ) > ') or False
        cls = input('class ( empty for None ) > ') or None
    
        dictionary = {
            'text':text,
            'tag':tag,
            'response':response,
            'action':action,
            'cls':cls
              }
              
        file = open(path+'DataSet.json')
        data = json.load(file)
        
        data['intents'].append(dictionary)
        
        file = open(path+'DataSet.json','w')
        json.dump(data,file,indent=4)
        data.clear()
    


def train_model():
    
    print('\nFeeding upon the new data')
    slow('..................\n')
    
    file = open(path+'DataSet.json','r')
    data = json.load(file)
    x,y=[],[]
    
    for i in range(len(data['intents'])):
        for j in range(len(data['intents'][i]['text'])):
            x += [data['intents'][i]['text'][j]]
            y += [data['intents'][i]['tag']]
    
    from sklearn.feature_extraction.text import CountVectorizer
    vect = CountVectorizer()
    vect.fit(x)
    
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    
    vectorized = vect.transform(x)
    clf.fit(vectorized,y)
    
    vocab = open(path+'vocabulary.pickle','wb')
    pickle.dump(vect,vocab)
    
    model = open(path+'model.pickle','wb')
    pickle.dump(clf,model)
    time.sleep(1)
    slow('\nIt was delicious :)')
    slow('\nSystem also restarted !')

