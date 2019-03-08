import os
import cursor


def clear_screen():
    """
        Determines whether player is using windows or *nix machine, then issues appropriate clear screen command.
    :return: clear screen command.
    """
    os.system("cls" if os.name == "nt" else "clear")


class Main:
    # Hide the cursor and clear screen so we can have a blank canvas.
    cursor.hide()
    clear_screen()

    # Find out how large our canvas shall be.
    term = os.get_terminal_size()
    width = term.columns

    for i in range(0, (term.lines//2) - 1):
        print()

    print('|'.center(width))
    print('Ceci n\'est pas une pipe.'.center(width))

    exit = input()
    if exit:
        cursor.show()
        pass

if __name__ == '__main__':
    Main()