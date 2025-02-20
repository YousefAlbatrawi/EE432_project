class Task:
    def __init__(self, description, priority, status=False):
        self.description = description
        self.priority = priority
        self.status = status

class ListNode:
    def __init__(self, task):
        self.task = task
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, task):
        new_node = ListNode(task)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1

class BST:
    def __init__(self):
        self.root = None

    def insert(self, priority_key, list_node):
        if not self.root:
            self.root = BSTNode(priority_key)
            self.root.tasks.append(list_node)
            return
        current = self.root
        while True:
            if current.priority_key == priority_key:
                current.tasks.append(list_node)
                return
            elif priority_key > current.priority_key:
                if current.right:
                    current = current.right
                else:
                    current.right = BSTNode(priority_key)
                    current.right.tasks.append(list_node)
                    return
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = BSTNode(priority_key)
                    current.left.tasks.append(list_node)
                    return

    def find(self, priority_key):
        current = self.root
        while current:
            if current.priority_key == priority_key:
                return current
            elif priority_key > current.priority_key:
                current = current.right
            else:
                current = current.left
        return None


