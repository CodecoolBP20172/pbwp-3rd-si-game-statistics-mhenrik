
# Report functions
import csv
import string

def read_file(file_name, title = None):  # reads an external file
    '''
    Argument: a file name
    Returns: a list
    '''
    with open(file_name, newline = "\n") as file:
        reader = csv.reader(file, delimiter = "\t")
        data = []
        for row in reader:
            #row = [title, number_sold, release_date, genre, publisher]
            title = 0
            number_sold = 1
            release_date = 2
            genre = 3
            publisher = 4
            data.append([row[title], float(row[number_sold]), row[release_date], row[genre], row[publisher]])
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


def get_latest(file_name):
    '''
    Finds the title of the latest game
    Argument: a file name
    Returns: the title of the game as a string
    '''
    #row = [title, number_sold, release_date, genre, publisher]
    years = []
    title = []
    for i, game in enumerate(read_file(file_name)):
        years.append(read_file(file_name)[i][2])
        title.append(read_file(file_name)[i][0])
    mix = list(zip(years,title))
    return(sorted(mix, key = lambda x: x[0], reverse = True)[0][1])


def count_by_genre(file_name, genre):
    '''
    Counts the games by the given genre.
    Arguments: a file name and a genre
    Returns: an integer
    '''
    genres = []
    for i, game in enumerate(read_file(file_name)):
        genres.append(read_file(file_name)[i][3])
    return(genres.count(genre))


def line_number_by_title(file_name, title):
    try:
        return([title in game for game in read_file(file_name)].index(True)+1)
    except BaseException:
        raise ValueError


def sort_list(indexlist):
    i = 1
    while i < len(indexlist):
        j = 0
        while j <= len(indexlist) -2 :
            if indexlist[j] > indexlist[j+1]:
                temp = indexlist[j+1]
                indexlist[j+1] = indexlist[j]
                indexlist[j] = temp
                j = j + 1
            else:
                j = j+1
        i = i +1
    return(indexlist)

def sort_abc(file_name):
    '''
    Sorts the games by title.
    Argument: a file name
    Returns: a list of strings
    '''

    lower_list = list(string.printable)
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
        indexlist1.append(lower_list.index(letter))
    for letter in second_letter:
        indexlist2.append(lower_list.index(letter))
    for letter in third_letter:
        indexlist3.append(lower_list.index(letter))

    mix = list(zip(indexlist1, indexlist2, indexlist3, titles))
    a = sort_list(mix)
    b = [row[-1] for row in a]
    print(b)

sort_abc("game_stat.txt")

def get_genres(file_name):
    '''
    Find the genres in the file.
    Argument: a file name
    Returns: abc sorted list of the genres
    '''
    genres = []
    for i, game in enumerate(read_file(file_name)):
        genres.append(read_file(file_name)[i][3])
    return(sorted(set(genres)))


def when_was_top_sold_fps(file_name):
    '''Finds the release date of the top sold "First-person shooter" game
    Argument: a file name
    Returns: an integer
    '''
    sold = []
    date = []
    if decide("game_stat.txt", "First-person shooter"):
        for i, game in enumerate(read_file(file_name)):
            if read_file(file_name)[i][3] == "First-person shooter":
                sold.append(read_file(file_name)[i][1])
                date.append(read_file(file_name)[i][2])
        mix = list(zip(sold,date))
        return sorted(mix, key = lambda x: x[0], reverse = True)[0][1]
    else:
        raise ValueError
