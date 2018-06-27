class Node(object):

    def __init__(self, ID, parent=None, children=None):
        self.id = ID
        self.parent = parent
        if children is None:
            self.children = []
        else:
            self.children = children

    def child_append(self, other):
        if isinstance(other, list):
            self.children += other
        else:
            self.children.append(other)


def main():
    nodes, non_leaf = [int(_) for _ in input().split()]
    if nodes == 1:
        print("1", end='')
        return

    nodes_dict = {}

    for i in range(non_leaf):
        leaf_id, children, *children_id = input().split()
        if leaf_id not in nodes_dict:
            leaf_node = Node(ID=leaf_id)
            nodes_dict[leaf_id] = leaf_node
        else:
            leaf_node = nodes_dict[leaf_id]

        for child in children_id:
            if child not in nodes_dict:
                child_node = Node(ID=child, parent=leaf_node)
                nodes_dict[child] = child_node
            else:
                child_node = nodes_dict[child]
                child_node.parent = leaf_node

            leaf_node.child_append(child_node)

    root_queue = [nodes_dict['01']]
    res = []

    def recursive(layer_queue):
        nonlocal res
        if layer_queue:
            non_leaf_num = 0
            next_queue = []
            for node in layer_queue:
                if not node.children:
                    non_leaf_num += 1
                else:
                    next_queue += node.children

            res.append(non_leaf_num)
            recursive(next_queue)

    recursive(root_queue)
    res = [str(_) for _ in res]
    print(' '.join(res), end='')

if __name__ == '__main__':
    main()
    
