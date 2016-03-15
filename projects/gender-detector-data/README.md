#**About the dataset:**
##This dataset is a list of all Nobel Prize winners since 1901 (extending to 2010), along with their field, birthdate, birth place, county, residence, role/affiliation, field/language, prize name, and motivation (the "why" part of it). I would like to see how the gender of winners balances, how it has has changed over time, how many women win in each particular field, and potentially if there are countries that have a particularly large number/percentage of female winners. The analysis found a dramatic imbalance (weighted towards males, with a ratio of around 15 males to 1 female) in the gender of Nobel Prize winners over the years, and that imbalance tends to hold in almost every single decade without much improvement over time (except the 2000's, which did much better than any other decade and offers hope for a better balance). I also found that there are far more female winners in medicine, peace, and literature (relatively) than the other fields, and that physics is particularly imbalance with 164 male winners to just 3 females. Finally, there are only around 25 countries with any females whatsoever, and in most cases they are in the minority of winners from those countries (Iran, Persia, Israel Vietnam, and South Korea stand as outliers - an interesting phenomenon of more women than men winning in these Middle Eastern countries). Overall, the data demonstrate a severe (if relatively unsurprising) tendency towards male Nobel prize winners

#Data source:
###- The source of the data: https://www.aggdata.com/
###- The data's landing page: https://www.aggdata.com/awards/nobel_prize_winners
###- Direct link to the data: https://www.aggdata.com/download_sample.php?file=nobel.csv
###- The data format: CSV
###- Number of rows: 840 (including headers)

#Past articles:
###This study (http://stats.areppim.com/stats/stats_nobel_sexxcat.htm) did a similar analysis based on category, although they broke it down based on what percentage of total women and what percentage of total men had won in each category, rather than comparing women to men within each category. This study (http://fortune.com/2015/10/12/women-nobel-prizes/) did a nearly identical analysis as the one I did, and displayed it in a graphical format. Finally, this study (http://www.telegraph.co.uk/news/worldnews/11922707/Nobel-Prize-winners-How-many-women-have-won-awards.html) also looked at the women in specific countries, although they only included countries with more than 5 winners in their analysis. Cumulatively, these articles give a relatively detailed understanding entering my analysis that women are HEAVILY underrepresented among Nobel Prize winners, and while that trend may be improving over time, it is still far from complete.

#First name info and gender detector:
###- Because the names are relatively uniformly formatted as first name followed by middle and last names (separated by whitespaces), I am simply be able to extract the characters from the string up until the first whitespace character, and use that as the first name. For some names, they just include the first inital of the first name (names like "J. Edgar Hoover"), so I include an if statement to extract the first word post-whitespace character from these type of names, because the second name generally still delivers the correct gender. Once I have the first name I can pass it into a gender detector based on analysis of American baby names in 2014 (explained later).

#Potential caveats:
###- The country of origin tends to vary in how it is formatted (for example, whether or not to count Prussia as Germany or not), which makes it difficult to determine nationality. Also, we will be relying on an imperfect gender detector. In addition, many of these names are international names (by nature of the Nobel Prize winner distribution), and my gender detector doesn't recognize a large proportion of them because the dataset used to create that detector is based on largely American names. Finally, some Nobel Prize winners are organizations, so the gender detector doesn't really know what to do with them - most are listed as NA.

#How to use it
##Users should use these functions in the order they are listed, unless the function description articulates that the user does not need to use that particular function

##fetch_gender_data.py
###Use this python function first to download the files for the analysis and creation of a gender detector. Based on a previous assignment, downloads baby names data and puts it in a CSV file to help us detect gender.

##wrangle_gender_data.py
###Again based on a previous assignment, does the analysis to give us a function that can generally detect the gender of a given name. Basically goes through all the names in the text files and creates a gender detector that gives the likely gender of any given name, as well as the ratio of one gender to the other and the probability of it being that specific gender. Relies the data from fetch_gender_data.py

##gender.py
###Provides a reference to my gender detector for internal usage. The user will not need this function - it is just for ease of use of the gender detector we earlier created

##fetch_data.py
###Downloads the raw Nobel Prize winner data from aggdata as a CSV file and loads it into a subfolder of tempdata. Once you have set up the gender detector, use this function to gather the Nobel Prize data from online and store it in 'tempdata/nobel.csv'

##wrangle_data.py
###Moves the data from fetch_data.py into a more readable/useful CSV file for my purposes. In this case, it creates 'tempdata/nobel_wrangled.csv', which is similar to the previous CSV file but with fewer headers (it strips the ones we won't use for data analysis)

##classify.py
###Classifies each row in the wrangled CSV file as male, female, or NA (does much more than that internally, but that is the overall result). It then adds columns for 'gender', 'ratio', and usable_name (just the first name of each winner) and stores all of this data in 'tempdata/classified_data/csv'.

##analyze.py
###Performs the analyses given below. Use this function once you have used all the other given functions - it will print out all the data analysis results to the terminal window.


#Analysis:
###- I would like to first run an analysis simply seeing how many female and male prizes were awarded total. I will get the overall male/female ratio and the number of 'NA' names. The overall male/female ratio turned out to be around 15.205 (669 males and 44 females), with 126 names for whom the computer could not determine gender (or they were organizations)
###- I would then like to break down how many awards were awarded to men and women by category of Nobel Prize, and calculate the male/female ratio for each individual prize. The results of this section indicated that the male/female ratio was 31.0 for economics (62 males and 2 females), 54.667 for physics (164 males and 3 females), 6.364 for literature (70 males and 11 females), 7.3 for peace (73 males and 10 females), 12.308 for medicine (160 males and 13 females), and 28.0 for chemistry (140 male and 5 females).
###- In addition, I will break down the male/female ratio by decade, from the 1900s until today, to observe any change over time. The results here indicated that the male/female ratio was 14.333 (43 males and 3 females) for the 1900s, 15.0 (30 males and 2 females) for the 1910s, 15.0 (45 males and 3 females) for the 1920s, 24.5 (49 males and 2 females) for the 1930s, 17.0 (34 males and 2 females) for the 1940s, infinity (60 males and no females) for the 1950s, 11.6 (58 males and 5 females) for the 1960s, 22.0 (88 males and 4 females) for the 1970s, 14.8 (74 males and 5 females) for the 1980s, 17.2 (86 males and 5 females) for the 1990s, 7.833 (94 males and 12 females, the lowest of all ratios) for the 2000s, and 8.0 (8 males and 1 female) in the year 2010. This indicates minimal change in ratio over time, but a sharp drop in the 2000s.
###- Finally, I would like to see the countries in which there actually have been female winners, and see in those countries what percentage of the overall winners were female. The only countries with female winners were Northern Ireland (2), Egypt (1), Poland (3), Germany (2), Japan (1), Denmark (1), Chile (1), Austria (1), USA (13), South Africa (2), Switzerland (1), Italy (2), France (3), South Korea (1), Israel (1), Vietnam (1), Iran (1), Australia (2), Sweden (2), Persia/current Iran (1), and China (1). Interestingly, the only countries in which female winners were in the majority were Iran, Persia, Israel Vietnam, and South Korea - an interesting phenomenon of more women than men winning in these Middle Eastern countries, as well as a couple of East Asian nations.

