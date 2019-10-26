#  cli_utility
  
  
![GitHub](https://img.shields.io/github/license/bluewingtan/cli_utility ) ![GitHub pull requests](https://img.shields.io/github/issues-pr/bluewingtan/cli_utility ) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/bluewingtan/cli_utility/master ) ![Language](https://img.shields.io/badge/language-python-brightgreen ) ![Travis (.com) branch](https://img.shields.io/travis/com/bluewingtan/cli_utility/master ) [![Author](https://img.shields.io/badge/powered%20by-BlueWingTan-blue? )](https://github.com/bluewingtan)
  
> Cli_utility is a python module whitch provide a high-level API to generate an appealing colorful single/multiple selection menu and informational logging output. Cli-utility brings a new life to boring command-line menus and log output programming.
  
*What can I do?*
  
Most things that you can do with cli_utility module! Here are a few examples to get you started:
  
- Generate a single/multiple selection menu and get the result easily
- Logging messages with colorful `[+]` `[-]` `[!]` `[*]` symbol by using built-in functions
- Free logging output of custom foreground colors and meaningful symbols
- Using call chain to log messages
  
![Peek 2019-10-25 01-45](https://i.loli.net/2019/10/25/dJHh5wUZ8jupPlQ.gif )
  
Issues or pull requests are welcome.
  
##  Table of Contents
  
  
- [cli_utility](#cli_utility )
  - [Table of Contents](#table-of-contents )
  - [Features](#features )
  - [Getting Started](#getting-started )
    - [Installation](#installation )
    - [Usage](#usage )
  - [Dependences](#dependences )
  - [Change Log](#change-log )
  - [Alternatives](#alternatives )
  
##  Features
  
  
- Beautiful single/multiple selection menu with default value
- Highlight the selection line
- Standardized color log tools
- Highly customizable color log output
- Log tools supports chain call
- Support for all types of output supported by standard print functions
  
##  Getting Started
  
  
###  Installation
  
  
This module can be easily installed with `pip`:
  
```bash
pip install cli_utility
```
  
Or you can just use `git clone`:
  
```bash
git colne https://github.com/bluewingtan/cli_utility.git
```
  
###  Usage
  
  
**Example 1 - generate a single/multiple selection menu and get the result**
  
Use direction key `up`, `down` to move cursor. In single selection mode, use key `enter` to select and confirm. Comparatively, in multiple selection mode, use key `space` to select and key `enter` to confirm.
  
Here goes the single selection menu code:
  
***Code 1.1***
  
```python
import cli_utility
  
menu = cli_utility.cli_menu(False)
logger = cli_utility.output_manager()
  
choices = ['Haruhi Suzumiya', 'Yuki Nagato', 'Mikuru Asahina']
title = 'Who do you love?'
  
selected = menu.show(title, choices)
logger.print('Girls you selected:',
             fore_color=cli_utility.colorama.Fore.LIGHTCYAN_EX)
logger.print_success(choices[selected])
```
  
***Result 1.1***
  
![Peek 2019-10-25 01-29](https://i.loli.net/2019/10/25/Fo73ctIyPSqTzeJ.gif )
  
Here goes the multiple selection menu code:
  
***Code 1.2***
  
```python
import cli_utility
  
menu = cli_utility.cli_menu()
logger = cli_utility.output_manager()
  
choices = ['Haruhi Suzumiya', 'Yuki Nagato', 'Mikuru Asahina']
default_selection = [1]
title = 'Who do you love?'
  
selected = menu.show(title, choices, default_selection)
logger.print('Girls you selected:',
             fore_color=cli_utility.colorama.Fore.LIGHTCYAN_EX)
  
for index, choice in enumerate(choices):
    if index in selected:
        logger.print_success(choices[index])
```
  
***Result 1.2***
  
![Peek 2019-10-25 01-45](https://i.loli.net/2019/10/25/dJHh5wUZ8jupPlQ.gif )
  
**Example 2 - logging messages with colorful symbol**
  
Here goes the code:
  
***Code 2.1***
  
```python
import cli_utility
  
logger = cli_utility.output_manager()
  
logger.print('What if you woke up one morning')
logger.print('and everything changed?')
logger.print_success('Yuki Nagato')
logger.print_error('Haruhi Suzumiya')
logger.print_info('Mikuru Asahina')
logger.print_warn('Itsuki Koizumi')
```
  
***Result 2.1***
  
![2019-10-25_02-29](https://i.loli.net/2019/10/25/t9x6z7EuGDVPKoj.png )
  
**Example 3 - free logging output of custom foreground colors and meaningful symbols**
  
Here goes the code:
  
***Code 3.1***
  
```python
import cli_utility
  
logger = cli_utility.output_manager()
  
Kyon1 = logger.print_string_constructor(
    'What if you woke up one morning', 
    '[^] ',
    cli_utility.colorama.Fore.LIGHTGREEN_EX, 
    cli_utility.colorama.Fore.LIGHTBLUE_EX)
Kyon2 = logger.print_string_constructor(
    'and everything changed?',
    '[%] ',
    cli_utility.colorama.Fore.LIGHTRED_EX,
    cli_utility.colorama.Fore.RED)
  
logger.print(Kyon1)
logger.print(Kyon2)
logger.print_success('Yuki Nagato')
logger.print_error('Haruhi Suzumiya')
logger.print_info('Mikuru Asahina')
logger.print_warn('Itsuki Koizumi')
```
  
***Result 3.1***
  
![2019-10-25_17-44](https://i.loli.net/2019/10/25/qEaYZWJTui6fcD3.png )
  
**Example 4 - using call chain to log messages**
  
Here goes the code:
  
***Code 4.1***
  
```python
import cli_utility
  
logger = cli_utility.output_manager()
  
Kyon1 = logger.print_string_constructor(
    'What if you woke up one morning', 
    '[^] ',
    cli_utility.colorama.Fore.LIGHTGREEN_EX, 
    cli_utility.colorama.Fore.LIGHTBLUE_EX)
Kyon2 = logger.print_string_constructor(
    'and everything changed?',
    '[%] ',
    cli_utility.colorama.Fore.LIGHTRED_EX,
    cli_utility.colorama.Fore.RED)
  
logger.print(Kyon1)\
    .print(Kyon2)\
    .print_success('Yuki Nagato')\
    .print_error('Haruhi Suzumiya')\
    .print_info('Mikuru Asahina')\
    .print_warn('Itsuki Koizumi')
```
  
***Result 3.1***
  
![2019-10-25_17-44](https://i.loli.net/2019/10/25/qEaYZWJTui6fcD3.png )
  
##  Dependences
  
  
Cli_utility depend on [colorama](https://pypi.org/project/colorama/ ) version 0.4.1 and above version.
  
##  Change Log
  
  
version | simple description
--|--
1.0.0| Initial repo
  
##  Alternatives
  
  
[tty_menu](https://github.com/gojuukaze/tty_menu ) - python terminal memu (一个快速创建命令行菜单的工具) 
  
  