import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
import seaborn as sns
# import matplotlib.patches as mpatches

sns.set(palette='Pastel2')
g = 9.81
v_0 = float(input("Enter initial velocity: "))
alpha = (float(input("Enter angle of launch: ")))*(np.pi/180)
height = float(input("Enter initial height: "))

def t_flight(v_0, alpha, height, g):
    tf = (v_0*np.sin(alpha)+((v_0*np.sin(alpha))**2+2*g*height)**0.5)/g
    return tf

def h_range(v_0, alpha, height, g):
    h = v_0*np.cos(alpha)*t_flight(v_0, alpha, height, g)
    return h

def y(x):
    y = np.tan(alpha)*x-(g*(x**2))/(2*(v_0*np.cos(alpha))**2)+height
    return y

t_f = t_flight(v_0, alpha, height, g)
h_r = h_range(v_0, alpha, height, g)
x = np.linspace(0, h_r, 100)
h = y(x)

guess = np.array([1])
max_x = minimize(lambda x: -y(x),guess)
max_y = y(max_x.x[0]) 
print(max_y)

# Rectangle((x,y), width, height, color, facecolor, transparency level)
# rect = mpatches.Rectangle((h_r*0.6,height), 1.6, 2, color = 'g', facecolor = 'g', alpha = 0.25)
# plt.gca().add_patch(rect)

plt.figure(num=1, dpi=120)
plt.plot(x,h,'b')
plt.title('Projectile Motion', color = 'k', fontweight = 'bold', size = 16)
plt.xlabel('Distance [m]', fontweight = 'bold', size = 11)
plt.ylabel('Height [m]', fontweight = 'bold', size = 11)
plt.plot(h_r,0, marker='D', color='r')
plt.plot(max_x.x[0],max_y, marker='D', color='g')
# plt.legend(['Trajectory','Horizontal range', 'Max height'])

plt.annotate(f'  {round(h_r,3)} [m]', xy = (h_r,0), xytext = (h_r,0))
plt.annotate(f'Time of flight {round(t_f,2)} [s]', xy = (h_r*0.6,height))

plt.grid()
plt.show()