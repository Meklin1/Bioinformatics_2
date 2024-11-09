from ete3 import Tree

tree = Tree("phylogenetic_tree.tree")
outgroup = tree & "MN514967.1_4901_8458" # camel virus
tree.set_outgroup(outgroup)
print(tree)
tree.write(format=1, outfile="rooted_phylogenetic_tree.tree")
