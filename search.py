# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()

    #fifo to track state and path
    lifo = util.Stack()

    #create the first node it has no path so far
    node = Node(start_state, [])

    expanded_states = set()

    lifo.push(node)

    while not lifo.isEmpty():
        node_state = lifo.pop()

        #if the state is the goal state return the path
        if problem.isGoalState(node_state.state):
            path = node_state.get_path()
            return path

        elif node_state.state not in expanded_states:
            expanded_states.add(node_state.state)
            successors = problem.getSuccessors(node_state.state)
            for successor in successors:
                lifo.push(Node(successor[0], node_state.addPath(successor[1])))
    return []

class Node(object):
        """
        stores current state
        and the path used to reach that state

        """
        def __init__(self, state, path, cost=0):

            self.state = state
            self.path = path
            self.cost = cost

        def get_path(self):
            """
             :return :list which is the path
                      used to reach a certain path
            """
            if not self.path:
                return []
            return self.path

        def addPath(self, action):
            if not self.path:
                return [action]
            p = self.path[:]
            p.append(action)
            return p

        def get_state(self):
            """
            :return string -> state
            """
            return self.state

        def addCost(self, cost):
            return self.cost + cost


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    #the initial position of the pacman
    start_state = problem.getStartState()

    #breath first search uses first in first out queue
    #to transverse a tre
    fifo = util.Queue()

    #this keeps track of node that have been expanded
    expanded_sets  = set()

    #push/add the first node to the queue
    fifo.push(Node(start_state, []))

    while not fifo.isEmpty():
        node = fifo.pop()

        #if a state is the goal state then return the path
        if problem.isGoalState(node.get_state()):
            return node.get_path()

        # don't expand state twice
        if node.get_state() not in expanded_sets:
            expanded_sets.add(node.get_state())

            #expand state
            successors = problem.getSuccessors(node.get_state())

            for succesor in successors:
                fifo.push(Node(succesor[0], node.addPath(succesor[1])))
    return None

def uniformCostSearch(problem):
    "Search the node of least total cost first. "

    start_state = problem.getStartState()
    first_state = Node(start_state, [], 0)


    # the lowest node to be expanded first
    priority_queue = util.PriorityQueue()

    # add the first node to expand .the priority is zero (we want to exapand it first)
    priority_queue.push(first_state, first_state.cost)

    # to avoid repeating expanded states
    expanded_states = set()

    while not priority_queue.isEmpty():
        node_to_expand = priority_queue.pop()

        #don't expand the state if it is already expanded
        if node_to_expand.state not in expanded_states:
            #if its goal state return the path
            if problem.isGoalState(node_to_expand.state):
                return node_to_expand.path

            # don't expand this state again
            expanded_states.add(node_to_expand.state)

            # add the child node of this state to queue to be expanded
            for successor in problem.getSuccessors(node_to_expand.state):
                child_node = Node(successor[0], node_to_expand.addPath(successor[1]), node_to_expand.addCost(successor[2]))
                priority_queue.push(child_node, child_node.cost)

    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
