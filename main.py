import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0,150,1500)

# d is the number of groups (6 sets of peaks)
# t is for the 4 peaks in each set that have positive peaks
# n is for the 4 peaks in each set that have negative peaks
# Desmos reference: https://www.desmos.com/calculator/m8agxbd59z 

for d in range (1,8):
  if (d % 2 ==1):
    for t in range(4*d-4, 4*d,1):
      first_coef_up= 19/(math.sqrt(math.pi))
      exponent = -2 * ((x - 5*t - (5*d-2.5)) **2)
      y= first_coef_up * ((math.e)**exponent)
      plt.plot(x, y)
  else:
    for n in range(4*d-4, 4*d,1):
      first_coef_down = -19/(math.sqrt(math.pi)) 
      exponent = -2 * ((x- 5*n- (5*d-2))**2)
      y = first_coef_down * ((math.e)**exponent)
      plt.plot(x, y)

plt.title('Signal Strength vs Time Graph')
plt.xlabel('Time (s)', color='#1C2833')
plt.ylabel('Signal Strength (dB)', color='#1C2833')
plt.grid()
plt.show()