import csv
import math
import string
# Report functions


def read_file(file_name):
    '''
    Reads an external file
    Args:
        param1: a file name
    Returns:
        a list
    '''
    with open(file_name, newline="\n") as file:
        reader = csv.reader(file, delimiter="\t")
        data = []
        for row in reader:
            # row = [title, number_sold, release_date, genre, publisher]
            title = 0
            number_sold = 1
            release_date = 2
            genre = 3
            publisher = 4
            data.append([row[title], float(row[number_sold]),
                        int(row[release_date]), row[genre], row[publisher]])
    return(data)


def get_most_played(file_name):
    '''
    Finds the title of the most played game (i.e. sold the most copies)
    Args:
        param1: a file name
    Returns:
        a string
    '''
    copies = []
    title = []
    for i, game in enumerate(read_file(file_name)):  # i for indexing the file
        copies.append(read_file(file_name)[i][1])  # 1 is for the nr. of copies
        title.append(read_file(file_name)[i][0])  # 0 is for title
    return(sorted(list(zip(copies, title)), key=lambda x: x[0], reverse=True)[0][1])


def sum_sold(file_name):
    '''
    Finds how many copies have been sold total.
    Args:
        param1: a file name
    Returns:
        a float
    '''
    return sum([row[1] for row in read_file(file_name)])  # 1 is for the nr. of sold copies


def get_selling_avg(file_name):
    '''
    Finds the average selling.
    Args:
        param1: a file name
    Returns:
        a float
    '''
    sales = [row[1] for row in read_file(file_name)]  # 1 is for the nr. of sold copies
    return sum(sales)/len(sales)  # get avg


def count_longest_title(file_name):
    '''
    Finds how many characters long is the longest title.
    Args:
        param1: a file name
    Returns:
        an integer
    '''
    titles = [row[0] for row in read_file(file_name)]  # 0 is for the title
    lengths = [len(title) for title in titles]
    return max(lengths)


def get_date_avg(file_name):
    '''
    Finds the average of the release dates.
    Args:
        param1: a file name
    Return:
        a rounded up integer
    '''
    sales = [row[2] for row in read_file(file_name)]  # 2 is for the dates
    return math.ceil(sum(sales)/len(sales))  # round up is ceil


def get_game(file_name, title):
    '''
    Finds the properties of a given game.
    Args:
        param1: a file name
        param2: a title as string
    Returns:
        a list with all the properties
    '''
    return read_file(file_name)[[title in game for game in read_file(file_name)].index(True)]  # almost as in part1


def count_grouped_by_genre(file_name):
    '''
    Finds how many games are there grouped by genre.
    Args:
        param1: a file name
    Returns:
        dictionary with this structure: { [genre] : [count] }
    '''
    genres = []
    for i, game in enumerate(read_file(file_name)):
        genres.append(read_file(file_name)[i][3])  # 3 is for the genres
    return dict(set(list(zip(genres, [genres.count(genre) for genre in genres]))))  # create dict with comprehension


def get_date_ordered(file_name):
    '''
    Finds the date ordered list of the game.
    Args:
        param1: a file name
    Returns:
        a list
    '''
    dates = []
    title = []
    final_list = []
    for i, game in enumerate(read_file(file_name)):  # i for indexing the file
        dates.append(read_file(file_name)[i][2])  # 2 is for the dates
        title.append(read_file(file_name)[i][0])  # 0 is for title
    for year, title in sorted(list(zip(dates, title)), key=lambda x: (-x[0], x[1].lower()), reverse=False):   # -1 for reverse
        final_list.append(title)
    return final_list
