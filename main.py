import mwclient
import json
from LeagueOfElo import runMultiRegion

# site = mwclient.Site('lol.fandom.com', path='/')

# response = site.api('cargoquery',
#     tables = 'MatchSchedule=MS',
#     fields = 'MS.Team1, MS.Team2, MS.DateTime_UTC, MS.OverviewPage',
#     limit = 10,
#     where = "MS.DateTime_UTC >= '2022-02-19 00:00:00' AND MS.DateTime_UTC <= '2022-02-20 00:00:00' AND MS.OverviewPage LIKE '%LEC%'"
# )

# query = response["cargoquery"][0]

# print(query)

with open("sample-result.json") as file:
    data = json.load(file)


for match in data:
    data = match['title']

print(runMultiRegion('EU'))





