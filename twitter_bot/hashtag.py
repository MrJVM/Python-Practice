import tweepy
import csv
from twitter_bot import api


# Open/Create a file to append data
csvFile = open('twitter_output.csv', 'a')


# Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           "CNN",
                           100,
                           "en",
                           "2019-10-10").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

csvFile.close()