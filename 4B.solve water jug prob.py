jug1, jug2, aim = 4, 3, 2

def water_jug_solver(amt1, amt2, visited=None):
    if visited is None:
        visited = set()
    if (amt1, amt2) in visited:
        return False
    visited.add((amt1, amt2))
    print(amt1, amt2)
    if amt1 == aim or amt2 == aim:
        return True
    return (water_jug_solver(0, amt2, visited) or
            water_jug_solver(amt1, 0, visited) or
            water_jug_solver(jug1, amt2, visited) or
            water_jug_solver(amt1, jug2, visited) or
            water_jug_solver(amt1 + min(amt2, jug1-amt1), amt2 - min(amt2, jug1-amt1), visited) or
            water_jug_solver(amt1 - min(amt1, jug2-amt2), amt2 + min(amt1, jug2-amt2), visited))

print("Steps: ")
water_jug_solver(0, 0)