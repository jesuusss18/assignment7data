class DoctorNode:
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self,root_name = None):
        if root_name:
            self.root = DoctorNode(root_name)
        else:
            self.root = None
    
    def insert(self,parent_node,doctor_name,side = "left"):
        new_node = DoctorNode(doctor_name)
        if side == 'left':
            if parent_node.left == None:
                parent_node.left = new_node
            else:
                print(f"Left child of {parent_node.name} is already in use")
        elif side == "right":
            if parent_node.right == None:
                parent_node.right = new_node
            else:
                print(f"Right child of {parent_node.name} is already in use")
    
    def preorder(self,node):
        if node:
            print(node.name)
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.name)
            self.inorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.name)

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 
tree.insert(tree.root, "Dr. Goldsmith", "right")
tree.insert(tree.root, "Dr. Phan", "left")
tree.insert(tree.root.left, "Dr. Morgan", "left") 
tree.insert(tree.root.left, "Dr. Carson", "right")

print("Preorder Traversal:")
tree.preorder(tree.root)

print("Inorder Traversal:")
tree.inorder(tree.root)

print("Postorder Traversal:")
tree.postorder(tree.root)