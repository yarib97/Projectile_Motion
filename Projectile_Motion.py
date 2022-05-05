import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np
from scipy.optimize import minimize
import seaborn as sns

# Accepting only numeric input from the user
def check_numeric(value):
    """Checks if a string value is numeric and converts it to int or float"""
    while True:
        try:
            value = int(value)
            break
        except ValueError:
            try: 
                value = float(value)
                break
            except ValueError:
                value = input("Please, enter a numerical value: ")
    return value
 
# Receiving initial values from the user
v_0 = check_numeric(input("Enter initial velocity [m/s]: "))
angle_degrees = check_numeric(input("Enter angle of launch [deg]: "))
angle = angle_degrees*(np.pi/180)
height = check_numeric(input("Enter initial height [m]: "))

# Projectile motion functions
def t_flight(v_0, angle, height, g=9.81):
    """Returns time of flight"""
    tf = (v_0*np.sin(angle)+((v_0*np.sin(angle))**2+2*g*height)**0.5)/g
    return tf

def h_range(v_0, angle, height, g=9.81):
    """Returns horizontal range"""
    h = v_0*np.cos(angle)*t_flight(v_0, angle, height, g)
    return h

def y(x, g=9.81):
    """Returns the height at any point of the motion"""
    y = np.tan(angle)*x-(g*(x**2))/(2*(v_0*np.cos(angle))**2)+height
    return y

time_of_flight = t_flight(v_0, angle, height)
horizontal_range = h_range(v_0, angle, height)
x = np.linspace(0, horizontal_range, 100)
h = y(x)

guess = np.array([1])
max_x = minimize(lambda x: -y(x),guess)
max_y = y(max_x.x[0]) 

# Set color palette
sns.set_style('darkgrid')

# Plotting figure
plt.figure(num=1, dpi=120, figsize=(9,6))
plt.plot(x,h,'b')
plt.title('Projectile Motion',
        color='k',
        fontweight='bold',
        fontname='Century Gothic',
        size=18)
plt.xlabel('Distance [m]',
        fontweight='bold',
        fontname='Century Gothic',
        size=14)
plt.ylabel('Height [m]',
        fontweight='bold',
        fontname='Century Gothic',
        size=14)
plt.plot(horizontal_range,0, marker='D', color='r')
plt.plot(max_x.x[0],max_y, marker='D', color='g')
plt.annotate(f'Max range\n {round(horizontal_range,2)} [m]',
            xy=(horizontal_range,0),
            xytext=(0.865,0.725),
            xycoords='data',
            textcoords='axes fraction',
            weight='bold',
            fontname='Century Gothic',
            arrowprops=dict(arrowstyle='<|-',
                            connectionstyle='arc3',
                            edgecolor='r'),
            bbox=dict(facecolor='w', edgecolor='r', boxstyle='round'))
plt.annotate(f'Time of flight\n {round(time_of_flight,2)} [s]',
            xy=(0.865,0.825),
            xycoords='axes fraction',
            weight='bold',
            fontname='Century Gothic',
            bbox=dict(facecolor='w', edgecolor='b', boxstyle='round'))
plt.annotate(f'Max height\n x: {round(max_x.x[0],2)} [m]; y: {round(max_y,2)} [m]',
            xy=(max_x.x[0],max_y),
            xytext=(0.735,0.925),
            xycoords='data',
            textcoords='axes fraction',
            weight='bold',
            fontname='Century Gothic',
            arrowprops=dict(arrowstyle='<|-',
                            connectionstyle='arc3',
                            edgecolor='g'),
            bbox=dict(facecolor='w', edgecolor='g', boxstyle='round'))
plt.show()