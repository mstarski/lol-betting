from audioop import mul
import mwclient
import json

from LeagueOfElo import runMultiRegion

def getWinMultiplier(elo1, elo2):
    diff = abs(elo1 - elo2)
    multiplier = diff * 0.02

    base = elo1 / elo2

    if elo1 > elo2:
        return base + 0.1
    else: 
        return base * multiplier

def get_schedule_with_rating(region, startDate, endDate, league):
    # site = mwclient.Site('lol.fandom.com', path='/')

    # response = site.api('cargoquery',
    #     tables = 'MatchSchedule=MS',
    #     fields = 'MS.Team1, MS.Team2, MS.DateTime_UTC, MS.OverviewPage',
    #     limit = 1,
    #     where = f"MS.DateTime_UTC >= '{startDate}' AND MS.DateTime_UTC <= '{endDate}' AND MS.OverviewPage LIKE '%{league}%'"
    # )

    # print(json.dumps(response['cargoquery'])) => schedule_file

    with open("src/mock/sample-schedule.json") as schedule_file, open("src/mock/sample-rating.json") as rating_file:
        result = []

        schedule = json.load(schedule_file)
        rating = json.load(rating_file)

        for match in schedule:
            data = {}

            details = match['title']

            team1Name = details['Team1']
            team2Name = details['Team2']

            team1Elo = rating[team1Name]['rating']
            team2Elo = rating[team2Name]['rating']

            data = {
                'date': details['DateTime UTC'],
                'event': details['OverviewPage'],

                'team1': {
                    'name': team1Name,
                    'abbrev': rating[team1Name]['abbrev'],
                    'winMultiplier': getWinMultiplier(team1Elo, team2Elo),
                    'elo': team1Elo
                },
                'team2': {
                    'name': team2Name,
                    'abbrev': rating[team2Name]['abbrev'],
                    'winMultiplier': getWinMultiplier(team2Elo, team1Elo),
                    'elo': team2Elo
                }
            }

            result.append(data)

    # print(runMultiRegion('EU'))
    return result

