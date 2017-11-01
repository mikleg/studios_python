class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next



def delete_at_index(linked_list, index):
    if linked_list is None:
        return None
    if index == 0:

        linked_list = linked_list.next
        return linked_list

    current = linked_list
    i = 0
    while current.next is not None:
        if i == index - 1:
            current.next = current.next.next
            return linked_list
        i = i + 1
        current = current.next

    return linked_list

def read(linked_list, index):
    if linked_list is None:
        return None
    head = linked_list
    for i in range(0, index+1):
        if i == index:
            return head.value
        if head.next is None:
            return None
        head = head.next
    return None


def is_anagram(str1, str2):
    if len(str2) != len(str1):
        return False
    my_dict = {}
    for symb in str1:
        if symb in my_dict:
            my_dict[symb] += 1
        else:
            my_dict[symb] = 1
    for symb in str2:
        if symb not in my_dict:
            return False
        else:
            if my_dict[symb] > 0:
                my_dict[symb] -= 1
            else:
                return False

    return True

head = Node(1, None)
head = Node(2, head)
head = Node(3, head)
head = Node(4, head)

#head = delete_at_index(head, 3)

#print(head.value, head.next.value, head.next.next.value)
print(read(head, 0), read(head, 1), read(head, 2), read(head, 3))
# print(head.value, head.next.value, head.next.next.value, head.next.next.next.value)

