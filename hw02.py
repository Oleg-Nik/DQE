# Module 2 homework
import random

# max elements number for list of dictionaries
len_of_dic_list = 3
# number of key/value pairs in dictionary
len_of_dic = 2
# range of values for dict values
probability_range = 100
# list of names for keys
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
       'u', 'v', 'w', 'x', 'y', 'z']
# list of random dictionaries (len_of_dic) with length = len_of_dic_list
random_dict = [{random.choice(abc): random.randint(1, probability_range)
                for _ in range(len_of_dic)} for _ in range(len_of_dic_list)]
print("List of random dicts:", random_dict)
# creation of new dictionary based on random list random_dict
united_dict_0 = {}
united_dict_1 = {}
print(random_dict[0].keys())
print(random_dict[0].values())
print({k: v for (k, v) in random_dict[0].items()})
print({k: v for (k, v) in random_dict[1].items()})
print({k: v for (k, v) in random_dict[2].items()})
united_dict_1 = random_dict[0] | random_dict[1] | random_dict[2]
print("United dictionary 0:", united_dict_0)
print("United dictionary 1:", united_dict_1)
p = random_dict[0].update(random_dict[1])
print(type(p))
print(type(random_dict[0]))
print(random_dict[0])
