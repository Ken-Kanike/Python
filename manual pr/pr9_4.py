dataList = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
print("Original List ", dataList)
u_value = set(val for dic in dataList for val in dic.values())
print("Unique values : ", u_value)
