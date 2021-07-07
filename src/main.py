import keyboard
import pyperclip
import time


commands = 'saves/commands.txt'
intervals = 'saves/intervals.txt'
players = 'saves/players.txt'
coordinates = 'saves/coordinates.txt'


# read file and assign it's contents to a dictionary
def read_file(path, mode):
    file = open(path, 'r')
    output = dict()
    for line in file:
        line = line.replace('\n', '')
        keys, values = line.split(':')
        if mode == 'float':
            output[keys] = float(values)
        elif mode == 'string':
            output[keys] = values
    return output


# save file
def save_file(path, data):
    file = open(path, 'w')
    for keys, values in data.items():
        file.write(str(keys.replace("'", '') + ':' + values.replace("'", '') + '\n'))
    file.close()


# read files and map them to dictionaries
hotkeys_list = read_file(commands, 'string')
intervals_list = read_file(intervals, 'float')
players_list = read_file(players, 'string')
coordinates_list = read_file(coordinates, 'string')


# key pressing routine
def key_routine(times):
    keyboard.press_and_release('/')
    time.sleep(times['init_sleep'])
    keyboard.press_and_release('ctrl + v')
    time.sleep(times['paste_sleep'])
    keyboard.press_and_release('enter')
    time.sleep(times['enter_sleep'])


# additional data
check_interval = intervals_list['check_sleep']
username = players_list['your_nickname']

# successful launch
print(f"Ready to work. Delay is {check_interval} seconds.")
print(hotkeys_list)
save_file(commands, hotkeys_list)
exit(0)
# main loop
while True:
    for opt, key in hotkeys_list.items():
        if keyboard.is_pressed(key):
            if opt == 'home':
                pyperclip.copy('tp ' + username + ' ' + coordinates_list[opt])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'cave2':
                pyperclip.copy('tp ' + username + ' ' + coordinates_list[opt])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'cave3':
                pyperclip.copy('tp ' + username + ' ' + coordinates_list[opt])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'nether-portal':
                pyperclip.copy('tp ' + username + ' ' + coordinates_list[opt])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'portal-in-nether':
                pyperclip.copy('tp ' + username + ' ' + coordinates_list[opt])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'village1':
                pyperclip.copy('tp ' + username + ' ' + coordinates_list[opt])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'witch1':
                pyperclip.copy('tp ' + username + ' ' + coordinates_list[opt])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'to-player':
                pyperclip.copy('tp ' + username + ' ' + players_list['1'])
                print('copied')
                key_routine(intervals_list)
            elif opt == 'to-me':
                pyperclip.copy('tp ' + players_list['1'] + ' ' + username)
                key_routine(intervals_list)

    time.sleep(check_interval)
