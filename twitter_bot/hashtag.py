import tweepy
import csv
from twitter_bot import api


# United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')


# Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           "#covid19",
                           100,
                           "en",
                           "2019-10-10").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

csvFile.close()