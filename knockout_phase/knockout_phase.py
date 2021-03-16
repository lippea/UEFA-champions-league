import initial_pair
import round_match
import round_print
import round_repair
import final_match
import final_print

def process_phase(winners_from_group_stage):
  print('\n\033[1;34;40m{:^145}'.format('KNOCKOUT PHASE'))
  pairs = initial_pair.pair(winners_from_group_stage)

  proccessed_rounds = 0
  while len(pairs) > 1:
    winners = round_match.round_match(pairs)

    round_print.round_print(pairs, proccessed_rounds)

    pairs = round_repair.repair(winners)
    proccessed_rounds += 1

  champain = final_match.final_match(pairs[0])
  final_print.final_print(pairs[0], champain)
    
    
# test knockout_phase individually
# process_phase([{'winner': 'Sevilla', 'runner-up': 'Liverpool'}, {'winner': 'Man City', 'runner-up': 'Real Madrid'}, {'winner': 'Ajax', 'runner-up': 'İstanbul'}, {'winner': 'Chelsea', 'runner-up': 'Dynamo Kiev'}, {'winner': 'Juventus', 'runner-up': 'Dortmund'}, {'winner': 'Porto', 'runner-up': 'RB Salzburg'}, {'winner': 'Man United', 'runner-up': 'M. Gladbach'}, {'winner': 'Lokomotiv', 'runner-up': 'Lazio'}])