import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

import matplotlib.pyplot as plt
import numpy as np

def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb_color[0] * 255), 
                                        int(rgb_color[1] * 255), 
                                        int(rgb_color[2] * 255))
    
def generate_shades(color, N):
    shades = [rgb_to_hex(tuple(np.clip(np.array(color) * (1 - i / (N - 1)), 0, 1))) for i in range(N)]
    return shades

def visualize_traversal(tree_root, traversal_order):
    colors_to_use = generate_shades((0.3, 0.5, 0.5), len(traversal_order))

    for i, node in enumerate(traversal_order):
        node.color = colors_to_use[i]
        
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color="white")
    plt.show()

def dfs(root):
    if root is None:
        return []
    
    stack = [root]
    order_of_visit = []

    while stack:
        node = stack.pop()
        order_of_visit.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return order_of_visit

def bfs(root):
    visited = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs_order = dfs(root)
print("DFS Order:", [node.val for node in dfs_order])
visualize_traversal(root, dfs_order)

bfs_order = bfs(root)
print("BFS Order:", [node.val for node in bfs_order])
visualize_traversal(root, bfs_order)
