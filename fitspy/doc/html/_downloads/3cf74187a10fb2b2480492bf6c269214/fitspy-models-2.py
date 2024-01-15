import numpy as np
import matplotlib.pyplot as plt
from fitspy.models import gaussian_asym

x = np.linspace(-10, 10, 201)
y = gaussian_asym(x, ampli=1, fwhm_l=4, fwhm_r=2, x0=2)
plt.figure()
plt.grid()
plt.plot(x, y)