maze=tinyMaze
pacman=GoWestAgent
speed=0.2
layout=tinyMaze
quiz=1


playPacman:
	@python pacman.py --frameTime $(speed)

GoWestAgent:
	@python pacman.py --layout $(layout) --pacman $(pacman)

autogradeAllQuestions:
	@python autograder.py

autograde:
	@python autograder.py -q q$(quiz)


typesOfMaize:
	@echo tinyMaze
	@echo testMaze