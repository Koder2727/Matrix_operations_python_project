import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#setting the numerator and denominator of the the transfer fucntions
numerator = [1]
denominator=[10**-9,(10**-4.5)/(2**(-0.5)),1]

#generate the frequency response and the bode plot 
w,h = signal.freqresp((numerator,denominator))
w_bode , y_bode , x_bode = signal.bode((numerator,denominator),w=w)

#plot the frequency response
plt.figure()
plt.plot(w,np.angle(h),w,np.abs(h))
plt.title("frquency response")
plt.legend(("Phase","magnitude"),loc="upper right")
plt.xlabel("w(rad/s)")

#plot the bode plot vs frequency response

plt.figure()
plt.plot(w,np.abs(h),w_bode,y_bode)
plt.legend(("freq","bode"),loc="upper right")
plt.xlabel("w(rad/s)")
plt.title("Q=-0.5")