import initialise

def process_phase(winners_from_group_stage):
  initilised_groups = initialise.pair(winners_from_group_stage)
  print(initilised_groups)

process_phase([{'winner': 'Sevilla', 'runner-up': 'Liverpool'}, {'winner': 'Man City', 'runner-up': 'Real Madrid'}, {'winner': 'Ajax', 'runner-up': 'İstanbul'}, {'winner': 'Chelsea', 'runner-up': 'Dynamo Kiev'}, {'winner': 'Juventus', 'runner-up': 'Dortmund'}, {'winner': 'Porto', 'runner-up': 'RB Salzburg'}, {'winner': 'Man United', 'runner-up': 'M. Gladbach'}, {'winner': 'Lokomotiv', 'runner-up': 'Lazio'}])