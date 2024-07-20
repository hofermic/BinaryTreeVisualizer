from binarytree import build, Node
import matplotlib.pyplot as plt
import networkx as nx

def list_to_binary_tree(numbers):
    """Converts a list of numbers into a binary tree."""
    return build(numbers)

def visualize_binary_tree(tree, filename="binary_tree.png"):
    """Visualizes the binary tree with a hierarchical layout, different colors for each level, and saves it as an image."""

    G = nx.Graph()
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'plum']  # Add more colors as needed

    def add_nodes_and_edges(node, x, y, y_step, level=0):
        """Recursively add nodes and edges to the graph with hierarchical positioning and color assignment."""
        if node:
            G.add_node(node.value, pos=(x, y), color=colors[level % len(colors)])
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_nodes_and_edges(node.left, x - y_step, y - 1, y_step / 2, level + 1)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_nodes_and_edges(node.right, x + y_step, y - 1, y_step / 2, level + 1)

    add_nodes_and_edges(tree, 0, 0, 2)

    # Get node positions and colors from the graph
    pos = nx.get_node_attributes(G, 'pos')
    node_colors = [G.nodes[node]['color'] for node in G.nodes]  # Extract color for each node

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos=pos, with_labels=True, node_size=1500, node_color=node_colors, font_size=10, font_color="black")
    plt.savefig(filename)
    print(f"Binary tree saved as {filename}")


# Example usage
# numbers = [7, 4, 9, 1, 6, 14, 10] 
# Get user input for the list of numbers
numbers_input = input("Enter a list of numbers separated by spaces (e.g., 7 4 9 1 6 14 10): ")

# Convert the input string into a list of integers
try:
    numbers = [int(num) for num in numbers_input.split()]
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
    exit()  # Exit the program if input is not valid

tree = list_to_binary_tree(numbers)
print(tree) 
visualize_binary_tree(tree)