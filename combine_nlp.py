import pandas as pd

old_crp_2019_2020_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP 2019-2020 (NLP - DistilBERT).csv')
old_crp_2020_2021_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP 2020-2021 (NLP - DistilBERT).csv')
old_mhp_2019_2020_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP 2019-2020 (NLP - DistilBERT).csv')
old_mhp_2020_2021_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP 2020-2021 (NLP - DistilBERT).csv')

old_crp_2019_2020_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP 2019-2020 (NLP - BERT).csv')
old_crp_2020_2021_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP 2020-2021 (NLP - BERT).csv')
old_mhp_2019_2020_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP 2019-2020 (NLP - BERT).csv')
old_mhp_2020_2021_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP 2020-2021 (NLP - BERT).csv')

new_crp_2019_2020_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP Newcastle 2019-2020 (NLP - DistilBERT).csv')
new_crp_2020_2021_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP Newcastle 2020-2021 (NLP - DistilBERT).csv')
new_mhp_2019_2020_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP Newcastle 2019-2020 (NLP - DistilBERT).csv')
new_mhp_2020_2021_db_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP Newcastle 2020-2021 (NLP - DistilBERT).csv')

new_crp_2019_2020_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP Newcastle 2019-2020 (NLP - BERT).csv')
new_crp_2020_2021_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP Newcastle 2020-2021 (NLP - BERT).csv')
new_mhp_2019_2020_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP Newcastle 2019-2020 (NLP - BERT).csv')
new_mhp_2020_2021_b_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP Newcastle 2020-2021 (NLP - BERT).csv')

crp_2019_2020_db_df = pd.concat([old_crp_2019_2020_db_df, new_crp_2019_2020_db_df])
crp_2020_2021_db_df = pd.concat([old_crp_2020_2021_db_df, new_crp_2020_2021_db_df])
mhp_2019_2020_db_df = pd.concat([old_mhp_2019_2020_db_df, new_mhp_2019_2020_db_df])
mhp_2020_2021_db_df = pd.concat([old_mhp_2020_2021_db_df, new_mhp_2020_2021_db_df])

crp_2019_2020_b_df = pd.concat([old_crp_2019_2020_b_df, new_crp_2019_2020_b_df])
crp_2020_2021_b_df = pd.concat([old_crp_2020_2021_b_df, new_crp_2020_2021_b_df])
mhp_2019_2020_b_df = pd.concat([old_mhp_2019_2020_b_df, new_mhp_2019_2020_b_df])
mhp_2020_2021_b_df = pd.concat([old_mhp_2020_2021_b_df, new_mhp_2020_2021_b_df])

# Add BERT_Lable column
crp_2019_2020_b_df.loc[crp_2019_2020_b_df.BERT_Score == 1, 'BERT_Label'] = "Mostly Negative"
crp_2020_2021_b_df.loc[crp_2020_2021_b_df.BERT_Score == 1, 'BERT_Label'] = "Mostly Negative"
mhp_2019_2020_b_df.loc[mhp_2019_2020_b_df.BERT_Score == 1, 'BERT_Label'] = "Mostly Negative"
mhp_2020_2021_b_df.loc[mhp_2020_2021_b_df.BERT_Score == 1, 'BERT_Label'] = "Mostly Negative"

crp_2019_2020_b_df.loc[crp_2019_2020_b_df.BERT_Score == 2, 'BERT_Label'] = "Slightly Negative"
crp_2020_2021_b_df.loc[crp_2020_2021_b_df.BERT_Score == 2, 'BERT_Label'] = "Slightly Negative"
mhp_2019_2020_b_df.loc[mhp_2019_2020_b_df.BERT_Score == 2, 'BERT_Label'] = "Slightly Negative"
mhp_2020_2021_b_df.loc[mhp_2020_2021_b_df.BERT_Score == 2, 'BERT_Label'] = "Slightly Negative"

crp_2019_2020_b_df.loc[crp_2019_2020_b_df.BERT_Score == 3, 'BERT_Label'] = "Neutral"
crp_2020_2021_b_df.loc[crp_2020_2021_b_df.BERT_Score == 3, 'BERT_Label'] = "Neutral"
mhp_2019_2020_b_df.loc[mhp_2019_2020_b_df.BERT_Score == 3, 'BERT_Label'] = "Neutral"
mhp_2020_2021_b_df.loc[mhp_2020_2021_b_df.BERT_Score == 3, 'BERT_Label'] = "Neutral"

