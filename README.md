# Path Finding Visualizer AI
A*, LRTA* and RTA* algorithms simulation in python with different heuristic functions including eucledian distance, manhattan disrance and octile distance.

<br>

## Objective
The objective of this task is to differentiate three different heuristic based informed search algorithms with the help of the diagrams. In this analysis, I have tested all of these three algorithms (A*, RTA*, LRTA*) on the same environment and found out that A* and LRTA* has successfully found the shortest path quickly which proves their property of optimality and completeness. Unlike the previous two algorithms, RTA* has opted the path where it has to visit the minimum number of nodes and reach the goal node as soon as possible. It is important to identify the difference between the two requirements. Former is to find the shortest path between two nodes and the latter is to reach the goal as soon as possible.

<br>

## Algorithms Description

<br>

### 1) A* Algorithm
A* is a best-first search algorithm where the merit of a node, f(n), is the sum of the actual cost in reaching that node from the initial state, g(n), and the estimated cost of reaching the goal state from that node, h(n). A* has the property that it will always find an optimal solution to a problem if the heuristic function never overestimates the actual solution cost. Its major drawback is that it requires exponential space in practice.

<br>

![Fig. 1: A* Algorithm](/assets/images/a_star.png)

<br>

### 2) Real-Time A* Algorithm
In RTA*, the merit of a node n is f(n) = g(n) + h(n), as in A*. However, unlike A*, the interpretation of g(n) in RTA* is the actual distance of a node n from the current state-of the problem solver, rather than from the original initial state. The key difference between RTA* and A* is that in RTA*, the merit of every node is measured relative to the current position of the problem solver, and the initial state is irrelevant. RTA* is simply a best-first search given this slightly different cost function.

<br>

![Fig. 1: Real Time A* Algorithm](/assets/images/real_time_a_star.png)

<br><br>

### 3) Learning Real-Time A* Algorithm
LRTA* retains the completeness and optimality property of RTA* by repeatedly refining the suboptimal path. It does not, however, always make locally optimal decisions but repeated trials cause the heuristic values to converge to their exact values.


<br><br>

![Fig. 1: Learning Real Time A* Algorithm](/assets/images/learning_real_time_a_star.png)

<br>


#### How to run the visualizer?
    1. Open terminal and go to the directory that contain `main.py` file.
    2. Type `python3 main.py` on terminal and hit enter.
    3. The simulator will be opened on a new screen.

<br>

#### How to use visualizer?
    1. Left click -> to add a start, end, or an obstacle node.
    2. right click -> to remove a start, end, or an obstacle node.
    3. Press 1 -> to start simulation with A* algorithm.
    4. Press 2 -> to start simulation with Learning Real-Time A* algorithm.
    5. Press 3 -> to start simulation with Real-Time A* algorithm.
    6. Press SPACE -> to reset grid (obstacles, start and end nodes will not be removed).
    7. Press ESCAPE -> to quit.
