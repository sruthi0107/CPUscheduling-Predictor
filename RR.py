def sort(l):
    n=len(l)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if l[j][0]>l[j+1][0]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def rr(proc_id,n,burst,arrival):
    p=[]
    for i in range(n):
        p.append([arrival[i],burst[i],burst[i]])
    #print(p)
    time_quantum=2
    total_time= 0
    proc=sort(p)
    #print(proc)
    bt,wt,ct,tat,ready_queue=[0]*n,[0]*n,[0]*n,[0]*n,[0]
    for i in range(n):
        total_time+=proc[i][1]
    curr_time,flag,finished=proc[0][0],0,0

    for i in range(1,n):
        if proc[i][0]==curr_time:
            ready_queue.append(i)
    
    #print(ready_queue)

    while finished!=n:
        if(len(ready_queue)==0):
            curr_time=proc[currpro+1][0]
            currpro+=1
        else:
            currpro=ready_queue.pop(0)
        initime=curr_time
        if proc[currpro][2]>time_quantum:
            curr_time+=time_quantum
            proc[currpro][2]-=time_quantum
        else:
            curr_time+=proc[currpro][2]
            proc[currpro][2]=0
            ct[currpro]=curr_time
            finished+=1

        if flag==0:
            for i in range(n):
                if proc[i][0]>initime and proc[i][0]<=curr_time:
                    ready_queue.append(i)
                    if i==n-1: flag=1

        if proc[currpro][2]>0:
            ready_queue.append(currpro)

    total_tat,total_wt=0,0

    for i in range(n):
        tat[i]=ct[i]-proc[i][0]
        wt[i]=tat[i]-proc[i][1]
    
    #print(proc)
    #print(tat)
    #print(ct)

    for i in range(n):
        total_wt+=wt[i]
        total_tat+=tat[i]

    return total_wt/n

#Driver code
if __name__ == '__main__':
    print(rr([1,2,3,4,5],5,[7,5,9,15,1],[0,0,9,0,2]))