import pandas as pd
import numpy as np
import os

df = pd.DataFrame()

df['class'] = 0
df['image'] = ""

direc = r'/Users/mitchell.carmen/Projects/Public_Projects/CV_brody/assets_for_dr_training'
files_to_run = os.listdir(direc)

image_names = []
for file in files_to_run:
    # df[file] = os.path.join('assets_for_dr_training', file)
    image_names.append(os.path.join('assets_for_dr_training', file))

df['image'] = image_names
df = df.sort_values(by='image', ascending=True)

print(df)

#df.to_csv('training_data.csv')