TOP_32_TEAMS = ('Bayern', 'Atleti', 'RB Salzburg', 'Lokomotiv', 'Real Madrid', 'M. Gladbach', 'Shakhtar', 'Inter Milan', 'Man City', 'Porto', 'Olympiacos', 'Marseille', 'Liverpool', 'Atalanta', 'Ajax', 'Midtjylland', 'Chelsea', 'Sevilla', 'Krasnodar', 'Rennes', 'Dortmund', 'Lazio', 'Club Brugge', 'Zenit', 'Juventus', 'Barcelona', 'Dynamo Kiev', 'Ferencváros', 'Paris SG', 'RB Leipzig', 'Man United', 'İstanbul')

import initialise
import match
import sort
import output

def process_stage(top_32_teams):
  initilised_groups = initialise.random_group(top_32_teams)
  print(initilised_groups)

  groups_with_points = match.round_robin(initilised_groups)
  print(groups_with_points)

  groups_with_points_desc = sort.sort_by_points_desc(groups_with_points)
  print(groups_with_points_desc)

  output.print_result(groups_with_points_desc)

process_stage(TOP_32_TEAMS)