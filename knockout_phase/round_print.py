def round_print(pairs, winners, round_number):
  print_str = '\033[0;37;40m{:^17}'
  if round_number == 1:
    print_str = '\033[0;37;40m{:^36}'
  elif round_number == 2:
    print_str = '\033[0;37;40m{:^72}'

  # print pairs and scores
  for pair in pairs:
    print(print_str.format(f'{pair["team_a"]} ({pair["a:b"][0]}:{pair["a:b"][1]})'), end=" ")
  print()
  for pair in pairs:
    print(print_str.format(f'{pair["team_b"]} ({pair["b:a"][0]}:{pair["b:a"][1]})'), end=" ")
  print()

  # print winners
  for winner in winners:
    print(print_str.format(f'|'), end=" ")
  print()
  for winner in winners:
    print(print_str.format(f'V'), end=" ")
  print()
  for winner in winners:
    print(print_str.format(f'{winner}'), end=" ")
  print()

  # print separators  
  for j in range(0, (round_number+1)*2):
    space = ' ' * j * 10
    for i in range(0, len(pairs)//2):
      print(print_str.format(f'{space}\\'), end=" ")
      print(print_str.format(f'/{space}'), end=" ")
    print()
