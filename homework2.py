import numpy as np 
import matplotlib.pyplot as plt
import random
def F(x, a, b, c):
	return (a*x**2)+(b*x)+c


def train(w, x, y):
	epoh = 10
	g = 0.1 
	for j in range(epoh):
		for i in range(len(x)):
			delta = y[i]-F(x[i], w[0], w[1], w[2])
			w0 = w[0] + g*delta*x[i]**2
			w1 = w[1] + g*delta*x[i]
			w2 = w[2] + g*delta
			w = [w0, w1, w2]
	return w 



def getRandomPointsAndCalassificate(n, w):
	x = [_ for _ in range(n)]
	y = [_ for _ in range(n)]
	i = 0
	while i < n:
		x[i] = random.randint(-50, 50)
		y[i] = random.randint(-50, 50)
		i += 1

	i = 0
	cx1 = []
	cy1 = []
	cx2 = []
	cy2 = []
	while i < n:
		yt = F(x[i], w[0], w[1], w[2])
		if yt <= y[i]:
			cx1.append(x[i])
			cy1.append(y[i])
		else:
			cx2.append(x[i])
			cy2.append(y[i])
		i += 1
	return [cx1, cy1], [cx2, cy2]
def classificate(x, y, w):
	cx1 = []
	cy1 = []
	cx2 = []
	cy2 = []
	yt = F(x, w[0], w[1], w[2])
	if yt <= y:
		cx1.append(x)
		cy1.append(y)
	else:
		cx2.append(x)
		cy2.append(y)
	return [cx1, cy1], [cx2, cy2]


a = 2
b = 5
c = 1


N = 1000
x = []
y = []

x = np.random.random(N+1)
y = [F(i, a, b, c)+np.random.random()/10 for i in x]
w = [np.random.random() for i in range(3)]

print(f'чыныгы маанилер: a = {a}, b = {b}, c = {c}')
print(f'кокус алынган маанилер = {w}')
w = train(w, x, y)
print(f'окутулгандан кийинки маанилер = {w}')

c1, c2 = getRandomPointsAndCalassificate(1000, w)
x = []
y = []
i = -100
while i <= 100:
	x.append(i)
	y.append(F(i, a, b, c))
	i += 1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

ax.scatter(c1[0][:], c1[1][:], s=10, c='red')
ax.scatter(c2[0][:], c2[1][:], s=10, c='blue')
ax.plot(x, y)
ax.set(xlim=(-20, 20), ylim=(-20, 50))
plt.show()
while True:
	xt = input('x = ')
	if len(xt) == 0:
		break
	else:
		xt = float(xt)
	yt = input('y = ')
	if len(yt) == 0:
		break
	else:
		yt = float(yt)
	c1, c2 = classificate(xt, yt, w)
	fig = plt.figure(figsize=(7, 4))
	ax = fig.add_subplot()
	ax.scatter(c1[0][:], c1[1][:], s=10, c='red')
	ax.scatter(c2[0][:], c2[1][:], s=10, c='blue')
	ax.plot(x, y)
	ax.set(xlim=(-20, 20), ylim=(-20, 50))
	plt.show()