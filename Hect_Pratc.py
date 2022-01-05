"""
Heitor Gabriel, the author:
   https://github.com/HeitorGabriel
Pratice Excercise with Pokemon Data:
   https://www.kaggle.com/rounakbanik/pokemon

# ! >>>> On working: unfinished project.  <<<< ! #

"""

import os                        # interact with system
import numpy             as np   # manipulation
import pandas            as pd   # manipulation
import statsmodels       as stm  # statistics
import seaborn           as sea  # visualization
#import matplotlib       as mpl  #      "
import matplotlib.pyplot as plt  #      "


# change working directory
os.chdir("/home/heitor/ProjetosPy/ML_PyPratice/Basic")

# import the csv file as "dd"
dd = pd.read_csv("pokemon.csv")

# 1) View Raw Data =======================================================

dd                              # general
dd.head(5)                      # first 5 lines
dd["abilities"][0:7]            # spec variable and lines
dd[["speed", "name", "type1"]]  # list spec variables

dd.columns  # see col titles
dd.dtypes   # see col variables types

dd           .describe()
dd["speed"]  .describe()

# Lets see the strings variables
dd["abilities"]     .describe()  # freq: most common value’s frequency
dd["classfication"] .describe()
dd["capture_rate"]  .describe()  # 'capture_rate' should be an int!!
dd['is_legendary']  .value_counts()

dd["type1"].describe()
dd["type1"].value_counts()
dd["type2"].describe()
dd["type2"].value_counts()

# sorting
dd.sort_values(by=["type1", "hp"],
               ascending=[1, 0])  # ascending by type1 but not by hp

dd[["name", "type1", "hp", "attack", "defense"]].sort_values(
    by=["type1", "hp"], ascending=[1, 0]
)


# 2) Changing Data ======================================================

# modify the type of 'capture_rate'
dd["capture_rate"]  .astype(int)
dd.loc[dd['capture_rate'] == '30 (Meteorite)255 (Core)']
# there's an observ in 'capture_rate' thar have a text, lets change this observ to 30+255 = 285:
dd.loc[dd['capture_rate'] == '30 (Meteorite)255 (Core)',
       'capture_rate'] = '285'
# now we can aplly the tranformation to int:
dd["capture_rate"] = dd["capture_rate"].astype(int)

# transforming some variables in categorical
dd["generation"]   = dd["generation"]   .astype('category')
dd["is_legendary"] = dd["is_legendary"] .astype('category')
dd["type1"]        = dd["type1"]        .astype('category')
dd["type2"]        = dd["type2"]        .astype('category')

# creating new var:
    # normality of Attack among generation subgroups:
    # (var - var.min) / (var.max - var.min)
dd.groupby('generation')['attack'].min()
dd.groupby('generation')['attack'].max()
    # we need a same length vector containing min & max of the generations: 
dd.groupby('generation')['attack'].transform(min)
dd.groupby('generation')['attack'].transform(max)
    # so:
dd['atk_gen_dnorm'] = (dd['attack'] - dd.groupby('generation')['attack'].transform(min)) / (dd.groupby('generation')['attack'].transform(max) - dd.groupby('generation')['attack'].transform(min))

dd['atk_gen_dnorm'].describe()

# creating new var:
    # mean of the against_x variables:
dd["Against_M"] = dd.iloc[:, 1:18].mean(axis=1)
dd['Against_M'].describe()

# creating new var from type1:
    # water. ice                      -> Aqua
    # normal. fighting                -> Normal
    # fire. dragon. electric          -> Energy
    # rock. steel. ground. grass. bug -> Earth
    # dark. ghost. psychic. poison    -> Dark
    # fairy. flying                   -> Air

dd['group1'] = dd['type1'].astype('str')

dd.group1[(dd['type1']=='water') | (dd['type1']=='ice')] = 'aqua'
dd.group1[(dd['type1']=='normal') | (dd['type1']=='fighting')] = 'body'
dd.group1[(dd['type1']=='fire') | (dd['type1']=='dragon') |
          (dd['type1']=='electric')] = 'energy'
dd.group1[(dd['type1']=='rock') | (dd['type1']=='steel') |
          (dd['type1']=='ground') | (dd['type1']=='grass') |
          (dd['type1']=='bug')] = 'earth'
dd.group1[(dd['type1']=='dark') | (dd['type1']=='ghost') |
           (dd['type1']=='psychic') | (dd['type1']=='poison')] = 'dark'
dd.group1[(dd['type1']=='fairy') | (dd['type1']=='flying')] = 'air'

dd['group1'] = dd['group1'].astype('category')
dd['group1'].value_counts()

