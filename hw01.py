import random

# define Length of the list and the Depth of probability
list_length = 100
probability_range = 1000
# empty lists
sorted_list = []
list_of_random_numbers = []
# creation list with random numbers
for _ in range(list_length):
    list_of_random_numbers.append(random.randint(1, probability_range))
# test = [random.randint(1, probability_range) for _ in range(list_length)]
# an output for random lists
print("------->: unsorted random List:\n", list_of_random_numbers)
# sorting the List
for _ in range(list_length):
    min_number = min(list_of_random_numbers)
    sorted_list.append(min_number)
    list_of_random_numbers.remove(min_number)
# an output for sorted lists
print("-------> sorted random List:\n", sorted_list)
# Averages calculation
even_list = [val for val in sorted_list if val % 2 == 0]
odd_list = [val for val in sorted_list if val % 2 == 1]
print("The average for even number:", round(sum(even_list)/len(even_list)))
print("The average for odd number:", round(sum(odd_list)/len(odd_list)))
