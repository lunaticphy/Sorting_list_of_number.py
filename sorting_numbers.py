my_list = [11, 21, 312, 52, 6]
print(f"We are going to organize it from least -> greatest {my_list}")
maximum = max(my_list) #32
minimum = min(my_list) #1
my_list.remove(maximum)
my_list.remove(minimum)
print(my_list)
less_max = max(my_list) #21
less_min = min(my_list) #5
my_list.remove(less_min)
print(my_list)
my_list.remove(less_max) 

print(my_list)  # r 6
new_list = [minimum, less_min] + my_list + [less_max, maximum]
print(new_list) #[6, 11, [21], 52, 312] 

WANT TO ADD USER INPUT BUT ONLY 5 NUMBERS AND USES SPACES
# Get user input as a string separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string and convert each element to an integer
user_list = [int(num) for num in user_input.split()]

# Print the list
print(user_list)
