# 作者:李一安
# 2026年01月04日20时59分34秒


for day in range(1,31):
    print(f"第{day}天")
    print("练习第1组")
    print("练习第2组")
    print("练习第3组")
    if 30==day:
        print("肌肉闪闪发光")
    else:
        print(f"第{day}天健身计划已完成")

print("-"*50)

day = 1
while day<30:
    print(f"第{day}天")
    print("练习第1组")
    print("练习第2组")
    print("练习第3组")
    print(f"第{day}天健身计划已完成")
    day+=1

print(f"第{day}天")
print("肌肉闪闪发光")