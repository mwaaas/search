maze=tinyMaze
pacman=SearchAgent
speed=0.2
layout=tinyMaze
quiz=1
fn=tinyMazeSearch



playPacman:
	@python pacman.py --frameTime $(speed)

GoWestAgent:
	@python pacman.py --layout $(layout) --pacman SearchAgent

autogradeAllQuestions:
	@python autograder.py

autograde:
	@python autograder.py -q q$(quiz)

playAgent:
	@python pacman.py --layout $(layout) --pacman $(pacman)  -a fn=$(fn)

typesOfMaize:
	@echo tinyMaze
	@echo testMaze
	@echo mediumMaze