from datetime import datetime


user_input = input("Enter you goal along with deadline separated by colon (eg. learn java:20.10.2020)\n")

input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
current_date = datetime.today()

print(f"deadline date: {deadline_date}")
print(f"current date: {current_date}")

time_till = deadline_date - current_date
hours_till= int(time_till.total_seconds()/60/60)
print(f"Dear User!, Time remaining for your goal:{goal} is {hours_till} hours")
# learn java:20.10.2022