# import pandas, numpy
# Create the required data frames by reading in the files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
    print("Q1 Find least sales amount for each item")
    ls = df.groupby(['Item'])['Sale_amt'].min().reset_index()
    return ls

# Q2 compute total sales at each year X region
def sales_year_region(df):
    # write code to return pandas dataframe
    print("Q2 compute total sales at each year X region")
    df['year'] = pd.DatetimeIndex(sales['OrderDate']).year
    sales_year_region = df.groupby(['year','Region'])['Unit_price'].sum().reset_index()
    return sales_year_region

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    print("Q3 append column with no of days difference from present date to each order date")
    # write code to return pandas dataframe
    df['days_diff'] = np.datetime64('today') - df['OrderDate']
    return df 

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    print("""Q4 get dataframe with manager as first column and  
          salesman under them as lists in rows in second column.""")
    # write code to return pandas dataframe
    mgr_slsmn = df.groupby(['Manager']).agg({'SalesMan':'unique'}).reset_index()
    mgr_slsmn.columns = ['manager','list_of_salesmen']
    return mgr_slsmn

# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe
    print("Q5 For all regions find number of salesman and number of units")
    slsmn_units = df.groupby(['Region']).agg({'SalesMan':pd.Series.nunique, 
                         'Units':'sum'}).reset_index()
    slsmn_units.columns = ['region', 'salesmen_count','total_sales']
    return slsmn_units

# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    # write code to return pandas dataframe
    print("Q6 Find total sales as percentage for each manager")
    q10 = df.groupby(['Manager']).agg({'Sale_amt':'sum'}).reset_index()
    q10['percent_sales'] = q10['Sale_amt'].apply(lambda x : 100*(x/sum(q10['Sale_amt'])))
    q10 = q10.drop(['Sale_amt'], axis=1)
    return q10

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	# write code here
    print("Q7 get imdb rating for fifth movie of dataframe")
    fifth_movie = df.loc[df['type'] == "video.movie"]['imdbRating'][4]
    return fifth_movie

# Q8 return titles of movies with shortest and longest run time
def formating_column(x):
    try:
        x = int(x)
    except:
        try: 
            x = float(x)
        except:
            x = np.nan
    return x

def movies(df):
	# write code here
    print("Q8 return titles of movies with shortest and longest run time")
    df['duration'] = df['duration'].apply(lambda x : formating_column(x))
    movies = df[((df.duration == df.duration.max()) | (df.duration == df.duration.min()))]['title'].reset_index()
    return movies

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	# write code here
    print("Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)")
    df['year'] = df['year'].apply(lambda x : formating_column(x))
    df['imdbRating'] = df['imdbRating'].apply(lambda x : round(formating_column(x),1))
    df = df.dropna(subset = ['year','imdbRating'], inplace=False).reset_index()
    df = df.loc[(((df['year'] > 1900.0) & (df['year'] < 2021.0)) & ((df['imdbRating'] > 0.0) & (df['imdbRating'] < 10.1)))]
    sort_df = df.sort_values(['year','imdbRating'], ascending=[True, False]).reset_index()
    return sort_df

# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	# write code here
    print("""Q10 subset revenue more than 2 million and spent less than 1 million & 
          duration between 30 mintues to 180 minutes""")
    list_col = ['gross','budget','duration']
    condition = ["df['gross'] > 2000000",
                 "df['budget'] < 1000000",
                 "df['duration'].between(30,180)"]
    print(len(df))
    
    for i in range(len(list_col)):
        print(df.head())
        if list_col[i] in df.columns:
            print(list_col[i])
            df = df.loc[eval(condition[i])] 
            print(len(df))
    df = df.reset_index()  
    return df 

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
    # write code here
    print("Q11 count the duplicate rows of diamonds DataFrame.")
    df_dup = df[df.duplicated(keep='first')]
    return len(df_dup)

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here
    print("Q12 droping those rows where any value in a row is missing in carat and cut columns")
    drop_row = df.dropna(subset = ['carat','cut'], inplace=False).reset_index()
    return drop_row

# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here
    print("Q13 subset only numeric columns")
    sub_numeric = df[df.select_dtypes([np.number]).columns]
    return sub_numeric

# Q14 compute volume as (x*y*z) when depth > 60 else 8

def vol(x,y,z):
    try: 
        volume = float(x)*float(y)*float(z)
    except:
        volume = np.nan
    return volume

