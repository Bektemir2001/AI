import numpy as np
import matplotlib.pyplot as plt
def Msigma(e):
    return(np.exp(e)-np.exp(-e))/(np.exp(e)+np.exp(-e))
N = 100
Xx, Xy, Classter, ClColor = [], [], [], []  # Класстердин координаталары
dolya1=0.4
dolya2=0.3
for i in range(N):
    if np.random.rand() < 0.5:
        Xx.append(dolya1*np.random.rand())  # 1-класстердин координаталары
        Xy.append(dolya1*np.random.rand())  # 1-класстердин координаталары
        Classter.append(1)
        ClColor.append('red')
    #elif np.random.rand() < 0.66:
    #    Xx.append(np.random.randint(1, 30))  # 2-класстердин координаталары
    #    Xy.append(np.random.randint(60, 90))  # 2-класстердин координаталары
    #    Xcolors.append(np.random.randint(0, len(MyColors)))
    else:
        Xx.append(1.0-dolya2*np.random.rand())  # 2-класстердин координаталары
        Xy.append(1.0-dolya2*np.random.rand())  # 2-класстердин координаталары
        Classter.append(-1)
        ClColor.append('blue')

plt.title('Берилген чекиттер', fontsize=20)
plt.scatter(Xx, Xy, s=100, c=ClColor, alpha=0.5)
plt.show()
#Нейрондун баштапкы маанилери
eta=0.1
w1,w2,w3 = 0.0, 0.0, 0.0
print('Нейрондун баштапкы маанилери')
print(w1)    
print(w2)    
print(w3)    
procent=0.80 # үйрөнүү үчүн көптүктүн канча прцентин алабыз
t = np.linspace(0.0, 1.0, 100) # график үчүн
# бакпропогейшн
for i in range(5): # Эпохалардын саны
    for k in range(0,int(procent*len(Classter))): #үйрөнүүчү берилиштер 
            e = w1+Xx[k]*w2+Xy[k]*w3
            y=Msigma(e)
            sigma=Classter[k]-y
            w1 = w1+eta*sigma*(1.0-y*y)
            w2 = w2+eta*sigma*(1.0-y*y)*Xx[k]
            w3 = w3+eta*sigma*(1.0-y*y)*Xy[k]
    plt.title('Эпоха '+str(i), fontsize=20)
    plt.scatter(Xx, Xy, s=100,  c=ClColor, alpha=0.5)
    plt.plot(t,(-w1-w2*t)/w3)
    plt.show()
    print('Үйрөтүлгөн Нейрондун маанилери')
    print(w1)    
    print(w2)    
    print(w3)    
plt.title('Жообу', fontsize=20)
plt.scatter(Xx, Xy, s=100,  c=ClColor, alpha=0.5)
plt.plot(t,(-w1-w2*t)/w3)
plt.show()
