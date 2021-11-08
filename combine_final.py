import pandas as pd
from collections import Counter

crp_2019_2020_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\States\CRP 2019-2020 (Complete-State).csv')
crp_2020_2021_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\States\CRP 2020-2021 (Complete-State).csv')
mhp_2019_2020_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\States\MHP 2019-2020 (Complete-State).csv')
mhp_2020_2021_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\States\MHP 2020-2021 (Complete-State).csv')

crp_df = pd.concat([crp_2019_2020_df, crp_2020_2021_df])
mhp_df = pd.concat([mhp_2019_2020_df, mhp_2020_2021_df])

crp_df.sort_values(by=['Datetime', 'State', 'City', 'Text'], inplace=True, ascending=True)
crp_df.to_csv('CRP (Complete).csv', sep=',', index=False)
mhp_df.sort_values(by=['Datetime', 'State', 'City', 'Text'], inplace=True, ascending=True)
mhp_df.to_csv('MHP (Complete).csv', sep=',', index=False)

df = pd.concat([crp_df, mhp_df])
df.sort_values(by=['Datetime', 'State', 'City', 'Text'], inplace=True, ascending=True)
df.to_csv('Australia (Complete).csv')

c = Counter(df['State'])
c.items()