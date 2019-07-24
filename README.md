# cs-188-ucb
Here you will find implementations of assignments, homeworks, demos and other interesting pieces of code. Feel free to use!
# Projects
## Project 1: Search
**Notes:** Pending...

![alt text](https://github.com/divyam02/cs-188-ucb/blob/master/screenshots/project1.png)

## Project 2: Multi-Agent Search
**Notes:** Pending...

![alt text](https://github.com/divyam02/cs-188-ucb/blob/master/screenshots/project2.png)

## Project 3: Reinforcement Learning
**Notes:** Pending...

![alt text](https://github.com/divyam02/cs-188-ucb/blob/master/screenshots/project3.png)

## Project 4: Particle Filtering
**Notes:** Pending...

![alt text](https://github.com/divyam02/cs-188-ucb/blob/master/screenshots/project4.png)

# Theory
## Uninformed Search
Works by maintaining an outer **fringe**; a set of nodes that the agent has to currently explore. We expand the fringe by replacing a node selected by our strategy(BFS,DFS,UCS) and replace that node with its children. In tree search we don't have to keep track of visited states (nodes).
```
def tree_search(problem, fringe):
  fringe <- insert initial state
  while(fringe is not empty):
    node <- remove using strategy from fringe
    if node is goal_state:
      return node
    for child_nodes of node:
      fringe <- insert child_nodes
```
* **DFS:** Selects the deepest fringe node. Upon expansion the child nodes are now necessarily the deepest nodes on the fringe. A stack can be used to represent the fringe. 
  * *Completness:* DFS is not complete. Consider a state space graph with a cycle. The corresponding search tree will be of infinite depth and DFS gets stuck.
  * *Optimal:* Does not yield the lowest cost path, the first goal state encountered could be on the longest path.
  * *Time Complexity:* (Can't escape this!) O(b^m) where b is the branching factor; the children added per expansion of fringe and m is the depth to which the fringe is expanded before obtaining a solution. Worst case the entire tree is explored.
  * *Space Complexity:* From above, we maintatin a size b fringe at every depth of so O(bm)

* **BFS:** Selects the shallowest fringe node. The nodes of a given layer are expanded entirely before moving to the child nodes. A queue can be used to represen the fringe.
  * *Completeness:* BFS is complete! It will always find the shallowest goal state first.
  * *Optimal:* Only when all edge weights are the same as it does not account for the cost of getting to a particular node.
  * *Time Complexity:* (Can't escape this!) Worst case every node on the fringe is expanded, so O(b^m)
  * *Space Complexity:* From above, we maintatin all children of the previous layer on the fringe. Worst case at the bottom layer we get b^m children, so O(b^m)
  
* **UCS:** Selects the lowest cost node for expansion. Cost associated with a node is from the sum of edge weights of path to the node. Can be represented using a priority queue.
  * *Completeness:* UCS is complete! It will find the lowest cost goal state first. Infact, BFS is a special case of UCS where all edge weights are the same.
  * *Optimal:* UCS is optimal when edge weights are non negative. Consider a search tree where at m-1 depth a more expensive path has a -inf edge. This path will never be explored and a goal state would be reached else where.
  * *Time Complexity:* (Can't escape this!) Let the optimal path cost be C* and the minimal edge cost be e. Then if each node is explored in between, time complexity is O(b^(C*/e))
  * *Space Complexity:* From above, we maintatin a size b^(C*/e) fringe of the cheapest path nodes.
  
## Informed Search
Search algorithms like UCS can be made mush faster if there was some notion of searching in the right direction. Informed search uses **heuristics** to estimate the "distance" to goal states. Heuristics strictly depend on the current state and are solutions to relaxed versions of the search problem.
* **Greedy Search:** Selects node with the lowest heuristic value. Does not guarantee completeness or optimality.
    * *Greedy faliure:* Counter example: Consider the following maze.![alt text](https://github.com/divyam02/cs-188-ucb/blob/master/screenshots/greedy_search_counter_example.png)
* **A* Search:** Selects node with the lowest estimated total cost of evaluation. This is the cost of the path from start to current node + the heuristic estimated distance of the current node. It is complete and optimal provided a sensible heuristic us being used. 
* **Admissibility and Consistency:** Let g(n) be the backward cost, h(n) be the heuristic cost and f(n) = g(n) + h(n) where n is a node.
**Admissibile:** 0≤h(n)≤h*(n) where h*(n) is the true optimal cost between the node and the goal state. 
    * *Theorem:* For a given search problem, if the admissibility constraint is satisfied by a heuristic function h,using A* ***tree search*** with h on that search problem will yield an optimal solution.
    * *Proof:* Assume two reachable goal states are located in the search tree for a given search problem, an optimal goal A and a suboptimal goal B. Some ancestor of A(including perhaps A itself) must currently be on the fringe, since A is reachable from the start state.  We claim n will be selected for expansion before B, using the following three statements:
        * 1.g(A)<g(B). Because Ais given to be optimal and B is given to be suboptimal, we can conclude that A has a lower backwards cost to the start state than B.
        * 2.h(A)=h(B)=0, because we are given that our heuristic satisfies the admissibility constraint.  Since both A and B are goal states, the true optimal cost to a goal state from A or B is simply h*(n)=0;h ence 0≤h(n)≤0.
        * 3.f(n)≤f(A), because, through admissibility of h,f(n)=g(n)+h(n)≤g(n)+h*(n)=g(A)=f(A).The total cost through node n is at most the true backward cost of A, which is also the total cost of A.We can combine statements 1. and 2. to conclude that f(A)<f(B) as follows: f(A)=g(A)+h(A)=g(A)<g(B)=g(B)+h(B)=f(B). A simple consequence of combining the above derived inequality with statement 3. is the following: f(n)≤f(A)∧f(A)<f(B) => f(n)<f(B)Hence, we can conclude that n is expanded before B.  Because we have proven this for arbitrary n, we can conclude that all ancestors ofA(including A itself) expand before B.
**Consistency:** ∀A,C h(A)−h(C)≤cost(A,C). We understimate not only the distance from the goal but also underestimates the weight of each edge.
    * *Theorem:* For a given search problem, if the consistency constraint is satisfied by a heuristic function h,using A* ***graph search*** with h on that search problem will yield an optimal solution.
    * *Proof:* Pending...

## Constraint Satisfaction Problems
**Some assumptions:** Single friendly agent, completely deterministic. We also assume a fully observed space and a discrete state space.
* Used for identification tasks by making valid assignments to some variables satisfying the constraints of the problem.
* The goal state is important, not the path (cost) involved.
* Subset of standard seach problems. States are ***variables*** with values from a set called the ***domain***.
* ***Goal test:*** Set of constraints giving allowable combination of domain values for a subset of variables. 
  * **Implicit:** Variable specific constraints. eg. A!=B
  * **Explicit:** Set of all legal values. eg. A = {a, b, c, f} etc.
* ***Solutions:*** Assignments to all variables satisfying all constraints.
### How to deal with constraint violations?
* **Filtering:** Ruling out candidates for unassigned variables by keeping track of domains of unassigned variables.
  * **Forward Checking:** Check immediate violations. The problem gets detected only when the domain of a variable upon assignment is empty. We enforce consistency by deleting conflicting candidates from the variable domain.
  * **Arc Consistency:** If the constraints are given as a graph between variables and each variable has all of its possible candidates, problems can be detected and removed earlier. A directed edge(arc) from A to B is consistent iff for all x in the domain of A (tail) there is some y in the domain of B (head) such that upon assignment there is no constraint violation.
  eg. Constraint: a!=b. So, {3} <- {1,2,3} is not consistent but {1,3} <- {1,2,3} is. 
* **Use Problem Structure:** Pending...
  
  Now to enforce consistency, we must delete conflicting candidates of the tail domain, but then all other arcs with their head in this node will have to be checked for consistency again. However this is only enforcing consistency between pairs of variables and indeed fails for 3 way constraints. eg. A={1,2} B={1,2} and C={1,2} with the previous constraint. Then A<-B, B<-C, C<-A are all consistent. But there is no legal assignment for all three.
* **Ordering:** Order in which variables are to be chosen. For CSPs we have heuristics based on variables and values assigned.
  * **Variable Order:** Select the variable with minimum remaining values in its domain. This is the most constrained variable and upon should the assignment be invalid it will have lesser backtracking.
  * **Value Order:** Select the value that rules out the fewest values.
## Adversarial Search
Now there are agents not in our control. The actions taken are no longer deterministic. Many of these search problems can be treated as **zero sum games**.
* **Zero Sum Game:** All agents attempt to maximize their utility using a common resource. In a zero sum game, adversarial agents can maximize their utility by actively minimizing the opponent's utility. What follows below is based on actions being taken in discrete time ie, the agents are turn based and control a layer of the adversarial search tree.
* Adversarial search returns a **policy**, that recommends an action to yield maximum utility.
* **Value of a state:** The best achievable utility from that state in a zero sum game. Value(state) = V(s in S) = max V(s in children of s), where S is the set of all states and the value terminal states are known (the game has ended). 
* How to optimize? Pretend to be the other agent and try to minimize your opponent's score (ie maximize your own).
### Minimax Search
Each node in the tree computes its minimax value; the best utility against a rational adversary. For efficieny, it traverses in a post-order format.
```
def value(state):
 if terminial state:
  return state utility
 elif max_agent state:
  return max_value(state)
 else:
  return min_value(state)
  
def max_value(state):
 init v = -inf
 for all successors of state:
  v = min(v, value(successors))
 return v
 
def min_value(state):
 init v = +inf
 for all successors of state:
  v = min(v, value(successors))
 return v
```
### Minimax Efficiency
* DFS time: O(b^m) considering all branches for all possible moves.
* However we can get away with not exploring the entire tree!
* **Search-tree/Alpha-Beta Pruning:** We will need to explore atleast one branch entirely, to get the initial utilities of branching states. Now we can compare: If a minimizer node has a possible value less that the utility of a previously explored min node with the same maximizer parent, we can stop exploring that branch. The maximizer already has a better option. Hence if we are trying to determine the value of some node by looking at its successors we can stop as soon as we know its value can at best be the optimal value of the parent. Theoretical bound: O(b^(m/2)). 
* Actual search trees end up being far more complex. Typically in a game like chess, searching more than 2 levels deep starts becoming unfeasible. With this we can explore double the depth (actions).
```
# alpha = player1's best option on path.
# beta = player2's best option on path.

def max_value(state, alpha, beta):
 init v = -inf
 for successors of state:
  v = max(v, value(successor, alpha, beta))
  if v>= beta:return v
  alpha = max(v, alpha)
 return v
 
def min_value(state, alpha, beta):
 init v = +inf
 for successors of state:
  v = min(v, value(successor, alpha, beta))
  if v<= alpha:return v
  beta = min(v, beta)
 return v
```
### Evaluation Functions
Since reaching the bottom of adversarial search trees for more complex games, we must estimate the value of a node depending on the current state. In case of **depth-limited minimax**, non-terminal nodes at the maximum depth limit are treated as terminal and are given an estimate of the true minimax value. Typically a good evaluation function will ensure "better" state have a higher value than others.
* A common heuristic is to use a linear combination of features from the current state. Some approaches use machine learning to estimate over time, a good state and a bad state.

### Expectimax
This is a replacement for minimax when the opponent is playing suboptimally. 
