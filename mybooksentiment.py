pip install -r requirements.txt

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
porter = PorterStemmer()
from nrclex import NRCLex
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

stop_words_file = open("C:/Users/Srishti/Desktop/SmartStopList.txt", "r").read().split("\n")

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
            books = books.replace(to_replace=['\r', '\n'], value=' ', regex=True)
        return books

def sentiments(books, i):
    vader = SentimentIntensityAnalyzer()
    avgsentiment = books['Text'].apply(lambda title: vader.polarity_scores(title)['compound'])
    positive = books['Text'].apply(lambda title: vader.polarity_scores(title)['pos'])
    neutral = books['Text'].apply(lambda title: vader.polarity_scores(title)['neu'])
    negative = books['Text'].apply(lambda title: vader.polarity_scores(title)['neg'])
    a = [avgsentiment, positive, neutral, negative]
    return a[i]

def clean(books):
    words = [word_tokenize(sent) for sent in books['Text']]
    newList = []
        for element in words:
            for item in element:
                if item.isalpha():
                    newList.append(item)

        clean_words = [word.lower() for word in newList]
        clean_words = [w for w in clean_words if not w in stop_words_file]
        clean_words = [porter.stem(word) for word in clean_words]
        return clean_words

def book_emotions(books):
    word = [word for word in books['Text'] if word not in stop_words_file]
    word = str([cell.encode('utf-8') for cell in word])
    emotions = NRCLex(word)
    emotions = emotions.raw_emotion_scores
    emotions = pd.DataFrame(emotions, index=[0])
    emotions = pd.melt(emotions)
    emotions.columns = ('Emotions', 'Count')
    emotions = emotions.sort_values('Count')
    return emotions


def wordplots(books, name):
    # plot average sentiment throughout the book
    books['sentiment'].plot(kind='hist')
    plt.xlabel('Paragraphs from {}'.format(name))
    plt.ylabel('Sentiment with mean={}'.format(round((books.sentiment).mean(), 3)))
    plt.show()

    # plot all sentiments
    books[["positive", "negative", "neutral"]].plot(alpha=0.4, legend=True)
    plt.xlabel('Paragraphs from {}'.format(name))
    plt.ylabel('Range of sentiments with their magnitude')

    #create wordcloud
    clean_words = clean(books)
    wordcloud = WordCloud(background_color="white").generate(str(clean_words))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    #plot emotions
    emo = book_emotions(books)
    plt.figure(figsize=(12, 6))
    plt.title(('{} and its emotional effects').format(name))
    sns.set_style('dark')
    sns.set_context(context='notebook', font_scale=1.5)
    sns.barplot(x='Emotions', y='Count', data=emo[0:8], palette='viridis')

    # Create frequency distribution and plot
    freqdist1 = nltk.FreqDist(clean_words)
    plt.figure(figsize=(10, 10))
    freqdist1.plot(25)


def plot_a_book():
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
    wordplots(new, names[book_id - 1])

plot_a_book()
