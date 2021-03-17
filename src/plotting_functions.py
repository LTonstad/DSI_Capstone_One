import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def mil_format(x):
    return "${:.1f}M".format(x/1000000)

def k_format(x):
    return "${:.1f}K".format(x/1000)

if __name__ == '__main__':