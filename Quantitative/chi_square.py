import scipy.stats as stats
import numpy as np
import pandas as pd


def chi_test(data):
    """
       This function calculates Chi-square test for 8 original categories of gaming frequencies.
    """
    counts = pd.Series(data["gaming_frequency"]).value_counts().sort_index()
    count_list = {"day": counts.index.astype(int).tolist(),
                  "day_frequency": counts.tolist()}

    chi2, p = stats.chisquare(f_obs=count_list["day_frequency"])
    print("chi:", chi2, " p:", p)
    print(f" {chi2:<7.2f} | {p:<8.3f} ")

    print(count_list["day_frequency"])


def chi_test_binary(data):
    """
       This function calculates Chi-square test for 2 category of high and low gaming frequencies.
    """
    # Create the binary categories
    # 0-3 days -> Low, 4-7 days -> High
    df = pd.DataFrame(data)
    df['gaming_cat'] = np.where(df['gaming_frequency'] >= 4, 'High', 'Low')

    # Get observed frequencies for the 2 groups
    counts = df['gaming_cat'].value_counts().sort_index()
    observed = counts.tolist()

    # Run Chi-square (assumes equal distribution 50/50 as null hypothesis)
    chi2, p = stats.chisquare(f_obs=observed)

    print(f"Binary Chi-square Results (Low vs High):")
    print(f"Chi-square: {chi2:.2f} | p-value: {p:.5f}")
    print(f"Observed counts (High, Low): {observed}")
