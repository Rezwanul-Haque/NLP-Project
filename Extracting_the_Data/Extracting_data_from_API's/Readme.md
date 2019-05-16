Step 1 Log in to the Twitter developer portal

Create your own app in the Twitter developer portal, and get the keys
mentioned below. Once you have these credentials, you can start pulling
data. Keys needed:
    • consumer key: Key associated with the application
    (Twitter, Facebook, etc.).
    • consumer secret: Password used to authenticate with
    the authentication server (Twitter, Facebook, etc.).
    • access token: Key given to the client after successful
    authentication of above keys.
    • access token secret: Password for the access key.

Step 2 Execute below query in Python
    • For accessing tweeter api we need tweepy libaray from pypi
        • pip install tweepy

    • Create a credentials.py file which will contains the secret keys of the developer portal