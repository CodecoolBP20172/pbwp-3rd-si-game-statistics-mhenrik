
# Report functions
import csv


def read_file(file_name):  # reads an external file
    '''
    Argument: a file name
    Returns: list
    '''
    with open(file_name, newline = "\n") as file:
        reader = csv.reader(file, delimiter = "\t")
        data = []
        for row in reader:
            #row = [title, number_sold, release_date, genre, publisher]
            title = row[0]
            number_sold = float(row[1])
            release_date = row[2]
            genre = row[3]
            publisher = row[4]
            data.append([title, number_sold, release_date, genre, publisher])
        return(data)


def count_games(file_name):
    '''
    Argument: a file name
    Counts the number of games in a file.
    Returns: an integer
    '''
    return(len(read_file(file_name)))


def decide(file_name, year):
    '''
    Arguments: a file name and a year
    Returns: a boolean if there is a game in the given year
    '''
    return any(year in game for game in read_file(file_name))
