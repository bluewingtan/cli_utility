'''
DESCRIPTION: A simple multiple CLI menu and print utility
FILE: cli_utility.py
PROJECT: Utility
CREATED DATE: 2019-10-23
AUTHOR: BlueWingTan
LAST MODIFIED: 2019-10-25
MODIFIED BY: the developer formerly known as BlueWingTan

Copyright (c) 2019 STG

-----
HISTORY:
2019-10-24	BW  V1.0.0 released
'''


import sys
import termios
import tty

import colorama


class output_manager(object):
    """
    Print color indicator before objects, support call chain  
    """

    def __init__(self):
        colorama.init()

    def print_success(self, *values: object, condition: bool = True, fore_color: int = colorama.Fore.RESET, **kwargs):
        """
        Print green '[+]' before objects with foreground color  

        Parameters:  
        values - object to print  
        fore_color - colorama foreground color  
        kwargs - other parameter print support, like sep etc.
        """
        if condition:
            condition = None
            return self._print_symbol(
                *values, symbol='[+] ', symbol_color=colorama.Fore.GREEN, fore_color=fore_color, **kwargs)

    def print_error(self, *values: object, condition: bool = True, fore_color: int = colorama.Fore.RESET, **kwargs):
        """
        Print red '[-]' before objects with foreground color  

        Parameters:  
        values - object to print  
        fore_color - colorama foreground color  
        kwargs - other parameter print support, like sep etc.
        """
        if condition:
            return self._print_symbol(
                *values, symbol='[-] ', symbol_color=colorama.Fore.RED, fore_color=fore_color, **kwargs)

    def print_warn(self, *values: object, condition: bool = True, fore_color: int = colorama.Fore.RESET, **kwargs):
        """
        Print yellow '[!]' before objects with foreground color  

        Parameters:  
        values - object to print  
        fore_color - colorama foreground color  
        kwargs - other parameter print support, like sep etc.
        """
        if condition:
            return self._print_symbol(
                *values, symbol='[!] ', symbol_color=colorama.Fore.YELLOW, fore_color=fore_color, **kwargs)

    def print_info(self, *values: object, condition: bool = True, fore_color: int = colorama.Fore.RESET,  **kwargs):
        """
        Print blue '[*]' before objects with foreground color  

        Parameters:  
        values - object to print  
        fore_color - colorama foreground color  
        kwargs - other parameter print support, like sep etc.
        """
        if condition:
            return self._print_symbol(
                *values, symbol='[*] ', symbol_color=colorama.Fore.BLUE, fore_color=fore_color, **kwargs)

    def print(self, *values: object, condition: bool = True, fore_color: int = colorama.Fore.RESET, **kwargs):
        """
        Print wrapper with foreground color  

        Parameters:  
        values - object to print  
        fore_color - colorama foreground color  
        kwargs - other parameter print support, like sep etc.
        """
        if condition:
            print(fore_color, end='')
            print(*values, colorama.Fore.RESET, **kwargs)
            return self

    def print_string_constructor(self, message: object, symbol=None, symbol_color: int = colorama.Fore.RESET, fore_color: int = colorama.Fore.RESET):
        """
        Construct print string with colored symbols  

        Parameters:  
        message - message to print  
        symbol - symbol to print  
        symbol_color - symbol color  
        fore_color - colorama foreground color  
        """
        return symbol_color + symbol + colorama.Fore.RESET + fore_color + str(message) + colorama.Fore.RESET

    def _print_symbol(self, *values: object, symbol=None, symbol_color: int = colorama.Fore.RESET, fore_color: int = colorama.Fore.RESET, **kwargs):
        """
        [PRIVATE FUNCTION]  
        Print colored symbo before objects with foreground color  

        Parameters:  
        values - object to print  
        symbol - symbol to print  
        symbol_color - symbol color  
        fore_color - colorama foreground color  
        kwargs - other parameter print support, like sep etc.
        """
        for value in values:
            print(self.print_string_constructor(
                value, symbol, symbol_color, fore_color), **kwargs)
        return self


