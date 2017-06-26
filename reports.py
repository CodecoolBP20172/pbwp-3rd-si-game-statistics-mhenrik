
# Report functions
import csv
import string


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


def count_games(file_name):
    '''
    Counts the number of games in a file.
    Args:
        param1: a file name
    Returns:
        an integer
    '''
    return(len(read_file(file_name)))


def decide(file_name, year):
    '''
    Decides if there is a game from a given year
    Args:
        param1: a file name and a year
    Returns:
        a boolean if there is a game in the given year
    '''
    return any(year in game for game in read_file(file_name))


def get_latest(file_name):
    '''
    Finds the title of the latest game
    Args:
        param1: a file name
    Returns:
        the title of the game as a string
    '''
    # row = [title, number_sold, release_date, genre, publisher]
    years = []
    title = []
    for i, game in enumerate(read_file(file_name)):  # i for indexing the file
        years.append(read_file(file_name)[i][2])  # 2 is for release_date
        title.append(read_file(file_name)[i][0])  # 0 is for title
    mix = list(zip(years, title))  # join the lists
    return(sorted(mix, key=lambda x: x[0], reverse=True)[0][1])  # key is for the sorted the find the years


def count_by_genre(file_name, genre):
    '''
    Counts the games by the given genre.
    Args:
        param1: a file name
        param2: a genre
    Returns:
        an integer
    '''
    genres = []
    for i, game in enumerate(read_file(file_name)):
        genres.append(read_file(file_name)[i][3])  # 3 is for the genres
    return(genres.count(genre))


def get_line_number_by_title(file_name, title):
    '''
    Finds the line number of the given game (by title)
    Args:
        param1: a file name
        param2 : a title
    Returns:
        an integer
    '''
    try:
        return([title in game for game in read_file(file_name)].index(True)+1)  # return if any is True, finds index
    except BaseException:
        raise ValueError


def sort_list(indexlist):
    '''
    Sorting algorithm.
    Args:
        param1: a list
    Returs:
        a sorted list
    '''
    i = 1
    while i < len(indexlist):
        j = 0
        while j <= len(indexlist) - 2:
            if indexlist[j] > indexlist[j+1]:
                temp = indexlist[j+1]
                indexlist[j+1] = indexlist[j]
                indexlist[j] = temp
                j += 1
            else:
                j += 1
        i += 1
    return(indexlist)


def sort_abc(file_name):
    '''
    Sorts the games by title.
    Args:
        param1: a file name
    Returns:
        a list of strings
    '''
    printable_list = list(string.printable)

    first_letters = []
    second_letter = []
    third_letter = []

    titles = []

    for row in read_file(file_name):
        first_letters.append(row[0][0])
    for row in read_file(file_name):
        second_letter.append(row[0][1])
    for row in read_file(file_name):
        third_letter.append(row[0][2])
    for row in read_file(file_name):
        titles.append(row[0])

    indexlist1 = []
    indexlist2 = []
    indexlist3 = []

    for letter in first_letters:
        indexlist1.append(printable_list.index(letter))
    for letter in second_letter:
        indexlist2.append(printable_list.index(letter))
    for letter in third_letter:
        indexlist3.append(printable_list.index(letter))
    return [row[-1] for row in sort_list(list(zip(indexlist1, indexlist2, indexlist3, titles)))]


def get_genres(file_name):
    '''
    Find the genres in the file.
    Args:
        param1: a file name
    Returns:
        abc sorted list of the genres
    '''
    genres = []
    for i, game in enumerate(read_file(file_name)):
        genres.append(read_file(file_name)[i][3])  # 3 is for the genres
    return(sorted(set(genres), key=str.lower))  # "a" and "A" is different for sorted


def when_was_top_sold_fps(file_name):
    '''Finds the release date of the top sold "First-person shooter" game
    Args:
    param1: a file name
    Returns:
        an integer
    '''
    sold = []
    date = []
    if decide("game_stat.txt", "First-person shooter"):
        for i, game in enumerate(read_file(file_name)):
            if read_file(file_name)[i][3] == "First-person shooter":
                sold.append(read_file(file_name)[i][1])  # 1 is for nr.sold
                date.append(read_file(file_name)[i][2])  # 2 is for release_date
        mix = list(zip(sold, date))
        return int(sorted(mix, key=lambda x: x[0], reverse=True)[0][1])
    else:
        raise ValueError
