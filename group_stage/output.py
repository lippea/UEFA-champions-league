def print_result(groups_with_points_desc):
  print('\n\033[1;34;40m{:^145}'.format('GROUP STAGE FINAL SCORES'))
  # print group names
  for group in range(0, 8):
    group_name = 'GROUP ' + chr(65+group)
    print('\033[1;34;40m{:>17}'.format(f'{group_name}'), end="|")
  print()

  # print all points
  for rank in range(0, 4):
    for group in range(0,8):
      team = groups_with_points_desc[group][rank]['team']
      team_points = groups_with_points_desc[group][rank]['points']
      print('\033[0;37;40m{:>17}'.format(f'{team}: {team_points}'), end="|")
    print()

  # print separators between all points and qualified teams
  separators = ['|', '|', 'V']
  for char in separators:
    for group in range(0, 8):
      print('\033[0;37;40m{:>17}'.format(f'{char}    '), end=" ")
    print()

  # print winners and runners-up
  for group in range(0, 8):
    winner = groups_with_points_desc[group][0]['team']
    print('\033[0;37;40m{:>17}'.format(f'{winner}'), end=" ")
  print()
  for group in range(0, 8):
    runner_up = groups_with_points_desc[group][1]['team']
    print('\033[0;37;40m{:>17}'.format(f'{runner_up}'), end=" ")
  print()
