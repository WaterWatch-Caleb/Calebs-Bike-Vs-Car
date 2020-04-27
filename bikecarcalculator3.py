#import time for pause aesthetic/pacing
import time
#arbitary average speed for car
acspeed = 68
#arbitary average speed for car
abspeed = 10
#arbitary cost of gas
dpg = 1.4
#main function
def main():
    print("welcome to caleb's car/bike calculator!")
    time.sleep(0)
    jobdistance, biketime = average_time()
    time.sleep(0)
    gas_cost(jobdistance)
    time.sleep(0)
    bike_workout(biketime)
    
#calculates and prints the amount of time it takes to drive to work or ride your bike
def average_time():
    jobdistance = int(input("How many miles away is your job?\n"))
    cartime = round(jobdistance / acspeed * 60, 2)
    biketime = round(jobdistance / abspeed * 60, 2)
    print(f"your job is {cartime} minutes away by car and {biketime} minutes by bike")
    if biketime >= 30: 
        print("That isn't very long is it?")
        time.sleep(0)
    else: 
        print("that is a bit of a hike huh?")
        
    return jobdistance, biketime

#function for calculating cost of gas usuage
def gas_cost(jobdistance):
    mpg = int(input("how many miles per gallon does your car get?\n"))
    fgallon = jobdistance / mpg
    cod = fgallon * dpg
    print(f"it cost you ${round(cod, 2)} to drive to work each day in gas")
    time.sleep(0)
    weekly = round(cod * 5,2)
    print(f"Assuming you work 5 days a week that's ${weekly} a week")
    time.sleep(0)
    print(f"${weekly * 4} a month")
    print(f"and ${weekly * 4 * 12} a year!")
    print("not to mention that you had to buy the damned thing for anywhere from $1000 to $30,000 or more!")
    
def bike_workout(biketime):
    print("now what about all that time on the bike? that's just a waste of time!")
    print(f"well if it takes {biketime} minutes to get there and {biketime} minutes to get back then that's {biketime * 2} of workout time at the same time!")
          
if __name__=="__main__":
    main()
