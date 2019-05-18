# cs-188-ucb
Here you will find implementations of assignments, homeworks, demos and other interesting pieces of code. Feel free to use!
# Theory
## Uninformed Search
1. Uniform Cost Search: Pending...
## Informed Search
1. A*: Pending...
## Heuristics
Pending...
### Greedy faliure
Counter example: Consider the following maze.![alt text](https://github.com/divyam02/cs-188-ucb/blob/master/screenshots/greedy_search_counter_example.png)
## Admissibility and Consistency
Pending...
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
def max_value(state):
 init v = -inf
 for all successors of state:
  v = min(v, max_value(successors))
 return v
 
def min_value(state):
 init v = +inf
 for all successors of state:
  v = min(v, min_value(successors))
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
# Projects
## Project 1: Search
**Notes:** Pending...

![alt text](https://github.com/divyam02/cs-188-ucb/blob/master/screenshots/project1.png)

## Project 2: Multi-Agent Search
**Notes:** Pending...

