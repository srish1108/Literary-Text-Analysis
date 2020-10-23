from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

url = ['http://gutenberg.org/files/146/146-h/146-h.htm ',
       'http://gutenberg.org/files/2600/2600-h/2600-h.htm',
       'http://gutenberg.org/files/1184/1184-h/1184-h.htm',
       'http://gutenberg.org/files/1260/1260-h/1260-h.htm',
       'http://gutenberg.org/files/1727/1727-h/1727-h.htm',
       'http://gutenberg.org/files/2680/2680-h/2680-h.htm',
       'http://gutenberg.org/files/1400/1400-h/1400-h.htm',
       'http://gutenberg.org/cache/epub/16389/pg16389-images.html']

def book(i,bk):
        req = Request(url=url[i-1], headers={'user-agent': 'booksays'})
        response = urlopen(req)
        html = BeautifulSoup(response, 'html.parser')
        para = html.select("p")
        for index, row in enumerate(para):
            title = row.text
            bk = bk.append({'Text': title}, ignore_index=True)
            bk = bk.replace(to_replace=['\r', '\n'], value='', regex=True)

        ind = pd.Series(range(len(bk)))
        bk.set_index([ind])
        return bk

def senti(bk):
    vader = SentimentIntensityAnalyzer()
    score = lambda title: vader.polarity_scores(title)['compound']
    emo = bk['Text'].apply(score)
    return emo

def plottin(bk, s, n):
    # plot sentiment through book
    plt.plot(range(len(bk['Text'])), s)
    plt.xlabel(n)
    plt.ylabel('Sentiment through the book')
    plt.show()
    # plot sentiment graph
    plt.figure(figsize=(10, 8))
    bk.plot(kind='hist')
    plt.xlabel(n)
    plt.ylabel('Sentiment with mean = {}'.format(round(s.mean(), 3)))
    plt.show()

def plotmybook():
    new = pd.DataFrame(columns=['Text'])
    print('These are the available books:\n',
          1, ' A Little Princess, by Frances Hodgson Burnett\n',
          2, ' War and Peace, by Leo Tolstoy\n',
          3, ' The Count of Monte Cristo, by Alexandre Dumas\n',
          4, ' Jane Eyre, by Charlotte Bronte\n',
          5, ' The Odyssey, by Homer\n',
          6, ' Meditations, by Marcus Aurelius\n',
          7, ' Great Expectations, by Charles Dickens\n',
          8, ' The Enchanted April, by Elizabeth von Arnim\n')

    b = int(input('Which number book do you want to see?'))
    if b == 1:
        y = 'A Little Princess, by Frances Hodgson Burnett'
    elif b == 2:
        y = 'War and Peace, by Leo Tolstoy'
    elif b == 3:
        y = 'The Count of Monte Cristo, by Alexandre Dumas'
    elif b == 4:
        y = 'Jane Eyre, by Charlotte Bronte'
    elif b == 5:
        y = 'The Odyssey, by Homer'
    elif b == 6:
        y = 'Meditations, by Marcus Aurelius'
    elif b == 7:
        y = 'Great Expectations, by Charles Dickens'
    else:
        y = 'The Enchanted April, by Elizabeth von Arnim'

    new = book(b, new)
    new['sentiment'] = senti(new)
    plottin(new, new['sentiment'], y)

plotmybook()
