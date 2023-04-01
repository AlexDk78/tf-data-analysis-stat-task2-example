import pandas as pd
import numpy as np

chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import t
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    t_value = t.ppf(1 - (1-p)/2, n-1)
    margin_of_error = t_value * std / np.sqrt(n)
    lower_limit = mean - margin_of_error
    upper_limit = mean + margin_of_error
    return (lower_limit, upper_limit)
