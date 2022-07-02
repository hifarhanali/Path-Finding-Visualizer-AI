# Path Finding Visualizer AI
A*, LRTA*, and RTA* algorithms simulation in python with different heuristic functions including euclidian distance, manhattan distance, and octile distance.

<br>

## Objective
The objective of this task is to differentiate three different heuristic-based informed search algorithms with the help of the diagrams. In this analysis, I have tested all of these three algorithms (A*, RTA*, LRTA*) in the same environment and found out that A* and LRTA* have successfully found the shortest path quickly which proves their property of optimality and completeness. Unlike the previous two algorithms, RTA* has opted for the path where it has to visit the minimum number of nodes and reach the goal node as soon as possible. It is important to identify the difference between the two requirements. The former is to find the shortest path between two nodes and the latter is to reach the goal as soon as possible.

<br>

## Algorithms Description

<br>

### 1) A* Algorithm
A* is a best-first search algorithm where the merit of a node, f(n), is the sum of the actual cost of reaching that node from the initial state, g(n), and the estimated cost of reaching the goal state from that node, h(n). A* has the property that it will always find an optimal solution to a problem if the heuristic function never overestimates the actual solution cost. Its major drawback is that it requires exponential space in practice.

<br>

![Fig. 1: A* Algorithm](/assets/images/a_star.png)

<br>

### 2) Real-Time A* Algorithm
In RTA*, the merit of a node n is f(n) = g(n) + h(n), as in A*. However, unlike A*, the interpretation of g(n) in RTA* is the actual distance of a node n from the current state of the problem solver, rather than from the original initial state. The key difference between RTA* and A* is that in RTA*, the merit of every node is measured relative to the current position of the problem solver, and the initial state is irrelevant. RTA* is simply a best-first search given this slightly different cost function.

<br>

![Fig. 2: Real-Time A* Algorithm](/assets/images/real_time_a_star.png)

<br><br>

### 3) Learning Real-Time A* Algorithm
LRTA* retains the completeness and optimality property of RTA* by repeatedly refining the suboptimal path. It does not, however, always make locally optimal decisions but repeated trials cause the heuristic values to converge to their exact values.


<br><br>

![Fig. 3: Learning Real-Time A* Algorithm](/assets/images/learning_real_time_a_star.png)

<br>


## Block Colors Index

| Block Color               | Meaning                                                |
|:-------------------------:|:------------------------------------------------------:|
| Light Green               | Represents the opened node when the algorithm stopped  |
| Light Yellow              | Represents the visited node when the algorithm stopped |
| Normal Cyan               | Represents the start node                              |
| Normal Green              | Represents the end node                                |
| Dark Brown                | Represents an obstacle                                 |
| Black Line                | Represents the path between the start and end node     |

<br>

## How to run the visualizer?
    1. Open the terminal and go to the directory that contains `main.py` file.
    2. Type `python3 main.py` on the terminal and hit enter.
    3. The simulator will be opened on a new screen.

<br>

## How to use the visualizer?
    1. Left click -> to add a start, end, or obstacle node.
    2. right-click -> to remove a start, end, or obstacle node.
    3. Press 1 -> to start the simulation with the A* algorithm.
    4. Press 2 -> to start the simulation with Learning Real-Time A* algorithm.
    5. Press 3 -> to start the simulation with Real-Time A* algorithm.
    6. Press SPACE -> to reset the grid (obstacles, start and end nodes will not be removed).
    7. Press ESCAPE -> to quit.