def volume(df):
	# write code here
    print("Q14 compute volume as (x*y*z) when depth > 60 else 8")
    df['volume'] = df.apply(lambda row : vol(row['x'],row['y'],row['z'])  if row['depth'] > 60 else 8, axis = 1)
    return df

# Q15 impute missing price values with mean
def impute(df):
	# write code here
    df['price'].fillna(df['price'].mean(), inplace=True)
    return df


# BONUS QUESTIONS 
    
""" Bonus Q1 Generate a report that tracks the various Genere combinations for each type year on year.
The result data frame should contain type, Genere_combo, year, avg_rating,
min_rating, max_rating, total_run_time_mins """

def rev_encoding(row):
    global columns_genre
    lst_genre = []
    for c in columns_genre:
        if row[c]==1:
            lst_genre.append(c)
    return lst_genre

def genere_report_bonusQ1(df):
    print(""" Bonus Q1 Generate a report that tracks the various Genere combinations for each type year on year.
          The result data frame should contain type, Genere_combo, year, avg_rating, min_rating, max_rating,total_run_time_mins""")
    columns_genre = ['Action','Adult','Adventure','Animation',
                     'Biography','Comedy','Crime','Documentary',
                     'Drama','Family','Fantasy','FilmNoir',
                     'GameShow','History','Horror','Music',
                     'Musical','Mystery','News','RealityTV',
                     'Romance','SciFi','Short','Sport',
                     'TalkShow','Thriller','War','Western']

    df['genere_combo'] = df[columns_genre].apply(rev_encoding, axis = 1)
    df['genere_combo'] = df['genere_combo'].apply(lambda x: '|'.join(map(str, x)) )
    '|'.join(map(str, df['genere_combo'][1]))
    genere_df = df.groupby(['type','genere_combo','year']).agg({'ratingCount':['mean','min','max'],'duration':'sum'}).reset_index()
    genere_df.columns = ["_".join(x) for x in genere_df.columns.ravel()]
    return genere_df 


""" Bonus Q2 Is there a relation between the length of a movie title and the ratings ? Generate a report that captures
the trend of the number of letters in movies titles over years. We expect a cross tab between the year of
the video release and the quantile that length fall under. The results should contain year, min_length,
max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile ,
num_videos_50_75Percentile, num_videos_greaterthan75Precentile """


def genere_report_bonusQ2(df):
    print(""" Bonus Q2 Is there a relation between the length of a movie title and the ratings ? Generate a report that captures
    the trend of the number of letters in movies titles over years. We expect a cross tab between the year of
    the video release and the quantile that length fall under. The results should contain year, min_length,
    max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile ,
    num_videos_50_75Percentile, num_videos_greaterthan75Precentile""")
    df['title_length'] = df['title'].apply(lambda x: len(x))
    print("\nThe coorelation value between the length of movies & imdb rating -", df['title_length'].corr(df['imdbRating']))
    plt.plot( df['title_length'],df['imdbRating'], linestyle='', marker='o', markersize=0.7)
    plt.xlabel('Title length')
    plt.ylabel('imdb Rating')
    plt.title(' Relation between Title_length - imdbRating ')
    plt.show()
    df['title_quantile'] = pd.qcut(df['title_length'],q=[0,.25, .5, .75, 1], labels=False)
    df_quantile = pd.get_dummies(df['title_quantile'],prefix=['title_quantile'])
    df_quantile.columns = ['quantile_1','quantile_2','quantile_3','quantile_4']
    df = df.join(df_quantile)
    cross_tab_year_length = df.groupby(['year']).agg({'title_length':['min','max'],'quantile_1':'sum','quantile_2' :'sum','quantile_3':'sum','quantile_4':'sum'}).reset_index()
    cross_tab_year_length.columns = ["_".join(x) for x in cross_tab_year_length.columns.ravel()]
    return cross_tab_year_length


""" Bonus Q3 In diamonds data set Using the volumne calculated above, create bins that have equal population within
them. Generate a report that contains cross tab between bins and cut. Represent the number under
each cell as a percentage of total."""


def factors(x):
   print("The factors of",x,"are:")
   factors = list()
   for i in range(2, x + 1):
       if x % i == 0:
           factors.append(i)
   return min(factors)       


