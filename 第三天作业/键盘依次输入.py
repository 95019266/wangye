l = []
for i in range(0,10):
  a = int(input("请输入数值: "))
  l.append(a)
  avg = sum(l)/10
print('求和结果为:',sum(l),'最大的数为:',max(l),'平均数为:',avg)