class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
                next_node = current.next    
                current.next = prev
                prev = current 
                current = next_node 
        
        self.head = prev
    
    # merge sort
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None
        
        left = self.merge_sort_util(self.head)
        right = self.merge_sort_util(next_to_middle)
        
        sorted_list = self.sorted_merge(left, right)
        self.head = sorted_list

    def merge_sort_util(self, head):
        if head is None or head.next is None:
            return head
        
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        
        left = self.merge_sort_util(head)
        right = self.merge_sort_util(next_to_middle)
        
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head
        
        slow = head
        fast = head.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        
        return result
    
    def merge_other_list(self, other):
        merged_list = LinkedList()
        
        p = self.head
        q = other.head
        
        if p is None:
            return other
        if q is None:
            return self
        
        if p.data <= q.data:
            merged_list.head = p
            p = p.next
        else:
            merged_list.head = q
            q = q.next
        
        current = merged_list.head
        
        while p and q:
            if p.data <= q.data:
                current.next = p
                p = p.next
            else:
                current.next = q
                q = q.next
            current = current.next
        
        if p is None:
            current.next = q
        else:
            current.next = p
        
        return merged_list
    
llist = LinkedList()

llist.insert_at_beginning(65)
llist.insert_at_beginning(30)
llist.insert_at_beginning(25)

llist.insert_at_end(96)
llist.insert_at_end(3)

print("Linked list:")
llist.print_list()

print("doing reverse...")
llist.reverse()

print("Reversed Linked list:")
llist.print_list()

print("doing merge sort...")
llist.merge_sort()

print("Sorted Linked list:")
llist.print_list()


llist_2 = LinkedList()

llist_2.insert_at_beginning(73)
llist_2.insert_at_beginning(27)
llist_2.insert_at_beginning(22)

print("List 2:")
llist_2.print_list()


print("doing merge to list 2...")

new = llist.merge_other_list(llist_2)

print("Sorted merged:")
new.print_list()