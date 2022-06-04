from subscriber import Subscriber


class Node:
    def __init__(self, data: Subscriber = None):
        self.data: Subscriber = data
        self.next: Node = None


class ClosedUnidirectionalLinkedList:
    def __init__(self):
        self.head: Node = Node(None)
        self.tail: Node = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    # add a subscriber to list
    def add_subscriber(self, data: Subscriber):
        new_node: Node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    #  print all elements of list
    def print_list(self):
        current: Node = self.head
        if self.head.data is None:
            print("List is empty!")
        else:
            print(current.data, end='\n'),
            while current.next != self.head:
                current = current.next
                print(current.data, end='\n')

    # return some element
    def get(self, index: int) -> Subscriber:
        k = 0
        current: Node = self.head
        if self.head.data is None:
            print("List index out of range")
        else:
            if k == index:
                return current.data
            else:
                while current.next != self.head:
                    k += 1
                    current = current.next
                    if k == index:
                        return current.data
                    elif k > index:
                        print("List index out of range")

    # get information about data from element
    def get_information_about_person(self, index: int):
        k = 0
        current: Node = self.head
        if self.head.data is None:
            print("List index out of range")
        else:
            if k == index:
                print(current.data, end='\n')
                return
            else:
                while current.next != self.head:
                    k += 1
                    current = current.next
                    if k == index:
                        print(current.data, end='\n')
                        return
                    elif k > index:
                        print("List index out of range")

    # output information about device, which have same limit of measurement
    def find_a_person_with_surname(self, specific_surname: int):
        current: Node = self.head
        if self.head.data is None:
            print("List is empty!")
        else:
            k = self.__length()
            if current.data.get_surname() == specific_surname:
                print(current.data, end='')
                k -= 1
            while current.next != self.head:
                current = current.next
                if current.data.get_surname() == specific_surname:
                    print(current.data, end='')
                    k -= 1
            if k == self.__length():
                print("There are no one with this surname")

    # find a length of list (number of elements)
    def __length(self):
        if self.head.data is None:
            return 0
        else:
            current: Node = self.head
            length = 1
            while current.next:
                if current.next == self.head:
                    break
                current = current.next
                length += 1
            return length

    # add head to list
    def __add_head(self, data: Subscriber):
        new_node: Node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    # add tail to list
    def __add_tail(self, data: Subscriber):
        new_node: Node = Node(data)
        if self.head.data is None:
            self.__add_head(data)
        else:
            temporary_node: Node = self.head
            n = 1
            length = self.__length()
            while n < length:
                n += 1
                temporary_node = temporary_node.next
            temporary_node.next = new_node
            new_node.next = self.head
            self.tail = new_node

    # Add new sub in sorted list
    def put_by_phone_number_sorted_list(self, data: Subscriber):
        current: Node = self.head
        if self.head.data is None:
            self.__add_head(data)
        else:
            if data.get_phone_number() > current.data.get_phone_number():
                self.__add_head(data)
                return
            else:
                index = 1
                while current.next != self.head:
                    if data.get_phone_number() > current.data.get_phone_number():
                        new_node: Node = Node(data)
                        temporary_node: Node = self.head
                        n = 1
                        while n < index - 1:
                            temporary_node = temporary_node.next
                            n += 1
                        a: Node = temporary_node.next
                        temporary_node.next = new_node
                        new_node.next = a
                        return
                    elif self.__length() - 1 == index:
                        self.__add_tail(data)
                        return
                    index += 1
                    current = current.next

    #  delete an sub details
    def delete_person_details_with_index(self, index: int):
        if self.head.data is None:
            return
        current: Node = self.head
        length = self.__length()
        if index == 0:
            self.head = current.next
            self.tail.next = self.head
        elif index == length - 1:
            n = 1
            while n < length - 1:
                current = current.next
                n += 1
            current.next = self.head
            self.tail = current
        else:
            n = 1
            while n < index - 1:
                current = current.next
                n += 1
            temporary_node: Node = current.next.next
            current.next = temporary_node

    #  delete the list
    def delete(self):
        print("LinkedList has deleted")
        del self
