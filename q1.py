def depth(a):
    d={}
    def index(a,s):
        count=a.count(s)
        l=[]
        i=-1
        while count!=len(l):
            l.append(a.index(s,i+1))
            i=a.index(s,i+1)
        return l 
    d[-1]=index(a,-1)
    count=-1
    def overcome(d,count):
        d1={}
        for i in d:
            for j in d[i]:
                if j in a:
                    d1[j]=index(a,j)
        return (d1,count) 
    while d!={}:
        count+=1
        d,count=overcome(d,count)
        
    return count
    
c=[]   
t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    a = list(map(int,input().strip().split()))[:n] 
    c.append(depth(a))
    
for i in c:
    print(i)
    
    
