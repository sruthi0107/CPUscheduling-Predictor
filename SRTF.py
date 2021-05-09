def SRTF_findWaitingTime(processes, n, bt, wt, at): 
    rt = [0] * n 
    for i in range(n): 
        rt[i] = bt[i]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and 
                (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue
        rt[short] -= 1
        minm = rt[short] 
        if (minm == 0): 
            minm = 999999999
        if (rt[short] == 0): 
            complete += 1
            check = False
            fint = t + 1
            wt[short] = (fint - bt[short] -    
                                at[short])
  
            if (wt[short] < 0):
                wt[short] = 0
        t += 1
def SRTF_findavgTime(processes, n, bt, at): 
    wt = [0] * n
    SRTF_findWaitingTime(processes, n, bt, wt, at) 
    total_wt = 0
    for i in range(n):
        total_wt = total_wt + wt[i] 
    return total_wt/n
      
# Driver code 
if __name__ =="__main__":
      
    # Process id's 
    #proc = [[1, 6, 1], [2, 8, 1],
    #        [3, 7, 2], [4, 3, 3]]
    proc=[1,2,3,4]
    arrival=[1,1,2,3]
    burst=[6,8,7,3]
    n = 4
    print(SRTF_findavgTime(proc, n, burst, arrival))
      
# This code is contributed
# Shubham Singh(SHUBHAMSINGH10)