class cli_menu(object):
    """
    The menu that support single and multiple selection   

    Parameters:  
    multiple - whether the menu are multiple selection or not
    """

    def __init__(self, multiple: bool = True):
        """
        Define constant of keyboard   
        """
        self.key_ctrl_c = '\x03'
        self.key_direction_prefix = '\x1b'
        self.key_direction_up = '\x1b[A'
        self.key_direction_down = '\x1b[B'
        self.key_space = '\x20'
        self.key_enter = '\r'
        self.selector_selected_multiple = '[*] '
        self.selector_selected_multiple_placeholder = '[ ] '
        self.selector_selected_single = ' >  '
        self.selector_selected_single_placeholder = '    '
        self.selector_newline = '\n'
        self.multiple = multiple
        self.selection_finish_position = -1
        colorama.init()

    def _rendering_menu(self, choices: list, selected: list, position: int):
        """
        [PRIVATE FUNCTION]  
        Rendering menu with default choices  

        Parameters:  
        choices - choices list  
        selected - default choices list index in choices list  
        position - now pointer position
        """
        if position not in range(len(choices)) and position != self.selection_finish_position:
            raise IndexError

        if not self.multiple:
            selected.clear()

        render_string = ''

        selector_selected_not_position = self.selector_selected_single
        selector_selected_position = colorama.Style.BRIGHT + \
            colorama.Fore.GREEN + self.selector_selected_single
        selector_not_selected_not_position = self.selector_selected_single_placeholder
        selector_not_selected_position = selector_selected_position

        if self.multiple:
            selector_selected_not_position = colorama.Fore.GREEN + \
                self.selector_selected_multiple
            selector_selected_position = colorama.Style.BRIGHT + \
                colorama.Fore.BLUE + self.selector_selected_multiple
            selector_not_selected_not_position = self.selector_selected_multiple_placeholder
            selector_not_selected_position = colorama.Style.BRIGHT + \
                colorama.Fore.BLUE + self.selector_selected_multiple_placeholder

        selector_selected_end_not_position = colorama.Fore.RESET + self.selector_newline
        selector_selected_end_position = colorama.Fore.RESET + \
            colorama.Style.RESET_ALL + self.selector_newline

        for index, choice in enumerate(choices):
            # formal selected
            if index in selected:
                # pointer not on index pointed entry
                if position != index:
                    selector = selector_selected_not_position
                # pointer on index pointed entry
                else:
                    selector = selector_selected_position
            # not selected
            else:
                # pointer not on index pointed entry
                if position != index:
                    selector = selector_not_selected_not_position
                # pointer on index pointed entry
                else:
                    selector = selector_not_selected_position

            if position != index:
                selector += choice + selector_selected_end_not_position
            else:
                selector += choice + selector_selected_end_position

            render_string += selector

        sys.stdout.write(render_string)
        sys.stdout.flush()

    def _get_input(self):
        """
        [PRIVATE FUNCTION]  
        Get user's input  
        """
        ch = sys.stdin.read(1)
        if ch == self.key_direction_prefix:
            ch += sys.stdin.read(2)
        return ch

    def _clear_menu_item(self, item_number: int):
        """
        [PRIVATE FUNCTION]  
        Clear menu iteams except the tile  

        NOTE:  
        \033[nA cursor Move Up n line  
        \033[K  clear the contentfrom cursor to the end of the line  
        """
        sys.stdout.write('\033[{}A\033[K'.format(item_number))
        sys.stdout.flush()

    def show(self, title: str, choices: list, selected: list = []):
        """
        Show menu

        Parameters:  
        title - title of the menu  
        choices - choices list  
        selected - [optional] default choices list index in choices list  

        NOTE:  
        In multiple selection mode, `Ctrl+C` is determination of select,
        `Enter` to select the pointed item;
        In single selection mode, `Ctrl+C` is the signal of abort,
        `Enter` is determination of select.
        """
        position = 0

        if not selected:
            selected = []

        sys.stdout.write(title + '\n')
        sys.stdout.flush()

        self._rendering_menu(choices, selected, position)

        while True:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = self._get_input()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            if key == self.key_ctrl_c:
                break
            elif key == self.key_enter:
                if self.multiple:
                    self._clear_menu_item(len(choices))
                    self._rendering_menu(
                        choices, selected, self.selection_finish_position)
                    return selected
                else:
                    return position
            elif key == self.key_space:
                if self.multiple:
                    if position in selected:
                        selected.remove(position)
                    else:
                        selected.append(position)
            elif key == self.key_direction_up:
                position -= 1
            elif key == self.key_direction_down:
                position += 1

            # range fix
            if position < 0:
                position = len(choices) - 1
            elif position >= len(choices):
                position = 0

            self._clear_menu_item(len(choices))
            self._rendering_menu(choices, selected, position)
