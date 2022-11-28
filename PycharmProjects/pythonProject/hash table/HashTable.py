class HashTable:
    def __init__(self,max_size):
        self.data=[None]*max_size
    def insert(self,key,value):
        index=get_index(self.data,key)
        print(index)
        self.data[index]=key,value
    def update(self,key,value):
        index=find_index(self.data,key)
        if index is not None:
            self.data[index]=key,value
    def find(self,key):
        index=find_index(self.data,key)
        print(index)
        if index is not None:
           k,v=self.data[index]
           return v
    def listAll(self):
        return[ x for x in self.data if x is not None]

def get_index(data,key):
    result=0;
    for char in key:
        result+=ord(char)
    result=result%len(data)
    while(True):
        if(data[result]==None):
            return result
        else:
            result+=1
        if(result==len(data)):
            result=0

def find_index(data,key):
    result=0
    for char_num in key:
        result+=ord(char_num)
    result=result%len(data)

    if (data[result])==None:
        return None
    while(True):
        k,v=data[result]
        if(key==k):
            return result
        else:
            result+=1
        if(result==len(data)):
            result=0

hashtable=HashTable(400)
hashtable.insert('naveen',45)
hashtable.insert('navene',78)
hashtable.update('naveen',88)
data=hashtable.find('naveen')
print(data)