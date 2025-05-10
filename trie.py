# python3
import sys

def build_trie(patterns):
    tree = dict()
    node_id = 0
    tree[node_id] = dict()
    for pattern in patterns:
        current_node = 0
        for symbol in pattern:
            if symbol in tree[current_node]:
                current_node = tree[current_node][symbol]
            else:
                node_id += 1
                tree[current_node][symbol] = node_id
                tree[node_id] = dict()
                current_node = node_id
    return tree

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    patterns = input_data[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))