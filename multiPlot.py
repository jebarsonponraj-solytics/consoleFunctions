
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Console.package import Functions


f = Functions()

col = f.get_args("arg1")
# your code here

np.random.seed(10)
data1 = np.random.normal(100, 20, 200)
data2 = np.random.normal(80, 15, 200)
data3 = np.random.normal(85,20,200)

# Creating the first boxplot and saving it as Image 1
fig1, ax1 = plt.subplots(figsize=(10, 7))
ax1.boxplot(data1)
f.save_image(fig1)

# Creating the second boxplot and saving it as Image 2
fig2, ax2 = plt.subplots(figsize=(10, 7))
ax2.boxplot(data2)
f.save_image(fig2)

# Creating the second boxplot and saving it as Image 3
fig3, ax3 = plt.subplots(figsize=(10, 7))
ax3.boxplot(data3)
f.save_image(fig3)
