# CuCengRL-mcts-homework-final-project2
 Monte Carlo Tree Search (MCTS) for Tic-Tac-Toe
# Monte Carlo Tree Search (MCTS) for Tic-Tac-Toe

This repository contains a Python implementation of the Monte Carlo Tree Search (MCTS) algorithm applied to the classic game of Tic-Tac-Toe. The primary objective is to demonstrate the application of MCTS for decision-making in a simple gaming environment.

## Overview

MCTS is a powerful algorithm widely used in artificial intelligence for decision-making in various domains, including games, robotics, and optimization problems. This implementation focuses on the game of Tic-Tac-Toe, providing insights into how MCTS can be leveraged for making intelligent moves in a strategic, turn-based game.

## Contents

- `monte_carlo_tree_search.py`: The main implementation of the MCTS algorithm.
- `node.py`: Definition of the Node class representing nodes in the MCTS tree.
- `utils.py`: Utility functions for performing moves, checking terminal states, and computing rewards.
- `visualization.py`: Functions for visualizing the MCTS tree and results.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/mcts-tic-tac-toe.git
   cd mcts-tic-tac-toe
   ```

2. **Run the Algorithm:**
   ```bash
   python monte_carlo_tree_search.py
   ```
   This will execute the MCTS algorithm on a Tic-Tac-Toe board for a specified number of iterations (default: 5,000).

3. **Explore the Results:**
   - The result state of the Tic-Tac-Toe board after applying MCTS will be displayed.
   - Visualizations showing the number of visits for each child node in the MCTS tree will be generated.

## Experimentation

- Conduct experiments by varying the number of iterations in the MCTS algorithm to observe changes in performance.
- Analyze the visualizations to understand how the algorithm explores different moves.

## Results and Analysis

- The performance of MCTS in reaching optimal or near-optimal moves in Tic-Tac-Toe can be observed.
- Insights into the algorithm's ability to balance exploration and exploitation can be gained through visualizations.

  Action 1: Visits=5000, Value=1.0
Action 2: Visits=0, Value=N/A
Action 3: Visits=0, Value=N/A
Action 4: Visits=0, Value=N/A
Action 5: Visits=0, Value=N/A
Action 6: Visits=0, Value=N/A
Action 7: Visits=0, Value=N/A
Action 8: Visits=0, Value=N/A
Action 9: Visits=0, Value=N/A
Result State:
[[0. 0. 0.] 
 [0. 1. 0.] 
 [0. 0. 0.]]
![1](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/c4d67b7b-a11c-452a-aef4-3415defa8677)

![image](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/3a901e78-ad86-4f9c-97e5-013288925944)

Action 1: Visits=5000, Value=0.0
Action 2: Visits=0, Value=N/A
Action 3: Visits=0, Value=N/A
Action 4: Visits=0, Value=N/A
Action 5: Visits=0, Value=N/A
Action 6: Visits=0, Value=N/A
Action 7: Visits=0, Value=N/A
Action 8: Visits=0, Value=N/A
Action 9: Visits=0, Value=N/A
[[0. 0. 0.] 
 [1. 0. 0.] 
 [0. 0. 0.]]

![image](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/995b2937-d13e-451e-8864-9f508f18a219)

Action 1: Visits=5000, Value=1.0
Action 2: Visits=0, Value=N/A
Action 3: Visits=0, Value=N/A
Action 4: Visits=0, Value=N/A
Action 5: Visits=0, Value=N/A
Action 6: Visits=0, Value=N/A
Action 7: Visits=0, Value=N/A
Action 8: Visits=0, Value=N/A
Action 9: Visits=0, Value=N/A
Result State:
[[0. 0. 0.]
 [1. 0. 0.]
 [0. 0. 0.]]



![image](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/bb9ea475-d80c-458d-9d6d-15b0a9c4ef2b)

Action 1: Visits=5000, Value=0.0
Action 2: Visits=0, Value=N/A
Action 3: Visits=0, Value=N/A
Action 4: Visits=0, Value=N/A
Action 5: Visits=0, Value=N/A
Action 6: Visits=0, Value=N/A
Action 7: Visits=0, Value=N/A
Action 8: Visits=0, Value=N/A
Action 9: Visits=0, Value=N/A
Result State:
[[1. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]


![image](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/92849ad4-35cb-4db2-a183-7c4596718e87)

Action 1: Visits=5000, Value=0.0
Action 2: Visits=0, Value=N/A
Action 3: Visits=0, Value=N/A
Action 4: Visits=0, Value=N/A
Action 5: Visits=0, Value=N/A
Action 6: Visits=0, Value=N/A
Action 7: Visits=0, Value=N/A
Action 8: Visits=0, Value=N/A
Action 9: Visits=0, Value=N/A
Result State:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 1.]]


![image](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/8839bd2a-29a8-4fa7-8789-093cd6fd80d0)


![image](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/1a0f8f6d-6518-4f9a-bdf9-2f262a4c0a9d)

Action 1: Visits=5000, Value=0.0
Action 2: Visits=0, Value=N/A
Action 3: Visits=0, Value=N/A
Action 4: Visits=0, Value=N/A
Action 5: Visits=0, Value=N/A
Action 6: Visits=0, Value=N/A
Action 7: Visits=0, Value=N/A
Action 8: Visits=0, Value=N/A
Action 9: Visits=0, Value=N/A
Result State:
[[0. 0. 0.]
 [0. 1. 0.]
 [0. 0. 0.]]

Action 1: Visits=5000, Value=0.0
Action 2: Visits=0, Value=N/A
Action 3: Visits=0, Value=N/A
Action 4: Visits=0, Value=N/A
Action 5: Visits=0, Value=N/A
Action 6: Visits=0, Value=N/A
Action 7: Visits=0, Value=N/A
Action 8: Visits=0, Value=N/A
Action 9: Visits=0, Value=N/A
Result State:
[[0. 0. 1.]
 [0. 0. 0.]
 [0. 0. 0.]]
![image](https://github.com/KAMAlhameedawi/CuCengRL-mcts-homework-final-project2/assets/149914341/99b68a59-586e-4caa-b77f-0b7d65d188d6)

## Comparison

- Optionally, compare the performance of the MCTS implementation with other strategies or algorithms applicable to Tic-Tac-Toe.
- Discuss the strengths and weaknesses of MCTS in comparison to alternative approaches.

## Documentation

For a comprehensive overview of the project, refer to the detailed documentation in the [docs](docs/) directory. The documentation includes:

- Introduction to Tic-Tac-Toe as the chosen environment.
- Description of the MCTS algorithm and its implementation details.
- Details of experiments conducted, including variations in iterations.
- Results and analysis of MCTS performance in Tic-Tac-Toe.
- Optional comparison with other approaches.
- Conclusion and suggestions for future work.

## Contributors

- [Your Name](https://github.com/your-username): Project Lead, Algorithm Implementation
- [Collaborator Name](https://github.com/collaborator-username): Visualizations, Documentation

## Acknowledgments

- Mention any external libraries, tutorials, or resources used during the project development.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your purposes. Contributions are welcome!

---

Feel free to customize the README according to your project's specifics and add more sections as needed.
