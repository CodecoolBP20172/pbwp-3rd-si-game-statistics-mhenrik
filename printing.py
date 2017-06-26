from reports import *
import pprint
# Printing functions
pp = pprint.PrettyPrinter(width=80, compact=True)
pp.pprint(count_games("game_stat.txt"))
pp.pprint(decide("game_stat.txt", "2009"))
pp.pprint(get_latest("game_stat.txt"))
pp.pprint(count_by_genre("game_stat.txt", "RPG"))
pp.pprint(get_line_number_by_title("game_stat.txt", "Command & Conquer"))
pp.pprint(sort_abc("game_stat.txt"))
pp.pprint(get_genres("game_stat.txt"))
pp.pprint(when_was_top_sold_fps("game_stat.txt"))
