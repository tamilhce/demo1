class linkedList(): 
    'singly linked list' 
    def __init__(self,data,next=None): 
        self.data=data
        self.next=next
    
    def traverse(self):
        print self.data,'--->', 
        while self.next:
            print self.next.data,'--->',
            #print self.next
            if self.next.next == None: 
                print 'Null'
            self.next=self.next.next                  

if __name__ =='__main__':
    print __name__ 
    s1=linkedList(10)
    s2=linkedList(20,s1) 
    s3=linkedList(30,s2) 
    s3.traverse() 
