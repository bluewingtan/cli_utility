import cli_utility

logger = cli_utility.output_manager()

Kyon1 = logger.print_string_constructor(
    'What if you woke up one morning', '[^] ', cli_utility.colorama.Fore.LIGHTGREEN_EX, cli_utility.colorama.Fore.LIGHTBLUE_EX)
Kyon2 = logger.print_string_constructor(
    'and everything changed?', '[%] ', cli_utility.colorama.Fore.LIGHTRED_EX, cli_utility.colorama.Fore.RED)

logger.print(Kyon1)\
    .print(Kyon2)\
    .print_success('Yuki Nagato')\
    .print_error('Haruhi Suzumiya')\
    .print_info('Mikuru Asahina')\
    .print_warn('Itsuki Koizumi')