crp_2019_2020_b_df.loc[crp_2019_2020_b_df.BERT_Score == 4, 'BERT_Label'] = "Slightly Positive"
crp_2020_2021_b_df.loc[crp_2020_2021_b_df.BERT_Score == 4, 'BERT_Label'] = "Slightly Positive"
mhp_2019_2020_b_df.loc[mhp_2019_2020_b_df.BERT_Score == 4, 'BERT_Label'] = "Slightly Positive"
mhp_2020_2021_b_df.loc[mhp_2020_2021_b_df.BERT_Score == 4, 'BERT_Label'] = "Slightly Positive"

crp_2019_2020_b_df.loc[crp_2019_2020_b_df.BERT_Score == 5, 'BERT_Label'] = "Mostly Positive"
crp_2020_2021_b_df.loc[crp_2020_2021_b_df.BERT_Score == 5, 'BERT_Label'] = "Mostly Positive"
mhp_2019_2020_b_df.loc[mhp_2019_2020_b_df.BERT_Score == 5, 'BERT_Label'] = "Mostly Positive"
mhp_2020_2021_b_df.loc[mhp_2020_2021_b_df.BERT_Score == 5, 'BERT_Label'] = "Mostly Positive"

# Sorted by City
# CRP 2019 - 2020
crp_2019_2020_dfs = pd.merge(crp_2019_2020_db_df, crp_2019_2020_b_df)
crp_2019_2020_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
crp_2019_2020_dfs.sort_values(by=['City', 'Datetime', 'Text'], inplace=True, ascending=True)
crp_2019_2020_dfs.to_csv('CRP 2019-2020 (Complete-City).csv', sep=',', index=False)

# CRP 2020 - 2021
crp_2020_2021_dfs = pd.merge(crp_2020_2021_db_df, crp_2020_2021_b_df)
crp_2020_2021_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
crp_2020_2021_dfs.sort_values(by=['City', 'Datetime', 'Text'], inplace=True, ascending=True)
crp_2020_2021_dfs.to_csv('CRP 2020-2021 (Complete-City).csv', sep=',', index=False)

# MHP 2019 - 2020
mhp_2019_2020_dfs = pd.merge(mhp_2019_2020_db_df, mhp_2019_2020_b_df)
mhp_2019_2020_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
mhp_2019_2020_dfs.sort_values(by=['City', 'Datetime', 'Text'], inplace=True, ascending=True)
mhp_2019_2020_dfs.to_csv('MHP 2019-2020 (Complete-City).csv', sep=',', index=False)

# MHP 2020 - 2021
mhp_2020_2021_dfs = pd.merge(mhp_2020_2021_db_df, mhp_2020_2021_b_df)
mhp_2020_2021_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
mhp_2020_2021_dfs.sort_values(by=['City', 'Datetime', 'Text'], inplace=True, ascending=True)
mhp_2020_2021_dfs.to_csv('MHP 2020-2021 (Complete-City).csv', sep=',', index=False)


# # Sorted by Datetime
# # CRP 2019 - 2020
# crp_2019_2020_dfs = pd.merge(crp_2019_2020_db_df, crp_2019_2020_b_df)
# crp_2019_2020_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
# crp_2019_2020_dfs.sort_values(by=['Datetime', 'City', 'Text'], inplace=True, ascending=False)
# crp_2019_2020_dfs.to_csv('CRP 2019-2020 (Complete-Datetime).csv', sep=',', index=False)

# # CRP 2020 - 2021
# crp_2020_2021_dfs = pd.merge(crp_2020_2021_db_df, crp_2020_2021_b_df)
# crp_2020_2021_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
# crp_2020_2021_dfs.sort_values(by=['Datetime', 'City', 'Text'], inplace=True, ascending=False)
# crp_2020_2021_dfs.to_csv('CRP 2020-2021 (Complete-Datetime).csv', sep=',', index=False)

# # MHP 2019 - 2020
# mhp_2019_2020_dfs = pd.merge(mhp_2019_2020_db_df, mhp_2019_2020_b_df)
# mhp_2019_2020_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
# mhp_2019_2020_dfs.sort_values(by=['Datetime', 'City', 'Text'], inplace=True, ascending=False)
# mhp_2019_2020_dfs.to_csv('MHP 2019-2020 (Complete-Datetime).csv', sep=',', index=False)

# # MHP 2020 - 2021
# mhp_2020_2021_dfs = pd.merge(mhp_2020_2021_db_df, mhp_2020_2021_b_df)
# mhp_2020_2021_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
# mhp_2020_2021_dfs.sort_values(by=['Datetime', 'City', 'Text'], inplace=True, ascending=False)
# mhp_2020_2021_dfs.to_csv('MHP 2020-2021 (Complete-Datetime).csv', sep=',', index=False)