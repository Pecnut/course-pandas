import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('exam_results.xlsx')

# 1. Top students
data['mean'] = data[['Quantum Mechanics','Lab work','Relativity','Waves']].mean(1,skipna=False)
print(data[data['Programme']=='Physics'].sort_values('mean',ascending=False).head(6))

# 2. Tutor group with highest mean
print(data.groupby('Tutor group').mean().sort_values('mean',ascending=False).head())

# 3. Mean of courses
course_means = data[['Waves','Quantum Mechanics','Lab work','Relativity']].mean().sort_values()
course_means.plot(kind='bar')
plt.tight_layout()
plt.show()

# 4. Firsts, 2:1s etc.
bins = [0,40,50,60,70,100]
labels = ['F','3','2:2','2:1','1']
pd.cut(data['Quantum Mechanics'],bins,labels=labels).value_counts().plot(kind='pie')
plt.show()

# 5. Failures
 for index, row in data[data['Programme']=='Physics'].iterrows():
    courses_passed = 0
    if row['Quantum Mechanics'] >= 40:
        courses_passed += 1
    if row['Lab work'] >= 40:
        courses_passed += 1
    if row['Relativity'] >= 40:
        courses_passed += 1
    if row['Waves'] >= 40:
        courses_passed += 1
    if courses_passed < 4:
        print("Dear " + row['Forename 1'] + ". You have failed.")

# 6. Histogram
data.hist('Quantum Mechanics')
plt.show()
data.hist()
plt.tight_layout()
plt.show()

from pandas.plotting import scatter_matrix
# kde = Kernal density estimation
scatter_matrix(data[['Quantum Mechanics','Waves','Relativity','Lab work']],diagonal='kde')
plt.show()
