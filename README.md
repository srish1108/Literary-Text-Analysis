## Welcome to Literary Text Analysis

**This project delves into the scientization of literary texts used in Bibliotherapy.**

![lit](https://user-images.githubusercontent.com/65708254/98934021-76057500-2507-11eb-9e26-ef9e88450f63.png)

### Bibliotherapy

[Bibliotherapy](https://en.wikipedia.org/wiki/Bibliotherapy#:~:text=Bibliotherapy%20) is the study of literary texts and their effects on the reader as a means of therapy. It is found to be useful in treatment of mental health especially patients with [mild depression](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpp.1814). The literary texts used are often selected from the self help genre but sometimes fiction and graphic novels (in the case of children) are used too.

### Project

This project takes its roots from Computational Linguistics. It is divided into multiple components for a comprehensive understanding of what factors play a major role in selecting literary texts for the purpose of Bibliotherapy. Here are the steps:

- Prepare and extract a copyright free list of books known to have been used in Bibliotherapy

- Use NLP techniques for text preprocessing to prepare the data for further analysis

- Extract the most used words with a frquency distribution across all texts for lexical analysis

- Create a sentiment analyzer and plot graphs that show the range of sentiments in the entire text

- Analyze emotional affect of each literary text using the NRC Lexicon

- Compare the texts to learn the similarities among them for further use

### Plot A Book

The libraries used are BeautifulSoup, Pandas, NLTK Vader's sentiment analyzer, NRC Lexicon, Matplotlib

The list of novels is retrieved from [Tolstoy Therapy](https://www.tolstoytherapy.com/bibliotherapy-recommendations/).
The books are extracted from [Project Gutenberg](http://gutenberg.org/) which includes a vast number of copyright free ebooks.

The novels used in this project are as follows: 

- A Little Princess, by Frances Hodgson Burnett
- War and Peace, by Leo Tolstoy
- The Count of Monte Cristo, by Alexandre Dumas
- Jane Eyre, by Charlotte Bronte
- The Odyssey, by Homer
- Meditations, by Marcus Aurelius
- Great Expectations, by Charles Dickens
- The Enchanted April, by Elizabeth von Arnim

### Observations
#### Sentiment Analysis

A common observation in the sentiment analysis of the books altogether is that they have a positive mean and most of the book ranges from neutral (0) to positive (+1). While the average mean of the overall sentiments of the books is closer to 0, in other words the texts don't exhibit a strong positive or negative theme. Each book as a whole has sentiments varying from negative(-1) to positive(+1) though there is a corresponding variation in themes. The strong positive sentiments utilize themes of love, joy and happiness while strong negative ones talk about grief, violence, tragedy and so on.

There are two graphs which indicate the sentiments, and by extension themes, displayed throughout the individual texts. The first graph shows the high positive (green) sentiment being balanced by negative (orange) and neutral ones. The second graph displays the overall sentiment with its mean.

Here are some of the graphs for you take a look at:

![The Little Princess : range of sentiments](https://user-images.githubusercontent.com/65708254/98933400-92ed7880-2506-11eb-9084-e8d7485461e8.png)

![The Little Princess : overall sentiment](https://user-images.githubusercontent.com/65708254/96993835-784c6300-1549-11eb-8f66-24beb444913d.png)

![Jane Eyre : range of sentiments](https://user-images.githubusercontent.com/65708254/98940943-ceda0b00-2511-11eb-9b68-f660ec142a1a.png)

![Jane Eyre : overall sentiment](https://user-images.githubusercontent.com/65708254/96993777-65d22980-1549-11eb-9518-82a80b33942a.png)

#### Emotion Analysis:

With the help of the **NRC Emotion Lexicon**, which is a list of English words and their associations with eight basic emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and two sentiments (negative and positive), the given literary texts were analysed.

- The most observed emotions throughout the texts are positive emotions of **Trust** and **Anticipation**
- The least observed of all the emotions were those of **Disgust** and **Surprise**
- There is a strong presence of positive emotions over the negative ones in each of these texts

You can take a look at the entire project [here](https://github.com/srish1108/Literary-Text-Analysis), I'll be updating it in the coming few weeks to add all the features. If you found this useful or have any questions regarding it, do let me know. Thank you.


### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
