def get_points(e):
  return e['points']
def sort_by_points_desc(groups_with_points):
  for group in range(0, 8):
    #sort by points desc
    group_teams = groups_with_points[group]
    group_teams.sort(key=get_points, reverse=True)
  
  return groups_with_points