#https://levelup.gitconnected.com/sentiment-analysis-using-machine-learning-python-9122e03f8f7b

#Import libraries
import nltk
from textblob import TextBlob
from newspaper import Article
#import datetime
import newspaper
import sys

#Get the article
url = str(input("Enter link of the article you want to parse :  "))
article = Article(url)
article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
#Download sentence tokenizer
# nltk.download('punkt')  #1 time download of the sentence tokenizer

#Keyword extraction wrapper
article.nlp()

#Write to file
sys.stdout = open("output.txt", 'w')
print('The author of the article is : ','\n\n', article.authors,'\n\n')
print("----------------------------------------------------------------")
print('The image in the article is :','\n\n', article.top_image,'\n\n')
print("----------------------------------------------------------------")

# Print text contained in the article
print('The entire text of the article is :','\n\n', article.text, '\n\n')
print("----------------------------------------------------------------")

#Print keywords
print('Some of the keywords in the article are :','\n\n', article.keywords, '\n\n')
print("----------------------------------------------------------------")

#Summary of article
text = article.summary 
print('The rough summary of the article : ', '\n\n', text, '\n\n')
print("----------------------------------------------------------------")

#Sentiment Value Calculation
obj = TextBlob(text) #returns the sentiment of text by returning a value between -1.0 and 1.0
#Print polarity of sentiment
sentiment = obj.sentiment.polarity 
print('The sentiment value is : ', '\n\n', sentiment, '\n\n')
print("----------------------------------------------------------------")

subjectivity = obj.sentiment.subjectivity

print("The subjectivity value of this article is : ", subjectivity)
print("----------------------------------------------------------------")

if sentiment==0:
    print('\nThe text is neutral\n\n')
elif sentiment>0:
    print('\nText is positive\n\n')
else:
    print('\nText is negative\n\n')







