import tweepy

class UserAuth:
    def __init__(self, ck, cs, ak, asc):
        self.__ck = ck
        self.__cs = cs
        self.__ak = ak
        self.__asc = asc
        self.auth = tweepy.OAuthHandler(self.__ck, self.__cs)

    def createAuth(self):
        return self.auth
    
    def setToken(self):
        return self.createAuth().set_access_token(self.__ak, self.__asc)


