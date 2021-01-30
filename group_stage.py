import common

print("\033[1;34;40mUEFA CHAMPIONS LEAGUE\033[1;37;40m\n\n")

# 32 teams diviced into 8 groups
# groups = (
#   range(0,4), range(4,8), range(8,12), range(12,16),
#   range(16,20), range(20,24), range(24,28), range(28,32)
# )
groups = []


# calculate points after a match
def calculate_points(home_team, home_score, away_team, away_score):
  if (home_score == away_score):
    home_team['points'] += 1
    away_team['points'] += 1
  elif (home_score > away_score):
    home_team['points'] += 3
  else:
    away_team['points'] += 3

def match(home_team, away_team):
  # get scores for two teams
  home_score = common.get_score()
  away_score = common.get_score()

  # add to history
  common.add_results(home_team['index'], home_score, away_team['index'], away_score)

  # add points
  calculate_points(home_team, home_score, away_team, away_score)

def get_points(e):
  return e['points']
def print_points():
  for group in range(0,8):
    print(f'\ngroup_{chr(97+group)}')
    group_teams = groups[group]
    #sort by points desc
    group_teams.sort(key=get_points, reverse=True)
    
    for team in range(0,4):
      team_index = group_teams[team]['index']
      team_points = group_teams[team]['points']
      print('{:>30}'.format(f'{common.TEAMS[team_index]} {team_points}'), end="")

  print('\n')

def initial_grouping():
  #8 groups
  for group in range(0, 8):
    #4 teams in a group
    grouping = []
    for team in range(0, 4):
      grouping.append(({'index': group*4+team, 'points': 0}))
      # grouping.append((group*4)+(team)
    
    groups.append(grouping)

def group_stage():
  initial_grouping()

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

  print_points()