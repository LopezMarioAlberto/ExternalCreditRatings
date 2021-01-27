import pandas as pd

def rating_matrix():
  """
  The function creates the External Credit Rating Matrix based on information provided from rating agency
  """

  probabilities_percentage = [(0.00, 0.00, 0.07, 0.15, 0.24, 0.66, 1.40, 1.40), 
                (0.18, 0.44, 0.72, 1.27, 1.78, 2.99, 4.34, 4.70), 
                (5.20, 11.00, 15.95, 19.40, 21.88, 25.14, 29.02, 30.65),
                (19.79, 26.92, 31.63, 35.97, 40.15, 42.64, 45.10, 45.10)]

  years = [1, 2, 3, 4, 5, 7, 10, 15]

  ratings = ['AAA', 'BBB', 'B', 'CCC']

  initial_ratings = pd.DataFrame(probabilities_percentage, columns = years, index = ratings)

  return initial_ratings


def probability_default (year, rating, period = 'end', defaulted = 'yes'):
  """
  The function calculates the probability of default based on an External Credit Rating

  inputs:
  - year (float)
  - rating(str) options: 'AAA', 'BBB', 'B', 'CCC'
  - period(str) options: 'end' (default), 'during'
  - defaulted(str) options: 'yes (default), 'no'
  """

  initial_ratings = rating_matrix()

  # probability of defaulting during year
  probability = initial_ratings.loc[rating,year]
    
  if period != 'end':
    probability = initial_ratings.loc[rating,year] - initial_ratings.loc[rating,year - 1]

  # probability of surviving until the end of the previous year
  surviving = 1

  final_probability = probability / surviving
  
  if defaulted == 'no':
    surviving = 100 - initial_ratings.loc[rating,year - 1]
    final_probability = 100 * probability / surviving
  
  return final_probability
