""
The function calculates the confidence interval
""

from scipy.stats import sem, t
from numpy import mean

def confidence_interval(x,ci): # ci = 0.95

  M = np.mean(x)                                   # Sample mean
  ME = sem(x)* t.ppf((1 + ci) / 2, len(x) - 1)     # Margin of error

  ci_endpoints = {

          'The lower endpoint of the 95% CI is:': M - ME,
          'The upper endpoint of the 95% CI is:': M + ME
  }
  return ci_endpoints
