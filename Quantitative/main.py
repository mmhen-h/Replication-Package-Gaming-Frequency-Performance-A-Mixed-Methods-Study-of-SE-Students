from Quantitative.chi_square import chi_test_binary, chi_test
from Quantitative.data_prepration import clean_data, concatenate_data
from Quantitative.logistice_regression import run_logistic_regression_bin
from Quantitative.plot import bar_plot_data, plot_mean_score_per_frequency, bar_plot_data_bin, \
    plot_mean_score_per_frequency_bin
from Quantitative.spearman_rank_order import spearman_test_bin

if __name__ == '__main__':
    # Call 'concatenate_data' once to concatenate the data
    # concatenate_data()

    # Get the data
    data = clean_data()

    # Run Chi-square test for the original 8 gaming frequency categories
    chi_test(data)

    # Run Chi-square test for 2 gaming frequency categories(low vs. high)
    chi_test_binary(data)

    # Run Logistic Regression test for 2 gaming frequency categories(low vs. high)
    run_logistic_regression_bin(data)

    # Run Spearman rank order test for 2 gaming frequency categories(low vs. high)
    spearman_test_bin(data)

    # Get line chart to show the overall trend of the data with original 8 categories
    plot_mean_score_per_frequency(data)

    # Get line chart to show the overall trend of the data for 2 gaming frequency categories(low vs. high)
    plot_mean_score_per_frequency_bin(data)

    # Get Bar Plot of the data with the original 8 gaming frequency categories
    bar_plot_data(data)

    # Get Bar Plot of the data with 2 gaming frequency categories(low vs. high)
    bar_plot_data_bin(data)




