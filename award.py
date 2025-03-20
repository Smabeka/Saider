# Get the qualifying time for each event
# Calculate the total time
# Calculate and display the total time
# Determine the award based on the total time

swimming = float(input("Enter the qualifying time: "))
cycling = float(input("Enter the qualifying time: "))
running = float(input("Enter the qualifying time: "))
                    
total_time = swimming + cycling + running

print(f"Qualifying time is{total_time} minutes")

qualifying_time =100

if total_time <= qualifying_time:
    print("Award!noprovincial colour.")
elif total_time <=qualifying_time + 5:
    print("Award!provincial half colour.")
elif total_time <=qualifying_time + 10:
    print("Award!provincial scroll.")
    
else : total_time >=qualifying_time + 10
print("Award!no award.")