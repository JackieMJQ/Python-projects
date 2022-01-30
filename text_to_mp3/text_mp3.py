from gtts import gTTS

#user guide
print('User guide')
print('1. Please creat a word document first.')
print('2. Write the sentences you want to transfer in this document.')
print("3. Make sure this '.txt' word document in same folder with this app.")
print("4. After input your text file name and MP3 name, you will find a mp3 file in same folder.\n")
print('Language guide (You should type simplified name according to your text file language.)')
print("English ---- 'en'\nChinese Mandarin ---- 'zh-cn'\nFrench ---- 'fr'\nPortuguese ---- 'pt'\nSpanish ---- 'es'")

#input exit to exit and ask file name
text = 1
while text != 'exit':
    text = input('\nWhat name is your text file? (without .txt)')
    if text == 'exit':
        print('Bye!')
        break
    file = open(f"{text}.txt", 'r').read()

#ask what kind of language
    lan = input('Which language in this text?')
    if lan != 'en' and lan != 'zh-cn' and lan != 'fr' and lan != 'pt' and lan != 'es':
        print('Please check your language name.')
        continue
        
# #ask the speed to read
#     speed = input('Slow?(True/False)')
#     if speed != 'True' and speed != 'False':
#         print('Please retype the True or False exactly.')
#         continue
    
    speech = gTTS(text= file, lang= f'{lan}', slow = False)

    #choose a name for mp3
    mp3 = input('what is this MP3 file name?')
    speech.save(f"{mp3}.mp3")

    print('Transfer successfully!')