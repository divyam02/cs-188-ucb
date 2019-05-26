# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        """
        Just make sure to keep away from the ghosts. 
        @Pending:
        Add points for edible ghost times.
        """
        "*** YOUR CODE HERE ***"
        #print(newScaredTimes)
        #print(newFood)
        #print(successorGameState)
        def get_ghost_dist(pacman, ghosts):
            dist = []
            index = 0
            for x, y in successorGameState.getGhostPositions():
                #if newScaredTimes[index] == 0:
                dist.append((abs(pacman[0] - x) + abs(pacman[1] - y)))
                #print("ghost-wise distance:", pow((pacman[0] - x), 2), pow((pacman[1] - y), 2))
            index += 1
            #if len(dist) > 0:
            if min(dist) <= 2:
                return -99999
            return 100 * min(dist)    
            #else:
            #    return 10000

        def get_pellet_score(currentGameState, successorGameState):
            if successorGameState.getNumFood() < currentGameState.getNumFood():
                return 2000
            return 0 

        def keep_moving(currentGameState, successorGameState):
            if currentGameState.getPacmanPosition() != newPos:
                return 10
            return -10
        """
        def get_closest_edible_ghost(pacman, ghosts, newScaredTimes):
            for i in range(len(newScaredTimes)):
                scared = []
                if newScaredTimes[i] != 0:
                    x, y = ghosts[i]
                    scared.append((abs(pacman[0] - x) + abs(pacman[1] - y)))
            if len(scared)>0:
                if get_closest_food(pacman, newFood) > min(scared):
                    return 10000
                else:
                    return 0
            return 0
        """

        def get_closest_food(pacman, newFood):
            dist = []
            for x, y in newFood.asList():
                dist.append(abs(pacman[0] - x) + abs(pacman[1] - y))
            if len(dist) > 0:
                return min(dist)
            return 0

        def abs_win(successorGameState):
            if successorGameState.isWin():
                return 99999
            return 0

        def abs_loss(successorGameState):
            if successorGameState.isLose():
                return -99999
            return 0

        score = get_ghost_dist(newPos, successorGameState.getGhostPositions()) 
        score += get_pellet_score(currentGameState, successorGameState)
        score += get_closest_food(newPos, newFood) * -100
        score += abs_win(successorGameState) + abs_loss(successorGameState)
        score += successorGameState.getScore()
        #score += get_closest_edible_ghost(newPos, successorGameState.getGhostPositions(), newScaredTimes)
        score += keep_moving(currentGameState, successorGameState) * 100
        #print(score)
        return score       


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        num_agents = gameState.getNumAgents()
        pacman_actions = gameState.getLegalActions()
        curr_depth = 0
        agent_index = 0
        max_depth = self.depth*num_agents
        #print(num_agents)

        def value(state, curr_depth, agent):
            agent = agent%num_agents
            """
            @Note:This fails when pacman is gets surrounded by ghosts and walls. 
            So either he has won or lost in that position, hence return
            terminal values.

            #if curr_depth == self.depth*num_agents:

            """
            if curr_depth == max_depth or state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            if agent == 0:
                return max_value(state, curr_depth, agent)
            else:
                return min_value(state, curr_depth, agent)

        def max_value(state, curr_depth, agent):
            v = -float("inf")
            if len(state.getLegalActions(agent))==0:
                print("WARNING. No actions available for agent", agent, "at depth", curr_depth)
                print(state.getLegalActions(agent))

            for action in state.getLegalActions(agent):
                next_state = state.generateSuccessor(agent, action)
                v = max(v, value(next_state, curr_depth+1, agent+1))
            return v

        def min_value(state, curr_depth, agent):
            v = float("inf")
            if len(state.getLegalActions(agent))==0:
                print("WARNING. No actions available for agent", agent, "at depth", curr_depth)
                print(state.getLegalActions(agent))

            for action in state.getLegalActions(agent):
                next_state = state.generateSuccessor(agent, action)
                v = min(v, value(next_state, curr_depth+1, agent+1))
            return v

        init_value = value(gameState, curr_depth, agent_index)
        #print("Initial value:\n", init_value)

        minimax_action = None
        init_value = -float("inf")
        next_state_values = [(init_value, minimax_action)]
        for action in gameState.getLegalActions(0):
            next_state_values.append((value(gameState.generateSuccessor(0, action), 1, 1), action))

        init_value, minimax_action = max(next_state_values)
        #print(init_value)
        return minimax_action


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        num_agents = gameState.getNumAgents()
        curr_depth = 0
        agent_index = 0
        max_depth = self.depth*num_agents
        alpha = -float("inf")
        beta = float("inf")

        def value(state, curr_depth, agent, alpha, beta):
            agent = agent%num_agents
            """
            @Note: Keeping global variables was a bad idea.

            """
            if curr_depth == max_depth or state.isWin() or state.isLose():
                score = self.evaluationFunction(state) 
                return score
            if agent == 0:
                return max_value(state, curr_depth, agent, alpha, beta)
            else:
                return min_value(state, curr_depth, agent, alpha, beta)

        def max_value(state, curr_depth, agent, alpha, beta):
            v = -float("inf")
            if len(state.getLegalActions(agent))==0:
                print("WARNING. No actions available for agent", agent, "at depth", curr_depth)
                print(state.getLegalActions(agent))

            for action in state.getLegalActions(agent):
                next_state = state.generateSuccessor(agent, action)
                v = max(v, value(next_state, curr_depth+1, agent+1, alpha, beta))
                if v > beta:return v
                alpha = max(alpha, v)
            return v

        def min_value(state, curr_depth, agent, alpha, beta):
            v = float("inf")
            if len(state.getLegalActions(agent))==0:
                print("WARNING. No actions available for agent", agent, "at depth", curr_depth)
                print(state.getLegalActions(agent))

            for action in state.getLegalActions(agent):
                next_state = state.generateSuccessor(agent, action)
                v = min(v, value(next_state, curr_depth+1, agent+1, alpha, beta))
                if v < alpha:return v
                beta = min(beta, v)
            return v

        minimax_action = None
        init_value = -float("inf")
        next_state_values = [(init_value, minimax_action)]
        for action in gameState.getLegalActions(0):
            state_value = value(gameState.generateSuccessor(0, action), 1, 1, alpha, beta)
            if init_value < state_value:
                init_value = state_value
                minimax_action = action
            alpha = max(alpha, init_value)

        #print(init_value)
        return minimax_action        

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        num_agents = gameState.getNumAgents()
        pacman_actions = gameState.getLegalActions()
        curr_depth = 0
        agent_index = 0
        max_depth = self.depth*num_agents
        #print(num_agents)

        def value(state, curr_depth, agent):
            agent = agent%num_agents
            """
            @Note: Expectimax can't use alpha-beta pruning.
            """
            if curr_depth == max_depth or state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            if agent == 0:
                return max_value(state, curr_depth, agent)
            else:
                return exp_value(state, curr_depth, agent)

        def max_value(state, curr_depth, agent):
            v = -float("inf")
            if len(state.getLegalActions(agent))==0:
                print("WARNING. No actions available for agent", agent, "at depth", curr_depth)
                print(state.getLegalActions(agent))

            for action in state.getLegalActions(agent):
                next_state = state.generateSuccessor(agent, action)
                v = max(v, value(next_state, curr_depth+1, agent+1))
            return v

        def exp_value(state, curr_depth, agent):
            v = 0
            if len(state.getLegalActions(agent))==0:
                print("WARNING. No actions available for agent", agent, "at depth", curr_depth)
                print(state.getLegalActions(agent))

            prob = 1/len(state.getLegalActions(agent))
            for action in state.getLegalActions(agent):
                next_state = state.generateSuccessor(agent, action)
                v += prob*value(next_state, curr_depth+1, agent+1)
            return v

        init_value = value(gameState, curr_depth, agent_index)
        #print("Initial value:\n", init_value)

        minimax_action = None
        init_value = -float("inf")
        next_state_values = [(init_value, minimax_action)]
        for action in gameState.getLegalActions(0):
            next_state_values.append((value(gameState.generateSuccessor(0, action), 1, 1), action))

        init_value, minimax_action = max(next_state_values)
        #print(init_value)
        return minimax_action        

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    #successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    #newGhostStates = currentGameState.getGhostStates()
    #newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    """
    Just make sure to keep away from the ghosts. 
    @Pending:
    Add points for edible ghost times.
    """
    "*** YOUR CODE HERE ***"
    #print(newScaredTimes)
    #print(newFood)
    #print(successorGameState)
    def get_ghost_dist(pacman, ghosts):
        dist = []
        index = 0
        for x, y in currentGameState.getGhostPositions():
            #if newScaredTimes[index] == 0:
            dist.append((abs(pacman[0] - x) + abs(pacman[1] - y)))
            #print("ghost-wise distance:", pow((pacman[0] - x), 2), pow((pacman[1] - y), 2))
        index += 1
        #if len(dist) > 0:
        if min(dist) <= 2:
            return -99999
        return 50 * min(dist)    
        #else:
        #    return 10000

    
    def get_pellet_score(currentGameState):
        return -100 * currentGameState.getNumFood()

    """
    def keep_moving(currentGameState):
        if currentGameState.getPacmanPosition() != newPos:
            return 10
        return -10
    
    def get_closest_edible_ghost(pacman, ghosts, newScaredTimes):
        for i in range(len(newScaredTimes)):
            scared = []
            if newScaredTimes[i] != 0:
                x, y = ghosts[i]
                scared.append((abs(pacman[0] - x) + abs(pacman[1] - y)))
        if len(scared)>0:
            if get_closest_food(pacman, newFood) > min(scared):
                return 10000
            else:
                return 0
        return 0
    """

    def get_closest_food(pacman, newFood):
        dist = []
        for x, y in newFood.asList():
            dist.append(abs(pacman[0] - x) + abs(pacman[1] - y))
        if len(dist) > 0:
            return min(dist) * currentGameState.getNumFood()
        return 0

    def abs_win(successorGameState):
        if successorGameState.isWin():
            return 99999
        return 0

    def abs_loss(successorGameState):
        if successorGameState.isLose():
            return -99999
        return 0

    score = get_ghost_dist(newPos, currentGameState.getGhostPositions()) 
    score += get_pellet_score(currentGameState)
    score += get_closest_food(newPos, newFood) * -10
    score += abs_win(currentGameState) + abs_loss(currentGameState)
    score += currentGameState.getScore()
    #score += get_closest_edible_ghost(newPos, successorGameState.getGhostPositions(), newScaredTimes)
    #score += keep_moving(currentGameState, successorGameState) * 100
    #print(score)
    return score

# Abbreviation
better = betterEvaluationFunction
