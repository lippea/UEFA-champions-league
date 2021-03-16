import random

# history match results
results = []
def add_results(home_team, home_score, away_team, away_score):
  results.append((home_team, home_score, away_team, away_score))

######
# single scores board for a team in a match
SCORE_CHOICES = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 8)
def get_score():
  return random.choice(SCORE_CHOICES)

def ninety_mins_match():
  # get scores for two teams
  home_score = get_score()
  away_score = get_score()

  return [home_score, away_score]

def overtime_match():
  # get scores for two teams
  home_score = get_score()
  away_score = get_score()

  # need a winner
  while (home_score == away_score):
    home_score = get_score()
    away_score = get_score()
  
  return [home_score, away_score]
