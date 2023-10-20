import time
# "enter the time in (24 hr clock)
current_time = time.localtime().tm_hour
timestamp = time.strftime("%m/%d/%Y, \n%H:%M:%S")
print(timestamp)

if 5<= current_time< 12:
    print("Breakfast Time")
elif 12<= current_time< 16:
    print("Lunch Time")
elif 16<= current_time<22:
    print("Snacks Time")
else:
    print("Dinner Time")