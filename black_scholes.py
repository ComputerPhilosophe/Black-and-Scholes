import numpy as np
from scipy.stats import norm

r = 0.01
s = 30
k = 40
t = 240/365

# Volatility
sigma = 0.30

def blackScholes(r, s, k, t, sigma, option_type="C"):
    
    d1 = (np.log(s/k) + (r + sigma**2/2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    
    if option_type == "C":
        price = s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    elif option_type == "P":
        price = k * np.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'C' for Call or 'P' for Put.")
    
    return price

option_price = round(blackScholes(r, s, k, t, sigma, option_type="P"), 2)
print("Option Price is:", option_price)
