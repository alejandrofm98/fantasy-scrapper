import scrapper
if __name__ == '__main__':
  scrapper = scrapper.scrapper()
  scrapper.login()
  leagues = scrapper.get_leagues()
  for league in leagues:
    print(league['name'])
    print(league['id'])
    print(league['token'])
    print(league['managersNumber'])
