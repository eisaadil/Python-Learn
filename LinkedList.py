class Node():
    def __init__(self, val = None, link=None):
        self.val = val
        self.link = link

class LinkedList():
    def __init__(self):
        self.root = Node()
    
    def __str__(self):
        x = []
        while(self.root):
            x.append(self.root.val) 
            self.root = self.root.link
        return str(x)

    def addElement(self, val):
        if (not self.root.val): #empty LL
            self.root = Node(val)
            return
        t = self.root
        while(t.link):
            t = t.link
        t.link = Node(val)

    def deleteElement(self, val):
        if (self.root.val is val): #first element
            self.root = self.root.link
            return
        p = self.root
        t = self.root.link
        while(t):
            if t.val is val:
                p.link = t.link
                return
            else:
                p = p.link
                t = t.link
        return

    def deleteElementK(self,k): #k 0..n-1
        if (k is 0):
            self.root = self.root.link
        t = self.root
        i = 1
        while(t.link and i<k):
            t = t.link
            i+=1
        if (t.link):
            t.link = t.link.link
        return
        
    def noOfElements(self):
        if (not self.root): return 0
        i = 1
        t = self.root
        while (t.link):
            i+=1
            t = t.link
        return i

    def insertElementK(self, k, val):
        if (k == 0):
            self.root = Node(val, self.root)
            return
        
        t = self.root.link
        p = self.root
        for i in range(1,k):
            if (t):
                p = p.link
                t = t.link
            else:
                break
        if (t):
            p.link = Node(val, t)
        else:
            p.link = Node(val)
    
    def reverseList(self):
        head = self.root

        if (not head or not head.link): #For zero or one elements
            self.root = head #return null or that single node
            return

        t = head #first element
        n = t.link #second element
        new = n.link #third element
        n.link = t
        t.link = None #first element's link is None because it will be the last element

        if(not new): #For two elements
            self.root = n
            return
        
        while(1):
            t = n
            if (new): n = new
            if (n and n.link):
                new = n.link
                n.link = t
            else:
                n.link = t
                self.root = n
                return

n = LinkedList()
n.addElement(2)
n.addElement(4)
n.addElement(3)
n.addElement(5)
n.deleteElement(6)
n.deleteElement(4)
n.insertElementK(2, 3)
n.insertElementK(1, 1)
n.insertElementK(0, 0)
n.insertElementK(4, 4)
n.deleteElementK(4)
n.deleteElement(2)
n.reverseList()
print(n.noOfElements())
print(n) #[0,1,8,3]