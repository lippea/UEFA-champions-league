def pair(winners_from_group_stage):
  pairs = []
  # 8 groups
  for group in range(0, 8):
    team_a = winners_from_group_stage[group]['winner']
    if (group % 2 == 0):
      team_b = winners_from_group_stage[group+1]['runner-up']
    else:
      team_b = winners_from_group_stage[group-1]['runner-up']

    pairs.append({
      'team_a': team_a,
      'team_b': team_b,
      'a:b': [0, 0],
      'b:a': [0, 0]
    })

  return pairs