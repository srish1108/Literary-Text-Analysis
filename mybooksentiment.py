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

def sentiments(books):
    vader = SentimentIntensityAnalyzer()
    score = lambda title: vader.polarity_scores(title)['compound']
    sentiment = books['Text'].apply(score)
    return sentiment

def plotsentiment(books, sentiment, name):
    # plot sentiment through book
    plt.plot(range(len(books['Text'])), sentiment)
    plt.xlabel(name)
    plt.ylabel('Sentiment through the book')
    plt.show()
    # plot sentiment graph
    plt.figure(figsize=(10, 8))
    books.plot(kind='hist')
    plt.xlabel(name)
    plt.ylabel('Sentiment with mean = {}'.format(round(sentiment.mean(), 3)))
    plt.show()

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

    book_id = int(input('Which number book do you want to see?'))
    new = book(book_id)
    new['sentiment'] = sentiments(new)
    plotsentiment(new, new['sentiment'], names[book_id - 1])

plotbooksentiment()
