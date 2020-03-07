import tweepy
import argparse

parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-h', "--help", action='help', default=argparse.SUPPRESS,
help="""
usage:
    python didtheyreally.py <username> <word1 word2 word3....>

    Example:
        python didtheyreally.py realDonaldTrump This what future State palestine can with of East Jerusalem.""")

parser.add_argument("username", help="Owner of the tweet to check")
parser.add_argument("-sens", "-s", default=False, action='store_true', help="Are the words case sensitive")
parser.add_argument("words", help="List of words that must be included in the tweet", nargs="+")

args = parser.parse_args()

# Put tweeter API data here
auth = tweepy.OAuthHandler("redacted", "redacted")
auth.set_access_token("redacted", "redacted")

def get_all_tweets(screen_name):
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, tweet_mode="extended")
    for twt in new_tweets:
        yield twt

    oldest = twt.id - 1
    while len(new_tweets) > 0:
        # Get 200 tweets every time
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest, tweet_mode="extended")
        for twt in new_tweets:
            yield twt
        oldest = twt.id - 1

def does_it_exist(usrname, must_includes, case_sensi=False):
    # Go through all tweets
    for twt in get_all_tweets(usrname):
        gotit = True
        # get text from tweet
        text = twt.full_text

        # Iterate over all the given words 
        for inc in must_includes:
            # If the search is case sensitive, search the word EXACTLY as it is
            # else, just lowercase it 
            if case_sensi:
                if inc not in text:
                    gotit = False
                    break
            else:
                if inc.lower() not in text.lower():
                    gotit = False
                    break
        if gotit:
            print(text, '\n>>URL>>', f"\nhttps://twitter.com/{twt.user.screen_name}/status/{twt.id}", '\n\n')

api = tweepy.API(auth, wait_on_rate_limit_notify=True)
print('Gotten username:', args.username)
print('Words:', args.words)
print("\n\n")
does_it_exist(usrname=args.username, must_includes=args.words, case_sensi=args.sens)