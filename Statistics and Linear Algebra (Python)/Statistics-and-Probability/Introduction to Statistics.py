## 1. Introduction to Scales ##

car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]
means = 0
oks = 0
for row in car_speeds:
    means += row
mean_car_speed = means/len(car_speeds)    

for row in earthquake_intensities:
    oks += row
mean_earthquake_intensities = oks/len(earthquake_intensities)

## 2. Discrete and Continuous Scales ##

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt
plt.plot(day_numbers,snail_crawl_length)
plt.show()
plt.plot(day_numbers,cars_in_parking_lot)
plt.show()

## 3. Understanding Scale Starting Points ##

fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]
population_zero = yearly_town_population
degrees_zero = [f + 459.67 for f in fahrenheit_degrees]

## 4. Working With Ordinal Scales ##

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey = ['none' , 'a few' , 'some' , 'a lot']
means = 0
for row in range(len(survey)):
    means += row
average_smoking = means/len(survey_responses)

## 5. Grouping Values with Categorical Scales ##

# Let's say that these lists are both columns in a matrix.  Index 0 in both is the first row, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]
mens_savings = [savings[i] for i in range(0,len(gender)) if gender[i] == 'male']
womens_savings = [savings[i] for i in range(0,len(gender)) if gender[i] == 'female']
male_savings = sum(mens_savings)/len(mens_savings)
female_savings = sum(womens_savings)/len(womens_savings)

## 6. Visualizing Counts with Frequency Histograms ##

# Let's say that we watch cars drive by, and measure average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()

# Let's say we measure student test scores, from 0-100
student_scores = [15, 80, 95, 100, 45, 75, 65]
plt.hist(student_scores)
plt.show()

## 7. Aggregating Values with Histogram Bins ##

average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed, bins=6)
plt.show()

# As you can see, the values in the list are counted into the nearest bin.
# If we have less bins, each bin will have a higher count (because it's showing all of the values that fall into it)
# With more bins, the counts are less, because each bin contains less values.
plt.hist(average_speed, bins=2)
plt.show()

## 8. Measuring Data Skew ##

# Some numpy arrays are already loaded in, and we'll make some plots with them.
# The arrays contain student test scores from an exam, on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there is a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot is negatively skewed.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This is positively skewed.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way -- most of the values are in the center, and there is no long slope either way.
# Is is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew
positive_skew = skew(test_scores_positive)
negative_skew = skew(test_scores_negative)
no_skew = skew(test_scores_normal)

## 9. Checking for Outliers with Kurtosis ##

import matplotlib.pyplot as plt

# This plot is short, making it platykurtic
# See how the values are distributed pretty evenly, and there isn't a huge cluster in the middle?
# Students had a wide variation in their performance
plt.hist(test_scores_platy)
plt.show()

# This plot is tall, and is leptokurtic
# Most students did very similarly to the others
plt.hist(test_scores_lepto)
plt.show()

# This plot is in between, and is mesokurtic
plt.hist(test_scores_meso)
plt.show()

# We can measure kurtosis with the kurtosis function
# Negative values indicate platykurtic distributions, positive values indicate leptokurtic distributions, and values close to 0 are mesokurtic
from scipy.stats import kurtosis
kurt_platy = kurtosis(test_scores_platy)
kurt_lepto = kurtosis(test_scores_lepto)
kurt_meso = kurtosis(test_scores_meso)

## 10. Modality ##

import matplotlib.pyplot as plt

# This plot has one mode, making it unimodal
plt.hist(test_scores_uni)
plt.show()

# This plot has two peaks, and is bimodal
# This could happen if one group of students learned the material, and one learned something else, for example.
plt.hist(test_scores_bi)
plt.show()

# More than one peak means that the plot is multimodal
# We can't easily measure the modality of a plot, like we can with kurtosis or skew.
# Often, the best way to detect multimodality is to observe the plot.
plt.hist(test_scores_multi)
plt.show()

