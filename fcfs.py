#First come first serve implementation in python
#taking proceeses as input from user
print("Enter the number of processes: ")
#creating array to store burst time
b_t=[]
num=int(input())
print("Enter the burst time of the processes: \n")
#creating burst list
b_t=list(map(int, raw_input().split()))
#creating list to store waiting time
w_t=[]
#initializing average waiting time with 0
avg_wt=0
#ttotal turn around time =0
t_at=[]
avg_tat=0
w_t.insert(0,0)
#putting loop
t_at.insert(0,b_t[0])
for j in range(1,len(b_t)):
    w_t.insert(j,w_t[j-1]+b_t[j-1])
    t_at.insert(j,w_t[j]+b_t[j])
    avg_wt+=w_t[j]
    avg_tat+=t_at[j]
    avg_wt=float(avg_wt)/num
    avg_tat=float(avg_tat)/num
    print("\n")


print("Processes\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for j in range(0,num):
    print(str(j)+"\t\t\t"+str(bt[j])+"\t\t\t\t"+str(w_t[j])+"\t\t\t\t\t"+str(t_at[j]))
#printing average wAITING AND TURN AROUND TIME
print("\n")
print("Average Waiting time : "+str(avg_wt))
print("Average Turn Arount Time : "+str(avg_tat))