# deleting
dd = dd[dd.columns.drop(list(dd.filter(regex='against')))]
dd = dd.drop(columns=["abilities"])
dd = dd.drop(columns=["classfication"])
dd = dd.drop(columns=["base_egg_steps"])
dd = dd.drop(columns=["base_happiness"])
dd = dd.drop(columns=["base_total"])
dd = dd.drop(columns=["height_m"])
dd = dd.drop(columns=["percentage_male"])
dd = dd.drop(columns=["pokedex_number"])
dd = dd.drop(columns=["sp_attack"])
dd = dd.drop(columns=["sp_defense"])
dd = dd.drop(columns=["japanese_name"])

# changing categorical var with contidions
dd.loc[dd["type1"] == "fire", "type1"] = "flamer"
dd.type1
dd.loc[dd["type1"] == "flamer", "type1"] = "fire"

# 3) Filtering Data =====================================================

print(dd.iloc[5:10])  # some specific lines
print(dd.loc[dd["type1"] == "fire"])  # some spec character

dd.loc[(dd["type1"] == "grass") & (dd["type2"] == "poison") & (dd["hp"] > 75)]
# iloc is purely by indexes and loc by names

# select what contains 'Mega' in name
dd.loc[dd["name"].str.contains("mega")]

# select type fire or water
dd.loc[dd["type1"].str.contains("fire|water")]

# 4) Grouping ===========================================================

dd.groupby("type1").mean().sort_values("attack")

# 5) Vizualizations =====================================================
sea.set()

g1  = sea.histplot(dd, x="attack")

g11 = sea.histplot(dd, x="attack", kde=True)

g2 = sea.relplot(x= 'attack', y='defense', data=dd)

g3 = sea.relplot(data=dd,
                 x= 'attack',
                 y='defense',
                 hue='group1')

g4 = sea.jointplot(data=dd,
                   x= 'attack',
                   y='defense',
                   hue='group1')

g41 = sea.jointplot(data=dd,
                   x= 'attack',
                   y='defense',
                   hue='is_legendary',
                   kind= 'kde')

g42 = sea.jointplot(data=dd,
                   x= 'attack',
                   y='defense',
                   #hue='is_legendary',
                   kind= 'reg')

g43 = sea.jointplot(data=dd,
                   x= 'attack',
                   y='defense',
                   #hue='is_legendary',
                   kind= 'hex')

g5 = sea.jointplot(data=dd,
                   y='hp',
                   x='capture_rate')
g5.plot_joint(sea.kdeplot,
              color='r',
              zorder=0,
              levels=6)
g5.plot_marginals(sea.rugplot,
                  color="r",
                  height=-.15,
                  clip_on=False)

g6 = sea.pairplot(dd[['attack', 'defense', 'hp', 'speed', 'group1']],
                  hue='group1', height=2.5)

sea.set_theme(style="ticks")
# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(7, 6))
# Plot the orbital period with horizontal boxes
sea.boxplot(data=dd,
            y="group1",
            x="hp", 
            whis=[0, 100],
            width=.6,
            palette="Set3", showmeans=True) # the means are hidden by scarttes
# Add in points to show each observation
sea.stripplot(data=dd,
              y="group1",
              x="hp",
              size=4,
              color=".3",
              linewidth=0,
              alpha=.45)
# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="Primary Type Group")
sea.despine(trim=True, left=True)

# Rain Cloud: --- {
    # https://towardsdatascience.com/violin-strip-swarm-and-raincloud-plots-in-python-as-better-sometimes-alternatives-to-a-boxplot-15019bdff8f8

plt.figure(figsize=(15, 10))
# Create violin plots without mini-boxplots inside.
ax = sea.violinplot(data=dd,
                    x='speed',
                    y='group1',
                    color='paleturquoise', 
                    cut=0,
                    inner=None)
# Clip the lower half of each violin.
for item in ax.collections:
    x0, y0, width, height = item.get_paths()[0].get_extents().bounds
    item.set_clip_path(plt.Rectangle((x0, y0), width, height/2,
                       transform=ax.transData))
# Create [swarm vs strip] plots with partially transparent points of different colors depending if is legendary.
num_items = len(ax.collections)
sea.stripplot(data=dd,
              x='speed',
              y='group1',
              hue='is_legendary', 
              palette=['deepskyblue', 'navy'],
              alpha=0.6,
              size=7)
# Shift each strip plot strictly below the correponding volin.
for item in ax.collections[num_items:]:
    item.set_offsets(item.get_offsets() + 0.15)
# Create narrow boxplots on top of the corresponding violin and strip plots, with thick lines, the mean values, without the outliers.
sea.boxplot(data=dd,
            x='speed',
            y='group1',
            width=0.25,
            showfliers=False,
            showmeans=True, 
            meanprops=dict(marker='o', markerfacecolor='gold',
                           markersize=10, zorder=3),
            boxprops=dict(facecolor=(0,0,0,0), 
                          linewidth=3, zorder=3),
            whiskerprops=dict(linewidth=3),
            capprops=dict(linewidth=3),
            medianprops=dict(linewidth=3))
plt.legend(frameon=False, fontsize=15, loc='upper left')

# --- }