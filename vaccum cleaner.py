import time
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}
current_location = 'A'
def vacuum_agent(location, environment):
    if environment[location] == 'Dirty':
        print(f"Location {location} is Dirty.")
        print("Action: Suck")
        environment[location] = 'Clean'
        print(f"Location {location} is now Clean.\n")
    else:
        print(f"Location {location} is already Clean.\n")
for i in range(2):  # Run through both rooms
    print(f"Step {i+1}")
    vacuum_agent(current_location, environment)
    if current_location == 'A':
        current_location = 'B'
        print("Action: Move Right to Room B\n")
    elif current_location == 'B':
        current_location = 'A'
        print("Action: Move Left to Room A\n")
print("Final Environment State:")
for room in environment:
    print(f"Room {room}: {environment[room]}")
