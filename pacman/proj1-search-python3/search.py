# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    return  [w, w, w, w, s, s, e, s, s, w]
    #return [w,w,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    print("Start:",problem.getStartState())
    print(type(problem.getStartState()))
    print("Is start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start state successors:", problem.getSuccessors(problem.getStartState()))
    print(type(problem.getSuccessors(problem.getStartState())))

    """
    Check legal actions for every state. Encounter leaf node iff no legal actions remaining...
    Make grid to mark visited nodes. (Copy GameState.getWalls())
    Keep stack to append or pop legal path.
    """
    visited_grid = dict()
    parent_dict = dict()
    var_dict = dict()

    start_state_var = (problem.getStartState(), '', 0)
    fringe = util.Stack()
    fringe.push(start_state_var)
    goal_state = util.Stack()
    goal_path = util.Stack()

    parent_dict[problem.getStartState()] = 0

    while(not fringe.isEmpty()):
        next_state, action, cost = fringe.pop()
        visited_grid[next_state] = None
        var_dict[next_state] = (next_state, action, cost)
        #goal_path.push(action)

        #print("Next state:",next_state)
        #print("goal_path:",goal_path.list)
        #print("visited_grid:",visited_grid.keys())

        if(problem.isGoalState(next_state)):
            print("Hit goal state:", next_state)
            # Start traceback...
            #return goal_path.list[1:]
            #goal_path.push(var_dict[next_state][1])
            parent_state = next_state
            _1, action, _2 = var_dict[parent_state]
            #print(action)
            goal_state.push(action)
            while parent_state!=problem.getStartState():
                #print("Parent state:",parent_state)
                parent_state = parent_dict[parent_state]
                _1, action, _2 = var_dict[parent_state]
                #print(action)
                goal_state.push(action)

            while not goal_state.isEmpty():
                goal_path.push(goal_state.pop())

            print(goal_path.list[1:])
            print(len(goal_path.list[1:]))
            return goal_path.list[1:]

        else:
            """
            Maintain grid copy and mark off visited nodes...
            Leaf if all successor states already visited.
            Keep dict node:parent to get path.
            """
            no_successors = True
            successor_list = problem.getSuccessors(next_state)

            for i, j, k in successor_list:
                if not i in visited_grid:
                    fringe.push((i, j, k))
                    parent_dict[i] = next_state
                    no_successors = False

            #print("successor_list:",successor_list)
            #print("Fringe:", fringe.list)

    return goal_path

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    print("Start:",problem.getStartState())
    print(type(problem.getStartState()))
    print("Is start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start state successors:", problem.getSuccessors(problem.getStartState()))
    print(type(problem.getSuccessors(problem.getStartState())))

    """
    Check legal actions for every state. Encounter leaf node iff no legal actions remaining...
    Make grid to mark visited nodes. (Copy GameState.getWalls())
    Keep stack to append or pop legal path.
    """
    visited_grid = dict()
    parent_dict = dict()
    var_dict = dict()

    start_state_var = (problem.getStartState(), '', 0)
    fringe = util.Queue()
    fringe.push(start_state_var)
    goal_state = util.Stack()
    goal_path = util.Stack()

    parent_dict[problem.getStartState()] = 0

    while(not fringe.isEmpty()):
        next_state, action, cost = fringe.pop()
        visited_grid[next_state] = None
        var_dict[next_state] = (next_state, action, cost)

        if(problem.isGoalState(next_state)):
            print("Hit goal state:", next_state)
            parent_state = next_state
            _1, action, _2 = var_dict[parent_state]
            goal_state.push(action)
            while parent_state!=problem.getStartState():
                parent_state = parent_dict[parent_state]
                _1, action, _2 = var_dict[parent_state]
                goal_state.push(action)

            while not goal_state.isEmpty():
                goal_path.push(goal_state.pop())

            print(goal_path.list[1:])
            print(len(goal_path.list[1:]))
            return goal_path.list[1:]

        else:
            no_successors = True
            successor_list = problem.getSuccessors(next_state)

            for i, j, k in successor_list:
                if not i in visited_grid:
                    fringe.push((i, j, k))
                    parent_dict[i] = next_state
                    no_successors = False

    return goal_path

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    print("Start:",problem.getStartState())
    print(type(problem.getStartState()))
    print("Is start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start state successors:", problem.getSuccessors(problem.getStartState()))
    print(type(problem.getSuccessors(problem.getStartState())))

    """
    Check legal actions for every state. Encounter leaf node iff no legal actions remaining...
    Make grid to mark visited nodes. (Copy GameState.getWalls())
    Keep stack to append or pop legal path.
    """
    visited_grid = dict()
    parent_dict = dict()
    var_dict = dict()

    start_state_var = (problem.getStartState(), '', 0)
    fringe = util.PriorityQueue()
    fringe.push(start_state_var)
    goal_state = util.Stack()
    goal_path = util.Stack()

    parent_dict[problem.getStartState()] = 0

    while(not fringe.isEmpty()):
        next_state, action, cost = fringe.pop()
        visited_grid[next_state] = None
        var_dict[next_state] = (next_state, action, cost)

        if(problem.isGoalState(next_state)):
            print("Hit goal state:", next_state)
            parent_state = next_state
            _1, action, _2 = var_dict[parent_state]
            goal_state.push(action)
            while parent_state!=problem.getStartState():
                parent_state = parent_dict[parent_state]
                _1, action, _2 = var_dict[parent_state]
                goal_state.push(action)

            while not goal_state.isEmpty():
                goal_path.push(goal_state.pop())

            print(goal_path.list[1:])
            print(len(goal_path.list[1:]))
            return goal_path.list[1:]

        else:
            no_successors = True
            successor_list = problem.getSuccessors(next_state)

            for i, j, k in successor_list:
                if not i in visited_grid:
                    fringe.push((i, j, k))
                    parent_dict[i] = next_state
                    no_successors = False

    return goal_path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
