filename = 'input.txt'

first_nums = []
second_nums = []

with open(filename, "r") as f:
    for l in f:
        
        p = l.split()
        if len(p) == 2:
            first_nums.append(int(p[0]))
            second_nums.append(int(p[1]))

def match(first, second):

    first.sort()
    second.sort()

    total_distance = 0

    for i in range(len(first)):

        difference = abs(first[i] - second[i])
        total_distance = total_distance + difference

    return total_distance

# part 1
print(match(first_nums, second_nums))


def similar(first, second):

    similarity_score = 0

    for i in range(len(first)):

        amount = 0

        for j in range(len(second)):

            if first[i] == second[j]:
                amount += 1
        
        similarity_score = similarity_score + (first[i]*amount)
    
    return similarity_score

# part 2
print(similar(first_nums, second_nums))