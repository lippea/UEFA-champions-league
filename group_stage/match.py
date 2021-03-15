import sys
sys.path.append('..')
import common

def calculate_points(home_team, home_score, away_team, away_score):
  if (home_score == away_score):
    home_team['points'] += 1
    away_team['points'] += 1
  elif (home_score > away_score):
    home_team['points'] += 3
  else:
    away_team['points'] += 3

def match(home_team, away_team):
  scores = common.ninety_mins_match()
  home_score = scores[0]
  away_score = scores[1]

  # add to history
  common.add_results(home_team['team'], home_score, away_team['team'], away_score)

  # add points
  calculate_points(home_team, home_score, away_team, away_score)

def round_robin(groups):
  round1_arragement = ((0, 1), (2, 0), (0, 3), (1, 2) ,(1, 3), (2, 3))
  round2_arragement = ((3, 2), (3, 1), (1, 2), (3, 0) ,(2, 0), (0, 1))

  for day in range(0,6):
    for group in range(0,8):
      group_teams = groups[group]
      home_team = group_teams[round1_arragement[day][0]]
      away_team = group_teams[round1_arragement[day][1]]
      match(home_team, away_team)

      home_team = group_teams[round2_arragement[day][0]]
      away_team = group_teams[round2_arragement[day][1]]
      match(home_team, away_team)

  return groups