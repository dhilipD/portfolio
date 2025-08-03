import pandas as pd
from datetime import datetime,timedelta


start_date = datetime.now() + timedelta(days=1)
data =[ start_date + timedelta(days=i) for i in range(7) ]

#for d in data:
    #print(d)

fintness_data =[]
for date in data:
    day_name = date.strftime("%a")
    #print(day_name)
    workOut_plan = ""
    if day_name == "Sun":
        workOut_plan = "Rest"
    elif day_name in ["Fri","Wed"]:
        workOut_plan = "Running"
    elif day_name == "Mon":
        workOut_plan = "Push_day"
    elif day_name == "Tue":
        workOut_plan = "Pull_day"
    elif day_name == "Sat":
        workOut_plan = "leg_day"
    else:
        workOut_plan = "Active_Recovery"
    fintness_data.append({
        'Date': date.date(),
        'Day': day_name,
        'Planned Workout': workOut_plan,
        'Duration (min)': '1.5 to 2.0',
        'Calories Burned': 'NotYet',
        'Steps': '8000',
        'Water Intake (L)': '4L ABOVE',
        'Sleep (hrs)': '6-7hr',
        'Notes': ''
    })
fitness = pd.DataFrame(fintness_data)
#print(fitness)
learning_data = []
topics_cycle = ['AWS-python', 'PySpark-Python']
for i, d in enumerate(data):
    day_name = d.strftime('%A')
    planned_topic = topics_cycle[i % len(topics_cycle)] #doubt
    learning_data.append({
        'Date': d.date(),
        'Day': day_name,
        'Planned Topic': planned_topic,
        'Time Spent (hrs)': '1hr to 2hr',
        'Notes': '',
        'New Word Learned': ''
    })

learning_df = pd.DataFrame(learning_data)


# Write to Excel
file_path = 'C:/Users/Dhilip Kumar/OneDrive/Desktop/My_Fitness/fitness_tracker.xlsx'
file_path_01 = 'C:/Users/Dhilip Kumar/OneDrive/Desktop/My_Fitness/Learning_tracker.xlsx'
try:
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        fitness.to_excel(writer, sheet_name='Fitness', index=False)
    with pd.ExcelWriter(file_path_01,engine='xlsxwriter') as writerr:
        learning_df.to_excel(writerr, sheet_name='Learning', index=False)
    
# Provide file to user
   # file_path
except PermissionError as e:
    print("❌ File is open or protected. Please close it and try again.")