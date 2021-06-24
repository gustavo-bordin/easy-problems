COMPETITIONS = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]

RESULTS = [0, 0, 1]

# SOLUTION 1 -------------------------------------------------------------------

def tournamentWinner(competitions, results):
	map_ = {}
	
	for index, team in enumerate(competitions):
		winner = team[1 if results[index] == 0 else 0]
		
		if winner not in map_:
			map_[winner] = 0
			
		map_[winner] += 3
	
	highest_value = -1
	highest_name = 0
	for k,v in map_.items():
		if v > highest_value:
			highest_value = v
			highest_name = k
	
	return highest_name

answer = tournamentWinner(competitions=COMPETITIONS, results=RESULTS)
print(f"First solution's answer: {answer}")

# SOLUTION 2 -------------------------------------------------------------------

def tournamentWinner(competitions, results):
	map_ = {'winning': {'score': 0, 'name': None}}
	
	def add_points(winner):
		if winner not in map_:
			map_[winner] = 0
		
		map_[winner] += 3
		
	def update_best_team(winner):
		if map_[winner] > map_['winning']['score']:
			map_['winning']['score'] = map_[winner]
			map_['winning']['name'] = winner
	
	for index, team in enumerate(competitions):
		winner = team[1 if results[index] == 0 else 0]
		add_points(winner)
		update_best_team(winner)
		
	return map_['winning']['name']

answer = tournamentWinner(competitions=COMPETITIONS, results=RESULTS)
print(f"Second solution's answer: {answer}")