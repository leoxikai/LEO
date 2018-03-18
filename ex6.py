type_of_people=10
x=f"There are {type_of_people} types of people."

binary="binary"
do_not="don't"
y=f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
print(f"I said : {x}")
# 如果去掉‘f’打印出来的就是I said : {x}，变量x的内容没有打印出来
print(f"I also said :'{y}'")
#如果单独打印x的内容是print(x)可以直接实现的，但是当要打印组合内容时（比如"I said : {x}，就需要用到f格式化字符串）
hilarious=False
joke_evaluation="Isn't that joke so funny!{}"

print(joke_evaluation.format(hilarious))
#不太懂？format的用法不熟悉？--update:变量joke_evaluation内容的最后有个{}
#与后面的.format连接起来就是.format的用法。注意这里format括号内的是一个变量
#hilarious。如果里面是个字符串主要要加上单引号。比如ex7里的.format('snow')。
w="This is the left side of..."
e="a string with a right side."
print(w+e)

