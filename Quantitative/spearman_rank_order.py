import scipy.stats as stats
import numpy as np
import pandas as pd


def spearman_test_bin(data):
    """
       This function calculates spearman rank order test for 2 category of high and low gaming frequencies.
    """
    df = pd.DataFrame(data)
    df['gaming_cat'] = np.where(df['gaming_frequency'] >= 4, 1, 0)
    rho, p_val = stats.spearmanr(df['gaming_cat'], df['final_score'])

    print(f"Spearman's Rho: {rho:.4f}")
    print(f"P-value: {p_val:.5f}")

    if p_val < 0.05:
        print("Result: Statistically Significant")
    else:
        print("Result: Not Statistically Significant")
