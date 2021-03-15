def get_next_phase_teams(groups_with_points_desc):
  next_phase_teams = []
  for group in range(0, 8):
    next_phase_teams.append({
      'winner': groups_with_points_desc[group][0]['team'],
      'runner-up': groups_with_points_desc[group][1]['team']
    })

  return next_phase_teams