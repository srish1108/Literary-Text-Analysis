## Welcome to Literary Text Analysis

**This project delves into the scientization of literary texts used in Bibliotherapy.**

### Bibliotherapy

[Bibliotherapy](https://en.wikipedia.org/wiki/Bibliotherapy#:~:text=Bibliotherapy%20) is the study of literary texts and their effects on the reader as a means of therapy. It is found to be useful in treatment of mental health especially patients with [mild depression](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpp.1814). The literary texts used are often selected from the self help genre but sometimes fiction and graphic novels (in the case of children) are used too.

### Project

This project is divided into multiple components.

- Prepare and extract a copyright free list of books known to have been used in Bibliotherapy

- Create a sentiment analyzer and plot graphs that show the range of sentiments in the entire text

- Continue with text preprocessing to prepare the data for further text analysis

- Extract the most used words, including positive and negative words

- Compare the texts in terms of sentiments and language to learn the similarities among them for further use

### My Book Sentiment

This part of the project constitutes the first two aspects of analyzing the sentiments of the classic literary novels. 

The libraries used are Pandas, NLTK and Matplotlib. Vader's sentiment analyzer is used to conduct the sentiment analysis.

The list of novels is retrieved from [Tolstoy Therapy](https://www.tolstoytherapy.com/bibliotherapy-recommendations/).
The books are extracted from [Project Gutenberg](http://gutenberg.org/) which includes a vast number of copyright free ebooks.

The novels used in this project are classics and are as follows: 

- A Little Princess, by Frances Hodgson Burnett
- War and Peace, by Leo Tolstoy
- The Count of Monte Cristo, by Alexandre Dumas
- Jane Eyre, by Charlotte Bronte
- The Odyssey, by Homer
- Meditations, by Marcus Aurelius
- Great Expectations, by Charles Dickens
- The Enchanted April, by Elizabeth von Arnim

A common observation in the sentiment analysis of the books altogether is that they have a positive mean and most of the book ranges from neutral (0) to positive (+1) sentiments. While each of the book as a whole has sentiments varying from negative(-1) to positive(+1), a major portion lies in the positive zone utilizing themes of love, joy and happiness. Here are some of the graphs for you take a look at:

![The Little Princess](https://user-images.githubusercontent.com/65708254/96993831-76829f80-1549-11eb-9701-34f49831e1e7.png)

![The Little Princess](https://user-images.githubusercontent.com/65708254/96993835-784c6300-1549-11eb-8f66-24beb444913d.png)

![Meditations_sentiment](https://user-images.githubusercontent.com/65708254/96993789-6965b080-1549-11eb-8167-9f0085c4ad11.png)

![Meditations_sentiment](https://user-images.githubusercontent.com/65708254/97003252-ccab0f00-1558-11eb-8911-f567271e70d7.png)

![Jane Eyre](https://user-images.githubusercontent.com/65708254/96993770-62d73900-1549-11eb-9385-6bb9ad5fd1ab.png)

![Jane Eyre](https://user-images.githubusercontent.com/65708254/96993777-65d22980-1549-11eb-9518-82a80b33942a.png)


You can take a look at the entire project [here](https://github.com/srish1108/Literary-Text-Analysis), I'll be updating it in the coming few weeks to add all the features. If you found this useful or have any questions regarding it, do let me know. Thank you.


### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
