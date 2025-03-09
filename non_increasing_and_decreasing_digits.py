# 1. Iterate the number till x
# 2. Number is increasing (n)
# 3. Square of that number is increasing (n*n)
# 4. If both are true we print the number and it's suqare (print(n) print (n^2))
# 5. How to check if n is acending

#5. Starting from a small digt to a bigger digit (eg.123) 5 -> 6
def is_non_decreasing(num):
    num_str = str(num)  # Convert number to string to access individual digits
    for i in range(len(num_str) - 1):  # Loop through each digit (except the last one)
        if num_str[i] > num_str[i + 1]:  # If a digit is greater than the next one, return False
            return False
    return True  

def is_non_increasing(num):
    num_str = str(num)  # Convert number to string
    for i in range(len(num_str) - 1):  # Loop through each digit
        if num_str[i] < num_str[i + 1]:  # If a digit is smaller than the next one, return False
            return False
    return True  


def find_numbers(limit):
    results = {"Task1": [], "Task2": [], "Task3": [], "Task4": []}
     
     # 1. Iterate the user input from 1 to the limit
    for n in range(1, limit):
        square = n ** 2 # square the number
        
        non_dec_n = is_non_decreasing(n) # check if number is non_decreasing
        non_dec_n_square = is_non_decreasing(square) #check if square is non_decreasing
        
        non_inc_n = is_non_increasing(n) # check if number is non_increasing
        non_inc_n_square = is_non_increasing(square) #check if square is non_increasing
        
        non_dec_n_3 = is_non_decreasing(n) # check if number is non_increasing
        non_inc_n_square_3 = is_non_increasing(square) #check if square is non_increasing
        
        if (non_dec_n and non_dec_n_square): #print the number and the square if both are non_decrasing
           results["Task1"].append(f"{n}: {square}")
        if (non_inc_n and non_inc_n_square): #print the number and the square if both are non_decrasing
            results["Task2"].append(f"{n}: {square}")
        if (non_dec_n_3 and non_inc_n_square_3): 
            results["Task3"].append(f"{n}: {square}")
                                
    return results

x = 100
print(f"Finding numbers up to {x}:")
results = find_numbers(x)
for key, values in results.items(): 
    print(f"{key}: {values}")