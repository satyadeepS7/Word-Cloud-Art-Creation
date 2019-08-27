"""
//Created on Tue Aug 27 05:38:32 PM 2019

// satyadeep singh
"""
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

stopwords = set(STOPWORDS)

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        font_path='C:\\Windows.old\\WINDOWS\\Fonts\\Candara.ttf',
        background_color='black',
        stopwords=stopwords,
        max_words=30,
        max_font_size=40, 
        min_font_size=10,
        scale=5,
        width=1200,
        height=500,
        repeat=True,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(facecolor = None, figsize=(8, 8))
    plt.tight_layout(pad = 0)
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()
    plt.imsave("Hello1.png",wordcloud)
    
data = "Tarannum'19,Debate,Kavyanjali,PosterMaking,RangoliMaking,Roadies,TreasureHunt,BestOfWaste,BillionDollarIdea,BhangraNight,FolkSinging,TED-X,DJ-Night".replace(',',' ')

show_wordcloud(data)