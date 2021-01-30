import random

# all teams entering the competetion
TEAMS = ('Bayern', 'Atleti', 'RB Salzburg', 'Lokomotiv', 'Real Madrid', 'M. Gladbach', 'Shakhtar', 'Inter Milan', 'Man City', 'Porto', 'Olympiacos', 'Marseille', 'Liverpool', 'Atalanta', 'Ajax', 'Midtjylland', 'Chelsea', 'Sevilla', 'Krasnodar', 'Rennes', 'Dortmund', 'Lazio', 'Club Brugge', 'Zenit', 'Juventus', 'Barcelona', 'Dynamo Kiev', 'Ferencváros', 'Paris SG', 'RB Leipzig', 'Man United', 'İstanbul')

# single scores board for a team in a match
SCORE_CHOICES = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 8)
def get_score():
  return random.choice(SCORE_CHOICES)

# history match results
results = []
def add_results(home_index, home_score, away_index, away_score):
  results.append((home_index, home_score, away_index, away_score))
