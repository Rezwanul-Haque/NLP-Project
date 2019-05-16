# credentials
consumer_key = "adjbiejfaaoeh"
consumer_secret = "had73haf78af"

# API access token and secret key
access_token = "jnsfby5u4yuawhafjeh"
access_token_secret = "jhdfgay768476r"

class Authenticate:
    def __init__:
        _consumer_key = ""
        _consumer_secret = ""

        # API access token and secret key
        _access_token = ""
        _access_token_secret = ""
    
    def set_consumer_token(consumer_key:str, consumer_secret:str):
        """[These function will set the consumer key and secret key]
        
        Arguments:
            consumer_key {[str]} -- [consumers key]
            consumer_secret {[str]} -- [consuers secret key]
        """
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
    
    def set_consumer_access_token(access_token:str, access_token_secret:str):
        """[Consumers access token and secret for accessing the API]
        
        Arguments:
            access_token {[str]} -- [Consumers API access token]
            access_token_secret {[str]} -- [Consumers API access token secret]
        """
        self._access_token = access_token
        self._access_token_secret = access_token_secret
    
    def authenticate():
        """For twitter authenticate
        """
        import tweepy
        from tweepy import OAuthHandler

        auth = OAuthHandler(this._consumer_key, this._consumer_secret)
        auth.set_access_token(this._access_token, this._access_token_secret)

        return auth

