import pgsheets
from pgsheets import Token, Client

my_client_id = '41450492988-tkq79hqc6flqcq156vircgu63uiojbl8.apps.googleusercontent.com'
my_client_secret = '7yz-_NWzycTvEv-YTHM1vBJZ'
c = Client(my_client_id, my_client_secret)
c.getOauthUrl()