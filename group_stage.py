import common

print("\033[1;34;40mUEFA CHAMPIONS LEAGUE\033[1;37;40m\n\n")

# points in group stage for each team
points = [
  0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,
  0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0
]

# 32 teams diviced into 8 groups
groups = (
  range(0,4), range(4,8), range(8,12), range(12,16),
  range(16,20), range(20,24), range(24,28), range(28,32)
)

# calculate points after a match
def calculate_points(home_index, home_score, away_index, away_score):
  if (home_score == away_score):
    points[home_index] += 1
    points[away_index] += 1
  elif (home_score > away_score):
    points[home_index] += 3
  else:
    points[away_index] += 3

def match(home_index, away_index):
  # get scores for two teams
  home_score = common.get_score()
  away_score = common.get_score()

  # add to history
  common.add_results(home_index, home_score, away_index, away_score)

  # add points
  calculate_points(home_index, home_score, away_index, away_score)

def print_points():
  for group in range(0,8):
    print(f'\ngroup_{chr(97+group)}', end="")
    group_teams = groups[group]
    
    for team in range(0,4):
      print('{:>30}'.format(f'{common.TEAMS[group_teams[team]]} {points[group_teams[team]]}'), end="")

  print('\n')

def group_stage():
  round1_arragement = ((0, 1), (2, 0), (0, 3), (1, 2) ,(1, 3), (2, 3))
  round2_arragement = ((3, 2), (3, 1), (1, 2), (3, 0) ,(2, 0), (0, 1))

  for day in range(0,6):
    for group in range(0,8):
      group_teams = groups[group]
      home_index = group_teams[round1_arragement[day][0]]
      away_index = group_teams[round1_arragement[day][1]]
      match(home_index, away_index)

      home_index = group_teams[round2_arragement[day][0]]
      away_index = group_teams[round2_arragement[day][1]]
      match(home_index, away_index)

  print_points()