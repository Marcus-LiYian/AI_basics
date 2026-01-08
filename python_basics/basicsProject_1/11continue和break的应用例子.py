# 作者:李一安
# 2026年01月05日13时40分02秒


print("答题闯关开始，按q可随时退出")

# 题目与答案
ques1, ans1 = "Python中用于输出的函数是？", "print"
ques2, ans2 = "Python中用于表示逻辑并且的关键字是？", "and"
ques3, ans3 = "Python属于编译型还是解释型？", "解释型"

# 最多尝试次数
max_tries = 3

# 总关卡数量
total_levels = 3

# 是否处于游戏状态
is_playing = True

for level in range(1,total_levels+1):
    print("-"*20+f"第{level}关"+"-"*20)

    question,answer = "",""
    if 1==level:
        question, answer=ques1,ans1
    elif 2==level:
        question, answer = ques2, ans2
    elif 3==level:
        question, answer = ques3, ans3



    # 记录当前这个关卡的尝试次数
    tries = 1

    while tries <= max_tries:
        # 提问并获取答案
        user_input=input("提问："+question+"\n")

        # 审核答案
        if user_input == answer:
            print("回答正确！")
            break

        elif user_input == "":
            print("输入的答案为空，请重新输入：")
            continue

        elif user_input == "q":
            print("已退出游戏。")
            is_playing = False
            break

        else:
            leave = max_tries-tries

            if leave>0:
                print(f"回答错误！还有{leave}次机会。")
                tries+=1
                continue
            else:
                print(f"挑战失败，本题答案是：{answer},游戏结束。")
                is_playing = False
                break

    if not is_playing:
        break

if is_playing:
    print("恭喜你，通过了所有关卡！")