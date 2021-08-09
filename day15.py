if __name__ == '__main__':
    name = "baidu_x_system.log"
    with open(file=name,mode="r",encoding="utf-8") as f:
        lines = f.readlines()#获取所有行
        sum = 0
        list = []
        list1 = []
        for line in lines:#第i行
            #找到第一个空格
            for j in range(len(line)):
                if line[j].isspace() == True:
                    a = line[:j]
                    list1.append(a)
                    if a not in list:
                        list.append(a)
                        sum += 1
                    break
        print(list1)
        print(list)
list = set(list1)  #list是另外一个列表，里面的内容是list1里面的无重复项
for item in list:
  print("the %s has found %s" %(item,list1.count(item)))
  f.close()
