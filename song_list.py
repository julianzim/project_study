last_sanya_msg = '''https://music.yandex.ru/album/2532013/track/21998692

https://music.yandex.ru/album/9471/track/101330

https://music.yandex.ru/album/19363746/track/95108082

https://music.yandex.ru/album/2075287/track/47006709'''

song_list = last_sanya_msg.split('\n')

for i in range(len(song_list)-1, -1, -1):
    if song_list[i] == '':
        del song_list[i]

for i in range(len(song_list)):
    if i % 2 == 0:
        print('song ' + str(i+1) +' is zaebis')
    else:
        print('song ' + str(i+1) + ' - polnay huinya')