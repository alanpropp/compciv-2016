#**About the dataset:**
##This dataset is a list of all Nobel Prize winners since 1901 (extending to 2010), along with their field, birthdate, birth place, county, residence, role/affiliation, field/language, prize name, and motivation (the "why" part of it). I would like to see how the gender of winners has changed over time, see how many women win in each particular field, and potentially if there are countries that have a particularly large number/percentage of female winners.

#Data source:
###- The source of the data: https://www.aggdata.com/
###- The data's landing page: https://www.aggdata.com/awards/nobel_prize_winners
###- Direct link to the data: https://www.aggdata.com/download_sample.php?file=nobel.csv
###- The data format: CSV
###- Number of rows: 840 (including headers)

#First name info:
###- Because the names are relatively uniformly formatted, I believe I will simply be able to extract the characters from the string up until the first space, and use that as the first name

#Potential caveats:
###- The country of origin tends to vary in how it is formatted (for example, whether or not to count Prussia as Germany or not), which could make it difficult to determine birthplaces. Also, we will be relying on an imperfect gender detector

#How to use it
### I am relatively unclear on this thus far, but my best guess...

##fetch_data.py
### Downloads the raw Nobel Prize winner data from aggdata as a CSV file and loads it into a subfolder of tempdata

##wrangle_data.py
###Moves the data into a more readable/useful CSV file for my purposes

##fetch_gender_data.py
###Based on a previous assignment, downloads baby names data and puts it in a CSV file to help us detect gender

##wrangle_gender_data.py
###Again based on a previous assignment, does the analysis to give us a function that can generally detect the gender of a given name

##gender.py
###Provides a reference to my gender detector

##classify.py
###Classifies each row in my CSV file as male, female, or NA (does much more than that internally, but that is the overall result)

##analyze.py
###Performs the analyses given below

#Analysis:
###- I would like to first run an analysis simply seeing how many female and male prizes were awarded each year
###- I would then like to break down how many awards were awarded to men and women by category of Nobel Prize
###- Finally, I would like to see the percentage of men and women who won prizes from specific countries, to see if there are any particularly good or horrendous countries in terms of gender breakdown