import common

def initial_grouping(qualified_teams):
  groups = []
  for index in range(0, 4):
    groups.append([{'index': qualified_teams[index*2]['winner'], 'scores': 0},
      {'index': qualified_teams[index*2+1]['runner-up'], 'scores': 0}])
    groups.append([{'index': qualified_teams[index*2+1]['winner'], 'scores': 0},
      {'index': qualified_teams[index*2]['runner-up'], 'scores': 0}])
  
  return groups

def match(home_team, away_team):
  # get scores for two teams
  home_score = common.get_score()
  away_score = common.get_score()
  # add to scores
  home_team['scores'] += home_score
  away_team['scores'] += away_score

  # add to history
  common.add_results(home_team['index'], home_score, away_team['index'], away_score)
  
def knockout_phase(qualified_teams):
  print(qualified_teams)
  groups = initial_grouping(qualified_teams)

  print('groups')
  print(groups)
  for group in groups:
    match(group[0], group[1])
    match(group[1], group[0])
    print(group)