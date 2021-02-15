# Module 2 homework
import random
# max elements number for list of dictionaries
len_of_dic_list = 4
# number of key/value pairs in dictionary
len_of_dic = 3
# range of values for dict values
probability_range = 100
# list of names for keys
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
       'u', 'v', 'w', 'x', 'y', 'z']
# list of random dictionaries (len_of_dic) with length = len_of_dic_list
random_dict = [{random.choice(abc): random.randint(1, probability_range)
                for i in range(len_of_dic)} for i in range(len_of_dic_list)]
print(random_dict)
# creation new dictionary based on random list random_dict
united_dict = {}
k = list(random_dict[0])
for i in range(len_of_dic_list):
    for j in range(len_of_dic):
        if k[j]
print(k)
