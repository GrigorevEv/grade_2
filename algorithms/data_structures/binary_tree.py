from typing import Tuple


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def append(self, data):
        appended_node = Node(data)

        if self.root is None:
            self.root = appended_node
            return

        node_to_append, _, flag_find = self._find(self.root, None, data)

        if not flag_find:
            if appended_node.data < node_to_append.data:
                node_to_append.left = appended_node
            else:
                node_to_append.right = appended_node

    def delete(self, data):
        node_to_delete, parent, flag_find = self._find(self.root, None, data)

        if not flag_find:
            return

        if node_to_delete.left is None and node_to_delete.right is None:
            self._del_leaf(node_to_delete, parent)
        elif node_to_delete.left is None or node_to_delete.right is None:
            self._del_one_child(node_to_delete, parent)
        else:
            min_node, parent = self._find_min(
                node_to_delete.right, node_to_delete)
            node_to_delete.data = min_node.data
            self._del_one_child(min_node, parent)

    def search(self, data):
        current = self.root
        while True:
            if current is None:
                return
            elif current.data == data:
                return data
            elif current.data > data:
                current = current.left
            else:
                current = current.right

    def display(self, node):
        lines, *_ = self._display_aux(node)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + \
                shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + \
                shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + \
            s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + \
            '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def _find(self, node, parent, data) -> Tuple[Node, Node, bool]:
        if data == node.data:
            return node, parent, True

        if data < node.data:
            if node.left:
                return self._find(node.left, node, data)

        if data > node.data:
            if node.right:
                return self._find(node.right, node, data)

        return node, parent, False

    def _del_leaf(self, node, parent):
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None

    def _del_one_child(self, node, parent):
        if parent.left == node:
            if node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left
        elif parent.right == node:
            if node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left

    def _find_min(self, node, parent):
        if node.left:
            return self._find_min(node.left, node)
        return node, parent


if __name__ == '__main__':
    data_list = [10, 5, 7, 16, 13, 2, 20, 3, 44, 27, 18, 67, 17, 19, 11, 15]
    tree = Tree()
    for data in data_list:
        tree.append(data)
    tree.display(tree.root)
    tree.delete(16)
    tree.display(tree.root)
    tree.delete(17)
    tree.display(tree.root)
    print(tree.search(13))
