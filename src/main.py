# import json
# import sys
#
# import twitter
#
# CONSUMER_KEY = ''
# CONSUMER_SECRET=''
# ACCESS_TOKEN_KEY= ''
# ACCESS_TOKEN_SECRET = ''
#
# def get_tweets(api=None, screen_name=None):
#     timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
#     earliest_tweet = min(timeline, key=lambda x: x.id).id
#     print("getting tweets before:", earliest_tweet)
#
#     while True:
#         tweets = api.GetUserTimeline(
#             screen_name=screen_name, max_id=earliest_tweet, count=200
#         )
#         new_earliest = min(tweets, key=lambda x: x.id).id
#
#         if not tweets or new_earliest == earliest_tweet:
#             break
#         else:
#             earliest_tweet = new_earliest
#             print("getting tweets before:", earliest_tweet)
#             timeline += tweets
#
#     return timeline
#
if __name__ == "__main__":
#     api = twitter.Api(
#         CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
#     )
#     screen_name = sys.argv[1]
#     print(screen_name)
#     timeline = get_tweets(api=api, screen_name=screen_name)
#
#     timeline = map(lambda x: (x.text, x.id_str), timeline)
#     with open('timeline_tweets_only.json', 'w') as f:
#         for tweet in timeline:
#             x,y = tweet
#             f.write(f'{x}, {y}')
#             f.write('\n\n')

    source = Source(input_address)
    # tweet = source.readline()
    # bot.tweet(tweet)
    # source.removeline(tweet)
