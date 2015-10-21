import matplotlib.pyplot as plt

ax = []
ay = []
az = []
phi = []
theta = []
psi = []

file = open('haptic_data.txt', 'r')

time = 0

while(1):
	line = file.readline()
	if not line:
		break

	ax.append(int(line))
	line = file.readline()

	ay.append(int(line))
	line = file.readline()

	az.append(int(line))
	line = file.readline()

	phi.append(int(line))
	line = file.readline()

	theta.append(int(line))
	line = file.readline()

	psi.append(int(line))

	time += 1

file.close()

time = range(time) 

g1 = plt.figure(1)

plt.plot(time, ax, label='acceleration vector for ax')

plt.xlabel('time in seconds')
plt.ylabel('inches per second')
plt.title('X Acceleration Vector for Sensor 1')
plt.legend()

g1 = plt.figure(2)

plt.plot(time, ay, label='acceleration vector for ay')

plt.xlabel('time in seconds')
plt.ylabel('inches per second')
plt.title('Y Acceleration Vector for Sensor 1')
plt.legend()

g1 = plt.figure(3)

plt.plot(time, az, label='acceleration vector for az')

plt.xlabel('time in seconds')
plt.ylabel('inches per second')
plt.title('Z Acceleration Vector for Sensor 1')
plt.legend()

g1 = plt.figure(4)

plt.plot(time, phi, label='acceleration vector for phi')

plt.xlabel('time in seconds')
plt.ylabel('inches per second')
plt.title('Phi Rotation Vector for Sensor 1')
plt.legend()

g1 = plt.figure(5)

plt.plot(time, theta, label='acceleration vector for theta')

plt.xlabel('time in seconds')
plt.ylabel('inches per second')
plt.title('Theta Rotation Vector for Sensor 1')
plt.legend()

g1 = plt.figure(6)

plt.plot(time, psi, label='acceleration vector for psi')

plt.xlabel('time in seconds')
plt.ylabel('inches per second')
plt.title('Psi Rotation Vector for Sensor 1')
plt.legend()

plt.show()