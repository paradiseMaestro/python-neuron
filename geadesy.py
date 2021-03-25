import math

def dannie():
print("Все длинны сторон производятся в метрах!")
global d,x1,y1,nb,np,xc
x1 = float(input("X-координата:"))
y1 = float(input("y-координата:"))
d = abs(float(input("Горизонтальное проложение:")))
print("Дерекционный угол:")
nb = abs(math.trunc(float(input("Градусы:"))))
if nb > 360:
while True:
print("Градус не может быть больше 360!")
nb = abs(math.trunc(float(input("Введите градус заново:"))))
if nb < 360:
break
np = abs(math.trunc(float(input("Минуты:"))))
if np > 60:
while True:
print("Минута не может быть больше 60!")
np = abs(math.trunc(float(input("Введите минуту заново:"))))
if np < 60:
break
xc = abs(math.trunc(float(input("Секунды:"))))
if xc > 60:
while True:
print("Секунда не может быть больше 60!")
xc = abs(math.trunc(float(input("Введите секунду заново:"))))
if xc < 60:
break
def qwe():
global crc,crs_pro,q,q1
crc = (xc / 100 + np) / 60
crs_pro = nb + crc
q = math.radians(crs_pro)
q1= q
def ty():
global bv,vb,X,Y,x2,y2,nu1,nu2,nur,nar,X1,Y1
bv = math.cos(q1)
vb = math.sin(q1)
X=d*bv
Y=d*vb
x2=x1+X
y2=y1+Y
def cv():
print("Проверьте введенные данные:")
print("Координаты первой точки:")
print("X = {0} метров;".format(x1))
print("Y = {0} метров.".format(y1))
print("Горизонтальное проложение между точками (длина линии): {0} метров.".format(d))
print("Дирекционный угол α = {0}°{1}′{2}″".format(nb, np, xc))
print("Решение прямой геодезической задачи:")
print("ΔX = d × cos {0}°{1}′{2}″ = {3}м × {4} = {5} метров.".format(nb, np, xc, d, bv, X))
print("ΔY = d × sin {0}°{1}′{2}″ = {3}м × {4} = {5} метров.".format(nb, np, xc, d, vb, Y))
print("X2 = X + ΔX = {0}м + {1}м = {2} метров;".format(x1, X, x2))
print("Y2 = Y + ΔY = {0}м + {1}м = {2} метров.".format(y1, Y, y2))
def pr_zd():
dannie()
qwe()
ty()
cv()
gra=0

r=0
r1=0
ry=0

def block_1():
global Xo,Yo,Xo2,Yo2
print("Все длинны сторон производятся в метрах!")
Xo = float(input("X1-координата:"))
Yo = float(input("Y1-координата:"))
Xo2 = float(input("X2-координата:"))
Yo2 = float(input("Y2-координата:"))

def block_2():
global r3, sec, mins, grad,dd,X_pro,Y_pro
X_pro=Xo2-Xo
Y_pro=Yo2-Yo
ry=Y_pro/X_pro
r1 = math.atan((ry)) * (180 / math.pi)
r = math.modf(r1)
rz1 = r[0]
grad = int(r[1])
minnr = (int((rz1 * 3600))) / 60
r3 = math.modf(minnr)
rz3 = r3[0]
mins = r3[1]
sec = int(rz3 * 60)
dd = math.sqrt((math.pow(X_pro, 2) + math.pow(Y_pro, 2)))
print("2). Определяем румб линии 1-2:")
print("r1-2 = atg |ΔY/ΔX| = atg | {0} / {1} | =".format(X_pro, Y_pro))
print("= atg |{0}| = {1}° = {2}°{3}′{4}″.".format(ry,grad,r1,mins,sec))

