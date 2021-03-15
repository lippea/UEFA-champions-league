import initialise
import round_match

def process_phase(winners_from_group_stage):
  groups = initialise.pair(winners_from_group_stage)
  print(groups)

  proccessed_rounds = 0
  while len(groups) > 1 and proccessed_rounds < 3:
    winners = round_match.round_match(groups)
    print(winners)
    proccessed_rounds += 1
    

process_phase([{'winner': 'Sevilla', 'runner-up': 'Liverpool'}, {'winner': 'Man City', 'runner-up': 'Real Madrid'}, {'winner': 'Ajax', 'runner-up': 'İstanbul'}, {'winner': 'Chelsea', 'runner-up': 'Dynamo Kiev'}, {'winner': 'Juventus', 'runner-up': 'Dortmund'}, {'winner': 'Porto', 'runner-up': 'RB Salzburg'}, {'winner': 'Man United', 'runner-up': 'M. Gladbach'}, {'winner': 'Lokomotiv', 'runner-up': 'Lazio'}])