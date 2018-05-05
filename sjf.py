#Shortest Job first implementation in python
#taking processes as input from user
print("Enter the number of process: ")
num=int(input())
pro=[]
for j in range(0,num):
    pro.insert(j,j+1)
#burst time array
b_t=[]
print("Enter the burst time of the processes: \n")
#burst timre list
b_t=list(map(int, raw_input().split()))
for j in range(0,len(bt)-1): 
 #applying bubble sort to sort process according to their burst time
    for i in range(0,len(bt)-i-1):
        if(b_t[i]>b_t[i+1]):
            temp=bt[i]
            b_t[i]=b_t[i+1]
            b_t[i+1]=temp
        temp=pro[i]
        pro[i]=pro[i+1]
        pro[i+1]=temp
w_t=[]   
 #w_t  waiting time
avg_wt=0  
#average waiting time
t_at=[]   
 #t_at turnaround time
avg_tat=0  
 #average  total turnaround time
w_t.insert(0,0)
t_at.insert(0,bt[0])
for j in range(1,len(b_t)):
    w_t.insert(j,wt[j-1]+b_t[j-1])
    t_at.insert(j,wt[j]+b_t[j])
    avg_wt+=w_t[j]
    avg_tat+=t_at[j]
avg_wt=float(avg_wt)/num
avg_tat=float(avg_tat)/num
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for j in range(0,num):
 print(str(processes[j])+"\t\t\t"+str(b_t[j])+"\t\t\t\t"+str(w_t[j])+"\t\t\t\t\t"+str(t_at[i]))

print("\n")

print("Average Waiting time : "+str(avg_wt))
print("Average Turn Arount Time : "+str(avg_tat))
