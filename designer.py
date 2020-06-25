#!/bin/python3

def int_message():
    print('Please input an iteger (i.e., 0, 1, 2, ...) greater than zero')
    quit()

prefix = input('Provide a prefix (no spaces) for this experimental design (i.e., a name for this trial/experiment): ')

def reformat_df(dataframe, design):
    return pd.wide_to_long(df,
            stubnames = design,
            i = list(treatments.keys()),
            j = 'id',
            sep = '_')


# COLLECT INPUT FROM USER
######################################################################
design = input('What is the experimental design (crd/rcbd): ').lower()
if design not in ['crd', 'rcbd']:
    print('Please use crd or rcbd as input.')
    quit()

replicates = int(input('How many replicates (integer): '))

if not isinstance(replicates, int):
    int_message()
    if replicates < 0:
        int_message()

num_factors = int(input('How many factors (integer): '))

# initialize a dictionary for factors and levels
treatments = {}

for fact in range(1, num_factors + 1):

    # get user input for factors and levels within factors
    f_name = input(f"What is the name of factor {fact} (string, no spaces): ")
    n_lvls = int(input(f"How many levels are within the factor {f_name}?: "))
    f_trts = [input(f"{f_name} - level {lvl}: ") for lvl in range(1, n_lvls + 1)]
    treatments[f_name] = f_trts

# MAIN PROCEDURE OF THE SCRIPT
######################################################################


from itertools import product
import pandas as pd
import numpy as np

#get all treament combinations
trt_combos = list(product(*treatments.values()))

# convert dictionary to dataframe
df = pd.DataFrame(trt_combos)

# convert ambiguous column names to treatment names
df.columns = [list(treatments.keys())]

# randomize treatments in a crd design
if design == 'crd':
    
    # for any complete crd, one needs `replicates` * the number of treatment combinations (i.e., the number of rows in `df`
    plots = [num for num in range(1, (replicates * len(df.index)) + 1)]
    
    np.random.shuffle(plots)

    # assign the shuffled plots to the dataframe
    for index, col in enumerate(np.array_split(np.array(plots), replicates), 1):
        name = 'rep_' + str(index)
        df[name] = col

# generate randomization for rcbd design
if design == 'rcbd':

    for plot in range(1, replicates + 1):
        block = [plot for plot in range(1, len(df.index) + 1)]
        np.random.shuffle(block)
        name = 'block_' + str(plot)
        df[name] = block

# provide a name for the plot map
plot_map_name = prefix + '_plot_map.csv'

# save csv file of plot map
df.to_csv(plot_map_name, index = False, encoding='utf-8')
df = pd.read_csv(plot_map_name)

# reformat the dataframe for a printable datasheet
if design == 'crd':
    reformatted_df = reformat_df(df, 'rep')
    
else:
    reformatted_df = reformat_df(df, 'block') 

reformatted_df.to_csv(prefix + '_manual_input_sheet.csv', encoding = 'utf-8')
