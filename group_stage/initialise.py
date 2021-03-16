import random

def random_group(top_32_teams):
  teams = list(top_32_teams)
  groups = []
  # 8 groups
  for group in range(0, 8):
    # 4 teams in a group
    grouping = []
    for team in range(0, 4):
      random_team = teams.pop(random.randrange(len(teams))) 
      grouping.append(({'team': random_team, 'points': 0}))
    
    groups.append(grouping)

  return groups
