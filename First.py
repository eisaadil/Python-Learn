# %%
import math
import os

import numpy as np

import requests

print(np.__version__)

a = np.array([3, 42, 14, 22])
b = np.array([3, 2, 1, 2])

c = np.dot(a, b)
d = np.mean(a)

print(d)

print(c)

# %%
print(np.dot(a, b))

# %%
statusCode = requests.get("http://google.com").status_code
print(statusCode)

# %%
