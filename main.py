TOP_32_TEAMS = ('Bayern', 'Atleti', 'RB Salzburg', 'Lokomotiv', 'Real Madrid', 'M. Gladbach', 'Shakhtar', 'Inter Milan', 'Man City', 'Porto', 'Olympiacos', 'Marseille', 'Liverpool', 'Atalanta', 'Ajax', 'Midtjylland', 'Chelsea', 'Sevilla', 'Krasnodar', 'Rennes', 'Dortmund', 'Lazio', 'Club Brugge', 'Zenit', 'Juventus', 'Barcelona', 'Dynamo Kiev', 'Ferencváros', 'Paris SG', 'RB Leipzig', 'Man United', 'İstanbul')

print('\033[1;34;40m{:^145}'.format('UEFA CHAMPIONS LEAGUE'))

import sys
sys.path.append('./group_stage')
import group_stage
next_phase_teams_by_group = group_stage.process_stage(TOP_32_TEAMS)

import sys
sys.path.append('./knockout_phase')
import knockout_phase
knockout_phase.process_phase(next_phase_teams_by_group)
