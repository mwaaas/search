maze=tinyMaze
pacman=SearchAgent
speed=0.2
layout=mediumMaze
quiz=1
fn=tinyMazeSearch
zoom=1.0
comma = ,


playPacman:
	@python pacman.py --frameTime $(speed)

GoWestAgent:
	@python pacman.py --layout $(layout) --pacman SearchAgent

autogradeAllQuestions:
	@python autograder.py

autograde:
	@python autograder.py -q q$(quiz)

playAgent:
	@python pacman.py --layout $(layout) -z $(zoom) --pacman $(pacman)  -a fn=$(fn),heuristic=manhattanHeuristic

typesOfMaize:
	@echo tinyMaze
	@echo testMaze
	@echo mediumMaze

typesOf_fn:
	@echo bfs
	@echo dfs
	@echo ucs
	@echo astar

help: typesOf_fn  typesOfMaize