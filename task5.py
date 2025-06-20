import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#1E3A8A"):  # початковий темно-синій колір
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
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, pause=0.8):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_size=14)
    plt.title("Обхід бінарного дерева")
    plt.show(block=False)
    plt.pause(pause)
    plt.clf()

def interpolate_color(start_color, end_color, factor: float):
    """Інтерполюємо кольори в 16-річному форматі #RRGGBB"""
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    def rgb_to_hex(rgb):
        return '#' + ''.join(f"{int(c):02X}" for c in rgb)

    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    new_rgb = tuple(start + (end - start) * factor for start, end in zip(start_rgb, end_rgb))
    return rgb_to_hex(new_rgb)

def dfs_iterative(root):
    stack = [root]
    visited_order = []
    while stack:
        node = stack.pop()
        visited_order.append(node)
        # Додаємо спочатку праву, щоб ліва була зверху у стеку
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited_order

def bfs_iterative(root):
    queue = deque([root])
    visited_order = []
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited_order

def visualize_traversal(root, traversal_func, traversal_name):
    nodes = traversal_func(root)
    n = len(nodes)
    start_color = "#1E3A8A"  # темно-синій
    end_color = "#A3CEF1"    # світло-синій

    # Встановлюємо початкові кольори
    def reset_colors(node):
        node.color = "#CCCCCC"  # сірий (не відвіданий)
        if node.left:
            reset_colors(node.left)
        if node.right:
            reset_colors(node.right)
    reset_colors(root)

    print(f"Візуалізація обходу {traversal_name}:")

    for i, node in enumerate(nodes):
        factor = i / max(n - 1, 1)
        node.color = interpolate_color(start_color, end_color, factor)
        draw_tree(root, pause=1)  # пауза 1 секунда, щоб побачити зміни

    print(f"Обхід {traversal_name} завершено.")

def build_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

def main():
    root = build_sample_tree()

    # DFS (обхід в глибину)
    visualize_traversal(root, dfs_iterative, "DFS (обхід в глибину)")

    # BFS (обхід в ширину)
    visualize_traversal(root, bfs_iterative, "BFS (обхід в ширину)")

    plt.close()

if __name__ == "__main__":
    main()