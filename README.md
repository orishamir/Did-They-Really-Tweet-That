# Did-They-Really-Tweet-That
 Have you ever seen a meme or post, that had a tweet in them
 and wondered:" This has got to be fake. no way" but did not have the time and energy to check?
 This program does it for you.

## Usage: python didtheyreally.py <username> [word1 word2 word3 ...]
 Note: you need to change in the code (line 20):
```py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)     
auth.set_access_token(access_token, access_token_secret)
```
To your own Tweeter API info.
 
### Example:
###     python didtheyreally.py elonmusk if life is video graphics confusing long
Returns:
 https://twitter.com/elonmusk/status/1205030950750412800?lang=en
