
from scipy import signal
import matplotlib.pyplot as plt

#setting the numerator and denominator of the the transfer fucntion
numerator = [0.1]
denominator = [1,0.1]

#generate the bode response with w 
w,h,angle = signal.bode((numerator,denominator))

#plot the bode response
plt.subplot(2,1,1)
plt.semilogx(w,h,color="Orange")
plt.title("Bode Plot")
plt.legend(("Magnitude",),loc="upper right")
plt.ylabel("dB")

#plot the phase response
plt.subplot(2,1,2)
plt.semilogx(w,angle,color="blue")
plt.xlabel("w(rad/s)")
plt.legend(("Phase",),loc="upper right")
plt.ylabel("dB")