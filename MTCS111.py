import numpy as np
import random
import math
import matplotlib.pyplot as plt

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0

def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def perform_move(board, move, player):
    i, j = move
    board[i][j] = player
    return board

def is_terminal(board):
    for i in range(3):
        if all(board[i][j] == 1 for j in range(3)) or all(board[i][j] == 2 for j in range(3)):
            return True  # Check rows

        if all(board[j][i] == 1 for j in range(3)) or all(board[j][i] == 2 for j in range(3)):
            return True  # Check columns

    if all(board[i][i] == 1 for i in range(3)) or all(board[i][2 - i] == 1 for i in range(3)):
        return True  # Check diagonals

    if all(board[i][i] == 2 for i in range(3)) or all(board[i][2 - i] == 2 for i in range(3)):
        return True  # Check diagonals

    return all(board[i][j] != 0 for i in range(3) for j in range(3))  # Check draw

def get_reward(board):
    if any(all(cell == 1 for cell in row) for row in board):
        return 1  # Player 1 wins
    elif any(all(cell == 2 for cell in row) for row in board):
        return -1  # Player 2 wins
    else:
        return 0  # Draw

def simulate_random_playout(board, player):
    while not is_terminal(board):
        possible_moves = get_possible_moves(board)
        random_move = random.choice(possible_moves)
        board = perform_move(board, random_move, player)
        player = 3 - player  # Switch players (1 to 2, 2 to 1)
    return get_reward(board)

def select_child(node, exploration_weight=1.0):
    log_total_visits = math.log(sum(child.visits for child in node.children))

    non_zero_children = [child for child in node.children if child.visits > 0]

    if not non_zero_children:
        return random.choice(node.children)

    best_child = max(non_zero_children, key=lambda child: child.value / child.visits + exploration_weight * math.sqrt(log_total_visits / child.visits))

    return best_child

def expand(node, board):
    possible_moves = get_possible_moves(board)
    for move in possible_moves:
        new_board = perform_move(board.copy(), move, player=1)
        new_child = Node(state=new_board, parent=node)
        node.children.append(new_child)
    return node.children[np.random.randint(len(node.children))] if node.children else None

def backpropagate(node, reward):
    while node is not None:
        node.visits += 1
        node.value += reward
        node = node.parent

def monte_carlo_tree_search(root_state, iterations=1000):
    root = Node(state=root_state)

    for i in range(iterations):
        node = root
        while not is_terminal(node.state):
            if len(node.children) < len(get_possible_moves(node.state)):
                node = expand(node, node.state)
            else:
                node = select_child(node)
        simulation_result = simulate_random_playout(node.state, player=1)
        backpropagate(node, simulation_result)

    best_child = max(root.children, key=lambda child: child.visits)

    # Plot visits after all iterations
    plot_visits(root)

    return best_child.state

def plot_visits(node):
    visits = [child.visits for child in node.children]
    actions = [i for i in range(1, len(visits) + 1)]

    # Sort children based on visits for better visualization
    sorted_children = [child for _, child in sorted(zip(visits, node.children), key=lambda x: x[0], reverse=True)]

    # Display sorted children
    for i, child in enumerate(sorted_children):
        print(f"Action {i + 1}: Visits={child.visits}, Value={child.value / child.visits if child.visits > 0 else 'N/A'}")

    plt.bar(actions, visits)
    plt.xlabel('Child Nodes')
    plt.ylabel('Number of Visits')
    plt.title('Number of Visits for Child Nodes')

    # Show the plot
    plt.show()

# Testing the algorithm with Tic-Tac-Toe
initial_state = np.zeros((3, 3))
result_state = monte_carlo_tree_search(initial_state, iterations=5000)
print("Result State:")
print(result_state)



