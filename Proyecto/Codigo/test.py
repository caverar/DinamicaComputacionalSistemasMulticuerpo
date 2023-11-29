from IPython.display import display
import numpy as np
import sympy as sp
sp.init_printing(use_unicode = True, use_latex="mathjax")       # Print en LateX para sympy

q_values = np.array([  0,    0, np.deg2rad( 0),                      # Eslabón 1 (x, y, theta)
                     -23,   11, np.deg2rad( 21),                     # Eslabón 2 (x, y, theta)
                      23,   11, np.deg2rad(-21),                     # Eslabón 3 (x, y, theta)
                     -15,  1.5, np.deg2rad( 63),                     # Eslabón 4 (x, y, theta)
                       0,   10, np.deg2rad(  0),                     # Eslabón 5 (x, y, theta)
                      15,  1.5, np.deg2rad(-63),                     # Eslabón 6 (x, y, theta)
                     -15,   -8, np.deg2rad( 63),                     # Eslabón 7 (x, y, theta)
                      15,    8, np.deg2rad(-63),                     # Eslabón 8 (x, y, theta)
                     -16,-31.8, np.deg2rad(  0),                     # Eslabón 9 (x, y, theta)
                      16,-31.8, np.deg2rad(  0)                      # Eslabón 10 (x, y, theta)
                    ]).reshape(-1,1)

display(q_values)

qr_values = np.concatenate((q_values.reshape(-1)[0:6],q_values.reshape(-1)[9:15])).reshape(-1,1)
display(qr_values)