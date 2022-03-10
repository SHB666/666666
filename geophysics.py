from colorama import init
init(autoreset=True)
print('\033[1;32m***!水平层状介质中首波走时计算程序，请输入合适的参数!***\033[0m')
import re
x = eval(input("请输入震中距(KM)："))
n = eval(input("请输入层数："))
h = eval(input("请输入震源深度(KM)："))
if h < 0 or n <= 0:
    if h < 0 and n > 0:
      print("\033[1;31m请关闭后重新输入震源深度\033[0m")
    elif n <= 0 and h > 0:
      print ("\033[1;31m请关闭后重新输入层数\033[0m")
    elif h < 0 and n <= 0:
     print("\033[1;31m请关闭后重新输入层数以及震源深度\033[0m")
    input()
else:
  for j in range (1,n+1):
    locals()['z'+ str(j)] = eval(input("请输入第"+str(j)+"层的厚度(KM)："))
    locals()['v'+ str(j)] = eval(input("请输入第"+str(j)+"层的波速(KM/S)："))
locals()['v' + str(j + 1)] = eval(input("请输入第" + str(j + 1) + "层的波速(KM/S)："))
m = str(locals().items())
z = re.findall('z\d',m)
v = re.findall('v\d',m)
if h <= z1 and n < 2:
 tp = (x/v2)+(((2*z1)-h)*((((1/v1)**2)-((1/v2)**2))**0.5))
 print("\033[1;31m首波的走时为\033[0m"+str(tp)+"\033[1;31m秒\033[0m")
else:
 a = z[-1]
 dz = locals()[f"{a}"]
 b = v[-2]
 dv = locals()[f"{b}"]
 c = v[-1]
 dc = locals()[f"{c}"]
 y = dv/dc
 dzz = 0
 dtt = 0
 try:
  for i in range(1,n):
   e = (locals()['z%d'%i])
   f = (locals()['v%d'%i])
   g = e*y
   g11 = e*(dv/((f)**2))
   k = dv/(f)
   l = k**2
   m = y**2
   n = l-m
   o = n**0.5
   dzz += (g/(o))
   dtt += (g11/(o))
  d = ((((dz)*y)/((1-y**2)**0.5))+dzz)
  t = (((dz)/(dv*((1-y**2)**0.5)))+dtt)
 except:
  print("\033[1;31m请勿在两层界面输入相同的波速,请关闭后重试\033[0m")
 w = h
 u = 0
 try:
  while w >= 0:
   u = u + 1
   w1 = (locals()['z%d'%u])
   w = w - w1
  else:
   w2 = (locals()['z%d'%u])
   dz1 = w2 + w
   vv = (locals()['v%d'%u])
   y1 = vv/dc
   dzz1 = 0
   dtt1 = 0
   for r in range(1, u):
    e1 = (locals()['z%d'%r])
    f1 = (locals()['v%d'%r])
    g1 = e1 * y1
    g12 = e1*(vv/((f1)**2))
    k1 = vv/(f1)
    l1 = k1 ** 2
    m1 = y1 ** 2
    n1 = l1 - m1
    o1 = n1 ** 0.5
    dzz1 += (g1/(o1))
    dtt1 += (g12/(o1))
   d1 = (((((dz1)*y1)/((1-y1**2)**0.5))+dzz1))
   t1 = (((dz1)/(vv*((1-y1**2)**0.5)))+dtt1)
   d2 = 2*d-d1
   t2 = 2*t-t1
   t3 = (x-d2)/dc
   tt = t2+t3
   if t3 < 0:
       print("\033[1;31m请输入正确的震中距\033[0m")
   else:
    print("\033[1;31m首波的走时为\033[0m"+str(tt)+"\033[1;31m秒\033[0m")
 except:
   print("\033[1;31m请勿将震源位置放置在最低点,请关闭后重试\033[0m")
print("\033[1;32m版权所有 不得复制 如有疑问请联系作者\033[0m")
print("\033[1;32m按回车键退出\033[0m")
input()
