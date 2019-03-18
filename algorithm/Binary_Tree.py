# Binary_Tree
# 节点定义
class Node(object):
    def __init__(self, value = -1, Leftchild = None, Rightchidl = None):
        self.value = value
        self.Leftchild = Leftchild
        self.Rightchild = Rightchidl

class Binary_Tree(object):
    def __init__(self):
        self.root = Node()
        self.list = []

    # 向树中添加节点
    def Build(self, value):
        node = Node(value)
        if self.root.value == -1:          # 空树，则对根节点赋值
            self.root = node
            self.list.append(self.root)        # 记录根节点
        else:
            TreeNode = self.list[0]         # 获取父节点
            if TreeNode.Leftchild == None:
                TreeNode.Leftchild = node
                self.list.append(TreeNode.Leftchild)
            else:
                TreeNode.Rightchild = node
                self.list.append(TreeNode.Rightchild)
                self.list.pop(0)        # 如果一个节点的子节点都已经存在，则删除这个节点的记录

    # 队列实现树的层次遍历
    def Order(self, root):
        if root == None:
            return
        queue = []  # 队列用来记录进出的节点
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            print(node.value, end = ' ')
            if node.Leftchild != None:
                queue.append(node.Leftchild)
            if node.Rightchild != None:
                queue.append(node.Rightchild)

    #前序遍历
    def preOrder(self, root):
        if root == None:
            return
        print(root.value, end = ' ')
        self.preOrder(root.Leftchild)
        self.preOrder(root.Rightchild)

    #中序遍历
    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.Leftchild)
        print(root.value, end = ' ')
        self.inOrder(root.Rightchild)

    #后序遍历
    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.Leftchild)
        self.postOrder(root.Rightchild)
        print(root.value, end = ' ')


tree = Binary_Tree()
for value in range(10):
    tree.Build(value)
print('层次遍历的结果:')
tree.Order(tree.root)
print('\n前序遍历的结果:')
tree.preOrder(tree.root)
print('\n中序遍历的结果:')
tree.inOrder(tree.root)
print('\n后序遍历的结果:')
tree.postOrder(tree.root)
