"""
Heitor Gabriel, the author:
   https://github.com/HeitorGabriel
Pratice Excercise with Pokemon Data:
   https://www.kaggle.com/rounakbanik/pokemon

# ! >>>> On working: unfinished project.  <<<< ! #

"""

import os                   # interact with system
import numpy        as np   # manipulation
import pandas       as pd   # manipulation
import statsmodels  as stm  # statistics
import seaborn      as sb   # visualization

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

# creating new var: normality of Attack among type1 subgroups:
dd["atk_type1_ratio"] = dd["attack"] / (dd.groupby('type1')['attack'].max() - dd.groupby('type1')['attack'].min())

# creating new var: mean of the against_x variables:
dd["Against_M"] = dd.iloc[:, 1:18].mean(axis=1)

# deleting
dd = dd.drop(columns=["def_ratio"])
dd = dd.drop(columns=["Against_Total"])
dd = dd.drop(columns=["base_total"])
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