## 11. Measures of Central Tendency ##

import matplotlib.pyplot as plt
# We're going to put a line over our plot that shows the mean.
# This is the same histogram we plotted for skew a few screens ago
plt.hist(test_scores_normal)
# We can use the .mean() method of a numpy array to compute the mean
mean_test_score = test_scores_normal.mean()
# The axvline function will plot a vertical line over an existing plot
plt.axvline(mean_test_score)

# Now we can show the plot and clear the figure
plt.show()

# When we plot test_scores_negative, a very negatively skewed distribution, we see that the mean is pulled to the left by the small values there.
# The mean can be changed easily by very large or very small values.
# This can make it misleading with distributions that are very skewed, when we expect the mean to be the center.
plt.hist(test_scores_negative)
plt.axvline(test_scores_negative.mean())
plt.show()

# We can do the same with the positive side
# See how the very high values pull the mean to the right more than you would expect?
plt.hist(test_scores_positive)
plt.axvline(test_scores_positive.mean())
plt.show()
mean_normal = test_scores_normal.mean()
mean_negative = test_scores_negative.mean()
mean_positive = test_scores_positive.mean()

## 12. Calcultaing the Median ##

# Let's plot the mean and median side by side in a negatively skewed distribution.
# Sadly, arrays don't have a nice median method, so we have to use a numpy function to compute it.
import numpy
import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(test_scores_negative)
# Compute the median
median = numpy.median(test_scores_negative)

# Plot the median in blue (the color argument of "b" means blue)
plt.axvline(median, color="b")

# Plot the mean in red
plt.axvline(test_scores_negative.mean(), color="r")

# See how the median is further to the right than the mean?
# It's less sensitive to outliers, and isn't pulled to the left.
plt.show()

plt.hist(test_scores_positive, color = "b")
plt.axvline(test_scores_positive.mean() , color = 'b')
plt.axvline(numpy.median(test_scores_positive) , color = 'r')
plt.show()

## 14. Removing Missing Data ##

import pandas
f = "titanic_survival.csv"
titanic_survival = pandas.read_csv(f)

# Luckily, pandas dataframes have a method that can drop rows that have missing data
# Let's look at how big the dataframe is first
print(titanic_survival.shape)

# There were 1310 passengers on the titanic, according to our data
# Now let's drop any row with missing data
# The dropna method on dataframes will do this for us
# Any row with any missing values will be removed
new_titanic_survival = titanic_survival.dropna()

# Hmm, it looks like we were too zealous with dropping rows with na values
# We now have no rows in our dataframe
# This is because some of the later columns, which aren't immediately relevant to our analysis, have a lot of missing values
print(new_titanic_survival.shape)

# We can use the subset keyword argument to the dropna method to only drop rows if there are na values in certain columns
# This will drop any row where the embarkation port (where people boarded the Titanic), or cabin number is missing
new_titanic_survival = titanic_survival.dropna(subset=["embarked", "cabin"])

# This is much better -- we have removed only the rows that we need to remove.
print(new_titanic_survival.shape)

new_titanic_survival = titanic_survival.dropna(subset=['age' , 'sex'])

## 15. Plotting Age ##

# The cleaned up data has been loaded into the new_titanic_survival variable
import matplotlib.pyplot as plt
import numpy
plt.hist(new_titanic_survival['age'])
plt.axvline(new_titanic_survival['age'].mean(), color='r')
plt.axvline(numpy.median(new_titanic_survival['age']) , color='b')
plt.show()

## 16. Calculating Indexes for Age ##

import numpy
from scipy.stats import skew
from scipy.stats import kurtosis
mean_age = new_titanic_survival["age"].mean()
median_age = numpy.median(new_titanic_survival["age"])
skew_age = skew(new_titanic_survival["age"])
kurtosis_age = kurtosis(new_titanic_survival["age"])