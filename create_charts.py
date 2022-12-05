import os
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image

name = "samantha"

# create folder for output images
current_directory = os.getcwd()
new_directory = os.path.join(current_directory, name)
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# read in data
sam = pd.read_csv(name, sep="\t")

# plot snps per chromosome and save
sns.countplot(data=sam, x='chromosome')
plt.title('SNPs per Chromosome')
plt.savefig(name + '/SnpsPerChromosome.png');

# taste visualizations

# create taste df and format outcomes
taste_df = pd.merge(sam, taste, right_on = 'RSID', left_on='# rsid', how='inner')
taste_df["Outcome"] = taste_df["Outcome"].apply(lambda x: x.lower())

# taste preference chart
taste_pref = taste_df[(taste_df["Type"] == "Taste") & (taste_df["Outcome"].str.contains('preference'))]
sns.countplot(data=taste_pref, y='Outcome', palette=sns.color_palette("hls", 6)).set_title("Preferences for Different Tastes")
plt.savefig(name + "/PreferencesForDifferentTastes.png");

# taste sensitivities chart
taste_sens = taste_df[(taste_df["Type"] == "Taste") & (taste_df["Outcome"].str.contains('sensitivity'))]
sns.countplot(data=taste_sens, y='Outcome', palette=sns.color_palette("hls", 6)).set_title("Sensitivities for Different Tastes")
plt.savefig(name + "/SensitivitiesForDifferentTastes");





