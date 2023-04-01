import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean_x = np.mean(x)
    std_x = np.std(x, ddof=1)
    t = norm.ppf(1 - (1-p)/2)
    interval = t * std_x / np.sqrt(n)
    left_limit = mean_x - interval
    right_limit = mean_x + interval
    return (left_limit, right_limit)
