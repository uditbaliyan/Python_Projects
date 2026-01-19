class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")


def create_binarytree(root: TreeNode) -> None:
    temp = root
    for i in range(0, 20):
        abc = TreeNode(data=i)
        temp.left = abc
        temp = abc
    temp = root
    for i in range(0, 20):
        abc = TreeNode(data=i)
        temp.right = abc
        temp = abc


def main():
    root = TreeNode(10)
    create_binarytree(root)
    # preOrderTraversal(root)
    # inOrderTraversal(root)
    postOrderTraversal(root)


if __name__ == "__main__":
    main()
