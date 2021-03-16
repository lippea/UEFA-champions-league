def final_print(pair, champain):
  print_str = '\033[0;37;40m{:^144}'

  print(print_str.format(f'{pair["team_a"]} {pair["a:b"][0]}:{pair["a:b"][1]} {pair["team_b"]}'), end=" ")
  print()

  print(print_str.format(f'|'), end=" ")
  print()
  print(print_str.format(f'|'), end=" ")
  print()
  print(print_str.format(f'V'), end=" ")
  print()
  print(print_str.format(f'{champain}'), end=" ")
  print()