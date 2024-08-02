import random

def random_loop(count):
    x = count
    iterations = 0
    
    while x > 1:
        number = random.randint(1, x)
        if number == 1:
            x -= 1
        else:
            iterations += 1
            
    return iterations

def calculate_average(num_trials, count):
    total_iterations = 0
    
    for _ in range(num_trials):
        total_iterations += random_loop(count)
        
    return total_iterations / num_trials

num_trials = 1000000

for y in range(12):
    if y<2:
        continue
    print(f"The average number of heals over {num_trials} trials is {calculate_average(num_trials, y):.2f}. for {y-1} success stones")