def block_3():
if X_pro > 0 and Y_pro > 0:
print("3). По знакам приращений координат определяем, что линия находится в 1 четверти, и румб равен ")
print("= СВ:{0}°{1}′{2}″.".format(grad, mins, sec))
print("4). Вычисляем дирекционный угол линии 1-2. Для 1 четверти согласно таблице, дирекционный угол ")
print("определяется по формуле α =r, тогда:")
print("α1-2 ={0}°{1}′{2}″.".format(grad, mins, sec))
if X_pro < 0 and Y_pro > 0:
print("3). По знакам приращений координат определяем, что линия находится в 2 четверти, и румб равен ")
# grad1=180-grad
print("= ЮВ:{0}°{1}′{2}″.".format(grad, mins, sec))
print("4). Вычисляем дирекционный угол линии 1-2. Для 2 четверти согласно таблице, дирекционный угол ")
print("определяется по формуле α =180° - r, тогда:")
gra = 180 - grad
print("α1-2 = 180° - {0}°{1}′{2}″ = {3}°{4}′{5}″.".format(grad, mins, sec, gra, mins, sec))
if X_pro < 0 and Y_pro < 0:
print("3). По знакам приращений координат определяем, что линия находится в 3 четверти, и румб равен ")
print("= ЮЗ:{0}°{1}′{2}″.".format(grad, mins, sec))
print("4). Вычисляем дирекционный угол линии 1-2. Для 3 четверти согласно таблице, дирекционный угол ")
print("определяется по формуле α = r + 180°, тогда:")
gra = grad + 180
print("α1-2 = {0}°{1}′{2}″ + 180° = {3}°{4}′{5}″.".format(grad, mins, sec, gra, mins, sec))
if X_pro > 0 and
 
Y_pro < 0:
print("3). По знакам приращений координат определяем, что линия находится в 4 четверти, и румб равен ")
# grad1=360-grad
print("= СЗ:{0}°{1}′{2}″.".format(grad, mins, sec))
print("4). Вычисляем дирекционный угол линии 1-2. Для 4 четверти согласно таблице, дирекционный угол ")
print("определяется по формуле α =360° - r, тогда:")
gra = 360 - grad
print("α1-2 = 360° - {0}°{1}′{2}″ = {3}°{4}′{5}″.".format(grad, mins,gra, sec, mins, sec))

print("5). Трижды (для контроля) определяем горизонтальное проложение линии 1-2:")

print("d = √‾(ΔX*ΔX + ΔY2*ΔY2) = {0} м.".format(dd))

def obr_zd():
block_1()
block_2()
block_3()


while True:
otv=input("Если прямая напишите-пр, если обратная напишите-обр")
if otv=="пр":
pr_zd()
if otv == "обр":
obr_zd()



# ------------------------

import math
def dannie():
global d,x1,y1,nb,nt,np,xc
x1 = float(input("X-координата:"))
y1 = float(input("y-координата:"))
d = abs(float(input("Горизонтальное проложение:")))
print("Дерекционный угол:")
nb = abs(math.trunc(float(input("Градусы:"))))
np = abs(math.trunc(float(input("Минуты:"))))
xc = abs(math.trunc(float(input("Секунды:"))))
if nb > 360:
while True:
print("Градус не может быть больше 360!")
nb = abs(math.trunc(float(input("Введите градус заново:"))))
if nb < 360:
break
if np > 60:
while True:
print("Минута не может быть больше 60!")
np = abs(math.trunc(float(input("Введите минуту заново:"))))
if np < 60:
break
if xc > 60:
while True:
print("Секунда не может быть больше 60!")
xc = abs(math.trunc(float(input("Введите секунду заново:"))))
if xc < 60:
break


def qwe():
global crc,crs_pro,q,q1
crc = (xc / 100 + np) / 60
crs_pro = nb + crc

q = math.radians(crs_pro)
q1= q
def ty():
global bv,vb,X,Y,x2,y2,nu1,nu2,nur,nar,X1,Y1
bv = math.cos(q1)
vb = math.sin(q1)
X=d*bv
Y=d*vb
x2=x1+X
y2=y1+Y
def cv():
print("Проверьте введенные данные:")
print("Координаты первой точки:")
print("X = {0} метров;".format(x1))
print("Y = {0} метров.".format(y1))
print("Горизонтальное проложение между точками (длина линии): {0} метров.".format(d))
print("Дирекционный угол α = {0}°{1}′{2}″".format(nb, np, xc))
print("Решение прямой геодезической задачи:")
print("ΔX = d × cos {0}°{1}′{2}″ = {3}м × {4} = {5} метров.".format(nb, np, xc, d, bv, X))
print("ΔY = d × sin {0}°{1}′{2}″ = {3}м × {4} = {5} метров.".format(nb, np, xc, d, vb, Y))
print("X2 = X + ΔX = {0}м + {1}м = {2} метров;".format(x1, X, x2))
print("Y2 = Y + ΔY = {0}м + {1}м = {2} метров.".format(y1, Y, y2))
dannie()

qwe()
ty()
cv()