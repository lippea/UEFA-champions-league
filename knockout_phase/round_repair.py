def repair(winners):
  pairs = []

  for group in range(0, len(winners)//2):
    team_a = winners[group*2]
    team_b = winners[group*2+1]

    pairs.append({
      'team_a': team_a,
      'team_b': team_b,
      'a:b': [0, 0],
      'b:a': [0, 0],
    })

  return pairs