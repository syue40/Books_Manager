"""
Assignment 2: Cozy Library Manager

Sean Yue
A01228440
Set F
November 14, 2020
"""
import doctest


def open_file(filename):
    """Adds books from the text file as dictionaries into a tuple. Adds details for title and shelf to sets.

    This function will open the books text file and begin adding all book details into a dictionary, adding to
    a different key if there is a tab between book details. It will add title and shelf details into two separate
    sets for titles and shelves in preparation for the move function later.

    :param: a text file containing book contents
    :precondition: the function must be able to locate the file ie. in the same folder
    :postcondition: create 2 sets with titles, shelves, and add all the books into a tuple containing dictionaries
    :returns: tuple of all books stored as dictionaries, and 2 sets containing titles and shelves
  """
    grand_library = []  # tuple container for all book dictionaries
    book_titles = set()  # creates sets for titles and shelves to be used in search
    book_shelves = set()
    with open(filename, encoding='UTF-16') as file_object:
        book_criteria = file_object.readline()[:-1].split('\t')  # reads the first line, does not add to library
        for line in file_object:
            book_rows = line[:-1].split('\t')
            if len(book_rows) == 6:
                individual_book = {}
                book_titles.add(book_rows[1])
                book_shelves.add(book_rows[3])

                for index in range(6):
                    individual_book[book_criteria[index]] = book_rows[index]
                grand_library.append(individual_book)

    return grand_library, book_titles, book_shelves


def menu():
    """Validates the user choice to make sure it is a number from 1 to 8

    This function has one purpose: make sure the user enters valid criterion. If the user does not enter a value
    from 1 to 8 it will continue to ask the user until a correct input is entered. After Executing searches or moves
    the program will return here

    :param: N/A
    :precondition: user must enter a value between 1 and 8, or function will continue looping
    :postcondition: function stores the user choice as an integer
    :returns: the user's choice
    """
    response = input("\nPlease enter a value from 1 to 8 for the action you want to perform, or type 9 to return\
 to the the intro: ").strip()

    while response not in ['1', '2', '3', '4', '5', '6', '7', '8']:  # validates user input
        if response == '9':
            books()
        else:
            response = input("Invalid entry. Please try a valid input from 1 to 8, or type 9 to return to intro."
                             ).strip()

    user_choice = int(response)
    return user_choice


def determine_criteria(user_choice: int):
    """Takes the user choice from menu and makes an equivalent string

    This function will open the books text file and begin adding all book details into a dictionary, adding to
    a different key if there is a tab between book details. It will add title and shelf details into two separate
    sets for titles and shelves in preparation for the move function later.

    :param: a user choice between 1 and 8
    :precondition: The value inputted for user_choice must be between 1 or 8 or program will not work
    :postcondition: The program will return a string corresponding to the user_choice
    :returns: The value corresponding to user choice
    >>> determine_criteria(1)
    'Title'
    >>> determine_criteria(3)
    'Publisher'
    >>> determine_criteria(6)
    'Subject'
    """
    criterion = {1: 'Title', 2: 'Author', 3: 'Publisher', 4: 'Shelf', 5: 'Category', 6: 'Subject'}

    return criterion[user_choice]


