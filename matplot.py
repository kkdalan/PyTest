import numpy as np
import matplotlib.pyplot as pt

x = np.arange(0,360)
y = np.sin( 2 * x * np.pi / 180.0)
z = np.cos( x * np.pi / 180.0)
k = 0.5 * np.cos( x * np.pi / 180.0)

pt.plot(x,y,color="blue",label="sin(2x)")
pt.plot(x,z,color="red",label="cos(x)")
pt.plot(x,k,color="green",label="0.5cos(x)")

pt.xlim(0,360)
pt.ylim(-1.2,1.2)

pt.xlabel("degree")
pt.ylabel("value")
pt.legend()
pt.grid()

pt.title("SIN & COS function")
pt.show()

