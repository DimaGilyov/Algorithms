"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import deque
from collections import Counter


class NodeData:
    def __init__(self, count, char=None):
        self.char = char
        self.count = count

    def __str__(self):
        return f"char:{self.char}, count:{self.count}"


class Node:
    def __init__(self, data: NodeData, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        text = f"data:{self.data}"
        if self.left:
            text += f"\nleft:{self.left}"
        if self.left:
            text += f"\nleft:{self.left}"
        return text


def huffman_encode(text):
    nodes = get_nodes(text)
    tree = build_tree(nodes)
    table = get_huffman_table(tree)
    code = ""
    for char in text:
        code += f"{table[char]} "
    return code.strip()


def get_nodes(text: str) -> deque:
    chars_and_counts = Counter(text)
    chars_and_counts = dict(sorted(chars_and_counts.items(), key=lambda item: item[1]))
    nodes = deque([Node(NodeData(count, char)) for char, count in chars_and_counts.items()])
    return nodes


def build_tree(nodes: deque):
    left_node = None
    tree = None
    while len(nodes) >= 1:
        current_node = nodes.popleft()
        if left_node:
            count = left_node.data.count + current_node.data.count
            new_node = Node(NodeData(count), left_node, current_node)

            is_inserted = False
            if new_node.data.count == 7:
                print()
            for i, node in enumerate(nodes):
                index = i
                if new_node.data.count <= node.data.count:
                    nodes.insert(index, new_node)
                    is_inserted = True
                    break
            if not is_inserted:
                nodes.append(new_node)

            tree = new_node
            left_node = None
        else:
            left_node = current_node

    return tree


def get_huffman_table(tree, code=''):
    table = dict()
    if tree.left:
        table.update(get_huffman_table(tree.left, f"{code}0"))
    if tree.right:
        table.update(get_huffman_table(tree.right, f"{code}1"))

    if tree.data.char:
        table[tree.data.char] = code
    return table


if __name__ == "__main__":
    huffman_code = huffman_encode("beep boop beer!")
    print(huffman_code)
