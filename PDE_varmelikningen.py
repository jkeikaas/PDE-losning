import numpy as np
import matplotlib.pyplot as plt

# Viser hvordan varmen sprer seg utover, numerisk løsning av varmelikningen:

n = 100 
deltaX = 0.1 
deltaY = 0.1  
deltaT = 0.1  

# Initialbetingelser
A = np.zeros((n, n))
mid = n // 2
A[mid, mid] = 50  # Initialtemperatur i midten

# Varmeelement
sizeHeatElement = 10
for i in range(mid - sizeHeatElement//2, mid + sizeHeatElement//2):
    for j in range(mid - sizeHeatElement//2, mid + sizeHeatElement//2):
        A[i, j] = 100


numSteps = 500
fig, ax = plt.subplots(figsize=(8, 6))

for step in range(numSteps):
    nextA = np.zeros((n, n))
    for i in range(1, n-1):
        for j in range(1, n-1):
            nextA[i, j] = -((A[i+1, j] - 2*A[i, j] + A[i-1, j]) / deltaX**2 +
                           (A[i, j+1] - 2*A[i, j] + A[i, j-1]) / deltaY**2) * deltaT + A[i, j]
    A = nextA

    # Plotting
    ax.clear()
    im = ax.imshow(A, cmap='hot', interpolation='nearest')
    ax.set_title('Numerisk løsning av varmelikningen')
    plt.pause(0.01)

plt.colorbar(im, ax=ax)
plt.show()

