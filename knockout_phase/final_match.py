import sys
sys.path.append('..')
import common

def final_match(pair):
  winner = ''

  ninety_mins_match_scores = common.ninety_mins_match()
  team_a_score = ninety_mins_match_scores[0]
  team_b_score = ninety_mins_match_scores[1]

  # decide winner
  overtime_match_scores = [0, 0]
  if (team_a_score > team_b_score):
    winner = pair['team_a']
  elif (team_b_score > team_a_score):
    winner = pair['team_b']
  else:
    overtime_match_scores = common.overtime_match()
    if (overtime_match_scores[0] > overtime_match_scores[1]):
      winner = pair['team_a']
    else:
      winner = pair['team_b']
  
  final_scores = [ninety_mins_match_scores[0]+overtime_match_scores[0], ninety_mins_match_scores[1]+overtime_match_scores[1]]
  pair['a:b'] = final_scores

  # add to history
  common.add_results(pair['team_a'], final_scores[0], pair['team_b'], final_scores[1])

  return winner