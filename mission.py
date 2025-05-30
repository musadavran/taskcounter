import time
input_tasks  = []
completed_tasks = []
def thework():
    for eleman in input_tasks:
        completed_tasks.append(eleman)
    print("Tasks you have completed:", completed_tasks)
mission = 0
mission_u = input("What your mission?: ")
input_tasks.append(mission_u)
minute_u = int(input("After how many minutes should I remind you? : "))
seconds_u = minute_u * 60
time.sleep(seconds_u)
while ( mission < 1 ):
    finished_u = input("Did you finish yes or no? : ").lower()
    if "yes" in finished_u:
        thework()
        print("Well done work!")
        misssion = mission +1
        break
    elif "no" in finished_u:
        print ("I'm giving you a little more time.")
        time.sleep(60)
        
        

