class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node to delete found
            if node.left is None:   # No left child
                return node.right
            if node.right is None:  # No right child
                return node.left
            # Two children: replace with in-order successor (min of right subtree)
            successor = self._min_node(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    # Traversals
    def inorder(self):    # Left → Root → Right (sorted order)
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def preorder(self):   # Root → Left → Right
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):  # Left → Right → Root
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)


# --- Demo ---
bst = BST()
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)

print("Inorder (sorted):", bst.inorder())   # [1, 3, 4, 5, 6, 7, 8]
print("Preorder:        ", bst.preorder())   # [5, 3, 1, 4, 7, 6, 8]
print("Postorder:       ", bst.postorder())  # [1, 4, 3, 6, 8, 7, 5]

print("Search 4:", bst.search(4).val)        # 4
print("Search 9:", bst.search(9))            # None

bst.delete(3)
print("After deleting 3:", bst.inorder())    # [1, 4, 5, 6, 7, 8]