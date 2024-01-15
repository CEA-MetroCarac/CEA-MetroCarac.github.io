import numpy as np
import matplotlib.pyplot as plt
from fitspy.models import lorentzian

x = np.linspace(-10, 10, 201)
y = lorentzian(x, ampli=1, fwhm=2, x0=2)
plt.figure()
plt.grid()
plt.plot(x, y)