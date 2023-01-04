import random

# 创建1-100的数列.
sequence = [i for i in range(1, 101)]

# 最大(最佳)
largest_value = sequence[-1]  # 100
second_largest_value = sequence[-2]  # 99
third_largest_value = sequence[-3]  # 98

# 概率统计
largest_value_times = 0
second_largest_value_times = 0
third_largest_value_times = 0

# 测试100万次
trials = 100000
for i in range(trials):
    # 储存遇到过最大的数字
    max_value = 0

    # 打乱数列
    random.shuffle(sequence)

    # 每一次trial测试100次
    for ii in range(len(sequence)):
        current_value = sequence[ii]

        if current_value > max_value:
            max_value = current_value
            if ii >= 37-1:
                break
    else:  # 如果在前37个里已经出现了最大的数字, 那么按道理之后不会选择任何数字. 但因为现实中不会空手而归, 所以这里是选择了最后一个.
        max_value = sequence[-1]

    if max_value == largest_value:
        largest_value_times += 1
    elif max_value == second_largest_value:
        second_largest_value_times += 1
    elif max_value == third_largest_value:
        third_largest_value_times += 1

print("The probability of picking the greatest number is:", str((largest_value_times/trials)*100)+'%')
print("The probability of picking the second greatest number is:", str((second_largest_value_times/trials)*100)+'%')
print("The probability of picking the third greatest number is:", str((third_largest_value_times/trials)*100)+'%')