def intro():
    """Introduction to the user. Provides instructions on how to use the program.

    Prints instructions to the user on which search criteria are available and which actions they can perform

    :param: N/A
    :precondition: N/A
    :postcondition: N/A
    :return: N/A


    >>> intro()
    <BLANKLINE>
    Hello, welcome to the your virtual library!
    Here are some instructions on how to use your library! You have the following options:
    <BLANKLINE>
    To search by title enter 1:
    To search by author enter 2:
    To search by publisher enter 3:
    To search by shelf enter 4:
    To search by category enter 5:
    To search by subject enter 6:
    <BLANKLINE>
    To move a book to a different shelf enter 7:
    <BLANKLINE>
    And to quit the program and save changes, press 8:
    <BLANKLINE>
    After you enter a number for your search criteria, please enter a keyword that you wish to search by.
    You can enter a full title, name, publisher etc. or a partial one if you're having trouble remembering!
    If you want to move a book, please search for the exact title of the book you wish to move!
    """
    print("\nHello, welcome to the your virtual library!")
    print("Here are some instructions on how to use your library! You have the following options:\n\n"
          "To search by title enter 1:\n"
          "To search by author enter 2:\n"
          "To search by publisher enter 3:\n"
          "To search by shelf enter 4:\n"
          "To search by category enter 5:\n"
          "To search by subject enter 6:\n\n"
          "To move a book to a different shelf enter 7:\n\n"
          "And to quit the program and save changes, press 8:\n")
    print("After you enter a number for your search criteria, please enter a keyword that you wish to search by.\n"
          "You can enter a full title, name, publisher etc. or a partial one if you're having trouble remembering!\n"
          "If you want to move a book, please search for the exact title of the book you wish to move!"
          "")


def move_books(grand_library, titles: set, shelves: set) -> None:
    """Allows the user to move a book with a specific title to a different shelf.

    This function is used for moving books. It will require the user to enter the EXACT title of the book to move or
    it will not be able to locate the title. If the book has duplicates, it will ask the user to select which copy to
    move, then ask which shelf the user wants to move the book to. If there is only one copy, the function will ask
    where to move the book to. There is a validation step to ensure that the user enters a valid shelf.

    :param: the tuple containing all books, the set containing titles and the set containing shelves
    :precondition: User must enter a valid title. If duplicate select a valid copy. And enter a valid shelf.
    :postcondition: The program will move that book to the new shelf.
    :returns: to the menu for more user options
    """
    book_to_move = input("Please enter the exact title of the book you wish to move: ").strip()
    if book_to_move not in titles:  # Makes sure that an exact title is entered by user
        print("That book title isn't in the library! Returning to menu...")
        return
    matches_list = get_book_matches(grand_library, 1, book_to_move)
    # matches_list here uses the search function to find titles matching the user's search in grand_library titles

    if len(matches_list) > 1:  # checks if the number of books that matches criteria is greater than 1
        matches_list = get_single_book_to_move(matches_list)  # if it is then we will move one of them

    book_to_move = matches_list[0]
    print(f"\nYour book is currently in shelf {book_to_move['Shelf']}!\n")

    shelf_to_move_to = input("What shelf do you want to move to? ").strip()
    if shelf_to_move_to not in shelves:
        print("That shelf isn't in the library! Returning to menu...")  # validates the user's shelf choice
        return
    for book in grand_library:
        if book == book_to_move:
            book['Shelf'] = shelf_to_move_to
            print("Book successfully moved! Returning to menu...")
            return


def get_single_book_to_move(matches_list: list):
    """Called when the matches list of books to move is greater than 1. User will select which copy to move.

    This function will print the user the copies of duplicate books. It will ask the user to select a copy of the book
    to move and then pass that copy back to the move books function.

    :param: matches list containing the books that have multiple copies
    :precondition: the user must select a choice from the list of duplicate books
    :postcondition: the function will take that choice and return it to the move books function
    :return: user's choice in matches list for the book to move
    """
    print("I found multiple copies of that book!")
    print_book_list(matches_list)  # uses print book function to show the user duplicate matches

    choice = ""
    while choice not in [str(i) for i in range(1, len(matches_list) + 1)]:  # user selects the choice of book to move
        choice = input("Which result number shall I move? ").strip()

    return [matches_list[int(choice) - 1]]  # returns the copy of the book the user selected


