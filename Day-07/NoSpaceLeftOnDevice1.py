import fileinput
from anytree import Node, RenderTree, Resolver, PreOrderIter

root_node = Node("root", size=0)
current_node = root_node
resolver = Resolver('name')

for raw_line in fileinput.input():

    line_tokens = raw_line.split()

    print(f"current node = {current_node.path}")

    match line_tokens:
        case ["$", "cd", "/"]:
            print( f"command=cd, dirname=/")
            current_node = root_node
        case ["$", "ls"]:
            print( f"command=ls")
        case ["$", "cd", dirname]:
            print( f"command=cd, dirname={dirname}")
            current_node = resolver.get(current_node, dirname)
        case ["dir", dirname]:
            print( f"directory = {dirname}")
            temp_node = Node(dirname, parent=current_node, size=0)
            print( f"added {temp_node.path}")
        case _:
            print( f"file size={line_tokens[0]} name={line_tokens[1]}")
            temp_node = Node(line_tokens[1], parent=current_node, size=int(line_tokens[0]))

for one_node in PreOrderIter(root_node):
    if one_node.is_leaf:
        for one_dir in one_node.ancestors:
            one_dir.size += one_node.size

print(RenderTree(root_node))

result = 0
for one_dir in PreOrderIter(root_node):
    if (not one_dir.is_leaf) and (one_dir.size <= 100000):
        print( one_dir )
        result += one_dir.size

print( result )
