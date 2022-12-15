import numpy as np
import random
import matplotlib.pyplot as plt
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def Y(a,b,x):       # Y(x)=Ax+B, a<=x<=b ==> Y(t)=A(b-a)t+Aa+B 0<=t<=1 
    return a*x+b
at,bt = -4.0, -9.0
N=100
procent=50.0 # procent - берилген коптуктун уйротууго алган элементтердин проценти
epoh = 10
gamma   = 0.1 # минимумга карай кадамдын тездиги - машинени(нейронду) уйротуу тездиги
MyColors = ['black', 'maroon', 'orange', 'lawngreen', 'dodgerblue', 'violet', 'crimson']
x=[];y=[];fcolors=[]
AllSet=[]
x = np.random.random(N) # t=(x-a)/(b-a) колдонуп баарын (0,1) 
for i in range(N):
    y.append(Y(at,bt,x[i])+np.random.random()/10)
    fcolors.append(np.random.randint(0, len(MyColors)))
    AllSet.append([x[i],y[i],fcolors[i]])
# Берилген көптүктүн графиги -AllSet
plt.title('Берилген көптүк y={:2.2f}'.format(at)+'x+{:2.2f}'.format(bt)+' ф-сынан алынды', fontsize=12)
plt.scatter(x, y, s=100, c=fcolors, alpha=0.5)
#plt.savefig("Start0.png")
# plt.show()

# Тест жасоочу көптүктү түзөбүз
Tx = []; Ty = []; Lcolors=[]; TestSet=[]; LN = int(0.01*(100-procent)*N)
TestSet = random.sample(AllSet,LN)
for k in range(LN):
    Tx.append(AllSet[k][0])
    Ty.append(AllSet[k][1])
    Lcolors.append(AllSet[k][2])

plt.title('Бул тестирлөөчү көптүк', fontsize=12)
plt.scatter(Tx, Ty, s=100, c=Lcolors, alpha=0.5)
plt.show()

# Үйрөтүүчү көптүктү түзөбүз - LearningSet=AllSet-TestSet
LearningSet=[]
Lx = []; Ly = []; Lcolors=[]
for item in AllSet:
    if item not in TestSet:
        Lx.append(item[0])
        Ly.append(item[1])
        Lcolors.append(item[2])
        LearningSet.append(item)
plt.title('Бул үйрөтүүчү көптүк', fontsize=12)
plt.scatter(Lx, Ly, s=100,  c=Lcolors, alpha=0.5)
plt.show()
        
# Нейрон эки параметрден турат:a жана b -параметрлери. Y=ax+b
# Башында a жана b -параметрлерин кокустан алабыз
a=np.random.random()
b=np.random.random()
print('Нейронун рандом менен берилген баштапкы маанилери a='+str('{:2.2f}'.format(a)) + '  b='+str('{:2.2f}'.format(b)))
print('Нейрондун параметрлерин үйрөтүүчү көптүктө Backpropagation методу менен табабыз (б.а. үйрөтөбүз)')
A=[];B=[];A.append(a);B.append(b);
for k in range(epoh):
    for item in LearningSet:
        delta = item[1] - Y(a,b,item[0])
        #delta = 1.0
        a1 = a + gamma*delta*item[0]
        b1 = b + gamma*delta
        a = a1
        b = b1
        A.append(a) 
        B.append(b)
    ErrorProcentL=100.0
    for item in LearningSet:
            RelativeErrorL = np.abs((Y(a,b,item[0]) - item[1]) / (max(abs(Y(a,b,item[0])), abs(item[1])))+1.0e-15)
            if  ErrorProcentL > 100 - 100 * RelativeErrorL:
                ErrorProcentL = 100 - 100 * RelativeErrorL
    ErrorProcentT=100.0
    for item in TestSet:
            RelativeErrorT = np.abs((Y(a,b,item[0]) - item[1]) / (max(abs(Y(a,b,item[0])), abs(item[1])))+1.0e-15)
            if  ErrorProcentT > 100 - 100 * RelativeErrorT:
                ErrorProcentT = 100 - 100 * RelativeErrorT
    print('Эпоха k=' +str('{:2.0f}'.format(k+1))+' үйрөнүүчү   көптүктөгү тактык '+str('{:2.2f}'.format(ErrorProcentL))+'%' +
                                               ' тестирлөөчү көптүктөгү тактык '+str('{:2.2f}'.format(ErrorProcentT))+'%')
print('Нейрондун үйрөтүүдө табылган жооп a=',a,'  b=',b)
print('Жыйынтык:\nБерилген көптүктүн саны N=',N)
print('Машинаны үйрөтүү көптүгү берилген көптүктүн ',procent,'пайызын түзөт.')
print('Эпоханын саны',epoh)
print('Нейронду үйрөтүү үчүн баштапкы маанилери a={:2.2f}'.format(A[0]),' b={:2.2f}'.format(B[0]))
print('       Нейронду үйрөткөндөн кийинки абал a='+str('{:2.2f}'.format(a)) + ' b='+str('{:2.2f}'.format(b)))
print('                                Так жооп a='+str('{:2.2f}'.format(at)) + ' b='+str('{:2.2f}'.format(bt)))
print('Үйрөнүүчү көптүктүгүндө Машинанын тактыгы ={:2.2f}'.format(ErrorProcentL)+'%')
print('     Тест көптүктүгүндө Машинанын тактыгы ={:2.2f}'.format(ErrorProcentT)+'%')
plt.title('Үйронүү. Так жооп a='+str('{:2.2f}'.format(at)) + ' b='+str('{:2.2f}'.format(bt)) +
          '. Болду a='+str('{:2.2f}'.format(a))+' b='+str('{:2.2f}'.format(b)), fontsize=12)
plt.plot(range(len(A)), A, label='a')
plt.plot(range(len(B)), B, label='b')
plt.legend()
plt.show()
# Машина даяр болду
# аргументти берип функциянын маанисин табабыз
#print(len(AllSet),len(TestSet),len(LearningSet))
print('Машина үйрөттук, ал иштөөгө даяр')
while True:
    print('x тин маанисин киргиз')
    tt=input()
    if is_number(tt):
        t=float(tt)
        print('X = {:2.2f}'.format(t) + ' анда Y= {:2.2f}'.format(Y(a,b,t)))
        print('Туура жооп Y= {:2.2f}'.format(Y(at,bt,t)))
    else:
        break