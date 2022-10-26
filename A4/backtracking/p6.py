# implementation of problem 6 

# stack value is a value that 
# is positive if the bracket configuration is ok,
# it is 0 if it is perfect
# or it is negative if it is incorrect
def stack_value(config, par1, par2):
    stack_value = 0
    for paranthese in config:
        if paranthese == par1:
            stack_value += 1
        elif paranthese == par2:
            stack_value -= 1
    return stack_value


# iterative approach
def build_solution_iterative(n):
    solutions = [""]
    el_size = 0
    while el_size < n:
        el_size += 1
        new_elements = []
        for i in range(len(solutions)):
            new_solutions = ["", ""]
            new_solutions[0] = solutions[i] + "("
            new_solutions[1] = solutions[i] + ")"
            for new_solution in new_solutions:
                if el_size < n:
                    if stack_value(new_solution, "(", ")") >= 0:
                        new_elements.append(new_solution)
                elif el_size == n:
                     if stack_value(new_solution, "(", ")") == 0:
                        new_elements.append(new_solution)
        solutions = new_elements
    return solutions

# recursive approach
def build_solution_recursive(n, solutions):
    el_size = len(solutions[0])
    el_size = el_size + 1
    new_elements = []
    for i in range(len(solutions)):
        new_solutions = ["", ""]
        new_solutions[0] = solutions[i] + "("
        new_solutions[1] = solutions[i] + ")"
        for new_solution in new_solutions:
            if el_size < n:
                if stack_value(new_solution, "(", ")") >= 0:
                    new_elements.append(new_solution)           
            elif el_size == n:
                if stack_value(new_solution, "(", ")") == 0:
                    new_elements.append(new_solution)
    
    if el_size == n:
        return new_elements
    else:
        return build_solution_recursive(n, new_elements)

                

if __name__ == "__main__":
    resolution = build_solution_iterative(4)
    resolution2 = build_solution_recursive(4, [""])
    print(resolution2)
    print(resolution)

