import pandas as pd
import statsmodels.api as sm
import numpy as np


def run_logistic_regression_bin(data):
    """
    This function calculates logistic regression for 2 category of high and low gaming frequencies.
    """
    df = pd.DataFrame(data)
    threshold = 88
    df['is_high_score'] = (df['final_score'] >= threshold).astype(int)

    # 2. Re-categorize Gaming Frequency
    # 0-3 days -> 0 (Low), 4-7 days -> 1 (High)
    df['gaming_cat'] = np.where(df['gaming_frequency'] >= 4, 1, 0)

    # 3. Add constant for intercept
    # Use the new 'gaming_cat' instead of the raw frequency
    X = sm.add_constant(df['gaming_cat'])
    y = df['is_high_score']

    model = sm.Logit(y, X).fit(disp=False)

    params = model.params
    conf = model.conf_int()
    conf.columns = ['Lower CI', 'Upper CI']

    conf['Odds Ratio'] = np.exp(params)
    conf['Lower CI'] = np.exp(conf['Lower CI'])
    conf['Upper CI'] = np.exp(conf['Upper CI'])

    print(model.summary())
    print("\n--- Odds Ratios with 95% CI ---")
    print(conf)

    return conf
