def round_print(pairs):
  for pair in pairs:
    print('\033[0;37;40m{:>17}'.format(f'{pair["team_a"]} ({pair["a:b"][0]}:{pair["a:b"][1]})'), end=" ")

  print()

  for pair in pairs:
    print('\033[0;37;40m{:>17}'.format(f'{pair["team_b"]} ({pair["b:a"][0]}:{pair["b:a"][1]})'), end=" ")

  print()