def get_book_matches(grand_library, book_criteria: int, user_keyword: str) -> list:
    """Creates an empty list and adds books that match the criteria to this list

    This function will find matches in grand library based on the user's search criteria and search keywords. It also
    checks in grand_library for books with no publisher value. It will then change that value to None. Then it will
    append all matches to a list and return that list.

    :param: grand_library tuple with all the books, the user's search criteria, and the search string they entered
    :precondition: grand_library must be locatable and in correct format, book criteria and user input must be valid
                    inputs
    :postcondition: function will change all empty values for publisher to 'None', then execute a search appending all
                    matches to a list
    :return: the matches list containing a list of dictionaries matching the search criteria

    >>> len(get_book_matches([{'Title' : 'Book1', 'Publisher' : 'Pub1'},\
    {'Title' : 'Book2', 'Publisher' : 'Pub2'}], 1,'Book1'))
    1

    >>> get_book_matches([{'Title' : 'Book1', 'Publisher' : 'Pub1'},\
    {'Title' : 'Book2', 'Publisher' : 'Pub2'}], 1, 'Book1')[0]['Title']
    'Book1'

    >>> len(get_book_matches([{'Title' : 'Book1', 'Publisher' : 'Pub1'},\
    {'Title' : 'Book2', 'Publisher' : 'Pub2'}], 3, 'Pub'))
    2

    >>> get_book_matches([{'Title' : 'Book1', 'Publisher' : 'Pub1'},\
    {'Title' : 'Book2', 'Publisher' : 'Pub2'}], 3, 'Pub1')[0]['Title']
    'Book1'

    >>> get_book_matches([{'Title' :  '1984', 'Author': 'George Orwell', 'Publisher' : 'Penguin Classics'},\
    {'Title' : 'Animal Farm', 'Author' : 'George Orwell', 'Publisher': 'Penguin Classics'}], 2, 'Orwell')[0]['Title']
    '1984'

    >>> get_book_matches([{'Title' :  '1984', 'Author': 'George Orwell', 'Publisher' : 'Penguin Classics'},\
    {'Title' : 'Animal Farm', 'Author' : 'George Orwell', 'Publisher': 'Penguin Classics'},\
    {'Title': 'Brave New World', 'Author': 'Aldous Huxley', 'Publisher': 'Penguin Classics'}], 2, 'Orwell')
    [{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'}, {'Title': 'Animal Farm', \
'Author': 'George Orwell', 'Publisher': 'Penguin Classics'}]

    >>> get_book_matches([{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},\
    {'Title': 'Animal Farm', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},\
    {'Title': 'Brave New World', 'Author': 'Aldous Huxley', 'Publisher': 'Penguin Classics'}], 1, 'zxy')
    []
    """
    matches_list = []
    criteria = determine_criteria(book_criteria)

    for book in grand_library:
        if book['Publisher'] == '':  # if the publisher is empty, then a value of None will be assigned
            book['Publisher'] = 'None'
        if criteria != 'Shelf':  # allows users to use partial search for anything BUT shelf
            if user_keyword in book[criteria]:
                matches_list.append(book)  # if search criteria using keyword found, add it to the matches list
        elif criteria == 'Shelf':  # shelves must be searched with exact shelf name7
            if user_keyword == book['Shelf']:
                matches_list.append(book)
    return matches_list


def search_the_library(grand_library, book_criteria: int, user_keyword: str):
    """Uses the matches list from get_book_matches to print the length of items, and the search completed lines

    This function was refactored from get_book_matches. Its purpose is to print out the number of books that match
    the user's search, then call the function print_book_list. Finally, it will tell the user that the search was
    completed and then return to the menu.

    :param: grand library tuple, matches list, user's search criteria, and the user's search keyword
    :precondition: must be passed a valid search from get_book_matches function
    :postcondition: will print the number of matches then call print_book_list to print the matches
    :return: N/A but will go back to menu after execution

    >>> grand_library = [{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',\
'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',\
'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',\
'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',\
'Category': 'Mathematics', 'Subject': 'Algebra'},\
{'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':\
'Iglauer', 'Publisher': 'University of Washington Press',\
'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}]\

    >>> search_the_library(grand_library, 1, 'Skyscrapers')
    <BLANKLINE>
    You have 0 item(s) that match your search criteria:
    <BLANKLINE>
    <BLANKLINE>
    Search Completed. Returning to menu...
    <BLANKLINE>
    """
    matches_list = get_book_matches(grand_library, book_criteria, user_keyword)
    print(f'\nYou have {len(matches_list)} item(s) that match your search criteria:\n')
    print_book_list(matches_list)
    print("\nSearch Completed. Returning to menu...\n")


