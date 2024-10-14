# Define family relationships
male = {'John', 'Michael', 'David'}
female = {'Mary', 'Linda', 'Jennifer', 'Elizabeth'}

parent = {
    ('John', 'Michael'),   # John is the father of Michael
    ('Mary', 'Michael'),   # Mary is the mother of Michael
    ('John', 'Jennifer'),  # John is the father of Jennifer
    ('Mary', 'Jennifer'),  # Mary is the mother of Jennifer
    # Removed James and his parents
}

# Define family relation functions
def father(child):
    return next((p[0] for p in parent if p[1] == child and p[0] in male), None)

def mother(child):
    return next((p[0] for p in parent if p[1] == child and p[0] in female), None)

def brother(sibling):
    return next((s[1] for p in parent if p[1] == sibling for s in parent if s[1] != sibling and s[0] in male and s[1] in {p[1] for p in parent}), None)

def sister(sibling):
    return next((s[1] for p in parent if p[1] == sibling for s in parent if s[1] != sibling and s[0] in female and s[1] in {p[1] for p in parent}), None)

def cousin(child):
    parents = {p[1] for p in parent if p[1] != child}
    return [s[1] for p in parent for s in parent if s[1] != child and s[0] not in parents]

# Example Queries
print("Father of Michael:", father('Michael'))      # John
print("Mother of Jennifer:", mother('Jennifer'))     # Mary
print("Brother of Jennifer:", brother('Jennifer'))   # Michael
print("Sister of Michael:", sister('Michael'))       # Jennifer
print("Cousins of Jennifer:", cousin('Jennifer'))     # [] (No cousins since James was removed)
