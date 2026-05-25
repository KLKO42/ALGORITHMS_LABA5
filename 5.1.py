class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, target):
    if root is None or root.value == target:
        return root
    if target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)  
        result.append(root.value)        
        inorder(root.right, result)         
    return result
    
def height(root):
    if root is None:
        return -1
    left_h = height(root.left)
    right_h = height(root.right)
    return 1 + max(left_h, right_h)

# пример работы функций
if __name__ == "__main__":
    print("БИНАРНОЕ ДЕРЕВО ПОИСКА")

    # 1. ВСТАВКА
    root = None
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 65]

    for v in values:
        root = insert(root, v)

    # 2. Inorder обход
    sorted_list = inorder(root)
    print(f"   РЕЗУЛЬТАТ: {sorted_list}")

    # 3. ПОИСК
    test_cases = [40, 90, 25, 10, 100]

    for target in test_cases:
        node = search(root, target)
        if node:
            print(f"   {target}: НАЙДЕН (УЗЕЛ = {node.value})")
        else:
            print(f"   {target}: НЕ НАЙДЕН")

    # ВАРИАТИВНАЯ ЧАСТЬ:
    h = height(root)
    print(f"   ВЫСОТА={h}")   
