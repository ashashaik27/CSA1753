# Map Coloring using CSP (Constraint Satisfaction Problem)

# Variables (Regions)
regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Domains (Available Colors)
colors = ["Red", "Green", "Blue"]

# Constraints (Adjacency)
adjacency = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "SA", "Q"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "Q":   ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V":   ["SA", "NSW", "T"],
    "T":   ["V"]
}

def is_valid(region, color, assignment):
    for neighbor in adjacency[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    # Choose next unassigned region
    region = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]

    return None

solution = backtrack({})
print("Solution:", solution)
