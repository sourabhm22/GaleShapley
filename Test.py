with open('inputFile.txt') as to_read:
    input_data = to_read.read()

# Splitting input to get preference and men and women list
split_input_data = input_data.splitlines()
size = len(split_input_data)
overall_lists = [i.split() for i in split_input_data]

overall_preference_list = overall_lists[2:]
n = len(overall_preference_list)
mid = int(n / 2)
list_of_men = overall_lists[0]
list_of_women = overall_lists[1]

# Reverse mapping name to index
dictionary_of_men_women = {overall_lists[0][i]: i for i in range(0, mid)}
dictionary_of_men_women.update({overall_lists[1][i - mid]: i for i in range(mid, n)})
print(dictionary_of_men_women)

# Converting pref from string to index no via help of dictionary
men_women_pref = [[dictionary_of_men_women[i[j]] for j in range(1, mid + 1)] for i in overall_preference_list]
print(men_women_pref)
print(len(men_women_pref))

# Creating list to store engaged status for men and women
free_men = [False for i in range(0, mid)]
free_men_count = mid
women_engaged = [-1 for i in range(0, mid)]

# Dividing list to 2 halves
women_pref_list = men_women_pref[mid:]
men_pref_list = men_women_pref[:mid]
# print(women_pref_list)
# print(men_pref_list)

# Inverting women list
women_inv = [[-1 for j in range(0, mid)] for i in range(0, mid)]
for i in range(0, mid):
    for j in range(0, mid):
        t = women_pref_list[i][j]
        women_inv[i][t] = j
print(f'Women  Inverse pref list \n {women_inv}')

#############################################
# Alternative way for inversion of women list
# women_inv = [[women_pref_list[i].index(j) for j in range(0, mid)] for i in range(0, mid)]
# print(f'Women  Inverse pref list \n {women_inv}')
#############################################


def check_preference(current_man, woman):
    if women_inv[woman][current_man] < women_inv[woman][women_engaged[woman]]:
        return current_man
    else:
        return women_engaged[woman]

#  WHILE is used instead of FOR, bcoz FOR does not include condition


while free_men_count > 0:
    i = 0
    while i < mid:
        if not free_men[i]:
            break
        i += 1

    j = 0
    while free_men[i] == False and j < mid:
        current_woman = men_pref_list[i][j] - mid
        # print(current_woman)
        if women_engaged[current_woman] == -1:
            free_men[i] = True
            free_men_count -= 1
            women_engaged[current_woman] = i

        else:
            currently_engaged_man = women_engaged[current_woman]
            preferred_man = check_preference(i, current_woman)
            if preferred_man == i:
                free_men[currently_engaged_man] = False
                free_men[i] = True
                women_engaged[current_woman] = i
        j += 1

print('Stable matching : ')
result = [[f'{list_of_women[i]} -- {list_of_men[i]}'] for i in women_engaged]
print(result)
