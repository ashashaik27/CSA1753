# Vacuum Cleaner Problem (Simple Reflex Agent)

def vacuum_cleaner():
    # Initial environment
    environment = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    # Initial position of vacuum cleaner
    location = 'A'

    print("Initial State:")
    print(environment)
    print("Vacuum at location:", location)
    print()

    # Simple reflex agent behavior
    while environment['A'] == 'Dirty' or environment['B'] == 'Dirty':
        if environment[location] == 'Dirty':
            print(f"Vacuum cleans location {location}")
            environment[location] = 'Clean'
        else:
            if location == 'A':
                print("Vacuum moves from A to B")
                location = 'B'
            else:
                print("Vacuum moves from B to A")
                location = 'A'

        print("Current State:", environment, "Vacuum at:", location)
        print()

    print("All locations are clean!")

# Main program
if __name__ == "__main__":
    vacuum_cleaner()
