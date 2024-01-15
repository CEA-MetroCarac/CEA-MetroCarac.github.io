import numpy as np
import matplotlib.pyplot as plt
from fitspy.models import pseudovoigt

x = np.linspace(-10, 10, 201)
y = pseudovoigt(x, ampli=1, fwhm=2, x0=2, alpha=0.5)
plt.figure()
plt.grid()
plt.plot(x, y)