def diamonds_report_bonusQ3(df):
    print(""" Bonus Q3 In diamonds data set Using the volumne calculated above, create bins that have equal population within
    them. Generate a report that contains cross tab between bins and cut. Represent the number under
    each cell as a percentage of total.""")
    num = len(df)
    number_bin = factors(num) # number of bins required for equal proportion
    bin_size = int(num/number_bin) # size of bin
    sort_df = df.sort_values(['volume'], ascending=[True]).reset_index() # sort the dataframe w.r.t volume   
    sort_df['volume_bin'] = int()
    counter = 0
    for i in range(number_bin):
        sort_df['volume_bin'][(counter):(counter+bin_size)]= i
        counter = counter+bin_size
    cross_tab_report = pd.crosstab(sort_df['volume_bin'],sort_df['cut']).apply(lambda r: round((r/r.sum())*100,2), axis=1)
    return cross_tab_report


""" Bonus Q4 Generate a report that tracks the Avg. imdb rating quarter on quarter
, in the last 10 years, for movies that are top performing. 
You can take the top 10% grossing movies every quarter. Add the number of top
performing movies under each genere in the report as well."""

def movies_report_bonusQ4(df):
    print(""" Bonus Q4 Generate a report that tracks the Avg. imdb rating quarter on quarter
            , in the last 10 years, for movies that are top performing. 
            You can take the top 10% grossing movies every quarter. Add the number of top
            performing movies under each genere in the report as well.""")
    df_last10years = pd.DataFrame()
    df_last10years_groupby1 = pd.DataFrame()
    df_top10percentgross_groupby2 = pd.DataFrame()
    for i in range((int(max(df["title_year"]))-9),(int(max(df["title_year"]))+1)):
        print(i)
        df_subset = df.loc[df["title_year"] == float(i)].reset_index(drop = True)
        df_subset['year_quarter'] = pd.qcut(df_subset.index,q= 4, labels= False)
        df_last10years = df_last10years.append(df_subset).reset_index(drop = True)  
        df_subset_groupby = df_subset.groupby(['title_year','year_quarter']).agg({'imdb_score':'mean'}).reset_index()
        df_subset_groupby.columns = ['year','year_quarter','avg_imdb_score']
        df_last10years_groupby1 = df_last10years_groupby1.append(df_subset_groupby).reset_index(drop = True)
        for j in range(len(np.unique(df_subset['year_quarter']))):
            df_subset2 = df_subset.loc[df_subset['year_quarter'] == j].reset_index(drop = True)
            df_subset2 = df_subset2.sort_values(['gross'], ascending=[False]).reset_index(drop = True)
            df_subset2 = df_subset2.head(int(len(df_subset2['gross'])*(10/100)))
            genere_subset = df_subset2.genres.str.split("|",expand=True) 
            genere_count = pd.Series()
            for k in range(genere_subset.shape[1]):
                genere_count = genere_count.append((genere_subset[k].value_counts()))
            genere_data = pd.DataFrame()
            genere_data = pd.DataFrame(genere_count.groupby(level=0).sum()).T.reset_index(drop = True)
            genere_data["year"] =  i
            genere_data["year_quarter"] = j
            genere_data["Top_10%_Grossing_Movies"] = str(list(df_subset2.movie_title))
            df_top10percentgross_groupby2 = df_top10percentgross_groupby2.append(genere_data)
    #pd.unique(df_subset2['genres'].str.split("|",expand=True).stack())        
    df_last10years_groupby1['year'] = df_last10years_groupby1['year'].apply( lambda x : int(x))
    movies_report_bonusQ4 = df_last10years_groupby1.merge(df_top10percentgross_groupby2, on = ['year','year_quarter'])
    return movies_report_bonusQ4

""" Bonus Q5 Bucket the movies into deciles using the duration. 
Generate the report that tracks various features like
nomiations, wins, count, top 3 geners in each decile. """

