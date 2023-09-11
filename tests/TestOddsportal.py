import sys
sys.path.insert("..")
from ScraperFC import Oddsportal # import local ScraperFC
from shared_test_functions import get_random_league_seasons

num_links = {
    "EPL": {
        2004: 138, 2005: 377, 2006: 380, 2007: 376, 2008: 380, 2009: 380,
        2010: 380, 2011: 380, 2012: 380, 2013: 380, 2014: 380, 2015: 380,
        2016: 380, 2017: 380, 2018: 380, 2019: 380, 2020: 380, 2021: 380,
        2022: 380, 2023: 380,
    },
}

class TestOddsportal:

    def test_get_match_links(self, sample_size):
        samples = get_random_league_seasons("Oddsportal", sample_size)
        op = Oddsportal()
        for year, league in samples:
            links = op.get_match_links(year, league)
            
            assert len(links) = num_links[league][year], "wrong number of links"
        op.close()
        
            
    # def test_scrape_season_odds(self, sample_size):
    #     samples = get_random_league_seasons("Oddsportal", sample_size)
    #     op = Oddsportal()
    #     for year, league in samples:
    #         season_odds = op.scrape_season_odds(year, league)
    #         assert season_odds.shape[0] = num_links[league][year], "wrong number of matches"
    #     op.close()