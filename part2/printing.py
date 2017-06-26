from reports import *
import pprint
# Printing functions
pp = pprint.PrettyPrinter(width=80, compact=True)
pp.pprint(get_most_played("game_stat.txt"))
pp.pprint(sum_sold("game_stat.txt"))
