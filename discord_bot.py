import discord
import time
import os
import csv
import random



TOKEN= 'OTI1OTMxODE4MDM1ODYzNjIz.Yc0TNA.heoLy-40njZaD-bCCKNsUhkL6ss'
client = discord.Client()

@client.event
async def on_ready():
    print()
    print()
    print('{0.user} is ready to game'.format(client))


@client.event
async def on_message(message):
    id = str(message.author.id)
    time_since_last_message = time.time()

    if int(id) == 309515077403541505:
        id = 'Ryan'
    elif int(id) == 777046591209996308:
        id = 'Ainsley'
    elif int(id) == 925931818035863623:
        id = 'Alfredo'
    fileNameCheck=('./game_profile_folder/' + id + '.csv')

    user_message = str(message.content)
    message_time=time.localtime()
    if len(str(message_time.tm_sec)) == 1:
        new_sec=str('0' + str(message_time.tm_sec))
    else:
        new_sec=message_time.tm_sec
    if len(str(message_time.tm_min)) == 1:
        new_min=str('0' + str(message_time.tm_min))
    else:
        new_min=message_time.tm_min

    
    if int(message_time.tm_hour) > int(12) and int(message_time.tm_min) > 0:
        new_hour=int(message_time.tm_hour) - int(12)
        fixed_date=(str(message_time.tm_mon) + '/' + str(message_time.tm_mday) + '/' + str(message_time.tm_year))
        fixed_time=(str(new_hour) + ':' + str(new_min) + ':' + str(new_sec))
        final_time=str(fixed_date) + ' @ ' + str(fixed_time) + ' PM'
        final_message=(id + ' said ' + '"' + user_message + '"' + ' on ' + final_time)
        with open('last_message_times.txt','a',encoding='utf-8-sig') as f:
            f.write(final_time)
    else:
        fixed_date=(str(message_time.tm_mon) + '/' + str(message_time.tm_mday) + '/' + str(message_time.tm_year))
        fixed_time=(str(message_time.tm_hour) + ':' + str(new_min) + ':' + str(new_sec))
        final_time=str(fixed_date) + ' @ ' + str(fixed_time) + ' AM'
        final_message=(id + ' said ' + '"' + user_message + '"' + ' on ' + final_time)
        with open('last_message_times.txt','a',encoding='utf-8-sig') as f:
            f.write(final_time)
    print(id)
    file_name=str(id + '.txt')
    with open(file_name, 'a' ,encoding='utf-8-sig') as m:
        m.write(str(final_message))
        m.write('\n')



    #checking messages for command / other stuff

    if user_message.lower() == ';new':
        if os.path.exists(fileNameCheck) == False:
            time.sleep(1)
            await message.channel.send('Profile Created')



        elif os.path.exists(fileNameCheck == True):
            await message.channel.send('You already have a profile.')
            pass
    if user_message.lower() == ';collect':
        file_name_2 = str(id) + '.csv'




client.run(TOKEN)