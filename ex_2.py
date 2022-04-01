from random import randint

original_list = [randint(0, 1000) for _ in range(0, randint(2, 20))]
answer_list = [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]

print(original_list)
print(answer_list)