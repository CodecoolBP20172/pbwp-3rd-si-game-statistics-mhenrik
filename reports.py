
# Report functions
import csv


def read_file(filename):  # reads an external file
    '''
    Argument: a filename
    Returns: list
    '''
    with open(filename, newline = "\n") as file:
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


def count_games(filename):
    '''
    Argument: a filename
    Counts the number of games in a file.
    Returns: an integer
    '''
    return(len(read_file(filename)))
