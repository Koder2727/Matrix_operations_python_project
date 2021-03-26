import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#setting the numerator and denominator of the the transfer fucntion
numerator = [1]
denominator = [1,0.1]

#generate the frequency response with w 
w,h = signal.freqresp((numerator,denominator))

#seprate the magnitude and phase of frequency response  
magnitude = np.abs(h)
angle = np.angle(h)

#plot in subplot 1
plt.subplot(2,1,1)
plt.plot(w,magnitude,color="Orange")
plt.title("Frequency Response")
plt.legend(("Magnitude",),loc="upper right")

#plot in subplot 2
plt.subplot(2,1,2)
plt.plot(w,angle)
plt.xlabel("w(rad/s)")
plt.legend(("Phase",),loc="upper right")