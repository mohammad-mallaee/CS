class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.right.left = Node(30)
root.right.right = Node(35)
root.right.left.left = Node(40)


def print_depths(root):
    queue = []
    queue.append((root, 0))

    while len(queue) > 0:
        (node, depth) = queue.pop(0)
        print(node.data, depth)
        if node.right:
            queue.append((node.right, depth + 1))
        if node.left:
            queue.append((node.left, depth + 1))


def count_full_nodes(root):
    count = 0
    
    if not root.left and not root.right:
        return 1

    if root.left:
        count += count_full_nodes(root.left)
    if root.right:
        count += count_full_nodes(root.right)

    if root.right and root.right:
        count += 1

    return count


print_depths(root)
