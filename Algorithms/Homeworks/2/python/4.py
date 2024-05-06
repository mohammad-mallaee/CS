class Node:
    def __init__(self, name=None, parent=None) -> None:
        self.parent = parent
        self.name = name
        self.children: list["Node"] = []
        self.is_installed = None
        self.is_monitored = None

    def add_child(self, *nodes: "Node") -> None:
        for node in nodes:
            node.parent = self
        self.children.extend(nodes)

    def remove_child(self, node: "Node") -> None:
        self.children.remove(node)


def process_network_tree(root: Node):
    if len(root.children) == 0:
        if root.parent is None:
            return 1, [root.name]
        else:
            root.is_installed = False
            root.is_monitored = False
            return 0, []

    sofware_nodes = []
    softwares = 0

    for child in root.children:
        count, nodes = process_network_tree(child)
        sofware_nodes += nodes
        softwares += count

    x = any([not child.is_monitored for child in root.children])
    y = all([not child.is_installed for child in root.children])
    if x or y:
        root.is_installed = True
        root.is_monitored = True
        sofware_nodes = [root.name] + sofware_nodes
        softwares += 1
        root.parent.is_monitored = True
        for child in root.children:
            child.is_monitored = True

    return softwares, sofware_nodes


nodes = [None]
for i in range(1, 21):
    nodes.append(Node(i))

nodes[1].add_child(nodes[2], nodes[3], nodes[4])
nodes[2].add_child(nodes[5], nodes[6])
nodes[3].add_child(nodes[7])
nodes[4].add_child(nodes[8], nodes[9])
nodes[5].add_child(nodes[10])
nodes[6].add_child(nodes[11], nodes[12], nodes[13])
nodes[8].add_child(nodes[14])
nodes[10].add_child(nodes[15])
nodes[12].add_child(nodes[16], nodes[17])
nodes[14].add_child(nodes[18], nodes[19], nodes[20])
print(process_network_tree(nodes[1]))
