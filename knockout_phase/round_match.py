import sys
sys.path.append('..')
import common

def round_match(pairs):
  winners = []
  for pair in pairs:
    first_match_scores = common.ninety_mins_match()
    pair['a:b'] = first_match_scores

    # add to history
    common.add_results(pair['team_a'], first_match_scores[0], pair['team_b'], first_match_scores[1])

    second_match_scores = common.ninety_mins_match()
    team_a_score = first_match_scores[0] + second_match_scores[1]
    team_b_score = first_match_scores[1] + second_match_scores[0]

    # decide winner
    overtime_match_scores = [0, 0]
    if (team_a_score > team_b_score):
      winners.append(pair['team_a'])
    elif (team_b_score > team_a_score):
      winners.append(pair['team_b'])
    elif (second_match_scores[1] > first_match_scores[0]):
      winners.append(pair['team_a'])
    elif (first_match_scores[1] > second_match_scores[0]):
      winners.append(pair['team_b'])
    else:
      overtime_match_scores = common.overtime_match()
      if (overtime_match_scores[0] > overtime_match_scores[1]):
        winners.append(pair['team_b'])
      else:
        winners.append(pair['team_a'])
    
    second_match_final_scores = [second_match_scores[0]+overtime_match_scores[0], second_match_scores[1]+overtime_match_scores[1]]
    pair['b:a'] = second_match_final_scores

    # add to history
    common.add_results(pair['team_b'], second_match_final_scores[0], pair['team_a'], second_match_final_scores[1])

  return winners