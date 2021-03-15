import initialise
import round_match
import round_repair

def process_phase(winners_from_group_stage):
  pairs = initialise.pair(winners_from_group_stage)

  while len(pairs) > 1:
    winners = round_match.round_match(pairs)
    print(winners)

    pairs = round_repair.repair(winners)
    print(pairs)
    

process_phase([{'winner': 'Sevilla', 'runner-up': 'Liverpool'}, {'winner': 'Man City', 'runner-up': 'Real Madrid'}, {'winner': 'Ajax', 'runner-up': 'İstanbul'}, {'winner': 'Chelsea', 'runner-up': 'Dynamo Kiev'}, {'winner': 'Juventus', 'runner-up': 'Dortmund'}, {'winner': 'Porto', 'runner-up': 'RB Salzburg'}, {'winner': 'Man United', 'runner-up': 'M. Gladbach'}, {'winner': 'Lokomotiv', 'runner-up': 'Lazio'}])