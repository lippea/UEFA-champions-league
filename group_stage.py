import common

# 32 teams diviced into 8 groups
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

print('\n\033[1;34;40m{:^145}'.format('GROUP STAGE FINAL SCORES'))

def get_points(e):
  return e['points']
def print_result():
  for group in range(0, 8):
    group_name = 'GROUP ' + chr(65+group)
    print('\033[1;34;40m{:>17}'.format(f'{group_name}'), end="|")
    #sort by points desc
    group_teams = groups[group]
    group_teams.sort(key=get_points, reverse=True)
  print()

  for index in range(0, 4):
    for group in range(0,8):
      team_index = groups[group][index]['index']
      team_points = groups[group][index]['points']
      print('\033[0;37;40m{:>17}'.format(f'{common.TEAMS[team_index]}: {team_points}'), end="|")
    print()

  separators = ['|', '|', 'V']
  for char in separators:
    for group in range(0, 8):
      print('\033[0;37;40m{:>17}'.format(f'{char}    '), end=" ")
    print()

  # print qualified teams
  for group in range(0, 8):
    team_index = groups[group][0]['index']
    print('\033[0;37;40m{:>17}'.format(f'{common.TEAMS[team_index]}'), end=" ")
  print()
  for group in range(0, 8):
    team_index = groups[group][1]['index']
    print('\033[0;37;40m{:>17}'.format(f'{common.TEAMS[team_index]}'), end=" ")
  print()


def initial_grouping():
  #8 groups
  for group in range(0, 8):
    #4 teams in a group
    grouping = []
    for team in range(0, 4):
      grouping.append(({'index': group*4+team, 'points': 0}))
      # grouping.append((group*4)+(team)
    
    groups.append(grouping)

def get_qualified_teams():
  qualified_teams = []
  for group in range(0, 8):
    qualified_teams.append({
      'winner': groups[group][0]['index'],
      'runner-up': groups[group][1]['index']
    })

  return qualified_teams

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

  print_result()
  
  qualified_teams = get_qualified_teams()
  return qualified_teams
