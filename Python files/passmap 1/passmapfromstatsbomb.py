# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 23:05:09 2022

@author: dev
"""

match_id = 3869486

file_name=str(match_id)+'.json'
import seaborn as sns

import json
with open('E:/SoccermaticsForPython-master/statsbomb02/open-data-master/data/events/'+str(match_id)+'.json') as f:
    data = json.load(f)
    
from pandas.io.json import json_normalize
from pandas.io import json
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

Passes = df.loc[df['type_name'] == 'Pass'].set_index('id')


from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt
# Set up the pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw()
fig.set_facecolor('#22312b')
eriks = df.loc[df['player_name'] == 'Sofyan Amrabat'].set_index('id')


for i,passs in Passes.iterrows():
    if passs['player_name']=="Sofyan Amrabat":   
        x= passs['location'][0]
        y= passs['location'][1]
        xx= passs['pass_end_location'][0]
        yy= passs['pass_end_location'][1]
        plt.scatter(x,y,s=20,c='black')
        pitch.arrows(x, y,xx,yy, width=1,headwidth=5, headlength=5, color='#ad993c', ax=ax, label='completed passes')
        
ax_title = ax.set_title(f' Messi vs Croatia', fontsize=10,c='white')

