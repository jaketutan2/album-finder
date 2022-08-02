# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import random
import sys

def print_text():
    iteration = 0;

    print('\n\n')
    # pause = ('spotify pause')
    # os.system(str(pause))
    # Use a breakpoint in the code line below to debug your script.
    print(f'\n\n\n-----------------------------------------------------------')
    print(f'Press X to Exit')
    print(f'-----------------------------------------------------------')
    print(f'\n\tPress ENTER to Generate Random Album')
    print(f'\n\t\t\tOR ')
    print( f'\n\t\tFind Album by Decade')
    print(f'\n\t1 - 1950s | 2 - 1960s | 3 - 1970s | 4 - 1980s')
    print( f'\t5 - 1990s | 6 - 2000s | 7 - 2010s | 8 - 2020s')
    print(f'-----------------------------------------------------------\n\n\n')

def read_input():
    keystroke = str(input())  # Press Ctrl+F8 to toggle the breakpoint.
    if keystroke == '1':
        x = '5'
    elif keystroke == '2':
        x = '6'
    elif keystroke == '3':
        x = '7'
    elif keystroke == '4':
        x = '8'
    elif keystroke == '5':
        x = '9'
    elif keystroke == '6':
        x = '0'
    elif keystroke == '7':
        x = '1'
    elif keystroke == '8':
        x = '2'
    elif keystroke.lower() == 'x':
        exit()
    else:
        x = 'all'
    return x

def get_data_frame():
    import pandas as pd

    data = pd.read_csv(r'C:\Users\jrt15\PycharmProjects\album-finder\AOTYdata.csv')
    return pd.DataFrame(data)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def find_album(data_frame, iteration):
    max_index = len(data_frame.index)
    index = random.randint(1, max_index);
    album_iterator = 0
    x = read_input()
    if x == 'all':
        print('\t')
        print(*data_frame.iloc[index, 0:4], sep='\n')
    else:
        while album_iterator < max_index:
            index = random.randint(1, max_index - 1)
            year = str(data_frame.iloc[index, 2])
            decade = year[2:3]
            if decade == x:
                print('\t')
                print(*data_frame.iloc[index, 0:4], sep='\n')
                break
            album_iterator += 1
    print(f'\n\n\n-------------------------------------------------------------')
    play_spotify(index, iteration, data_frame)

def play_spotify(index, iteration, data_frame):
    print('\n\n')
    album = str(data_frame.iloc[index, 1])
    artist = str(data_frame.iloc[index, 0])
    if iteration == 1:
        print(f'\nENTER "y"')
        os.system(str('spotify queue --album ' + album + ' ' + artist))
        os.system(str('spotify next'))
    else:
        os.system(str('spotify queue --album ' + album + ' ' + artist))

    print(f'\n\n\nITERATION ' + str(iteration))

def generate_albums(iteration):
    print_text()
    df = get_data_frame()
    find_album(df, iteration)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i = 1
    while i < 10:
        generate_albums(i)
        i = i + 1


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
