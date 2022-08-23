import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
# nltk.download('punkt')
# url = 'https://www.cnn.com/2022/08/22/politics/donald-trump-special-master-request/index.html'


def summarize():
    url = utext.get('1.0', 'end').strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    authors.config(state='normal')
    pdate.config(state='normal')
    summary.config(state='normal')
    mood.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    authors.delete('1.0', 'end')
    authors.insert('1.0', article.authors)

    pdate.delete('1.0', 'end')
    pdate.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    polarity = TextBlob(article.text).polarity
    mood_string = f'{"Positive" if polarity > 0  else "Negative" if polarity < 0 else "Neutral"}'

    mood.delete('1.0', 'end')
    mood.insert('1.0', mood_string)

    # title.config(state='disabled')
    # authors.config(state='disabled')
    # pdate.config(state='disabled')
    # summary.config(state='disabled')
    # mood.config(state='disabled')


root = tk.Tk()
root.title('Lazy Box')
root.geometry('800x500')

# Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=80)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Authors
alabel = tk.Label(root, text='Authors')
alabel.pack()

authors = tk.Text(root, height=1, width=80)
authors.config(state='disabled', bg='#dddddd')
authors.pack()

# Publish date
plabel = tk.Label(root, text='Publish date')
plabel.pack()

pdate = tk.Text(root, height=1, width=80)
pdate.config(state='disabled', bg='#dddddd')
pdate.pack()

# Summary
slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=15, width=80)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Mood analysis
mlabel = tk.Label(root, text='Mood')
mlabel.pack()

mood = tk.Text(root, height=1, width=80)
mood.config(state='disabled', bg='#dddddd')
mood.pack()

# URL
ulabel = tk.Label(root, text='URL')
ulabel.pack()

utext = tk.Text(root, height=1, width=80)
utext.pack()

btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

root.mainloop()
