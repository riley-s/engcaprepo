import pandas as pd


crp_2019_2020_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP 2019-2020 (Complete-City).csv')
crp_2020_2021_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\CRP 2020-2021 (Complete-City).csv')
mhp_2019_2020_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP 2019-2020 (Complete-City).csv')
mhp_2020_2021_df = pd.read_csv(r'C:\Users\riley_pwqtduf\Desktop\City Datasets\MHP 2020-2021 (Complete-City).csv')

# Add State column


crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Melbourne', 'State'] = 'VIC'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Melbourne', 'State'] = 'VIC'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Melbourne', 'State'] = 'VIC'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Melbourne', 'State'] = 'VIC'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Sydney', 'State'] = 'NSW'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Sydney', 'State'] = 'NSW'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Sydney', 'State'] = 'NSW'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Sydney', 'State'] = 'NSW'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Brisbane', 'State'] = 'QLD'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Brisbane', 'State'] = 'QLD'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Brisbane', 'State'] = 'QLD'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Brisbane', 'State'] = 'QLD'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Perth', 'State'] = 'WA'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Perth', 'State'] = 'WA'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Perth', 'State'] = 'WA'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Perth', 'State'] = 'WA'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Adelaide', 'State'] = 'SA'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Adelaide', 'State'] = 'SA'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Adelaide', 'State'] = 'SA'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Adelaide', 'State'] = 'SA'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Gold Coast', 'State'] = 'QLD'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Gold Coast', 'State'] = 'QLD'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Gold Coast', 'State'] = 'QLD'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Gold Coast', 'State'] = 'QLD'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Newcastle', 'State'] = 'NSW'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Newcastle', 'State'] = 'NSW'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Newcastle', 'State'] = 'NSW'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Newcastle', 'State'] = 'NSW'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Canberra', 'State'] = 'ACT'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Canberra', 'State'] = 'ACT'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Canberra', 'State'] = 'ACT'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Canberra', 'State'] = 'ACT'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Sunshine Coast', 'State'] = 'QLD'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Sunshine Coast', 'State'] = 'QLD'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Sunshine Coast', 'State'] = 'QLD'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Sunshine Coast', 'State'] = 'QLD'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Central Coast', 'State'] = 'NSW'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Central Coast', 'State'] = 'NSW'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Central Coast', 'State'] = 'NSW'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Central Coast', 'State'] = 'NSW'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Wollongong', 'State'] = 'NSW'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Wollongong', 'State'] = 'NSW'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Wollongong', 'State'] = 'NSW'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Wollongong', 'State'] = 'NSW'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Geelong', 'State'] = 'VIC'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Geelong', 'State'] = 'VIC'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Geelong', 'State'] = 'VIC'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Geelong', 'State'] = 'VIC'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Hobart', 'State'] = 'TAS'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Hobart', 'State'] = 'TAS'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Hobart', 'State'] = 'TAS'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Hobart', 'State'] = 'TAS'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Townsville', 'State'] = 'QLD'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Townsville', 'State'] = 'QLD'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Townsville', 'State'] = 'QLD'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Townsville', 'State'] = 'QLD'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Cairns', 'State'] = 'QLD'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Cairns', 'State'] = 'QLD'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Cairns', 'State'] = 'QLD'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Cairns', 'State'] = 'QLD'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Toowoomba', 'State'] = 'QLD'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Toowoomba', 'State'] = 'QLD'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Toowoomba', 'State'] = 'QLD'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Toowoomba', 'State'] = 'QLD'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Darwin', 'State'] = 'NT'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Darwin', 'State'] = 'NT'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Darwin', 'State'] = 'NT'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Darwin', 'State'] = 'NT'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Ballarat', 'State'] = 'VIC'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Ballarat', 'State'] = 'VIC'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Ballarat', 'State'] = 'VIC'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Ballarat', 'State'] = 'VIC'

crp_2019_2020_df.loc[crp_2019_2020_df.City == 'Bendigo', 'State'] = 'VIC'
crp_2020_2021_df.loc[crp_2020_2021_df.City == 'Bendigo', 'State'] = 'VIC'
mhp_2019_2020_df.loc[mhp_2019_2020_df.City == 'Bendigo', 'State'] = 'VIC'
mhp_2020_2021_df.loc[mhp_2020_2021_df.City == 'Bendigo', 'State'] = 'VIC'

# Add State number column
crp_2019_2020_df.loc[crp_2019_2020_df.State == 'NSW', 'State Code'] = 1
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'NSW', 'State Code'] = 1
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'NSW', 'State Code'] = 1
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'NSW', 'State Code'] = 1

crp_2019_2020_df.loc[crp_2019_2020_df.State == 'VIC', 'State Code'] = 2
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'VIC', 'State Code'] = 2
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'VIC', 'State Code'] = 2
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'VIC', 'State Code'] = 2

crp_2019_2020_df.loc[crp_2019_2020_df.State == 'QLD', 'State Code'] = 3
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'QLD', 'State Code'] = 3
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'QLD', 'State Code'] = 3
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'QLD', 'State Code'] = 3

crp_2019_2020_df.loc[crp_2019_2020_df.State == 'SA', 'State Code'] = 4
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'SA', 'State Code'] = 4
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'SA', 'State Code'] = 4
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'SA', 'State Code'] = 4

crp_2019_2020_df.loc[crp_2019_2020_df.State == 'WA', 'State Code'] = 5
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'WA', 'State Code'] = 5
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'WA', 'State Code'] = 5
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'WA', 'State Code'] = 5

crp_2019_2020_df.loc[crp_2019_2020_df.State == 'TAS', 'State Code'] = 6
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'TAS', 'State Code'] = 6
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'TAS', 'State Code'] = 6
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'TAS', 'State Code'] = 6

crp_2019_2020_df.loc[crp_2019_2020_df.State == 'NT', 'State Code'] = 7
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'NT', 'State Code'] = 7
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'NT', 'State Code'] = 7
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'NT', 'State Code'] = 7

crp_2019_2020_df.loc[crp_2019_2020_df.State == 'ACT', 'State Code'] = 8
crp_2020_2021_df.loc[crp_2020_2021_df.State == 'ACT', 'State Code'] = 8
mhp_2019_2020_df.loc[mhp_2019_2020_df.State == 'ACT', 'State Code'] = 8
mhp_2020_2021_df.loc[mhp_2020_2021_df.State == 'ACT', 'State Code'] = 8

# Save to csv
crp_2019_2020_df.sort_values(by=['State', 'City', 'Datetime', 'Text'], inplace=True, ascending=True)
crp_2019_2020_df.to_csv(r'CRP 2019-2020 (Complete-State).csv', sep=',', index=False)

crp_2020_2021_df.sort_values(by=['State', 'City', 'Datetime', 'Text'], inplace=True, ascending=True)
crp_2020_2021_df.to_csv(r'CRP 2020-2021 (Complete-State).csv', sep=',', index=False)

mhp_2019_2020_df.sort_values(by=['State', 'City', 'Datetime', 'Text'], inplace=True, ascending=True)
mhp_2019_2020_df.to_csv(r'MHP 2019-2020 (Complete-State).csv', sep=',', index=False)

mhp_2020_2021_df.sort_values(by=['State', 'City', 'Datetime', 'Text'], inplace=True, ascending=True)
mhp_2020_2021_df.to_csv(r'MHP 2020-2021 (Complete-State).csv', sep=',', index=False)