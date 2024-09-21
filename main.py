class NLPApp:
    """
    A class to represent an NLP application that offers user registration, login, and various NLP functionalities 
    such as Named Entity Recognition (NER), Language Detection, and Sentiment Analysis.

    Attributes
    ----------
    __database : dict
        A private dictionary to store user data (email, name, password).

    Methods
    -------
    __init__():
        Initializes the NLPApp object and starts the new user menu.
    __new_user_menu():
        Displays the menu for new users, offering options to login, register, or exit.
    __login():
        Handles user login by checking credentials from the database.
    __register():
        Handles user registration and stores the data in the database.
    __logged_in_menu():
        Displays the options for logged-in users to perform various NLP tasks.
    __ner():
        Performs Named Entity Recognition (NER) using NLP Cloud API.
    __lang_detection():
        Detects the language of a given paragraph using NLP Cloud API.
    __sentiment_analysis():
        Analyzes the sentiment of a given comment using NLP Cloud API.
    """

    API_KEY = "PASTE YOUR API KEY HERE"

    def __init__(self) -> None:
        """
        Initializes the NLPApp class with an empty user database and triggers the new user menu.
        """
        self.__database = {}
        self.__new_user_menu()

    def __new_user_menu(self) -> None:
        """
        Displays a menu for new users, providing options to login, register, or exit the application.
        
        Prompts the user to input their choice and proceeds with the respective action.
        """
        inp = int(input("""
                    1. Already a user? Login
                    2. New User? Register
                    3. Exit
                    Enter your choice : """))
        
        if inp == 1:
            self.__login()
        elif inp == 2:
            self.__register()
        else:
            exit(0)

    def __login(self) -> None:
        """
        Prompts the user for login credentials (email and password) and verifies them against the database.

        If successful, the user is logged in and the logged-in menu is displayed. 
        If unsuccessful, the user is prompted to re-enter the credentials or register.
        """
        print('LOGIN'.center(51, '-'))
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        
        if email in self.__database:
            if password == self.__database[email][1]:
                print('Welcome {} :)'.format(self.__database[email][0]))
            else:
                print('Wrong Password :( Eat Almonds ;)')
                self.__login()
        else:
            print('You are not registered with us :( Please register...')
            self.__register()

        self.__logged_in_menu()

    def __register(self) -> None:
        """
        Handles user registration by taking name, email, and password as input and storing them in the database.
        
        If the user is already registered, it prompts them to login instead.
        After successful registration, it proceeds to login.
        """
        print('REGISTRATION'.center(50, '-'))
        name = input('Enter your name : ')
        email = input('Enter your email : ')
        password = input('Enter password : ')
        
        if email not in self.__database:
            self.__database[email] = [name, password]
            print('Registration Successful :)')
        else:
            print('You are already registered with us :) Please Login...')

        self.__login()

    def __logged_in_menu(self) -> None:
        """
        Displays the menu for logged-in users, allowing them to choose between different NLP functionalities.

        Prompts the user for input and calls the appropriate NLP method.
        """
        inp = int(input("""
                    What would you like to do?
                    1. NER (Entity Extraction)
                    2. Language Detection
                    3. Sentiment Analysis
                    4. Logout
                    Enter your choice : """))
        
        if inp == 1:
            self.__ner()
        elif inp == 2:
            self.__lang_detection()
        elif inp == 3:
            self.__sentiment_analysis()
        else:
            pass

    def __ner(self) -> None:
        """
        Performs Named Entity Recognition (NER) using NLP Cloud's API.

        Prompts the user for a paragraph and the entity they want to search for, then displays the extracted entities.

        Uses
        ----
        nlpcloud.Client : NLP Cloud API client for NER.
        pandas.DataFrame : Used to format the output for better visualization.
        """
        print('NER'.center(51, '-'))

        text = input('Enter paragraph : ')
        searched_entity = input('Which entity do you want to search in paragraph : ')

        import nlpcloud
        client = nlpcloud.Client("finetuned-llama-3-70b", NLPApp.API_KEY, gpu=True)
        output = client.entities(text = text, searched_entity = searched_entity)

        import pandas as pd
        output = pd.DataFrame(output['entities'])
        print(output)

    def __lang_detection(self) -> None:
        """
        Detects the language of a given paragraph using NLP Cloud's API.

        Prompts the user to input a paragraph, and then displays the detected languages with their scores.

        Uses
        ----
        nlpcloud.Client : NLP Cloud API client for language detection.
        pandas.DataFrame : Used to format the output for better visualization.
        """
        paragraph = input('Enter a paragraph : ')
        
        import nlpcloud
        client = nlpcloud.Client("python-langdetect", NLPApp.API_KEY, gpu=False)
        response = client.langdetection(paragraph)

        import pandas as pd
        data = pd.DataFrame(response['languages'])
        print(data)

    def __sentiment_analysis(self) -> None:
        """
        Performs sentiment analysis on a given comment using NLP Cloud's API.

        Prompts the user to input a comment, and then displays the sentiment scores.

        Uses
        ----
        nlpcloud.Client : NLP Cloud API client for sentiment analysis.
        pandas.DataFrame : Used to format the output for better visualization.
        """
        comment = input('Enter a comment : ')

        import nlpcloud
        client = nlpcloud.Client("distilbert-base-uncased-emotion", NLPApp.API_KEY, gpu=False)
        response = client.sentiment(comment)

        import pandas as pd
        data = pd.DataFrame(response['scored_labels'])
        print(data)


        
# Before running the code, make sure to get your API Key from NLPCloud and,
# Paste it in the variable API_KEY in NLPApp class.
        
# Driver Code
user = NLPApp()