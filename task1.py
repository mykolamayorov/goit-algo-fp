class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return merge_sorted_lists(left, right)


def get_middle(head):
    if head is None:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    # Приклад: створюємо список 4 -> 2 -> 1 -> 3
    nodes = [Node(i) for i in [4, 2, 1, 3]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    print("Оригінальний список:")
    print_list(head)

    # Сортуємо список
    sorted_head = merge_sort(head)
    print("Відсортований список:")
    print_list(sorted_head)

    # Реверсуємо список
    reversed_head = reverse_list(sorted_head)
    print("Реверсований список:")
    print_list(reversed_head)

    # Створюємо ще один відсортований список 0 -> 5 -> 6
    nodes2 = [Node(i) for i in [0, 5, 6]]
    for i in range(len(nodes2) - 1):
        nodes2[i].next = nodes2[i + 1]
    head2 = nodes2[0]

    print("Другий відсортований список:")
    print_list(head2)

    # Об'єднуємо два відсортовані списки
    merged = merge_sorted_lists(sorted_head, head2)
    print("Об'єднаний відсортований список:")
    print_list(merged)