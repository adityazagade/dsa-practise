# Implementation of Binary Tree

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.count = 0


class BinaryTree:
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTree(args[0])
        else:
            for arg in args[0]:
                self.insert(arg)
    
    def insert(self, node_data):
        new_node = BinaryTreeNode(node_data)
        if self.root is None:
            self.root = new_node
        else:
            parent_node = None
            current_node = self.root
            while current_node:
                parent_node = current_node                
                if node_data <= current_node.data:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            if node_data <= parent_node.data:
                parent_node.left = new_node
            else:
                parent_node.right = new_node

    def find_in_bst(self, data):
        return self.find_in_bst_rec(self.root, data)

    def find_in_bst_rec(self, node, data):
        if not self.node:
            return None
        if self.node.data == data:
            return self.root
        elif self.node.data < data:
            return self.find_in_bst_rec(node.left, data)
        else:
            return self.find_in_bst_rec(node.right, data)

    def populate_parents(self):
        return self.populate_parents_rec(self.root, None);

    def populate_parents_rec(self, node, parent):
        if node:
            node.parent = parent
            self.populate_parents_rec(node.left, node)
            self.populate_parents_rec(node.right, node)
    
    def populate_count(self):
        self.populate_count_rec(self.root)

    def populate_count_rec(self, node):
        if node:
            node.count = self.get_sub_tree_node_count(node)
            self.get_sub_tree_node_count(node.left)
            self.get_sub_tree_node_count(node.right)

    def get_sub_tree_node_count(self, node):
        if not node:
            return 0
        else:
            return 1 +  self.get_sub_tree_node_count(node.left) + self.get_sub_tree_node_count(node.right)
        
    # get_tree_deep_copy is used to make a deep copy of the BinaryTree
    def get_tree_deep_copy(self):
        if not self.root:
            return None
        else:
            tree_copy = BinaryTree()
            tree_copy.root = self.get_tree_deep_copy_rec(self.root)
            return tree_copy
    
    # get_tree_deep_copy_rec is a helper function used by get_tree_deep_copy
    def get_tree_deep_copy_rec(self, node):
        if node:
            new_node = BinaryTreeNode(node.data)
            new_node.left = self.get_tree_deep_copy_rec(node.left)
            new_node.right = self.get_tree_deep_copy_rec(node.right)
            return new_node
        else:
            return None
        
    # insert_bt inserts a given key into the binary tree
    # insert_bt is used for normal binary tree level by level insertion
    def insert_bt(self, key):
        temp_queue = []
        temp = self.root

        temp_queue.append(temp)

        while temp_queue:
            temp = temp_queue[0]
            temp_queue.pop(0)

            if not temp.left:
                temp.left = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.left)

            if not temp.right:
                temp.right = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.right)
