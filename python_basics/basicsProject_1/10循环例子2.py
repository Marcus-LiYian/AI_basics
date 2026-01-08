# 作者:李一安
# 2026年01月04日21时11分03秒


# 九九乘法表

for row in range(1, 10):  # 行从1到9
    for column in range(1, row + 1):  # 列从1到当前行数
        print(f"{column}×{row}={column * row}", end="\t")
    print()  # 换行


# print("文本", end="\n")这是print的默认输出情况，这也是为什么可以自动换行的原因，
# 可以自定义修改end的值，甚至可以改成空字符串