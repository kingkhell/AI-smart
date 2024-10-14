class Node:
    def __init__(self, name, value=None, children=None):
        self.name = name
        self.value = value
        self.children = children if children is not None else []

def alpha_beta(node, depth, alpha, beta, max_player):
    if depth == 0 or node.value is not None:
        return node.value
    if max_player:
        v = float('-inf')
        for child in node.children:
            v = max(v, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = float('inf')
        for child in node.children:
            v = min(v, alpha_beta(child, depth-1, alpha, beta, True))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

# Create nodes and run alpha-beta pruning
A = Node('A', children=[Node('B', children=[Node('D', 3), Node('E', 12)]), Node('C', children=[Node('G', 9), Node('H', 2)])])
print(alpha_beta(A, 3, float('-inf'), float('inf'), True))