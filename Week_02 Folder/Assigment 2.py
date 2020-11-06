# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # method to update the data of the Node
    def updateData(self, data):
        self.data = data

    # method to set Link for the Next Node
    def setLink(self, node):
        self.link = node

    # method returns data stored in the Node
    def getData(self):
        return self.data

    # method returns address of the next Node // goes to the Next Node
    def getNextNode(self):
        return self.link

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # method adds elements to the left of the Linked List
    def addToStart(self, data):  # 21
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # method adds elements to the right of the Linked List
    def addToEnd(self, data):  # data = 16
        start = self.head
        tempNode = Node(data)  # data = 16 : link = None
        # start  = 5
        # reach the last element TAIL
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True

    # method displays Linked List
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method returns length of linked list
    def length(self):
        start = self.head
        size = 0
        while start:  # start != None
            size += 1
            start = start.getNextNode()
        # print(size)
        return size

    # method returns index of the recieved data
    def index(self, data):
        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            else:
                position += 1
                start = start.getNextNode()

    # method removes item passed from the Linked List
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns max element from the List
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    # method returns minimum element of Linked list
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

    # method removes and returns the last element from the Linked List
    def pop(self):
        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data

    # method to clear LinkedList
    def clear(self):
        self.head = None
        return True

    # method returns count of Element recieved
    def count(self, element):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1

    ## ----Assignment2-----
    # method display first k elements in Linked List
    def first(self, k):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start and k:
            print(str(start.getData()), end=" ")
            start = start.link
            k -= 1
            if start and k != 0:
                print("-->", end=" ")
        print()
        if k != 0:
            print("pending {} elements".format(k))

    # push in O(1)
    def push(self, data):
        start = self.tail
        if start is None:
            self.addToStart(data)
        else:
            tempNode = Node(data)
            start.setLink(tempNode)
            del tempNode
            self.tail = start.link
        return True

    # method to reverse the element in linked list
    def reverseH(self):
        previous = None
        start = self.head

        while start is not None:
            next = start.link
            start.link = previous
            previous = start
            start = next

        self.head = previous

    def reverseE(self, list2):
        list2.clear()
        start = self.head

        while start:
            list2.addToStart(start.getData())
            start = start.getNextNode()

    # copy linked list to new linked list
    def copyList(self, list2):
        list2.clear()
        start = self.head

        while start:
            list2.push(start.getData())
            start = start.getNextNode()

    # convert linked list to a list
    def listArray(self):
        cur = self.head
        size = self.length()
        arr = []

        while cur:
            arr.append(cur.getData())
            cur = cur.getNextNode()

        for i in range(size):
            print("{}".format(arr[i]), end=" ")

    # check if the linked list is sorted or not
    def checkSort(self):
        cur = self.head
        next = cur.getNextNode()
        order = 0

        if cur is None:
            print("Empty List!!!")
            return False

        while next:
            if next.getData() > cur.getData():
                if order == 0:
                    order = 1
                elif order == -1:
                    return False
            elif next.getData() < cur.getData():
                if order == 0:
                    order = -1
                elif order == 1:
                    return False
            current = next
            next = next.getNextNode()

        return True

    # Swap 2 elements in the linked list
    def swap(self, x, y):
        cur = self.head
        k = 1
        swapx = None
        swapy = None

        while cur:
            if k is x:
                swapx = cur
            if k is y:
                swapy = cur
            cur = cur.getNextNode()
            k += 1

        if swapx and swapy:
            t = swapx.getData()
            swapx.updateData(swapy.getData())
            swapy.updateData(t)
        else:
            print("List is not big enough")


# creating LinkedList
myList = LinkedList()
secList = LinkedList()

# adding some elements to the start of LinkedList
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)
# 1 -> 2 -> 3 -> 4 -> 5 -> None

myList.display()

# adding some elements to the End of the LinkedList
myList.addToEnd(12)
myList.addToEnd(13)
myList.addToEnd(3)
myList.display()
# 1 -> 2 -> 3 -> 4 -> 5 -> 13 -> 3 -> 31
# printing Length
print(myList.length())

# printing index of an element
print(myList.index(12))

# removing an element
print(myList.remove(12))

myList.display()

# printing max and min element
print(myList.Max())
print(myList.Min())

# pushing and poping elements
print(myList.push(31))
myList.display()
print(myList.pop())
myList.display()

# printing count of particular element in the List
print(myList.count(3))

print(myList.clear())
myList.display()

# adding some elements to the start of LinkedList
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)
# 1 -> 2 -> 3 -> None

myList.display()

# adding some elements to the End of the LinkedList
myList.addToEnd(12)
myList.addToEnd(13)
myList.display()
# 1 -> 2 -> 3 -> 12 -> 13 -> None

# display some of the element in list
myList.first(2)
myList.first(5)

# push in O(1)
myList.push(7)
myList.addToStart(20)
myList.display()

# reverse element in the list
myList.reverseH()
myList.display()

myList.reverseE(secList)
secList.display()

# check and sort the list
print(myList.checkSort())

# swap 2 elements in the list
myList.swap(1, 6)
myList.display()

# copy the linked list
myList.copyList(secList)
secList.display()

# convert linked list to list
myList.listArray()
