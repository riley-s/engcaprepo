import snscrape.modules.twitter as sntwitter
import pandas as pd
from functools import reduce
import itertools

# Popular (>100,000) cities across Australia + coordinates

# Melbourne
mel_loc = '-37.8136, 144.9631, 50km'
mel_tweets_depression_list = []
mel_tweets_anxiety_list = []
mel_tweets_suicide_list = []
mel_tweets_mental_health_list = []
mel_tweets_covid19_list = []
mel_tweets_coronavirus_list = []
mel_tweets_pandemic_list = []
mel_tweets_lockdown_list = []
# Sydney
syd_loc = '-33.8688, 151.2093, 50km'
syd_tweets_depression_list = []
syd_tweets_anxiety_list = []
syd_tweets_suicide_list = []
syd_tweets_mental_health_list = []
syd_tweets_covid19_list = []
syd_tweets_coronavirus_list = []
syd_tweets_pandemic_list = []
syd_tweets_lockdown_list = []
#Brisbane
bri_loc = '-27.4705, 153.0260, 50km'
bri_tweets_depression_list = []
bri_tweets_anxiety_list = []
bri_tweets_suicide_list = []
bri_tweets_mental_health_list = []
bri_tweets_covid19_list = []
bri_tweets_coronavirus_list = []
bri_tweets_pandemic_list = []
bri_tweets_lockdown_list = []
#Perth
per_loc = '-31.9523, 115.8613, 50km'
per_tweets_depression_list = []
per_tweets_anxiety_list = []
per_tweets_suicide_list = []
per_tweets_mental_health_list = []
per_tweets_covid19_list = []
per_tweets_coronavirus_list = []
per_tweets_pandemic_list = []
per_tweets_lockdown_list = []
#Adelaide
ade_loc = '-34.9285, 138.6007, 50km'
ade_tweets_depression_list = []
ade_tweets_anxiety_list = []
ade_tweets_suicide_list = []
ade_tweets_mental_health_list = []
ade_tweets_covid19_list = []
ade_tweets_coronavirus_list = []
ade_tweets_pandemic_list = []
ade_tweets_lockdown_list = []
#Gold Coast  
golcoa_loc = '-28.0167, 153.4000, 50km'
golcoa_tweets_depression_list = []
golcoa_tweets_anxiety_list = []
golcoa_tweets_suicide_list = []
golcoa_tweets_mental_health_list = []
golcoa_tweets_covid19_list = []
golcoa_tweets_coronavirus_list = []
golcoa_tweets_pandemic_list = []
golcoa_tweets_lockdown_list = []
# Newcastle
new_loc = '-32.93, 151.75, 50km'
new_tweets_depression_list = []
new_tweets_anxiety_list = []
new_tweets_suicide_list = []
new_tweets_mental_health_list = []
new_tweets_covid19_list = []
new_tweets_coronavirus_list = []
new_tweets_pandemic_list = []
new_tweets_lockdown_list = []
# Canberra
can_loc = '-35.2809, 149.1300, 50km'
can_tweets_depression_list = []
can_tweets_anxiety_list = []
can_tweets_suicide_list = []
can_tweets_mental_health_list = []
can_tweets_covid19_list = []
can_tweets_coronavirus_list = []
can_tweets_pandemic_list = []
can_tweets_lockdown_list = []
# Sunshine Coast  
suncoa_loc = '-26.6500, 153.0667, 50km'
suncoa_tweets_depression_list = []
suncoa_tweets_anxiety_list = []
suncoa_tweets_suicide_list = []
suncoa_tweets_mental_health_list = []
suncoa_tweets_covid19_list = []
suncoa_tweets_coronavirus_list = []
suncoa_tweets_pandemic_list = []
suncoa_tweets_lockdown_list = []
# Central Coast  
cencoa_loc = '-33.3208, 151.2336, 50km'
cencoa_tweets_depression_list = []
cencoa_tweets_anxiety_list = []
cencoa_tweets_suicide_list = []
cencoa_tweets_mental_health_list = []
cencoa_tweets_covid19_list = []
cencoa_tweets_coronavirus_list = []
cencoa_tweets_pandemic_list = []
cencoa_tweets_lockdown_list = []
# Wollongong
wol_loc = '-34.4248, 150.8931, 50km'
wol_tweets_depression_list = []
wol_tweets_anxiety_list = []
wol_tweets_suicide_list = []
wol_tweets_mental_health_list = []
wol_tweets_covid19_list = []
wol_tweets_coronavirus_list = []
wol_tweets_pandemic_list = []
wol_tweets_lockdown_list = []
# Geelong
gee_loc = '-38.1499, 144.3617, 50km'
gee_tweets_depression_list = []
gee_tweets_anxiety_list = []
gee_tweets_suicide_list = []
gee_tweets_mental_health_list = []
gee_tweets_covid19_list = []
gee_tweets_coronavirus_list = []
gee_tweets_pandemic_list = []
gee_tweets_lockdown_list = []
# Hobart
hob_loc = '-42.8826, 147.3257, 50km'
hob_tweets_depression_list = []
hob_tweets_anxiety_list = []
hob_tweets_suicide_list = []
hob_tweets_mental_health_list = []
hob_tweets_covid19_list = []
hob_tweets_coronavirus_list = []
hob_tweets_pandemic_list = []
hob_tweets_lockdown_list = []
# Townsville
tow_loc = '-19.2590, 146.8169, 50km'
tow_tweets_depression_list = []
tow_tweets_anxiety_list = []
tow_tweets_suicide_list = []
tow_tweets_mental_health_list = []
tow_tweets_covid19_list = []
tow_tweets_coronavirus_list = []
tow_tweets_pandemic_list = []
tow_tweets_lockdown_list = []
# Cairns
cai_loc = '-16.9203, 145.7710, 50km'
cai_tweets_depression_list = []
cai_tweets_anxiety_list = []
cai_tweets_suicide_list = []
cai_tweets_mental_health_list = []
cai_tweets_covid19_list = []
cai_tweets_coronavirus_list = []
cai_tweets_pandemic_list = []
cai_tweets_lockdown_list = []
# Toowoomba
too_loc = '-27.5598, 151.9507, 50km'
too_tweets_depression_list = []
too_tweets_anxiety_list = []
too_tweets_suicide_list = []
too_tweets_mental_health_list = []
too_tweets_covid19_list = []
too_tweets_coronavirus_list = []
too_tweets_pandemic_list = []
too_tweets_lockdown_list = []
# Darwin
dar_loc = '-12.4637, 130.8444, 50km'
dar_tweets_depression_list = []
dar_tweets_anxiety_list = []
dar_tweets_suicide_list = []
dar_tweets_mental_health_list = []
dar_tweets_covid19_list = []
dar_tweets_coronavirus_list = []
dar_tweets_pandemic_list = []
dar_tweets_lockdown_list = []
# Ballarat
bal_loc = '-37.5622, 143.8503, 50km'
bal_tweets_depression_list = []
bal_tweets_anxiety_list = []
bal_tweets_suicide_list = []
bal_tweets_mental_health_list = []
bal_tweets_covid19_list = []
bal_tweets_coronavirus_list = []
bal_tweets_pandemic_list = []
bal_tweets_lockdown_list = []
# Bendigo
ben_loc = '-36.7570, 144.2794, 50km'
ben_tweets_depression_list = []
ben_tweets_anxiety_list = []
ben_tweets_suicide_list = []
ben_tweets_mental_health_list = []
ben_tweets_covid19_list = []
ben_tweets_coronavirus_list = []
ben_tweets_pandemic_list = []
ben_tweets_lockdown_list = []

# Setting variables to be used below
max_tweets = 10000
