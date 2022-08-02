# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os


def print_hi(name):
    print('\n\n')
    pause = ('spotify pause')
    os.system(str(pause))
    # Use a breakpoint in the code line below to debug your script.
    print(f'\n\n\n-----------------------------------------------------------')
    print(f'\tPress ENTER to Generate Random Album')
    print(f'\n\t\t\tOR ')
    print( f'\n\t\tFind Album by Decade')
    print(f'\n\t1 - 1950s | 2 - 1960s | 3 - 1970s | 4 - 1980s')
    print( f'\t5 - 1990s | 6 - 2000s | 7 - 2010s | 8 - 2020s')
    print(f'\n\tPress "B" for no Jazz or Bob Dylan')
    print(f'-----------------------------------------------------------\n\n\n')

    keystroke = str(input())# Press Ctrl+F8 to toggle the breakpoint.
    if keystroke == '1':
        x = '5'
    elif keystroke == '2':
        x = '6'
    elif keystroke == '3':
        x = '7'
    elif keystroke == '4':
        x = '8'
    elif keystroke == '5':
        x= '9'
    elif keystroke == '6':
        x = '0'
    elif keystroke == '7':
        x = '1'
    elif keystroke == '8':
        x = '2'
    else:
        x = 'all'
    import pandas as pd
    import random

    data = pd.read_csv (r'C:\Users\jrt15\PycharmProjects\album-finder\AOTYdata.csv')
    df = pd.DataFrame(data)

    # Get Index
    maxIndex = len(df.index)
    index = random.randint(1, maxIndex)

    i = 0
    if x == 'all':
        print('\t')
        print(*df.iloc[index, 0:4], sep='\n')
    else:
        while i < maxIndex:
            index = random.randint(1, maxIndex - 1)
            year = str(df.iloc[index, 2])
            decade = year[2:3]
            if decade == x:
                print('\t')
                print(*df.iloc[index, 0:4], sep='\n')
                break
            i += 1
    print('\n\n')
    album = str(df.iloc[index, 1])
    artist = str(df.iloc[index, 0])
    command = ('spotify play --album ' + album + ' ' + artist)
    os.system(str(command))

    print(f'\n\n\n-------------------------------------------------------------')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
