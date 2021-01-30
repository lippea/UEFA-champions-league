import random

# all teams entering the competetion
TEAMS = ('Bayern Müchen', 'Atletico de Madrid', 'Red Bull Salzburg', 'Lokomotiv Moscow', 'Real Madrid', 'Mönchengladbach', 'Shakhtar Donetsk', 'Inter Milan', 'Manchester City', 'Porto', 'Olympiacos', 'Marseille', 'Liverpool', 'Atalanta', 'Ajax', 'Midtjylland', 'Chelsea', 'Sevilla', 'Krasnodar', 'Rennes', 'Dortmund', 'Lazio', 'Club Brugge', 'Zenit St.Petersburg', 'Juventus', 'Barcelona', 'Dynamo Kiev', 'Ferencváros', 'Paris Saint Germain', 'RB Leipzig', 'Manchester United', 'İstanbul Başakşehir F.K.')

# single scores board for a team in a match
SCORE_CHOICES = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 8)
def get_score():
  return random.choice(SCORE_CHOICES)

# history match results
results = []
def add_results(home_index, home_score, away_index, away_score):
  results.append((home_index, home_score, away_index, away_score))
