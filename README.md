# cs-188-ucb
Here you will find implementations of assignments, homeworks, demos and other interesting pieces of code. Feel free to use!

## Uninformed Search
1. Uniform Cost Search: Pending...
## Informed Search
1. A*: Pending...
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
  * **Forward Checking:** Check immediate violations. The problem gets detected only when the domain of a domain upon assignment is empty. We enforce consistency by deleting conflicting candidates from the variable domain.
  * **Arc Consistency:** If the constraints are given as a graph between variables and each variable has all of its possible candidates, problems can be detected and removed earlier. A directed edge(arc) from A to B is consistent iff for all x in the domain of A (tail) there is some y in the domain of B (head) such that upon assignment there is no constraint violation.
  eg. Constraint: a!=b. So, {3} <- {1,2,3} is not consistent but {1,3} <- {1,2,3} is. 
  
  Now to enforce consistency, we must delete conflicting candidates of the tail domain, but then all other arcs with their head in this node will have to be checked for consistency again. However this is only enforcing consistency between pairs of variables and indeed fails for 3 way constraints. eg. A={1,2} B={1,2} and C=={1,2} with the previous constraint. Then A<-B, B<-C, C<-A are all consistent. But there is no legal assignment for all three.
* **Ordering:** Order in which variables are to be chosen. For CSPs we have heuristics based on variables and values assigned.
  * **Variable Order:** Select the variable with minimum remaining values in its domain. This is the most constrained variable and upon should the assignment be invalid it will have lesser backtracking.
  * **Value Order:** Select the value that rules out the fewest values.