def bucket_movies_bonusQ5(df):
    print(""" Bonus Q5 Bucket the movies into deciles using the duration.
          Generate the report that tracks various features like
          nomiations, wins, count, top 3 geners in each decile. """)
    df['movie_decile'] = pd.qcut(df['duration'],q=10, labels = False)
    columns_genre = ['Action','Adult','Adventure','Animation',
                     'Biography','Comedy','Crime','Documentary',
                     'Drama','Family','Fantasy','FilmNoir',
                     'GameShow','History','Horror','Music',
                     'Musical','Mystery','News','RealityTV',
                     'Romance','SciFi','Short','Sport',
                     'TalkShow','Thriller','War','Western']
    df_genere = df.groupby(['movie_decile'])[columns_genre].sum().reset_index()
    df_genere_T = pd.DataFrame(df_genere).T
    df_genere["top_genere"] = ""
    for i in df_genere_T.columns:
        df_genere["top_genere"][i]= df_genere_T[i].nlargest(3).index.tolist()    
    movie_decile_report = df.groupby(['movie_decile']).agg({'nrOfNominations':'sum','nrOfWins':'sum', 'duration':'count'}).reset_index()
    movie_decile_report["top_genere"] = df_genere["top_genere"]
    return movie_decile_report

""" Bonus Q6 Using the movie metadata set and the imdb data set 
come up with finidings (slice and dice the data to
identify insights) and also create charts whereever possible. """

# Describes all column including categorical column's                       
df1.describe(include='all')
# to plot the distribution of data in each column
for i in range(len(df1._get_numeric_data().columns)):
    plt.figure(figsize=(6, 3.5))
    sns.distplot(df1[df1._get_numeric_data().columns[i]], color='g', bins=100, hist_kws={'alpha': 0.4})
# nunique() would return the number of unique elements in each column
print(df1.nunique())
# plot the bivariate distributions to understand the relationship between 2 attributes of data
sns.pairplot(df1)
# missing value analysis 
df1.isnull().values.any()
df1.isnull().sum()
# outlier analysis
for i in range(len(df1._get_numeric_data().columns)):
    plt.figure(figsize=(8, 3.5))
    sns.boxplot(df1[df1._get_numeric_data().columns[i]],orient = "v", palette = sns.color_palette("RdBu", n_colors=7))
# Correlation analysis
corr = df1.corr() 
plt.figure(figsize=(15, 12))
sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);

df2.describe(include='all')
for i in range(len(df2._get_numeric_data().columns)):
    plt.figure(figsize=(7, 3.5))
    sns.distplot(df2[df2._get_numeric_data().columns[i]], color='r', bins=100, hist_kws={'alpha': 0.4})
print(df2.nunique())


""" *****************************Main Function*****************************"""

if __name__ == "__main__":
    # Solution for Q1 - Q6
    # Read the sales dataset 
    print("Solutions to 1-6 Questions with Sales Dataset \n")
    sales = pd.read_excel('SaleData.xlsx')
    print(sales.head())
    print("************************")
    print(least_sales(sales))
    print("************************")
    print(sales_year_region(sales))
    print("************************")
    print(days_diff(sales).head())
    print("************************")
    print(mgr_slsmn(sales))
    print("************************")
    print(slsmn_units(sales))
    print("************************")
    print(sales_pct(sales))
    print("************************#####***************************")
    print("Solutions to 7-10 Questions with Sales Dataset \n")
    imdb = pd.read_csv('imdb.csv', escapechar = '\\')
    print(imdb.head())
    print("************************")
    print(fifth_movie(imdb))
    print("************************")
    print(movies(imdb))
    print("************************")
    print(sort_df(imdb).head())
    print("************************")
    movie_metadata = pd.read_csv('movie_metadata.csv', escapechar = '\\')
    print(movie_metadata.head())
    print(subset_df(imdb))
    print("************************#####***************************")
    print("Solutions to 11-15 Questions with Diamond Dataset \n")
    diamonds = pd.read_csv('diamonds.csv')
    print(diamonds.head())
    print("************************")
    print(dupl_rows(diamonds))
    print("************************")
    print(drop_row(diamonds).head())
    print("************************")
    print(sub_numeric(diamonds).head())
    print("************************")
    volume_diamonds = volume(diamonds)
    print(volume_diamonds.head())
    print("************************")
    print(impute(diamonds).head())
    print("************************#####***************************")
    print("Solutions - Bonus Questions \n")
    print("************************")
    print(genere_report_bonusQ1(imdb).head(50))
    print("************************")
    print(genere_report_bonusQ2(imdb).head(50))
    print("************************")
    print(diamonds_report_bonusQ3(volume_diamonds))
    print("************************")
    print(movies_report_bonusQ4(df).head())
    print("************************")
    print(bucket_movies_bonusQ5(imdb))
    print("************************")
    