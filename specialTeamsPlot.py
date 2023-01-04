# -*- coding: utf-8 -*-
"""
ACC SPECIAL TEAMS
Created on Thu Oct 13 19:43:00 2022

@author: ericd
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.ticker as mtick

########################### NCAAF SPECIAL TEAMS EFFICIENCY PLOT#################################################
#read in team data
#Source: https://www.footballoutsiders.com/stats/ncaa/fei/overallst/2022
data = pd.read_csv('CFBSpecialTeams.csv')
data.head()

#subset down to ACC teams only
data = data[data['Team'].isin(['NC State','Clemson','Pittsburgh','Boston College','North Carolina',
                               'Virginia','Duke','Virginia Tech','Louisville','Miami',
                               'Wake Forest','Boston College','Florida State','Syracuse'])]

#set image paths
data['path'] = 'C:/Users/ericd/OneDrive - North Carolina State University/Desktop/College Football Stats/ACCLogos/'+ data['Team']  + '.png'


### PLOTS
#create plot area
fig, ax = plt.subplots()

#set plot size
fig.set_size_inches(7,5)


#add images
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.12, alpha=1)

#new plot
fig, ax = plt.subplots(figsize=(6, 4), dpi=600)
ax.scatter(data['FGE'], data['PRE'], color='white')
ax.set_title('ACC Special Teams Effectiveness, 2022-23 Season', size=10)
ax.set_xlabel('Field Goal Efficiency')
ax.set_ylabel('Punt Return Efficiency')
plt.xlim([-.9,1.4])

plt.axhline(y=data.PRE.mean(), color = 'black', linestyle='dashed', alpha=.5)
plt.axvline(x=data.FGE.mean(), color='black', linestyle='dashed', alpha=.5)    


#average line labels
fig.text(.75, .48, 'ACC Avg Punt Return Eff.', size=5, alpha=0.7)
fig.text(.46,.16, 'ACC Avg FG Eff.', size=5, alpha=0.7, rotation=90)
fig.text(0.03,.02, 'Source: https://www.footballoutsiders.com/stats/ncaa/fei/overallst/2022', size=4)
fig.text(.03,.04, 'Created By: Eric Drew',size=4)

#quadrant labels
fig.text(.61, .86, 'Good FG Kicker, Good Punt Returner', size=4)
fig.text(.2,.86, 'Bad FG Kicker, Good Punt Returner', size=4)
fig.text(.61, .14, 'Good FG Kicker, Bad Punt Returner', size=4)
fig.text(.2,.14, 'Bad FG Kicker, Bad Punt Returner', size=4)

#function to pull images
for index, row in data.iterrows():
    ab = AnnotationBbox(getImage(row['path']), (row['FGE'], row['PRE']), frameon=False)
    ax.add_artist(ab)