def print_book_list(matches_list: list):
    """Uses f-strings to make the books found in the matches list look nice

    This function will take the matches list generated by the get_book_matches function and print it in a more
    readable way for the user. Note I tried to doctest this function but could not manage to get rid of the
    <BLANKLINE> error.

    :param: matches_list which contains the books that matches user's search criteria
    :precondition: in order to execute this function must be passed a non-empty matches list
    :postcondition: the function will print an enumerated list of matching results usint f-string formatting
    :return: N/A but will go back to menu
    """
    for number, book in enumerate(matches_list, start=1):
        print("#---------------------------------------#")
        print(f"\tResult: #{number}\n")
        print(f"\tTitle: {book['Title']}\n"
              f"\tAuthor: {book['Author']}\n"
              f"\tPublisher: {book['Publisher']}\n"
              f"\tShelf: {book['Shelf']}\n"
              f"\tCategory: {book['Category']}\n"
              f"\tSubject: {book['Subject']}")
        print("#---------------------------------------#")


def quit_books(grand_library, filename):
    """Quit books writes any edits we made to the library into a text file and overwrites the current one.

    Quit books opens the file we extracted information from and using 'w' the function writes the top line with the
    criteria and then adds the entire library we extracted to the text file. Any edits made to a book's location will
    show up in the new overwritten file.

    :param: the tuple containing book dictionaries
    :param: the text file to write to
    :precondition: must be able to locate Books UTF-16.txt and be passed a valid tuple of book dictionaries
    :postcondition: overwrites Books UTF-16.txt with any current contents of grand_library, including moved books
    :returns: N/A
    """

    with open(filename, 'w', encoding='UTF-16') as file_object:
        file_object.write('Author\tTitle\tPublisher\tShelf\tCategory\tSubject\n ')
        for final_books in grand_library:
            file_object.write(f"{final_books['Author']}\t"
                              f"{final_books['Title']}\t"
                              f"{final_books['Publisher']}\t"
                              f"{final_books['Shelf']}\t"
                              f"{final_books['Category']}\t"
                              f"{final_books['Subject']}")
            file_object.write('\n')
    print('Saved!')


def books():
    """Will take the user choice for action and execute the function that performs the specific action.

    This function serves as the main console for the program. If the user enters 8 the program will perform the quit
    function then break. If the user enters 7 the move books function will be called. And if the user enters anything
    else from 1-7 it will attempt to perform a search using the criteria. The menu function will be used to validate
    whether or not the search function can proceed.

    :param: N/A
    :precondition: N/A
    :postcondition: Depending on the user's choice this function will call the corresponding function.
    :returns: N/A
    """
    user_option = None
    filename = 'Books UTF-16.txt'
    intro()  # prints instructions for the user
    library, titles, shelves = open_file(filename)  # initializes the text file and creates sets for titles, shelves
    while user_option != 8:
        user_option = menu()  # brings up the menu
        if user_option == 8:
            quit_books(library, filename)  # if user uses quit, it will overwrite the file and break
            quit()
        if user_option == 7:
            print("You selected move books.")
            move_books(library, titles, shelves)
        else:
            search_term = input(f'You selected search by {determine_criteria(user_option).lower()}.\
 Please enter your search keyword: ').strip()  # asks the user for their search
            search_the_library(library, user_option, search_term)  # calls the search function


def main():
    """
    Drives the program.
    """
    books()


if __name__ == '__main__':
    main()
    doctest.testmod()
