import matplotlib.pyplot as plt
x = 8
m = 1
b = 1
y = m*x+b
plt.plot(8, 2.6, 'kd')
plt.plot(y,x,'ro')
plt.ylabel('some numbers')
plt.xlabel('some more numbers')
plt.show()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print('Hello, World!')