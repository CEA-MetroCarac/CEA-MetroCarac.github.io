import numpy as np
import matplotlib.pyplot as plt
from fitspy.models import gaussian

x = np.linspace(-10, 10, 201)
y = gaussian(x, ampli=1, fwhm=2, x0=2)
plt.figure()
plt.grid()
plt.plot(x, y)