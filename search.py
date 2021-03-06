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
    """
    stack = util.Stack();
    root = problem.getStartState(),[]
    visited = []
    #visited.append(problem.getStartState())
    stack.push(root)
    while not stack.isEmpty():
        rootPosition, actionList = stack.pop()
        if rootPosition not in visited:
            visited.append(rootPosition)
            if problem.isGoalState(rootPosition):
                return actionList
            for coordinate, action, cost in problem.getSuccessors(rootPosition):
                stack.push((coordinate, actionList+[action]))

    return []
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    util.raiseNotDefined()
    "*** YOUR CODE HERE ***"

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited = []
    root = problem.getStartState(),[]
    queue.push(root)
    while not queue.isEmpty():
        rootPosition, actionList = queue.pop()
        if rootPosition not in visited:
            visited.append(rootPosition)
            if problem.isGoalState(rootPosition):
                return actionList
            for coordinate, action, cost in problem.getSuccessors(rootPosition):
                queue.push((coordinate, actionList+[action]))

    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    pqueue = util.PriorityQueue()
    visited = []
    root = problem.getStartState(),[]
    pqueue.push(root, 0)
    while not pqueue.isEmpty():
        rootPosition, actionList = pqueue.pop()
        if problem.isGoalState(rootPosition):
            return actionList
        if rootPosition not in visited:
            visited.append(rootPosition)
            for coordinate, action, cost in problem.getSuccessors(rootPosition):
                pqueue.push((coordinate,actionList+[action]),problem.getCostOfActions(actionList+[action]))
    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    opened = util.PriorityQueue()
    closed = []
    root = problem.getStartState(),[]
    opened.push(root, 0)
    while not opened.isEmpty():
        rootPosition, actionList = opened.pop()
        if problem.isGoalState(rootPosition):
            return actionList
        if rootPosition not in closed:
            closed.append(rootPosition)
            for coordinate, action, cost in problem.getSuccessors(rootPosition):
                #if coordinate not in closed:
                opened.push((coordinate,actionList+[action]),problem.getCostOfActions(actionList+[action])+heuristic(coordinate,problem))
    return []



    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
