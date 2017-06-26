from reports import *
# Export function


def export_all(file_name):
    '''
    Exports all answer to a .txt file
    Args:
        param1: a file name
    Returns:
        a text file
    '''
    with open(file_name, 'w', newline="\n") as file:
        file.writelines(str(count_games("game_stat.txt"))+"\n")
        file.writelines(str(decide("game_stat.txt", 2009))+"\n")
        file.writelines(str(get_latest("game_stat.txt"))+"\n")
        file.writelines(str(count_by_genre("game_stat.txt", "RPG"))+"\n")
        file.writelines(str(get_line_number_by_title("game_stat.txt", "Command & Conquer"))+"\n")
        file.writelines(str(sort_abc("game_stat.txt"))+"\n")
        file.writelines(str(get_genres("game_stat.txt"))+"\n")
        file.writelines(str(when_was_top_sold_fps("game_stat.txt")))


export_all("output.txt")
