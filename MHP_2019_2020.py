import snscrape.modules.twitter as sntwitter
import pandas as pd
from functools import reduce
import itertools
from standard_data import *

# Melbourne
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_depression_df = pd.DataFrame(mel_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_depression_df.insert(0, 'City', 'Melbourne')
mel_depression_df.to_csv('Melbourne 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_anxiety_df = pd.DataFrame(mel_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_anxiety_df.insert(0, 'City', 'Melbourne')
mel_anxiety_df.to_csv('Melbourne 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_suicide_df = pd.DataFrame(mel_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_suicide_df.insert(0, 'City', 'Melbourne')
mel_suicide_df.to_csv('Melbourne 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(mel_loc)).get_items()):
    if i>max_tweets:
        break
    mel_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
mel_mental_health_df = pd.DataFrame(mel_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
mel_mental_health_df.insert(0, 'City', 'Melbourne')
mel_mental_health_df.to_csv('Melbourne 19-20 (mental_health).csv', sep=',', index=False)

mel_dfs = pd.concat([mel_depression_df, mel_anxiety_df, mel_suicide_df, mel_mental_health_df])
mel_dfs.to_csv('Melbourne MHP 19-20 (Combined).csv', sep=',', index=False)

# Sydney
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_depression_df = pd.DataFrame(syd_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_depression_df.insert(0, 'City', 'Sydney')
syd_depression_df.to_csv('Sydney 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_anxiety_df = pd.DataFrame(syd_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_anxiety_df.insert(0, 'City', 'Sydney')
syd_anxiety_df.to_csv('Sydney 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_suicide_df = pd.DataFrame(syd_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_suicide_df.insert(0, 'City', 'Sydney')
syd_suicide_df.to_csv('Sydney 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(syd_loc)).get_items()):
    if i>max_tweets:
        break
    syd_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
syd_mental_health_df = pd.DataFrame(syd_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
syd_mental_health_df.insert(0, 'City', 'Sydney')
syd_mental_health_df.to_csv('Sydney 19-20 (mental_health).csv', sep=',', index=False)

syd_dfs = pd.concat([syd_depression_df, syd_anxiety_df, syd_suicide_df, syd_mental_health_df])
syd_dfs.to_csv('Sydney MHP 19-20 (Combined).csv', sep=',', index=False)

# Brisbane
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_depression_df = pd.DataFrame(bri_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_depression_df.insert(0, 'City', 'Brisbane')
bri_depression_df.to_csv('Brisbane 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_anxiety_df = pd.DataFrame(bri_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_anxiety_df.insert(0, 'City', 'Brisbane')
bri_anxiety_df.to_csv('Brisbane 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_suicide_df = pd.DataFrame(bri_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_suicide_df.insert(0, 'City', 'Brisbane')
bri_suicide_df.to_csv('Brisbane 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bri_loc)).get_items()):
    if i>max_tweets:
        break
    bri_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bri_mental_health_df = pd.DataFrame(bri_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bri_mental_health_df.insert(0, 'City', 'Brisbane')
bri_mental_health_df.to_csv('Brisbane 19-20 (mental_health).csv', sep=',', index=False)

bri_dfs = pd.concat([bri_depression_df, bri_anxiety_df, bri_suicide_df, bri_mental_health_df])
bri_dfs.to_csv('Brisbane MHP 19-20 (Combined).csv', sep=',', index=False)

# Perth
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_depression_df = pd.DataFrame(per_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_depression_df.insert(0, 'City', 'Perth')
per_depression_df.to_csv('Perth 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_anxiety_df = pd.DataFrame(per_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_anxiety_df.insert(0, 'City', 'Perth')
per_anxiety_df.to_csv('Perth 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_suicide_df = pd.DataFrame(per_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_suicide_df.insert(0, 'City', 'Perth')
per_suicide_df.to_csv('Perth 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(per_loc)).get_items()):
    if i>max_tweets:
        break
    per_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
per_mental_health_df = pd.DataFrame(per_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
per_mental_health_df.insert(0, 'City', 'Perth')
per_mental_health_df.to_csv('Perth 19-20 (mental_health).csv', sep=',', index=False)

per_dfs = pd.concat([per_depression_df, per_anxiety_df, per_suicide_df, per_mental_health_df])
per_dfs.to_csv('Perth MHP 19-20 (Combined).csv', sep=',', index=False)

# Adelaide
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_depression_df = pd.DataFrame(ade_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_depression_df.insert(0, 'City', 'Adelaide')
ade_depression_df.to_csv('Adelaide 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_anxiety_df = pd.DataFrame(ade_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_anxiety_df.insert(0, 'City', 'Adelaide')
ade_anxiety_df.to_csv('Adelaide 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_suicide_df = pd.DataFrame(ade_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_suicide_df.insert(0, 'City', 'Adelaide')
ade_suicide_df.to_csv('Adelaide 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ade_loc)).get_items()):
    if i>max_tweets:
        break
    ade_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ade_mental_health_df = pd.DataFrame(ade_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ade_mental_health_df.insert(0, 'City', 'Adelaide')
ade_mental_health_df.to_csv('Adelaide 19-20 (mental_health).csv', sep=',', index=False)

ade_dfs = pd.concat([ade_depression_df, ade_anxiety_df, ade_suicide_df, ade_mental_health_df])
ade_dfs.to_csv('Adelaide MHP 19-20 (Combined).csv', sep=',', index=False)

# Gold Coast
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_depression_df = pd.DataFrame(golcoa_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_depression_df.insert(0, 'City', 'Gold Coast')
golcoa_depression_df.to_csv('Gold Coast 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_anxiety_df = pd.DataFrame(golcoa_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_anxiety_df.insert(0, 'City', 'Gold Coast')
golcoa_anxiety_df.to_csv('Gold Coast 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_suicide_df = pd.DataFrame(golcoa_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_suicide_df.insert(0, 'City', 'Gold Coast')
golcoa_suicide_df.to_csv('Gold Coast 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(golcoa_loc)).get_items()):
    if i>max_tweets:
        break
    golcoa_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
golcoa_mental_health_df = pd.DataFrame(golcoa_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
golcoa_mental_health_df.insert(0, 'City', 'Gold Coast')
golcoa_mental_health_df.to_csv('Gold Coast 19-20 (mental_health).csv', sep=',', index=False)

golcoa_dfs = pd.concat([golcoa_depression_df, golcoa_anxiety_df, golcoa_suicide_df, golcoa_mental_health_df])
golcoa_dfs.to_csv('Gold Coast MHP 19-20 (Combined).csv', sep=',', index=False)

# Newcastle
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_depression_df = pd.DataFrame(new_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_depression_df.insert(0, 'City', 'Newcastle')
new_depression_df.to_csv('Newcastle 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_anxiety_df = pd.DataFrame(new_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_anxiety_df.insert(0, 'City', 'Newcastle')
new_anxiety_df.to_csv('Newcastle 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_suicide_df = pd.DataFrame(new_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_suicide_df.insert(0, 'City', 'Newcastle')
new_suicide_df.to_csv('Newcastle 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(new_loc)).get_items()):
    if i>max_tweets:
        break
    new_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
new_mental_health_df = pd.DataFrame(new_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
new_mental_health_df.insert(0, 'City', 'Newcastle')
new_mental_health_df.to_csv('Newcastle 19-20 (mental_health).csv', sep=',', index=False)

new_dfs = pd.concat([new_depression_df, new_anxiety_df, new_suicide_df, new_mental_health_df])
new_dfs.to_csv('Newcastle MHP 19-20 (Combined).csv', sep=',', index=False)

# Canberra
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_depression_df = pd.DataFrame(can_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_depression_df.insert(0, 'City', 'Canberra')
can_depression_df.to_csv('Canberra 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_anxiety_df = pd.DataFrame(can_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_anxiety_df.insert(0, 'City', 'Canberra')
can_anxiety_df.to_csv('Canberra 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_suicide_df = pd.DataFrame(can_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_suicide_df.insert(0, 'City', 'Canberra')
can_suicide_df.to_csv('Canberra 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(can_loc)).get_items()):
    if i>max_tweets:
        break
    can_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
can_mental_health_df = pd.DataFrame(can_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
can_mental_health_df.insert(0, 'City', 'Canberra')
can_mental_health_df.to_csv('Canberra 19-20 (mental_health).csv', sep=',', index=False)

can_dfs = pd.concat([can_depression_df, can_anxiety_df, can_suicide_df, can_mental_health_df])
can_dfs.to_csv('Canberra MHP 19-20 (Combined).csv', sep=',', index=False)

# Sunshine Coast
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_depression_df = pd.DataFrame(suncoa_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_depression_df.insert(0, 'City', 'Sunshine Coast')
suncoa_depression_df.to_csv('Sunshine Coast 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_anxiety_df = pd.DataFrame(suncoa_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_anxiety_df.insert(0, 'City', 'Sunshine Coast')
suncoa_anxiety_df.to_csv('Sunshine Coast 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_suicide_df = pd.DataFrame(suncoa_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_suicide_df.insert(0, 'City', 'Sunshine Coast')
suncoa_suicide_df.to_csv('Sunshine Coast 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(suncoa_loc)).get_items()):
    if i>max_tweets:
        break
    suncoa_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
suncoa_mental_health_df = pd.DataFrame(suncoa_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
suncoa_mental_health_df.insert(0, 'City', 'Sunshine Coast')
suncoa_mental_health_df.to_csv('Sunshine Coast 19-20 (mental_health).csv', sep=',', index=False)

suncoa_dfs = pd.concat([suncoa_depression_df, suncoa_anxiety_df, suncoa_suicide_df, suncoa_mental_health_df])
suncoa_dfs.to_csv('Sunshine Coast MHP 19-20 (Combined).csv', sep=',', index=False)

# Central Coast
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_depression_df = pd.DataFrame(cencoa_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_depression_df.insert(0, 'City', 'Central Coast')
cencoa_depression_df.to_csv('Central Coast 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_anxiety_df = pd.DataFrame(cencoa_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_anxiety_df.insert(0, 'City', 'Central Coast')
cencoa_anxiety_df.to_csv('Central Coast 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_suicide_df = pd.DataFrame(cencoa_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_suicide_df.insert(0, 'City', 'Central Coast')
cencoa_suicide_df.to_csv('Central Coast 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cencoa_loc)).get_items()):
    if i>max_tweets:
        break
    cencoa_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cencoa_mental_health_df = pd.DataFrame(cencoa_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cencoa_mental_health_df.insert(0, 'City', 'Central Coast')
cencoa_mental_health_df.to_csv('Central Coast 19-20 (mental_health).csv', sep=',', index=False)

cencoa_dfs = pd.concat([cencoa_depression_df, cencoa_anxiety_df, cencoa_suicide_df, cencoa_mental_health_df])
cencoa_dfs.to_csv('Central Coast MHP 19-20 (Combined).csv', sep=',', index=False)

# Wollongong
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_depression_df = pd.DataFrame(wol_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_depression_df.insert(0, 'City', 'Wollongong')
wol_depression_df.to_csv('Wollongong 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_anxiety_df = pd.DataFrame(wol_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_anxiety_df.insert(0, 'City', 'Wollongong')
wol_anxiety_df.to_csv('Wollongong 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_suicide_df = pd.DataFrame(wol_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_suicide_df.insert(0, 'City', 'Wollongong')
wol_suicide_df.to_csv('Wollongong 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(wol_loc)).get_items()):
    if i>max_tweets:
        break
    wol_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
wol_mental_health_df = pd.DataFrame(wol_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
wol_mental_health_df.insert(0, 'City', 'Wollongong')
wol_mental_health_df.to_csv('Wollongong 19-20 (mental_health).csv', sep=',', index=False)

wol_dfs = pd.concat([wol_depression_df, wol_anxiety_df, wol_suicide_df, wol_mental_health_df])
wol_dfs.to_csv('Wollongong MHP 19-20 (Combined).csv', sep=',', index=False)

# Geelong
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_depression_df = pd.DataFrame(gee_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_depression_df.insert(0, 'City', 'Geelong')
gee_depression_df.to_csv('Geelong 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_anxiety_df = pd.DataFrame(gee_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_anxiety_df.insert(0, 'City', 'Geelong')
gee_anxiety_df.to_csv('Geelong 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_suicide_df = pd.DataFrame(gee_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_suicide_df.insert(0, 'City', 'Geelong')
gee_suicide_df.to_csv('Geelong 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(gee_loc)).get_items()):
    if i>max_tweets:
        break
    gee_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
gee_mental_health_df = pd.DataFrame(gee_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
gee_mental_health_df.insert(0, 'City', 'Geelong')
gee_mental_health_df.to_csv('Geelong 19-20 (mental_health).csv', sep=',', index=False)

gee_dfs = pd.concat([gee_depression_df, gee_anxiety_df, gee_suicide_df, gee_mental_health_df])
gee_dfs.to_csv('Geelong MHP 19-20 (Combined).csv', sep=',', index=False)

# Hobart
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_depression_df = pd.DataFrame(hob_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_depression_df.insert(0, 'City', 'Hobart')
hob_depression_df.to_csv('Hobart 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_anxiety_df = pd.DataFrame(hob_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_anxiety_df.insert(0, 'City', 'Hobart')
hob_anxiety_df.to_csv('Hobart 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_suicide_df = pd.DataFrame(hob_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_suicide_df.insert(0, 'City', 'Hobart')
hob_suicide_df.to_csv('Hobart 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(hob_loc)).get_items()):
    if i>max_tweets:
        break
    hob_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
hob_mental_health_df = pd.DataFrame(hob_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
hob_mental_health_df.insert(0, 'City', 'Hobart')
hob_mental_health_df.to_csv('Hobart 19-20 (mental_health).csv', sep=',', index=False)

hob_dfs = pd.concat([hob_depression_df, hob_anxiety_df, hob_suicide_df, hob_mental_health_df])
hob_dfs.to_csv('Hobart MHP 19-20 (Combined).csv', sep=',', index=False)

# Townsville
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_depression_df = pd.DataFrame(tow_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_depression_df.insert(0, 'City', 'Townsville')
tow_depression_df.to_csv('Townsville 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_anxiety_df = pd.DataFrame(tow_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_anxiety_df.insert(0, 'City', 'Townsville')
tow_anxiety_df.to_csv('Townsville 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_suicide_df = pd.DataFrame(tow_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_suicide_df.insert(0, 'City', 'Townsville')
tow_suicide_df.to_csv('Townsville 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(tow_loc)).get_items()):
    if i>max_tweets:
        break
    tow_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
tow_mental_health_df = pd.DataFrame(tow_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tow_mental_health_df.insert(0, 'City', 'Townsville')
tow_mental_health_df.to_csv('Townsville 19-20 (mental_health).csv', sep=',', index=False)

tow_dfs = pd.concat([tow_depression_df, tow_anxiety_df, tow_suicide_df, tow_mental_health_df])
tow_dfs.to_csv('Townsville MHP 19-20 (Combined).csv', sep=',', index=False)

# Cairns
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_depression_df = pd.DataFrame(cai_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_depression_df.insert(0, 'City', 'Cairns')
cai_depression_df.to_csv('Cairns 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_anxiety_df = pd.DataFrame(cai_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_anxiety_df.insert(0, 'City', 'Cairns')
cai_anxiety_df.to_csv('Cairns 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_suicide_df = pd.DataFrame(cai_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_suicide_df.insert(0, 'City', 'Cairns')
cai_suicide_df.to_csv('Cairns 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(cai_loc)).get_items()):
    if i>max_tweets:
        break
    cai_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
cai_mental_health_df = pd.DataFrame(cai_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
cai_mental_health_df.insert(0, 'City', 'Cairns')
cai_mental_health_df.to_csv('Cairns 19-20 (mental_health).csv', sep=',', index=False)

cai_dfs = pd.concat([cai_depression_df, cai_anxiety_df, cai_suicide_df, cai_mental_health_df])
cai_dfs.to_csv('Cairns MHP 19-20 (Combined).csv', sep=',', index=False)

# Toowoomba
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_depression_df = pd.DataFrame(too_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_depression_df.insert(0, 'City', 'Toowoomba')
too_depression_df.to_csv('Toowoomba 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_anxiety_df = pd.DataFrame(too_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_anxiety_df.insert(0, 'City', 'Toowoomba')
too_anxiety_df.to_csv('Toowoomba 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_suicide_df = pd.DataFrame(too_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_suicide_df.insert(0, 'City', 'Toowoomba')
too_suicide_df.to_csv('Toowoomba 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(too_loc)).get_items()):
    if i>max_tweets:
        break
    too_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
too_mental_health_df = pd.DataFrame(too_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
too_mental_health_df.insert(0, 'City', 'Toowoomba')
too_mental_health_df.to_csv('Toowoomba 19-20 (mental_health).csv', sep=',', index=False)

too_dfs = pd.concat([too_depression_df, too_anxiety_df, too_suicide_df, too_mental_health_df])
too_dfs.to_csv('Toowoomba MHP 19-20 (Combined).csv', sep=',', index=False)

# Darwin
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_depression_df = pd.DataFrame(dar_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_depression_df.insert(0, 'City', 'Darwin')
dar_depression_df.to_csv('Darwin 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_anxiety_df = pd.DataFrame(dar_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_anxiety_df.insert(0, 'City', 'Darwin')
dar_anxiety_df.to_csv('Darwin 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_suicide_df = pd.DataFrame(dar_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_suicide_df.insert(0, 'City', 'Darwin')
dar_suicide_df.to_csv('Darwin 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(dar_loc)).get_items()):
    if i>max_tweets:
        break
    dar_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
dar_mental_health_df = pd.DataFrame(dar_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
dar_mental_health_df.insert(0, 'City', 'Darwin')
dar_mental_health_df.to_csv('Darwin 19-20 (mental_health).csv', sep=',', index=False)

dar_dfs = pd.concat([dar_depression_df, dar_anxiety_df, dar_suicide_df, dar_mental_health_df])
dar_dfs.to_csv('Darwin MHP 19-20 (Combined).csv', sep=',', index=False)

# Ballarat
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_depression_df = pd.DataFrame(bal_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_depression_df.insert(0, 'City', 'Ballarat')
bal_depression_df.to_csv('Ballarat 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_anxiety_df = pd.DataFrame(bal_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_anxiety_df.insert(0, 'City', 'Ballarat')
bal_anxiety_df.to_csv('Ballarat 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_suicide_df = pd.DataFrame(bal_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_suicide_df.insert(0, 'City', 'Ballarat')
bal_suicide_df.to_csv('Ballarat 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(bal_loc)).get_items()):
    if i>max_tweets:
        break
    bal_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
bal_mental_health_df = pd.DataFrame(bal_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
bal_mental_health_df.insert(0, 'City', 'Ballarat')
bal_mental_health_df.to_csv('Ballarat 19-20 (mental_health).csv', sep=',', index=False)

bal_dfs = pd.concat([bal_depression_df, bal_anxiety_df, bal_suicide_df, bal_mental_health_df])
bal_dfs.to_csv('Ballarat MHP 19-20 (Combined).csv', sep=',', index=False)

# Bendigo
# depression
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('depression since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_depression_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_depression_df = pd.DataFrame(ben_tweets_depression_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_depression_df.insert(0, 'City', 'Bendigo')
ben_depression_df.to_csv('Bendigo 19-20 (depression).csv', sep=',', index=False)

# anxiety
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('anxiety since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_anxiety_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_anxiety_df = pd.DataFrame(ben_tweets_anxiety_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_anxiety_df.insert(0, 'City', 'Bendigo')
ben_anxiety_df.to_csv('Bendigo 19-20 (anxiety).csv', sep=',', index=False)

# suicide
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_suicide_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_suicide_df = pd.DataFrame(ben_tweets_suicide_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_suicide_df.insert(0, 'City', 'Bendigo')
ben_suicide_df.to_csv('Bendigo 19-20 (suicide).csv', sep=',', index=False)

# mental-health
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mental-health since:2019-03-11 until:2020-03-11 geocode:"{}"'.format(ben_loc)).get_items()):
    if i>max_tweets:
        break
    ben_tweets_mental_health_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
ben_mental_health_df = pd.DataFrame(ben_tweets_mental_health_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
ben_mental_health_df.insert(0, 'City', 'Bendigo')
ben_mental_health_df.to_csv('Bendigo 19-20 (mental_health).csv', sep=',', index=False)

ben_dfs = pd.concat([ben_depression_df, ben_anxiety_df, ben_suicide_df, ben_mental_health_df])
ben_dfs.to_csv('Bendigo MHP 19-20 (Combined).csv', sep=',', index=False)




mhp_2019_2020_dfs = pd.concat([mel_dfs, syd_dfs, bri_dfs, per_dfs, ade_dfs, golcoa_dfs, new_dfs, can_dfs, suncoa_dfs, cencoa_dfs, wol_dfs, gee_dfs, hob_dfs, tow_dfs, cai_dfs, too_dfs, dar_dfs, bal_dfs, ben_dfs])
mhp_2019_2020_dfs.sort_values(by=['City', 'Datetime', 'Tweet Id', 'Username', 'Text'], inplace=True, ascending=True)
mhp_2019_2020_dfs.drop_duplicates(subset='Text', keep=False, inplace=True)
mhp_2019_2020_dfs.to_csv('MHP 2019-2020.csv', sep=',', index=False)