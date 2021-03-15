import initialise
import round_match
import round_print
import round_repair

def process_phase(winners_from_group_stage):
  pairs = initialise.pair(winners_from_group_stage)

  proccessed_rounds = 0
  while len(pairs) > 1:
    winners = round_match.round_match(pairs)

    round_print.round_print(pairs)

    pairs = round_repair.repair(winners)
    proccessed_rounds += 1
    
    

process_phase([{'winner': 'Sevilla', 'runner-up': 'Liverpool'}, {'winner': 'Man City', 'runner-up': 'Real Madrid'}, {'winner': 'Ajax', 'runner-up': 'İstanbul'}, {'winner': 'Chelsea', 'runner-up': 'Dynamo Kiev'}, {'winner': 'Juventus', 'runner-up': 'Dortmund'}, {'winner': 'Porto', 'runner-up': 'RB Salzburg'}, {'winner': 'Man United', 'runner-up': 'M. Gladbach'}, {'winner': 'Lokomotiv', 'runner-up': 'Lazio'}])