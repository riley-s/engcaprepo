import snscrape.modules.twitter as sntwitter
import pandas as pd
from functools import reduce
import itertools
from standard_data import *

# Melbourne
# covid19


for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
mel_covid19_df = pd.DataFrame(mel_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
mel_covid19_df.insert(0, 'City', 'Melbourne')
mel_covid19_df.to_csv('Melbourne 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
mel_coronavirus_df = pd.DataFrame(mel_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
mel_coronavirus_df.insert(0, 'City', 'Melbourne')
mel_coronavirus_df.to_csv('Melbourne 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
mel_pandemic_df = pd.DataFrame(mel_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
mel_pandemic_df.insert(0, 'City', 'Melbourne')
mel_pandemic_df.to_csv('Melbourne 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
mel_lockdown_df = pd.DataFrame(mel_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
mel_lockdown_df.insert(0, 'City', 'Melbourne')
mel_lockdown_df.to_csv('Melbourne 19-20 (lockdown).csv', sep=',', index=False)

mel_dfs = pd.concat([mel_covid19_df, mel_coronavirus_df, mel_pandemic_df, mel_lockdown_df])
mel_dfs.to_csv('Melbourne CRP 19-20 (Combined).csv', sep=',', index=False)

# Sydney
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
syd_covid19_df = pd.DataFrame(syd_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
syd_covid19_df.insert(0, 'City', 'Sydney')
syd_covid19_df.to_csv('Sydney 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
syd_coronavirus_df = pd.DataFrame(syd_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
syd_coronavirus_df.insert(0, 'City', 'Sydney')
syd_coronavirus_df.to_csv('Sydney 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
syd_pandemic_df = pd.DataFrame(syd_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
syd_pandemic_df.insert(0, 'City', 'Sydney')
syd_pandemic_df.to_csv('Sydney 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
syd_lockdown_df = pd.DataFrame(syd_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
syd_lockdown_df.insert(0, 'City', 'Sydney')
syd_lockdown_df.to_csv('Sydney 19-20 (lockdown).csv', sep=',', index=False)

syd_dfs = pd.concat([syd_covid19_df, syd_coronavirus_df, syd_pandemic_df, syd_lockdown_df])
syd_dfs.to_csv('Sydney CRP 19-20 (Combined).csv', sep=',', index=False)

# Brisbane
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
bri_covid19_df = pd.DataFrame(bri_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
bri_covid19_df.insert(0, 'City', 'Brisbane')
bri_covid19_df.to_csv('Brisbane 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
bri_coronavirus_df = pd.DataFrame(bri_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
bri_coronavirus_df.insert(0, 'City', 'Brisbane')
bri_coronavirus_df.to_csv('Brisbane 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
bri_pandemic_df = pd.DataFrame(bri_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
bri_pandemic_df.insert(0, 'City', 'Brisbane')
bri_pandemic_df.to_csv('Brisbane 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
bri_lockdown_df = pd.DataFrame(bri_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
bri_lockdown_df.insert(0, 'City', 'Brisbane')
bri_lockdown_df.to_csv('Brisbane 19-20 (lockdown).csv', sep=',', index=False)

bri_dfs = pd.concat([bri_covid19_df, bri_coronavirus_df, bri_pandemic_df, bri_lockdown_df])
bri_dfs.to_csv('Brisbane CRP 19-20 (Combined).csv', sep=',', index=False)

# Perth
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
per_covid19_df = pd.DataFrame(per_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
per_covid19_df.insert(0, 'City', 'Perth')
per_covid19_df.to_csv('Perth 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
per_coronavirus_df = pd.DataFrame(per_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
per_coronavirus_df.insert(0, 'City', 'Perth')
per_coronavirus_df.to_csv('Perth 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
per_pandemic_df = pd.DataFrame(per_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
per_pandemic_df.insert(0, 'City', 'Perth')
per_pandemic_df.to_csv('Perth 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
per_lockdown_df = pd.DataFrame(per_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
per_lockdown_df.insert(0, 'City', 'Perth')
per_lockdown_df.to_csv('Perth 19-20 (lockdown).csv', sep=',', index=False)

per_dfs = pd.concat([per_covid19_df, per_coronavirus_df, per_pandemic_df, per_lockdown_df])
per_dfs.to_csv('Perth CRP 19-20 (Combined).csv', sep=',', index=False)

# Adelaide
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
ade_covid19_df = pd.DataFrame(ade_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
ade_covid19_df.insert(0, 'City', 'Adelaide')
ade_covid19_df.to_csv('Adelaide 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
ade_coronavirus_df = pd.DataFrame(ade_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
ade_coronavirus_df.insert(0, 'City', 'Adelaide')
ade_coronavirus_df.to_csv('Adelaide 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
ade_pandemic_df = pd.DataFrame(ade_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
ade_pandemic_df.insert(0, 'City', 'Adelaide')
ade_pandemic_df.to_csv('Adelaide 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
ade_lockdown_df = pd.DataFrame(ade_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
ade_lockdown_df.insert(0, 'City', 'Adelaide')
ade_lockdown_df.to_csv('Adelaide 19-20 (lockdown).csv', sep=',', index=False)

ade_dfs = pd.concat([ade_covid19_df, ade_coronavirus_df, ade_pandemic_df, ade_lockdown_df])
ade_dfs.to_csv('Adelaide CRP 19-20 (Combined).csv', sep=',', index=False)

# Gold Coast
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
golcoa_covid19_df = pd.DataFrame(golcoa_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
golcoa_covid19_df.insert(0, 'City', 'Gold Coast')
golcoa_covid19_df.to_csv('Gold Coast 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
golcoa_coronavirus_df = pd.DataFrame(golcoa_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
golcoa_coronavirus_df.insert(0, 'City', 'Gold Coast')
golcoa_coronavirus_df.to_csv('Gold Coast 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
golcoa_pandemic_df = pd.DataFrame(golcoa_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
golcoa_pandemic_df.insert(0, 'City', 'Gold Coast')
golcoa_pandemic_df.to_csv('Gold Coast 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
golcoa_lockdown_df = pd.DataFrame(golcoa_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
golcoa_lockdown_df.insert(0, 'City', 'Gold Coast')
golcoa_lockdown_df.to_csv('Gold Coast 19-20 (lockdown).csv', sep=',', index=False)

golcoa_dfs = pd.concat([golcoa_covid19_df, golcoa_coronavirus_df, golcoa_pandemic_df, golcoa_lockdown_df])
golcoa_dfs.to_csv('Gold Coast CRP 19-20 (Combined).csv', sep=',', index=False)

# Newcastle
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
new_covid19_df = pd.DataFrame(new_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
new_covid19_df.insert(0, 'City', 'Newcastle')
new_covid19_df.to_csv('Newcastle 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
new_coronavirus_df = pd.DataFrame(new_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
new_coronavirus_df.insert(0, 'City', 'Newcastle')
new_coronavirus_df.to_csv('Newcastle 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
new_pandemic_df = pd.DataFrame(new_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
new_pandemic_df.insert(0, 'City', 'Newcastle')
new_pandemic_df.to_csv('Newcastle 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
new_lockdown_df = pd.DataFrame(new_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
new_lockdown_df.insert(0, 'City', 'Newcastle')
new_lockdown_df.to_csv('Newcastle 19-20 (lockdown).csv', sep=',', index=False)

new_dfs = pd.concat([new_covid19_df, new_coronavirus_df, new_pandemic_df, new_lockdown_df])
new_dfs.to_csv('Newcastle CRP 19-20 (Combined).csv', sep=',', index=False)

# Canberra
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
can_covid19_df = pd.DataFrame(can_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
can_covid19_df.insert(0, 'City', 'Canberra')
can_covid19_df.to_csv('Canberra 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
can_coronavirus_df = pd.DataFrame(can_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
can_coronavirus_df.insert(0, 'City', 'Canberra')
can_coronavirus_df.to_csv('Canberra 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
can_pandemic_df = pd.DataFrame(can_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
can_pandemic_df.insert(0, 'City', 'Canberra')
can_pandemic_df.to_csv('Canberra 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
can_lockdown_df = pd.DataFrame(can_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
can_lockdown_df.insert(0, 'City', 'Canberra')
can_lockdown_df.to_csv('Canberra 19-20 (lockdown).csv', sep=',', index=False)

can_dfs = pd.concat([can_covid19_df, can_coronavirus_df, can_pandemic_df, can_lockdown_df])
can_dfs.to_csv('Canberra CRP 19-20 (Combined).csv', sep=',', index=False)

# Sunshine Coast
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
suncoa_covid19_df = pd.DataFrame(suncoa_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
suncoa_covid19_df.insert(0, 'City', 'Sunshine Coast')
suncoa_covid19_df.to_csv('Sunshine Coast 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
suncoa_coronavirus_df = pd.DataFrame(suncoa_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
suncoa_coronavirus_df.insert(0, 'City', 'Sunshine Coast')
suncoa_coronavirus_df.to_csv('Sunshine Coast 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
suncoa_pandemic_df = pd.DataFrame(suncoa_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
suncoa_pandemic_df.insert(0, 'City', 'Sunshine Coast')
suncoa_pandemic_df.to_csv('Sunshine Coast 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
suncoa_lockdown_df = pd.DataFrame(suncoa_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
suncoa_lockdown_df.insert(0, 'City', 'Sunshine Coast')
suncoa_lockdown_df.to_csv('Sunshine Coast 19-20 (lockdown).csv', sep=',', index=False)

suncoa_dfs = pd.concat([suncoa_covid19_df, suncoa_coronavirus_df, suncoa_pandemic_df, suncoa_lockdown_df])
suncoa_dfs.to_csv('Sunshine Coast CRP 19-20 (Combined).csv', sep=',', index=False)

# Central Coast
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
cencoa_covid19_df = pd.DataFrame(cencoa_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
cencoa_covid19_df.insert(0, 'City', 'Central Coast')
cencoa_covid19_df.to_csv('Central Coast 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
cencoa_coronavirus_df = pd.DataFrame(cencoa_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
cencoa_coronavirus_df.insert(0, 'City', 'Central Coast')
cencoa_coronavirus_df.to_csv('Central Coast 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
cencoa_pandemic_df = pd.DataFrame(cencoa_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
cencoa_pandemic_df.insert(0, 'City', 'Central Coast')
cencoa_pandemic_df.to_csv('Central Coast 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
cencoa_lockdown_df = pd.DataFrame(cencoa_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
cencoa_lockdown_df.insert(0, 'City', 'Central Coast')
cencoa_lockdown_df.to_csv('Central Coast 19-20 (lockdown).csv', sep=',', index=False)

cencoa_dfs = pd.concat([cencoa_covid19_df, cencoa_coronavirus_df, cencoa_pandemic_df, cencoa_lockdown_df])
cencoa_dfs.to_csv('Central Coast CRP 19-20 (Combined).csv', sep=',', index=False)

# Wollongong
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
wol_covid19_df = pd.DataFrame(wol_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
wol_covid19_df.insert(0, 'City', 'Wollongong')
wol_covid19_df.to_csv('Wollongong 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
wol_coronavirus_df = pd.DataFrame(wol_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
wol_coronavirus_df.insert(0, 'City', 'Wollongong')
wol_coronavirus_df.to_csv('Wollongong 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
wol_pandemic_df = pd.DataFrame(wol_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
wol_pandemic_df.insert(0, 'City', 'Wollongong')
wol_pandemic_df.to_csv('Wollongong 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
wol_lockdown_df = pd.DataFrame(wol_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
wol_lockdown_df.insert(0, 'City', 'Wollongong')
wol_lockdown_df.to_csv('Wollongong 19-20 (lockdown).csv', sep=',', index=False)

wol_dfs = pd.concat([wol_covid19_df, wol_coronavirus_df, wol_pandemic_df, wol_lockdown_df])
wol_dfs.to_csv('Wollongong CRP 19-20 (Combined).csv', sep=',', index=False)

# Geelong
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
gee_covid19_df = pd.DataFrame(gee_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
gee_covid19_df.insert(0, 'City', 'Geelong')
gee_covid19_df.to_csv('Geelong 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
gee_coronavirus_df = pd.DataFrame(gee_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
gee_coronavirus_df.insert(0, 'City', 'Geelong')
gee_coronavirus_df.to_csv('Geelong 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
gee_pandemic_df = pd.DataFrame(gee_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
gee_pandemic_df.insert(0, 'City', 'Geelong')
gee_pandemic_df.to_csv('Geelong 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
gee_lockdown_df = pd.DataFrame(gee_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
gee_lockdown_df.insert(0, 'City', 'Geelong')
gee_lockdown_df.to_csv('Geelong 19-20 (lockdown).csv', sep=',', index=False)

gee_dfs = pd.concat([gee_covid19_df, gee_coronavirus_df, gee_pandemic_df, gee_lockdown_df])
gee_dfs.to_csv('Geelong CRP 19-20 (Combined).csv', sep=',', index=False)

# Hobart
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
hob_covid19_df = pd.DataFrame(hob_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
hob_covid19_df.insert(0, 'City', 'Hobart')
hob_covid19_df.to_csv('Hobart 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
hob_coronavirus_df = pd.DataFrame(hob_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
hob_coronavirus_df.insert(0, 'City', 'Hobart')
hob_coronavirus_df.to_csv('Hobart 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
hob_pandemic_df = pd.DataFrame(hob_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
hob_pandemic_df.insert(0, 'City', 'Hobart')
hob_pandemic_df.to_csv('Hobart 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
hob_lockdown_df = pd.DataFrame(hob_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
hob_lockdown_df.insert(0, 'City', 'Hobart')
hob_lockdown_df.to_csv('Hobart 19-20 (lockdown).csv', sep=',', index=False)

hob_dfs = pd.concat([hob_covid19_df, hob_coronavirus_df, hob_pandemic_df, hob_lockdown_df])
hob_dfs.to_csv('Hobart CRP 19-20 (Combined).csv', sep=',', index=False)

# Townsville
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
tow_covid19_df = pd.DataFrame(tow_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
tow_covid19_df.insert(0, 'City', 'Townsville')
tow_covid19_df.to_csv('Townsville 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
tow_coronavirus_df = pd.DataFrame(tow_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
tow_coronavirus_df.insert(0, 'City', 'Townsville')
tow_coronavirus_df.to_csv('Townsville 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
tow_pandemic_df = pd.DataFrame(tow_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
tow_pandemic_df.insert(0, 'City', 'Townsville')
tow_pandemic_df.to_csv('Townsville 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
tow_lockdown_df = pd.DataFrame(tow_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
tow_lockdown_df.insert(0, 'City', 'Townsville')
tow_lockdown_df.to_csv('Townsville 19-20 (lockdown).csv', sep=',', index=False)

tow_dfs = pd.concat([tow_covid19_df, tow_coronavirus_df, tow_pandemic_df, tow_lockdown_df])
tow_dfs.to_csv('Townsville CRP 19-20 (Combined).csv', sep=',', index=False)

# Cairns
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
cai_covid19_df = pd.DataFrame(cai_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
cai_covid19_df.insert(0, 'City', 'Cairns')
cai_covid19_df.to_csv('Cairns 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
cai_coronavirus_df = pd.DataFrame(cai_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
cai_coronavirus_df.insert(0, 'City', 'Cairns')
cai_coronavirus_df.to_csv('Cairns 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
cai_pandemic_df = pd.DataFrame(cai_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
cai_pandemic_df.insert(0, 'City', 'Cairns')
cai_pandemic_df.to_csv('Cairns 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
cai_lockdown_df = pd.DataFrame(cai_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
cai_lockdown_df.insert(0, 'City', 'Cairns')
cai_lockdown_df.to_csv('Cairns 19-20 (lockdown).csv', sep=',', index=False)

cai_dfs = pd.concat([cai_covid19_df, cai_coronavirus_df, cai_pandemic_df, cai_lockdown_df])
cai_dfs.to_csv('Cairns CRP 19-20 (Combined).csv', sep=',', index=False)

# Toowoomba
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
too_covid19_df = pd.DataFrame(too_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
too_covid19_df.insert(0, 'City', 'Toowoomba')
too_covid19_df.to_csv('Toowoomba 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
too_coronavirus_df = pd.DataFrame(too_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
too_coronavirus_df.insert(0, 'City', 'Toowoomba')
too_coronavirus_df.to_csv('Toowoomba 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
too_pandemic_df = pd.DataFrame(too_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
too_pandemic_df.insert(0, 'City', 'Toowoomba')
too_pandemic_df.to_csv('Toowoomba 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
too_lockdown_df = pd.DataFrame(too_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
too_lockdown_df.insert(0, 'City', 'Toowoomba')
too_lockdown_df.to_csv('Toowoomba 19-20 (lockdown).csv', sep=',', index=False)

too_dfs = pd.concat([too_covid19_df, too_coronavirus_df, too_pandemic_df, too_lockdown_df])
too_dfs.to_csv('Toowoomba CRP 19-20 (Combined).csv', sep=',', index=False)

# Darwin
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
dar_covid19_df = pd.DataFrame(dar_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
dar_covid19_df.insert(0, 'City', 'Darwin')
dar_covid19_df.to_csv('Darwin 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
dar_coronavirus_df = pd.DataFrame(dar_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
dar_coronavirus_df.insert(0, 'City', 'Darwin')
dar_coronavirus_df.to_csv('Darwin 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
dar_pandemic_df = pd.DataFrame(dar_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
dar_pandemic_df.insert(0, 'City', 'Darwin')
dar_pandemic_df.to_csv('Darwin 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
dar_lockdown_df = pd.DataFrame(dar_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
dar_lockdown_df.insert(0, 'City', 'Darwin')
dar_lockdown_df.to_csv('Darwin 19-20 (lockdown).csv', sep=',', index=False)

dar_dfs = pd.concat([dar_covid19_df, dar_coronavirus_df, dar_pandemic_df, dar_lockdown_df])
dar_dfs.to_csv('Darwin CRP 19-20 (Combined).csv', sep=',', index=False)

# Ballarat
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
bal_covid19_df = pd.DataFrame(bal_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
bal_covid19_df.insert(0, 'City', 'Ballarat')
bal_covid19_df.to_csv('Ballarat 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
bal_coronavirus_df = pd.DataFrame(bal_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
bal_coronavirus_df.insert(0, 'City', 'Ballarat')
bal_coronavirus_df.to_csv('Ballarat 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
bal_pandemic_df = pd.DataFrame(bal_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
bal_pandemic_df.insert(0, 'City', 'Ballarat')
bal_pandemic_df.to_csv('Ballarat 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
bal_lockdown_df = pd.DataFrame(bal_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
bal_lockdown_df.insert(0, 'City', 'Ballarat')
bal_lockdown_df.to_csv('Ballarat 19-20 (lockdown).csv', sep=',', index=False)

bal_dfs = pd.concat([bal_covid19_df, bal_coronavirus_df, bal_pandemic_df, bal_lockdown_df])
bal_dfs.to_csv('Ballarat CRP 19-20 (Combined).csv', sep=',', index=False)

# Bendigo
# covid19
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_covid19_list.append([tweet.date, tweet.id, tweet.content])
ben_covid19_df = pd.DataFrame(ben_tweets_covid19_list, columns=['Datetime', 'Tweet Id', 'Text'])
ben_covid19_df.insert(0, 'City', 'Bendigo')
ben_covid19_df.to_csv('Bendigo 19-20 (covid19).csv', sep=',', index=False)

# coronavirus
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('coronavirus since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_coronavirus_list.append([tweet.date, tweet.id, tweet.content])
ben_coronavirus_df = pd.DataFrame(ben_tweets_coronavirus_list, columns=['Datetime', 'Tweet Id', 'Text'])
ben_coronavirus_df.insert(0, 'City', 'Bendigo')
ben_coronavirus_df.to_csv('Bendigo 19-20 (coronavirus).csv', sep=',', index=False)

# pandemic
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pandemic since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_pandemic_list.append([tweet.date, tweet.id, tweet.content])
ben_pandemic_df = pd.DataFrame(ben_tweets_pandemic_list, columns=['Datetime', 'Tweet Id', 'Text'])
ben_pandemic_df.insert(0, 'City', 'Bendigo')
ben_pandemic_df.to_csv('Bendigo 19-20 (pandemic).csv', sep=',', index=False)

# lockdown
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lockdown since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_lockdown_list.append([tweet.date, tweet.id, tweet.content])
ben_lockdown_df = pd.DataFrame(ben_tweets_lockdown_list, columns=['Datetime', 'Tweet Id', 'Text'])
ben_lockdown_df.insert(0, 'City', 'Bendigo')
ben_lockdown_df.to_csv('Bendigo 19-20 (lockdown).csv', sep=',', index=False)

ben_dfs = pd.concat([ben_covid19_df, ben_coronavirus_df, ben_pandemic_df, ben_lockdown_df])
ben_dfs.to_csv('Bendigo CRP 19-20 (Combined).csv', sep=',', index=False)




crp_2019_2020_dfs = pd.concat([mel_dfs, syd_dfs, bri_dfs, per_dfs, ade_dfs, golcoa_dfs, new_dfs, can_dfs, suncoa_dfs, cencoa_dfs, wol_dfs, gee_dfs, hob_dfs, tow_dfs, cai_dfs, too_dfs, dar_dfs, bal_dfs, ben_dfs])
crp_2019_2020_dfs.sort_values(by=['City', 'Datetime', 'Tweet Id', 'Text'], inplace=True, ascending=True )
crp_2019_2020_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
crp_2019_2020_dfs.to_csv('CRP 2019-2020.csv', sep=',', index=False)