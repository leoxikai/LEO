print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
#print(f"Its fleece was white as {'snow'}.")
#.format('snow') 作用和f""一样。
#format 将括号内的字符串传到之前{}的位置
print("And everywhere that Mary went.")
print("."*10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1+end2+end3+end4+end5+end6,end='.')
#注意这里最后的end='.',起的作用是连接下一个print的语句的内容，打印的内容不会换行。
#print(end1+end2+end3+end4+end5+end6)--看看去掉有什么不同
print(end7+end8+end9+end10+end11+end12)
