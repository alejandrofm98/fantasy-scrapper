import requests
from dotenv import load_dotenv
import os

payload = {}


class scrapper:

  def __init__(self):
    load_dotenv()
    self.headers = None
    self.username = os.getenv('USERNAME')
    self.password = os.getenv('PASSWORD')
    self.client_id = os.getenv('CLIENT_ID')
    self.login_url = "https://login.laliga.es/laligadspprob2c.onmicrosoft.com/oauth2/v2.0/token?p=B2C_1A_ResourceOwnerv2"
    self.base_url = 'https://api-fantasy.llt-services.com/api/'

  def __call_api(self, url, authorization=True):
    final_url = self.base_url + url
    headers = self.headers
    if not authorization:
      headers={}
    response = requests.request("GET", final_url, headers=headers, data=payload)
    if response.status_code != 200:
      print('Failed to call api')
    return response.json()

  def login(self):

    payload_login = {'grant_type': 'password',
                     'client_id': self.client_id,
                     'scope': 'openid ' + self.client_id + ' offline_access',
                     'redirect_url': 'authredirect://com.lfp.laligafantasy',
                     'username': self.username,
                     'password': self.password,
                     'response_type': 'id_token'}

    response = requests.request("POST", self.login_url, headers={},
                                data=payload_login,
                                files={})
    if response.status_code != 200:
      print('Failed to login')
    self.headers = {
      'Authorization': 'Bearer ' + response.json().get('access_token')
    }

  def get_leagues(self):
    leagues_url = 'v4/leagues?x-lang=es'
    return self.__call_api(leagues_url)

  def get_team_players(self, league_id, team_id):
    team_url = 'v3/leagues/' + league_id + '/teams/' + team_id + '?x-lang=es'
    return self.__call_api(team_url)

  def get_all_players(self):
    all_players_url = 'v3/players'
    return self.__call_api(all_players_url)

  def get_ranking(self, league_id):
    ranking_url = 'v5/leagues/'+league_id+'/ranking?x-lang=es'
    return self.__call_api(ranking_url)

  def get_news(self, league_id):
    news_url = 'v3/leagues/'+league_id+'/news/1?x-lang=es'
    return self.__call_api(news_url)

  def get_market(self, league_id):
    market_url = '3/league/'+league_id+'/market?x-lang=es'
    return self.__call_api(market_url)


