def SJF_findWaitingTime(processes, n, bt, wt, at): 
    complete=0
    t=0
    buffer=[]
    while(complete!=n):
        check=False
        for i in range(len(at)):
            if(at[i]<=t):
                check=True
                if([bt[i],i] not in buffer):
                    buffer.append([bt[i],i])
        if(check==False):
            t+=1
            continue
        shortest=999999999
        index=0
        for i in range(len(buffer)):
            if(shortest>buffer[i][0]):
                shortest=buffer[i][0]
                index=buffer[i][1]
        t+=shortest
        wt[index]=t-at[index]-bt[index]
        buffer.remove([shortest,index])
        bt[index]=999999999
        at[index]=999999999
        complete+=1
def SJF_findavgTime(processes, n, bt, at): 
    wt = [0] * n
    SJF_findWaitingTime(processes, n, bt, wt, at) 
    total_wt = 0
    for i in range(n):
        total_wt = total_wt + wt[i] 
    return total_wt/n
      
# Driver code 
if __name__ =="__main__":
      
    # Process id's 
    #proc = [[1, 6, 1], [2, 8, 1],
    #        [3, 7, 2], [4, 3, 3]]
    proc=[1,2,3,4,5]
    arrival=[10,1,8,10,9]
    burst=[11,5,8,2,12]
    n = 5
    print(SJF_findavgTime(proc, n, burst, arrival))