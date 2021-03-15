def round_print(pairs, round):
  print_str = '\033[0;37;40m{:>17}'
  if round == 1:
    print_str = '\033[0;37;40m{:^36}'
  elif round == 2:
    print_str = '\033[0;37;40m{:^72}'

  for pair in pairs:
    print(print_str.format(f'{pair["team_a"]} ({pair["a:b"][0]}:{pair["a:b"][1]})'), end=" ")

  print()

  for pair in pairs:
    print(print_str.format(f'{pair["team_b"]} ({pair["b:a"][0]}:{pair["b:a"][1]})'), end=" ")

  print()