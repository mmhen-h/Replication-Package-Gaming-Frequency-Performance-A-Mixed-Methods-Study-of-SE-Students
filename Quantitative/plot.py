import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def bar_plot_data(data):
    counts_series = pd.Series(data["gaming_frequency"]).value_counts().sort_index()
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(7, 5))

    counts_series.index = counts_series.index.astype(int)
    plt.bar(counts_series.index, counts_series.values,
           color='lightgray',
           edgecolor='black',
           linewidth=1,
           width=0.6)

    plt.xlabel('Days per Week Gaming', fontsize=14)
    plt.ylabel('Number of Students ($N$)', fontsize=14)

    plt.xticks(counts_series.index, fontsize=12)
    plt.yticks(fontsize=12)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig("gaming_freq_distribution.pdf", dpi=300, bbox_inches='tight')
    plt.show()


def bar_plot_data_bin(data):
    df = pd.DataFrame(data)
    # Categorize: 0-3 -> Low, 4-7 -> High
    df['gaming_cat'] = np.where(df['gaming_frequency'] < 4, 'Low', 'High')
    counts = df['gaming_cat'].value_counts().reindex(['Low', 'High'])
    plt.style.use('seaborn-v0_8-paper')
    fig, ax = plt.subplots(figsize=(6, 5))

    ax.bar(counts.index, counts.values,
           color='lightgray',
           edgecolor='black',
           linewidth=1,
           width=0.6)

    ax.set_xlabel('Gaming Frequency Category', fontsize=14, labelpad=10)
    ax.set_ylabel('Total Number of Students', fontsize=14, labelpad=10)

    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Low Frequency Gamer\n(0-3 Days)', 'High Frequency Gamer\n(4-7 Days)'])
    ax.tick_params(axis='both', which='major', labelsize=12)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig("gaming_freq_bins_summary.pdf", dpi=300, bbox_inches='tight')
    plt.show()


def plot_mean_score_per_frequency_bin(data):
    df = pd.DataFrame(data)
    # 1. Create the binary category: 0-3 = Low, 4-7 = High
    # Using '0' and '1' as prefixes ensures the alphabetical sort puts Low first
    df['gaming_cat'] = np.where(df['gaming_frequency'] >= 4, 'High', 'Low')

    # 2. Group by the new category and calculate the mean
    # We reindex manually to ensure 'Low' is on the left and 'High' is on the right
    grouped_stats = (
        df.groupby('gaming_cat')['final_score']
        .mean()
        .reindex(['Low', 'High'])
        .reset_index()
    )

    plt.figure(figsize=(8, 5))
    plt.plot(grouped_stats['gaming_cat'],
             grouped_stats['final_score'],
             marker='o',
             linewidth=2,
             markersize=8)

    plt.xlabel('Gaming Frequency', fontsize=14)
    plt.ylabel('Average Final Score', fontsize=14)
    plt.grid(True)

    plt.margins(x=0.2)
    plt.savefig("LowHighTrend.pdf", format='pdf', bbox_inches='tight')
    plt.show()


def plot_mean_score_per_frequency(data):
    df = pd.DataFrame(data)
    grouped_stats = df.groupby('gaming_frequency')['final_score'].mean().reset_index()

    plt.figure(figsize=(8, 5))
    plt.plot(
        grouped_stats['gaming_frequency'],
        grouped_stats['final_score'],
        marker='o',
        linewidth=2,
        markersize=8,
    )

    plt.xlabel('Gaming Frequency', fontsize=14)
    plt.ylabel('Average Final Score', fontsize=14)

    plt.grid(True)
    plt.margins(x=0.2)

    plt.savefig("MeanFinalScorePerGamingFrequency.pdf", format='pdf', bbox_inches='tight')
    plt.show()
