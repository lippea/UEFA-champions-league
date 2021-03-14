TOP_32_TEAMS = ('Bayern', 'Atleti', 'RB Salzburg', 'Lokomotiv', 'Real Madrid', 'M. Gladbach', 'Shakhtar', 'Inter Milan', 'Man City', 'Porto', 'Olympiacos', 'Marseille', 'Liverpool', 'Atalanta', 'Ajax', 'Midtjylland', 'Chelsea', 'Sevilla', 'Krasnodar', 'Rennes', 'Dortmund', 'Lazio', 'Club Brugge', 'Zenit', 'Juventus', 'Barcelona', 'Dynamo Kiev', 'Ferencváros', 'Paris SG', 'RB Leipzig', 'Man United', 'İstanbul')

import initialise

def process_stage(top_32_teams):
  initilised_groups = initialise.random_group(top_32_teams)
  print(initilised_groups)

process_stage(TOP_32_TEAMS)