from dataclasses import dataclass


@dataclass
class TreeNode:
    data: int
    left = None
    right = None


def create_bst() -> TreeNode:
    root = TreeNode(data=100)
    temp = root
    for i in range(98, 0, -1):
        node = TreeNode(data=i)
        temp.left = node
        temp = node
    temp = root
    for i in range(100, 200):
        node = TreeNode(data=i)
        temp.right = node
        temp = node
    return root


def preOrderTraversal(node) -> None:
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def inOrderTraversal(node) -> None:
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


def postOrderTraversal(node) -> None:
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")


def search(node: TreeNode, target: int) -> TreeNode | None:
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)


def main() -> None:
    root: TreeNode = create_bst()
    # inOrderTraversal(root)
    # preOrderTraversal(root)
    postOrderTraversal(root)
    result = search(root, 330)
    if result:
        print(f"Found the node with value: {result.data}")
    else:
        print("Value not found in the BST.")


if __name__ == "__main__":
    main()
