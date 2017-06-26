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
        file.writelines(str(get_most_played("game_stat.txt"))+"\n")
        file.writelines(str(sum_sold("game_stat.txt"))+"\n")
        file.writelines(str(get_selling_avg("game_stat.txt"))+"\n")
        file.writelines(str(count_longest_title("game_stat.txt"))+"\n")
        file.writelines(str(get_date_avg("game_stat.txt"))+"\n")
        file.writelines(str(get_game("game_stat.txt", "Counter-Strike"))+"\n")
        file.writelines(str(count_grouped_by_genre("game_stat.txt"))+"\n")
        file.writelines(str(get_date_ordered("game_stat.txt"))+"\n")



export_all("output.txt")
