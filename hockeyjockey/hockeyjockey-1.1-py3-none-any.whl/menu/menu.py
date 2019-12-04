"""
Hockey Jockey main menu module.
"""
from os import system, name
import hockeyjockey as hj
import hockeyjockey.config as cfg
import hockeyjockey.utilities as ut


class Menu(object):
    """
    Menu class defines functions for displaying menus and handling user input. For the most part, menu does not handle
    any of the 'business logic'. It is for presentation of menus and prompts to the user throughout the life of a
    hockeyjockey instance.
    """

    def __init__(self, title: str, subtitle: str, opts: list, prompt_str:str) -> None:
        """
        Initializes a hockeyjockey menu. After the title and subtitle are displayed, a list of menu options is formed
        from the data in the opts argument. The dictionaries in the opts list provide the menu option title and payload
        (a function to execute, or a link to another menu). _prev and _prev_idx are used to point to the 'previous'
        menu. When another menu links to an instance of Menu, a final option is appended to the menu that allows the
        user to return to the previous menu.

        :param title: Menu title (string).
        :param subtitle: Menu subtitle (string).
        :param opts: A list of menu option dictionaries.
        :param prompt_str: Prompt to user (i.e. 'Please choose an option').
        """
        self.title = title
        self.subtitle = subtitle
        self.opts = opts
        self.prompt_str = prompt_str

        self._prev = None
        self._prev_idx = None

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value: 'Menu') -> None:
        """
        Stores the previous Menu object and its index number.

        :param value: The previous Menu object.
        :return: None.
        """
        self._prev = value
        self._prev_idx = len(self.opts)

    def __str__(self) -> str:
        """
        Returns a string representation of a Menu instance (i.e. displays the menu to the user).

        :return: A string representation of a Menu instance.
        """
        # Menu title and subtitle
        menu_str = f'\n{self.title}\n{self.subtitle}\n'

        # Append the menu options
        for i, opt in enumerate(self.opts, 1):
            menu_str += f'{i}. {opt["name"]}\n'

        # Append a 'return to previous menu option' if there was a previous menu
        if self._prev:
            menu_str += str(self._prev_idx + 1) + '. Return\n'

        return menu_str

    def prompt(self) -> None:
        """
        Prompts the user to enter a choice from the displayed menu. Loops until user enters a valid menu option. The
        verbiage of the prompt is provided by the prompt_str attribute.

        :return: None.
        """
        choice = None
        try:
            # Convert choice to integer and make it zero-based
            choice = int(input(self.prompt_str)) - 1
        except ValueError:
            self.choice_invalid()

        # Execute choice, display previous menu, or invalid choice
        if choice in range(len(self.opts)):
            self.execute(choice)
        elif self._prev and choice == self._prev_idx:
            self._prev.display_menu()
        else:
            self.choice_invalid()

    def choice_invalid(self) -> None:
        """
        Displays a message to the user if they enter an invalid menu choice. Pauses for an 'any key' press, and then
        displays the last menu.

        :return: None.
        """
        input('Invalid choice.  Press any key to continue... ')
        self.display_menu()

    def payload_director(self, fn) -> callable:
        """
        Returns a closure that encapsulates the information required to execute certain Jockey functions. Allows
        a Menu instance or class function to run before executing a Jockey function (i.e to prompt the user to enter a
        start and end date). Also allows the Jockey instance to pass information back to the Menu instance (i.e.
        a list of valid statistics that the user can choose from). The intent behind this is to separate the 'business
        logic' of Jockey from the user interface of Menu.

        :param fn: The Jockey function to execute.
        :return: The return value(s) of the executed function, or None, depending on the requirements.
        """

        def inner():
            if fn.__name__ == hj.Jockey.load_custom_games.__name__:
                return fn(*self.prompt_for_dates())
            elif fn.__name__ == hj.Jockey.rank_stat_menu_call.__name__:
                stat_keys, comp_func, rank_func, print_func = fn()
                s_idx = self.prompt_for_stat(stat_keys)
                comp_func()
                # rank all
                rank_func()
                # print single stat
                print_func(stat_idx=s_idx)
            else:
                # Default behaviour
                fn()

        return inner

    def execute(self, choice: int) -> None:
        """
        Executes the Menu option chosen by the user. The 'payload' to be executed could be a function or another Menu.
        If the payload is a Menu (i.e. a submenu to 'navigate' to) then display_menu is called on that Menu object.
        display_menu can be called in a way that sets a return path to the current menu (by supplying update_prev=True),
        or, by omitting this argument, the current menu can be re-displayed without changing the return path.

        :param choice: An integer representing the Menu option to execute.
        :return: None.
        """
        payload = self.opts[choice]['payload']
        if isinstance(payload, Menu):
            # The payload is a Menu, so update_prev tells the new menu to save a return path
            # to the current menu
            payload.display_menu(prev=self, update_prev=True)
        else:
            # The payload is a function to execute. payload_director returns a closure that knows how to
            # handle different functions
            payload = self.payload_director(payload)
            payload()
            # Give user a chance to read the output
            input('Press any key to continue...')
            # Re-display the menu and keep the current return path
            self.display_menu()

    def display_menu(self, prev: 'Menu' = None, update_prev: bool = False) -> None:
        """
        Clears the screen and displays the menu. If update_prev is set to True, stores a return path to the 'previous'
        menu. update_prev=True has the effect of the new menu having a final menu option, allowing navigation to the
        previously displayed menu.  Omitting update_prev will leave the current return path in place, useful for when
        you want to redisplay the 'current' menu without changing its previous menu.

        :param prev: The Menu instance that called this one.
        :param update_prev: A boolean that determines whether the return path to the previous Menu should be updated
        before displaying the Menu.
        :return: None.
        """
        # Setup a return path to the previous menu
        if prev and update_prev:
            self.prev = prev

        self.clear()
        print(self)
        self.prompt()

    @staticmethod
    def prompt_for_cached() -> tuple:
        """
        Prompts the user as to whether or not they would like to use Games or Stats data loaded to local disk. The
        alternative is to download new data from the internet (statsapi). One use case for loading data from disk would
        be if the user was conducting many analyses in one day and wanted to save time loading data. In most other
        cases it would make sense to download fresh data, as the stats are changing on a daily basis.
        Note: If the prompt_for_cached prompt is annoying on startup, it can be suppressed by providing the
        suppress_prompt=True keyword argument when instantiating Jockey.  In this configuration, the answers to the
        prompt_for_cache questions can automatically be entered by specifying their boolean values in
        hockeyjockey/config.py in the suppress namedtuple.

        :return: A tuple of booleans indicating the response to both questions.
        """
        Menu.clear()

        print('If you have previously run HockeyJockey, some data may have been cached to disk.')
        print('You can elect to use that data, or download new data from the internet.')
        print()
        m_choice = input(
            'Type \'Y\' to use last MATCHUPS loaded to disk, any other key to reload from internet: ').lower()
        s_choice = input('Type \'Y\' to use last STATS loaded to disk, any other key to reload from internet: ').lower()

        m_choice = m_choice == 'y'
        s_choice = s_choice == 'y'

        return m_choice, s_choice

    @staticmethod
    def prompt_for_dates() -> tuple:
        """
        Prompts the user to enter a start date and an end date.  Loops until a valid start date and end date have
        been entered. Dates must match the format supplied in hockeyjockey/config.py in the date namedtuple. At the time
        this docuementation was written, the date format is 'YYYY-MM-DD', which corresponds to the NHL Stats API. See
        https://gitlab.com/dword4/nhlapi for the API documentation.

        :return:  A tuple containing a string-formatted start date and end date.
        """

        def date_prompt(date_type: str) -> str:
            """
            Prompts the user to enter a date as specified by date_type. Loops until a valid date is provided.

            :param date_type: An string displayed in the date entry prompt. i.e. 'start date'.
            :return: A string-formatted date.
            """
            print()
            while True:
                date_str = input(f'Enter {date_type} date <{ut.DATE_STR}>: ')
                return ut.valid_date(date_str) or date_prompt(date_type)

        return date_prompt('start'), date_prompt('end')

    def prompt_for_stat(self, stat_keys: list) -> int:
        """
        Displays a list of statistics available for comparision and prompts the user to choose one. Loops until the
        user enters a valid stat. stat_keys are provided by a Jockey instance (see the Menu class' payload_director
        function to see the mechanism of how this is acheived).
        Displays the stats in a way that wraps the screen when the list of stats is too long. The desired screen width
        can be controlled with the hockeyjockey/config.py ts (TeamStatsPrintConfig) namedtuple, or a global screen
        width can be set at the top of the hockeyjockey/config.py file.

        :param stat_keys: A list of statistic key names provided by a Jockey instance.
        :return: The integer index of the stat.
        """
        print()

        key_wid = max(map(lambda x: len(x), stat_keys))
        idx_wid = 2
        acc_wid = 0
        stats_str = ''

        for i, f in enumerate(stat_keys):

            acc_wid += (idx_wid + 1 + key_wid + 1)
            if acc_wid >= cfg.ts.scr_wid:
                acc_wid = idx_wid + 1 + key_wid + 1
                stats_str += '\n'

            stats_str += f'{i:>{idx_wid + 1}}. {f:<{key_wid + 1}}'

        print(stats_str)
        print()
        choice = None
        while True:
            try:
                choice = int(input('Enter the number of the stat you wish to compare: '))
            except ValueError:
                self.choice_invalid()
            if choice in range(len(stat_keys)):
                return choice
            else:
                self.choice_invalid()

    @staticmethod
    def exit_() -> int:
        """
        Prints a goodbye message and exits the program with exit code 0.

        :return: int exit code 0.
        """
        print()
        print('Goodbye and good luck.')
        return exit(0)

    @staticmethod
    def clear() -> int:
        """
        Clears the screen. Should work in Windows or Linux.

        :return: int exit code 0.
        """
        if name == 'nt':
            return system('cls')
        else:
            return system('clear')
