import sys
sys.path.append("..")
from ScraperFC import get_source_comp_info # import local ScraperFC
import itertools
import datetime
import numpy as np
    
########################################################################################################################
def get_random_league_seasons(source, sample_size):
    """
    """
    source_comp_info = get_source_comp_info(2023, "EPL", source)
    
    leagues = source_comp_info[source].keys()
    first_valid_years = [source_comp_info[source][league]["first valid year"] for league in leagues]
    years = range(min(first_valid_years), datetime.datetime.now().year + 1)
    if source == "Oddsportal":
        years = list(years) + [None,]
    
    all_iterator = list(itertools.product(leagues, years))

    if type(sample_size) is str:
        
        if sample_size != "all":
            raise ValueError("If sample_size is a string, it must be \"all\".")
        
        iter = all_iterator

    elif type(sample_size) is int:

        if sample_size <= 0:
            raise ValueError("If sample_size is an integer, it must be > 0.")
        elif sample_size > len(all_iterator):
            raise ValueError(f"Sample size too large. For source {source}, sample size must <= {len(all_iterator)}.")
        
        # Try new league and year combos until we get n=sample_size valid seasons
        iter = list()
        while len(iter) < sample_size:
            random_idx = np.random.choice(len(all_iterator), size=1, replace=False)[0]
            league, year = np.array(all_iterator)[random_idx]
            league, year = str(league), int(year)
            if year < source_comp_info[source][league]["first valid year"]:
                # all_iterator spans minimum first valid year for all leagues from source
                continue
            _ = get_source_comp_info(year, league, source) # confirm the league year is valid
            if (league,year) not in iter:
                iter.append((year,league))

    else:
        raise TypeError("sample_size must be an int or the string \"all\".")

    return iter