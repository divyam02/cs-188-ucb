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
  * **Forward Checking:** Check immediate violations. The problem gets detected only when the domain of a domain upon assignment is empty.
  * **Constraint Propagation:** Pending...
