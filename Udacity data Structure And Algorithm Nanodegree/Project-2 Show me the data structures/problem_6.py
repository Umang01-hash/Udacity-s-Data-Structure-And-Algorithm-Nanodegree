  
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None  #Setting the head pointer to none.
    

    
    def append(self, value):
        
        if self.head is None:  #Making the first element as the head of the list if head pointer is none
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:  #Adding the nodes nodes after head
            node = node.next
        
        node.next = Node(value)
    
    def size(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next

        return length

    def __str__(self):
        currentHead = self.head
        OutputString = ""
        while currentHead:
            OutputString += str(currentHead.value) + " ,  "
            currentHead = currentHead.next
        return OutputString



def union(llist_1, llist_2):

    final = LinkedList() #Initialzing new node
    temporaryList = []
    node1 = llist_1.head #Head Of linked list 1
    node2 = llist_2.head#Head of linked list 2

    while node1 != None:
        if node1.value not in temporaryList:
            temporaryList.append(node1.value)
        node1 = node1.next
    while node2 != None:
        if node2.value not in temporaryList:
            temporaryList.append(node2.value)
        node2 = node2.next

        #Appended the values of linked list 1 and linked list 2 successfully in temporary list
    for i in temporaryList:
        final.append(i)  #for craeting the final linked list i.e. union of linked list 1 and linked list 2
    return final

def intersection(llist_1, llist_2):

    final = LinkedList()
    node1 = llist_1.head
    tmp_lst = []
    while node1 != None:
        node2 = llist_2.head
        while node2 != None:
            if node1.value == node2.value:
                if node1.value not in tmp_lst:
                    tmp_lst.append(node1.value)

            node2 = node2.next
        node1 = node1.next
    for i in tmp_lst:
        final.append(i)
    return final
# CASE 1 Both Union And Intersection

ll1 = LinkedList()
ll2 = LinkedList()

list1 = [3,2,4,35,6,65,6,4,3,21]
list2 = [6,32,4,9,6,1,11,21,1]

for i in list1:
    ll1.append(i)

for i in list2:
    ll2.append(i)

print ("U N I O N = ",union(ll1,ll2))
print ("I N T E R S E C T I O N = ",intersection(ll1,ll2))

#CASE 2 : NO INTERSECTION

linkedlist3 = LinkedList()
linkedlist4 = LinkedList()

a = [3,2,4,35,6,65,6,4,3,23]
b = [1,7,8,9,11,21,1]

for i in a:
    linkedlist3.append(i)

for i in b:
    linkedlist4.append(i)

print ("U  N I O N = ",union(linkedlist3,linkedlist4))
print ("I N T E R S E C T I O N =",intersection(linkedlist3,linkedlist4))

