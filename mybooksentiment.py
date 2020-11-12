pip install -r requirements.txt

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
names = ['A Little Princess, by Frances Hodgson Burnett',
         'War and Peace, by Leo Tolstoy',
         'The Count of Monte Cristo, by Alexandre Dumas',
         'Jane Eyre, by Charlotte Bronte',
         'The Odyssey, by Homer',
         'Meditations, by Marcus Aurelius',
         'Great Expectations, by Charles Dickens',
         'The Enchanted April, by Elizabeth von Arnim']

def book(i):
        books = pd.DataFrame(columns=['Text'])
        req = Request(url=url[i-1], headers={'user-agent': 'booksays'})
        response = urlopen(req)
        html = BeautifulSoup(response, 'html.parser')
        para = html.select("p")
        for index, row in enumerate(para):
            title = row.text
            books = books.append({'Text': title}, ignore_index=True)
            books = books.replace(to_replace=['\r', '\n'], value='', regex=True)
        return books

def sentiments(books, i):
    vader = SentimentIntensityAnalyzer()
    avgsentiment = books['Text'].apply(lambda title: vader.polarity_scores(title)['compound'])
    positive = books['Text'].apply(lambda title: vader.polarity_scores(title)['pos'])
    neutral = books['Text'].apply(lambda title: vader.polarity_scores(title)['neu'])
    negative = books['Text'].apply(lambda title: vader.polarity_scores(title)['neg'])
    a = [avgsentiment, positive, neutral, negative]
    return a[i]

def plotsentiment(books, avgsentiment, name):
    # plot average sentiment through book
    plt.plot(range(len(books['Text'])), avgsentiment)
    plt.xlabel('Paragraphs from {}'.format(name))
    plt.ylabel('Sentiment with mean={}'.format(round(avgsentiment.mean(), 3)))
    plt.show()
    # plot sentiment graph
    books[["positive", "negative", "neutral"]].plot(kind='hist', alpha=0.4, legend=True)
    plt.ylabel('Paragraphs from {}'.format(name))
    plt.xlabel('Range of sentiments')

def plotbooksentiment():
    print('These are the available books:\n',
          1, ' A Little Princess, by Frances Hodgson Burnett\n',
          2, ' War and Peace, by Leo Tolstoy\n',
          3, ' The Count of Monte Cristo, by Alexandre Dumas\n',
          4, ' Jane Eyre, by Charlotte Bronte\n',
          5, ' The Odyssey, by Homer\n',
          6, ' Meditations, by Marcus Aurelius\n',
          7, ' Great Expectations, by Charles Dickens\n',
          8, ' The Enchanted April, by Elizabeth von Arnim\n')

    book_id = int(input('Enter the number of the book you wish to plot'))
    new = book(book_id)
    new['sentiment'] = sentiments(new, 0)
    new['negative'] = sentiments(new, 1)
    new['positive'] = sentiments(new, 2)
    new['neutral'] = sentiments(new, 3)
    plotsentiment(new, new['sentiment'], names[book_id - 1])

plotbooksentiment()
