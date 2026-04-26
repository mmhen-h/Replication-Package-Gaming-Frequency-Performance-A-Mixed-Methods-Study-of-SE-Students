import pandas as pd


def concatenate_data():
    path1 = "cleaned_dataset_for_quantitative_analysis/FA22_Cleaned_Data.csv"
    path2 = "cleaned_dataset_for_quantitative_analysis/FA23_Cleaned_Data.csv"
    path3 = "cleaned_dataset_for_quantitative_analysis/FA24_Cleaned_Data.csv"
    path4 = "cleaned_dataset_for_quantitative_analysis/FA25_Cleaned_Data.csv"
    path5 = "cleaned_dataset_for_quantitative_analysis/SP22_Cleaned_Data.csv"
    path6 = "cleaned_dataset_for_quantitative_analysis/SP23_Cleaned_Data.csv"
    path7 = "cleaned_dataset_for_quantitative_analysis/SP24_Cleaned_Data.csv"
    path8 = "cleaned_dataset_for_quantitative_analysis/SP25_Cleaned_Data.csv"
    concatenated_path = "../cleaned_dataset_for_quantitative_analysis/concatenated_Cleaned_Data.csv"
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)
    df3 = pd.read_csv(path3)
    df4 = pd.read_csv(path4)
    df5 = pd.read_csv(path5)
    df6 = pd.read_csv(path6)
    df7 = pd.read_csv(path7)
    df8 = pd.read_csv(path8)
    concatenated = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True)

    concatenated.to_csv(concatenated_path, index=False)


def clean_data():
    concatenated_path = "../cleaned_dataset_for_quantitative_analysis/concatenated_Cleaned_Data.csv"
    df = pd.read_csv(concatenated_path)
    data = {"final_score": [], "gaming_frequency": []}
    for index, row in df.iterrows():
        if pd.notna(df.loc[index, "frequency"]) and df.loc[index, "frequency"] != "NA":
            data["gaming_frequency"].append(df.loc[index, "frequency"])
            if pd.notna(df.loc[index, "finalscore"]):
                data["final_score"].append(df.loc[index, "finalscore"])
        else:
            if not df.loc[index, "gamer"]:
                data["gaming_frequency"].append(0)
                if pd.notna(df.loc[index, "finalscore"]):
                    data["final_score"].append(df.loc[index, "finalscore"])
    return data
