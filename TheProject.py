import tkinter as tk
from tkinter import ttk
from collections import defaultdict
import sys
import os

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

class BSTNode:
    def __init__(self, priority_key):
        self.priority_key = priority_key
        self.left = None
        self.right = None
        self.tasks = []

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

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        self.master.geometry("600x500")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, 'app_icon.ico')
        try:
            if hasattr(sys, '_MEIPASS'):
                self.master.iconbitmap(os.path.join(sys._MEIPASS, 'app_icon.ico'))
            else:
                self.master.iconbitmap(icon_path)
        except Exception as e:
            print(f"Warning: {e}")

        self.tasks_list = LinkedList()
        self.hash_table = defaultdict(list)
        self.bst = BST()

        self.setup_styles()
        self.setup_gui()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('TCombobox', font=('Helvetica', 12))
        self.style.configure('TCheckbutton', background='#f0f0f0', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='#ffffff', background='#ff0000')  # Red buttons
        self.style.map('TButton', background=[('active', '#cc0000')])  # Darker red on hover

        self.style.configure('Treeview', font=('Helvetica', 12), rowheight=25, fieldbackground='#ffffff')
        self.style.configure('Treeview.Heading', font=('Helvetica', 13, 'bold'), background='#ff0000', foreground='#ffffff')  # Red headers
        self.style.map('Treeview.Heading', background=[('active', '#cc0000')])

    def setup_gui(self):
        entry_frame = ttk.Frame(self.master, padding="10 10 10 10", relief='raised')
        entry_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(entry_frame, text="Description:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.description_entry = ttk.Entry(entry_frame, width=40)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(entry_frame, text="Priority:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.priority_combobox = ttk.Combobox(entry_frame, values=['High', 'Medium', 'Low'], state='readonly')
        self.priority_combobox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.priority_combobox.set('Medium')

        self.status_var = tk.BooleanVar()
        self.status_checkbutton = ttk.Checkbutton(entry_frame, text="Completed", variable=self.status_var)
        self.status_checkbutton.grid(row=2, column=1, sticky=tk.W, pady=5)

        self.add_button = ttk.Button(entry_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=1, pady=10, sticky=tk.E)

        search_frame = ttk.Frame(self.master, padding="5 5 5 5", relief='raised')
        search_frame.pack(padx=10, pady=5, fill=tk.X)

        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        self.search_button = ttk.Button(search_frame, text="Search", command=self.search_task)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        display_frame = ttk.Frame(self.master, padding="5 5 5 5", relief='raised')
        display_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(display_frame, columns=('Description', 'Priority', 'Status'), show='headings')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Priority', text='Priority')
        self.tree.heading('Status', text='Status')
        self.tree.column('Description', width=250)
        self.tree.column('Priority', width=100, anchor='center')
        self.tree.column('Status', width=100, anchor='center')
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        control_frame = ttk.Frame(self.master, padding="5 5 5 5", relief='raised')
        control_frame.pack(padx=10, pady=5, fill=tk.X)

        ttk.Label(control_frame, text="Display Mode:").pack(side=tk.LEFT, padx=5)
        self.display_mode = tk.StringVar(value='insertion')
        ttk.Radiobutton(control_frame, text="Insertion Order", variable=self.display_mode, value='insertion', command=self.update_display).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(control_frame, text="Priority", variable=self.display_mode, value='priority', command=self.update_display).pack(side=tk.LEFT, padx=5)

        ttk.Label(control_frame, text="Filter:").pack(side=tk.LEFT, padx=10)
        self.filter_status = tk.StringVar(value='all')
        self.filter_combobox = ttk.Combobox(control_frame, textvariable=self.filter_status, values=['all', 'completed', 'incomplete'], state='readonly', width=12)
        self.filter_combobox.pack(side=tk.LEFT, padx=5)
        self.filter_status.trace('w', lambda *args: self.update_display())

        self.delete_button = ttk.Button(control_frame, text="Delete Selected", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=5)

    def add_task(self):
        description = self.description_entry.get().strip()
        priority = self.priority_combobox.get().strip()
        status = self.status_var.get()

        if not description or priority not in ['High', 'Medium', 'Low']:
            return

        new_task = Task(description, priority, status)
        self.tasks_list.append(new_task)
        new_node = self.tasks_list.tail

        self.hash_table[new_task.description].append(new_node)

        priority_key = self.priority_to_key(new_task.priority)
        self.bst.insert(priority_key, new_node)

        self.description_entry.delete(0, tk.END)
        self.status_var.set(False)
        self.update_display()

    def priority_to_key(self, priority):
        return {'High': 3, 'Medium': 2, 'Low': 1}.get(priority, 0)

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        display_mode = self.display_mode.get()
        filter_status = self.filter_status.get()

        tasks_with_nodes = []
        if display_mode == 'priority':
            self.collect_tasks_with_nodes_by_priority(self.bst.root, tasks_with_nodes)
        else:
            current = self.tasks_list.head
            while current:
                tasks_with_nodes.append((current.task, current))
                current = current.next

        for task, node in tasks_with_nodes:
            if filter_status == 'all' or \
               (filter_status == 'completed' and task.status) or \
               (filter_status == 'incomplete' and not task.status):
                status = 'Completed' if task.status else 'Incomplete'
                self.tree.insert('', 'end', values=(task.description, task.priority, status), tags=(id(node),))

    def collect_tasks_with_nodes_by_priority(self, node, tasks_with_nodes):
        if node:
            self.collect_tasks_with_nodes_by_priority(node.right, tasks_with_nodes)
            for list_node in node.tasks:
                tasks_with_nodes.append((list_node.task, list_node))
            self.collect_tasks_with_nodes_by_priority(node.left, tasks_with_nodes)

    def search_task(self):
        query = self.search_entry.get().strip()
        if not query:
            self.update_display()
            return

        tasks = []
        for desc, nodes in self.hash_table.items():
            if query.lower() in desc.lower():
                for node in nodes:
                    tasks.append((node.task, node))

        for row in self.tree.get_children():
            self.tree.delete(row)

        for task, node in tasks:
            status = 'Completed' if task.status else 'Incomplete'
            self.tree.insert('', 'end', values=(task.description, task.priority, status), tags=(id(node),))

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item_tags = self.tree.item(selected_item[0], 'tags')
        if not item_tags:
            return

        node_id = int(item_tags[0])
        current_node = self.tasks_list.head
        while current_node:
            if id(current_node) == node_id:
                task = current_node.task

                self.tasks_list.remove(current_node)

                if task.description in self.hash_table:
                    nodes = self.hash_table[task.description]
                    if current_node in nodes:
                        nodes.remove(current_node)
                        if not nodes:
                            del self.hash_table[task.description]

                priority_key = self.priority_to_key(task.priority)
                bst_node = self.bst.find(priority_key)
                if bst_node and current_node in bst_node.tasks:
                    bst_node.tasks.remove(current_node)

                break
            current_node = current_node.next

        self.update_display()

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()