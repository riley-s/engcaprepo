import snscrape.modules.twitter as sntwitter
import pandas as pd
from functools import reduce
import itertools
from standard_data import *

# Melbourne
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_covid19_df = pd.DataFrame(mel_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_covid19_df.insert(0, 'City', 'Melbourne')
mel_covid19_df.to_csv('Melbourne 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_coronavirus_df = pd.DataFrame(mel_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_coronavirus_df.insert(0, 'City', 'Melbourne')
mel_coronavirus_df.to_csv('Melbourne 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_pandemic_df = pd.DataFrame(mel_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_pandemic_df.insert(0, 'City', 'Melbourne')
mel_pandemic_df.to_csv('Melbourne 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_lockdown_df = pd.DataFrame(mel_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_lockdown_df.insert(0, 'City', 'Melbourne')
mel_lockdown_df.to_csv('Melbourne 20-21 (lockdown).csv', sep=',', index=False)

mel_dfs = pd.concat([mel_covid19_df, mel_coronavirus_df, mel_pandemic_df, mel_lockdown_df])
mel_dfs.to_csv('Melbourne CRP 20-21 (Combined).csv', sep=',', index=False)

# Sydney
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_covid19_df = pd.DataFrame(syd_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_covid19_df.insert(0, 'City', 'Sydney')
syd_covid19_df.to_csv('Sydney 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_coronavirus_df = pd.DataFrame(syd_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_coronavirus_df.insert(0, 'City', 'Sydney')
syd_coronavirus_df.to_csv('Sydney 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_pandemic_df = pd.DataFrame(syd_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_pandemic_df.insert(0, 'City', 'Sydney')
syd_pandemic_df.to_csv('Sydney 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_lockdown_df = pd.DataFrame(syd_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_lockdown_df.insert(0, 'City', 'Sydney')
syd_lockdown_df.to_csv('Sydney 20-21 (lockdown).csv', sep=',', index=False)

syd_dfs = pd.concat([syd_covid19_df, syd_coronavirus_df, syd_pandemic_df, syd_lockdown_df])
syd_dfs.to_csv('Sydney CRP 20-21 (Combined).csv', sep=',', index=False)

# Brisbane
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_covid19_df = pd.DataFrame(bri_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_covid19_df.insert(0, 'City', 'Brisbane')
bri_covid19_df.to_csv('Brisbane 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_coronavirus_df = pd.DataFrame(bri_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_coronavirus_df.insert(0, 'City', 'Brisbane')
bri_coronavirus_df.to_csv('Brisbane 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_pandemic_df = pd.DataFrame(bri_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_pandemic_df.insert(0, 'City', 'Brisbane')
bri_pandemic_df.to_csv('Brisbane 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_lockdown_df = pd.DataFrame(bri_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_lockdown_df.insert(0, 'City', 'Brisbane')
bri_lockdown_df.to_csv('Brisbane 20-21 (lockdown).csv', sep=',', index=False)

bri_dfs = pd.concat([bri_covid19_df, bri_coronavirus_df, bri_pandemic_df, bri_lockdown_df])
bri_dfs.to_csv('Brisbane CRP 20-21 (Combined).csv', sep=',', index=False)

# Perth
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_covid19_df = pd.DataFrame(per_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_covid19_df.insert(0, 'City', 'Perth')
per_covid19_df.to_csv('Perth 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_coronavirus_df = pd.DataFrame(per_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_coronavirus_df.insert(0, 'City', 'Perth')
per_coronavirus_df.to_csv('Perth 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_pandemic_df = pd.DataFrame(per_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_pandemic_df.insert(0, 'City', 'Perth')
per_pandemic_df.to_csv('Perth 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_lockdown_df = pd.DataFrame(per_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_lockdown_df.insert(0, 'City', 'Perth')
per_lockdown_df.to_csv('Perth 20-21 (lockdown).csv', sep=',', index=False)

per_dfs = pd.concat([per_covid19_df, per_coronavirus_df, per_pandemic_df, per_lockdown_df])
per_dfs.to_csv('Perth CRP 20-21 (Combined).csv', sep=',', index=False)

# Adelaide
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_covid19_df = pd.DataFrame(ade_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_covid19_df.insert(0, 'City', 'Adelaide')
ade_covid19_df.to_csv('Adelaide 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_coronavirus_df = pd.DataFrame(ade_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_coronavirus_df.insert(0, 'City', 'Adelaide')
ade_coronavirus_df.to_csv('Adelaide 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_pandemic_df = pd.DataFrame(ade_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_pandemic_df.insert(0, 'City', 'Adelaide')
ade_pandemic_df.to_csv('Adelaide 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_lockdown_df = pd.DataFrame(ade_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_lockdown_df.insert(0, 'City', 'Adelaide')
ade_lockdown_df.to_csv('Adelaide 20-21 (lockdown).csv', sep=',', index=False)

ade_dfs = pd.concat([ade_covid19_df, ade_coronavirus_df, ade_pandemic_df, ade_lockdown_df])
ade_dfs.to_csv('Adelaide CRP 20-21 (Combined).csv', sep=',', index=False)

# Gold Coast
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_covid19_df = pd.DataFrame(golcoa_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_covid19_df.insert(0, 'City', 'Gold Coast')
golcoa_covid19_df.to_csv('Gold Coast 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_coronavirus_df = pd.DataFrame(golcoa_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_coronavirus_df.insert(0, 'City', 'Gold Coast')
golcoa_coronavirus_df.to_csv('Gold Coast 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_pandemic_df = pd.DataFrame(golcoa_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_pandemic_df.insert(0, 'City', 'Gold Coast')
golcoa_pandemic_df.to_csv('Gold Coast 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_lockdown_df = pd.DataFrame(golcoa_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_lockdown_df.insert(0, 'City', 'Gold Coast')
golcoa_lockdown_df.to_csv('Gold Coast 20-21 (lockdown).csv', sep=',', index=False)

golcoa_dfs = pd.concat([golcoa_covid19_df, golcoa_coronavirus_df, golcoa_pandemic_df, golcoa_lockdown_df])
golcoa_dfs.to_csv('Gold Coast CRP 20-21 (Combined).csv', sep=',', index=False)

# Newcastle
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_covid19_df = pd.DataFrame(new_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_covid19_df.insert(0, 'City', 'Newcastle')
new_covid19_df.to_csv('Newcastle 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_coronavirus_df = pd.DataFrame(new_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_coronavirus_df.insert(0, 'City', 'Newcastle')
new_coronavirus_df.to_csv('Newcastle 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_pandemic_df = pd.DataFrame(new_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_pandemic_df.insert(0, 'City', 'Newcastle')
new_pandemic_df.to_csv('Newcastle 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_lockdown_df = pd.DataFrame(new_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_lockdown_df.insert(0, 'City', 'Newcastle')
new_lockdown_df.to_csv('Newcastle 20-21 (lockdown).csv', sep=',', index=False)

new_dfs = pd.concat([new_covid19_df, new_coronavirus_df, new_pandemic_df, new_lockdown_df])
new_dfs.to_csv('Newcastle CRP 20-21 (Combined).csv', sep=',', index=False)

# Canberra
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_covid19_df = pd.DataFrame(can_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_covid19_df.insert(0, 'City', 'Canberra')
can_covid19_df.to_csv('Canberra 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_coronavirus_df = pd.DataFrame(can_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_coronavirus_df.insert(0, 'City', 'Canberra')
can_coronavirus_df.to_csv('Canberra 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_pandemic_df = pd.DataFrame(can_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_pandemic_df.insert(0, 'City', 'Canberra')
can_pandemic_df.to_csv('Canberra 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_lockdown_df = pd.DataFrame(can_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_lockdown_df.insert(0, 'City', 'Canberra')
can_lockdown_df.to_csv('Canberra 20-21 (lockdown).csv', sep=',', index=False)

can_dfs = pd.concat([can_covid19_df, can_coronavirus_df, can_pandemic_df, can_lockdown_df])
can_dfs.to_csv('Canberra CRP 20-21 (Combined).csv', sep=',', index=False)

# Sunshine Coast
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_covid19_df = pd.DataFrame(suncoa_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_covid19_df.insert(0, 'City', 'Sunshine Coast')
suncoa_covid19_df.to_csv('Sunshine Coast 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_coronavirus_df = pd.DataFrame(suncoa_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_coronavirus_df.insert(0, 'City', 'Sunshine Coast')
suncoa_coronavirus_df.to_csv('Sunshine Coast 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_pandemic_df = pd.DataFrame(suncoa_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_pandemic_df.insert(0, 'City', 'Sunshine Coast')
suncoa_pandemic_df.to_csv('Sunshine Coast 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_lockdown_df = pd.DataFrame(suncoa_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_lockdown_df.insert(0, 'City', 'Sunshine Coast')
suncoa_lockdown_df.to_csv('Sunshine Coast 20-21 (lockdown).csv', sep=',', index=False)

suncoa_dfs = pd.concat([suncoa_covid19_df, suncoa_coronavirus_df, suncoa_pandemic_df, suncoa_lockdown_df])
suncoa_dfs.to_csv('Sunshine Coast CRP 20-21 (Combined).csv', sep=',', index=False)

# Central Coast
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_covid19_df = pd.DataFrame(cencoa_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_covid19_df.insert(0, 'City', 'Central Coast')
cencoa_covid19_df.to_csv('Central Coast 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_coronavirus_df = pd.DataFrame(cencoa_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_coronavirus_df.insert(0, 'City', 'Central Coast')
cencoa_coronavirus_df.to_csv('Central Coast 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_pandemic_df = pd.DataFrame(cencoa_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_pandemic_df.insert(0, 'City', 'Central Coast')
cencoa_pandemic_df.to_csv('Central Coast 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_lockdown_df = pd.DataFrame(cencoa_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_lockdown_df.insert(0, 'City', 'Central Coast')
cencoa_lockdown_df.to_csv('Central Coast 20-21 (lockdown).csv', sep=',', index=False)

cencoa_dfs = pd.concat([cencoa_covid19_df, cencoa_coronavirus_df, cencoa_pandemic_df, cencoa_lockdown_df])
cencoa_dfs.to_csv('Central Coast CRP 20-21 (Combined).csv', sep=',', index=False)

# Wollongong
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_covid19_df = pd.DataFrame(wol_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_covid19_df.insert(0, 'City', 'Wollongong')
wol_covid19_df.to_csv('Wollongong 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_coronavirus_df = pd.DataFrame(wol_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_coronavirus_df.insert(0, 'City', 'Wollongong')
wol_coronavirus_df.to_csv('Wollongong 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_pandemic_df = pd.DataFrame(wol_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_pandemic_df.insert(0, 'City', 'Wollongong')
wol_pandemic_df.to_csv('Wollongong 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_lockdown_df = pd.DataFrame(wol_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_lockdown_df.insert(0, 'City', 'Wollongong')
wol_lockdown_df.to_csv('Wollongong 20-21 (lockdown).csv', sep=',', index=False)

wol_dfs = pd.concat([wol_covid19_df, wol_coronavirus_df, wol_pandemic_df, wol_lockdown_df])
wol_dfs.to_csv('Wollongong CRP 20-21 (Combined).csv', sep=',', index=False)

# Geelong
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_covid19_df = pd.DataFrame(gee_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_covid19_df.insert(0, 'City', 'Geelong')
gee_covid19_df.to_csv('Geelong 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_coronavirus_df = pd.DataFrame(gee_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_coronavirus_df.insert(0, 'City', 'Geelong')
gee_coronavirus_df.to_csv('Geelong 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_pandemic_df = pd.DataFrame(gee_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_pandemic_df.insert(0, 'City', 'Geelong')
gee_pandemic_df.to_csv('Geelong 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_lockdown_df = pd.DataFrame(gee_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_lockdown_df.insert(0, 'City', 'Geelong')
gee_lockdown_df.to_csv('Geelong 20-21 (lockdown).csv', sep=',', index=False)

gee_dfs = pd.concat([gee_covid19_df, gee_coronavirus_df, gee_pandemic_df, gee_lockdown_df])
gee_dfs.to_csv('Geelong CRP 20-21 (Combined).csv', sep=',', index=False)

# Hobart
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_covid19_df = pd.DataFrame(hob_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_covid19_df.insert(0, 'City', 'Hobart')
hob_covid19_df.to_csv('Hobart 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_coronavirus_df = pd.DataFrame(hob_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_coronavirus_df.insert(0, 'City', 'Hobart')
hob_coronavirus_df.to_csv('Hobart 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_pandemic_df = pd.DataFrame(hob_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_pandemic_df.insert(0, 'City', 'Hobart')
hob_pandemic_df.to_csv('Hobart 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_lockdown_df = pd.DataFrame(hob_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_lockdown_df.insert(0, 'City', 'Hobart')
hob_lockdown_df.to_csv('Hobart 20-21 (lockdown).csv', sep=',', index=False)

hob_dfs = pd.concat([hob_covid19_df, hob_coronavirus_df, hob_pandemic_df, hob_lockdown_df])
hob_dfs.to_csv('Hobart CRP 20-21 (Combined).csv', sep=',', index=False)

# Townsville
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_covid19_df = pd.DataFrame(tow_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_covid19_df.insert(0, 'City', 'Townsville')
tow_covid19_df.to_csv('Townsville 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_coronavirus_df = pd.DataFrame(tow_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_coronavirus_df.insert(0, 'City', 'Townsville')
tow_coronavirus_df.to_csv('Townsville 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_pandemic_df = pd.DataFrame(tow_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_pandemic_df.insert(0, 'City', 'Townsville')
tow_pandemic_df.to_csv('Townsville 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_lockdown_df = pd.DataFrame(tow_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_lockdown_df.insert(0, 'City', 'Townsville')
tow_lockdown_df.to_csv('Townsville 20-21 (lockdown).csv', sep=',', index=False)

tow_dfs = pd.concat([tow_covid19_df, tow_coronavirus_df, tow_pandemic_df, tow_lockdown_df])
tow_dfs.to_csv('Townsville CRP 20-21 (Combined).csv', sep=',', index=False)

# Cairns
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_covid19_df = pd.DataFrame(cai_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_covid19_df.insert(0, 'City', 'Cairns')
cai_covid19_df.to_csv('Cairns 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_coronavirus_df = pd.DataFrame(cai_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_coronavirus_df.insert(0, 'City', 'Cairns')
cai_coronavirus_df.to_csv('Cairns 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_pandemic_df = pd.DataFrame(cai_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_pandemic_df.insert(0, 'City', 'Cairns')
cai_pandemic_df.to_csv('Cairns 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_lockdown_df = pd.DataFrame(cai_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_lockdown_df.insert(0, 'City', 'Cairns')
cai_lockdown_df.to_csv('Cairns 20-21 (lockdown).csv', sep=',', index=False)

cai_dfs = pd.concat([cai_covid19_df, cai_coronavirus_df, cai_pandemic_df, cai_lockdown_df])
cai_dfs.to_csv('Cairns CRP 20-21 (Combined).csv', sep=',', index=False)

# Toowoomba
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_covid19_df = pd.DataFrame(too_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_covid19_df.insert(0, 'City', 'Toowoomba')
too_covid19_df.to_csv('Toowoomba 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_coronavirus_df = pd.DataFrame(too_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_coronavirus_df.insert(0, 'City', 'Toowoomba')
too_coronavirus_df.to_csv('Toowoomba 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_pandemic_df = pd.DataFrame(too_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_pandemic_df.insert(0, 'City', 'Toowoomba')
too_pandemic_df.to_csv('Toowoomba 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_lockdown_df = pd.DataFrame(too_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_lockdown_df.insert(0, 'City', 'Toowoomba')
too_lockdown_df.to_csv('Toowoomba 20-21 (lockdown).csv', sep=',', index=False)

too_dfs = pd.concat([too_covid19_df, too_coronavirus_df, too_pandemic_df, too_lockdown_df])
too_dfs.to_csv('Toowoomba CRP 20-21 (Combined).csv', sep=',', index=False)

# Darwin
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_covid19_df = pd.DataFrame(dar_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_covid19_df.insert(0, 'City', 'Darwin')
dar_covid19_df.to_csv('Darwin 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_coronavirus_df = pd.DataFrame(dar_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_coronavirus_df.insert(0, 'City', 'Darwin')
dar_coronavirus_df.to_csv('Darwin 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_pandemic_df = pd.DataFrame(dar_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_pandemic_df.insert(0, 'City', 'Darwin')
dar_pandemic_df.to_csv('Darwin 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_lockdown_df = pd.DataFrame(dar_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_lockdown_df.insert(0, 'City', 'Darwin')
dar_lockdown_df.to_csv('Darwin 20-21 (lockdown).csv', sep=',', index=False)

dar_dfs = pd.concat([dar_covid19_df, dar_coronavirus_df, dar_pandemic_df, dar_lockdown_df])
dar_dfs.to_csv('Darwin CRP 20-21 (Combined).csv', sep=',', index=False)

# Ballarat
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_covid19_df = pd.DataFrame(bal_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_covid19_df.insert(0, 'City', 'Ballarat')
bal_covid19_df.to_csv('Ballarat 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_coronavirus_df = pd.DataFrame(bal_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_coronavirus_df.insert(0, 'City', 'Ballarat')
bal_coronavirus_df.to_csv('Ballarat 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_pandemic_df = pd.DataFrame(bal_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_pandemic_df.insert(0, 'City', 'Ballarat')
bal_pandemic_df.to_csv('Ballarat 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_lockdown_df = pd.DataFrame(bal_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_lockdown_df.insert(0, 'City', 'Ballarat')
bal_lockdown_df.to_csv('Ballarat 20-21 (lockdown).csv', sep=',', index=False)

bal_dfs = pd.concat([bal_covid19_df, bal_coronavirus_df, bal_pandemic_df, bal_lockdown_df])
bal_dfs.to_csv('Ballarat CRP 20-21 (Combined).csv', sep=',', index=False)

# Bendigo
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_covid19_df = pd.DataFrame(ben_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_covid19_df.insert(0, 'City', 'Bendigo')
ben_covid19_df.to_csv('Bendigo 20-21 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_coronavirus_df = pd.DataFrame(ben_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_coronavirus_df.insert(0, 'City', 'Bendigo')
ben_coronavirus_df.to_csv('Bendigo 20-21 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_pandemic_df = pd.DataFrame(ben_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_pandemic_df.insert(0, 'City', 'Bendigo')
ben_pandemic_df.to_csv('Bendigo 20-21 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2020-03-11 until:2021-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_lockdown_df = pd.DataFrame(ben_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_lockdown_df.insert(0, 'City', 'Bendigo')
ben_lockdown_df.to_csv('Bendigo 20-21 (lockdown).csv', sep=',', index=False)

ben_dfs = pd.concat([ben_covid19_df, ben_coronavirus_df, ben_pandemic_df, ben_lockdown_df])
ben_dfs.to_csv('Bendigo CRP 20-21 (Combined).csv', sep=',', index=False)




crp_2020_2021_dfs = pd.concat([mel_dfs, syd_dfs, bri_dfs, per_dfs, ade_dfs, golcoa_dfs, new_dfs, can_dfs, suncoa_dfs, cencoa_dfs, wol_dfs, gee_dfs, hob_dfs, tow_dfs, cai_dfs, too_dfs, dar_dfs, bal_dfs, ben_dfs])
crp_2020_2021_dfs.sort_values(by=['City', 'Datetime', 'Tweet Id', 'Username', 'Text'], inplace=True, ascending=True )
crp_2020_2021_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
crp_2020_2021_dfs.to_csv('CRP 2020-2021.csv', sep=',', index=False)