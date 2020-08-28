from __future__ import print_function
import os
import subprocess
import speech_recognition as sr
import pymsgbox

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
if not os.path.isdir(dir_path + '\Inputs'):
    os.mkdir(dir_path + '\Inputs')
    os.mkdir(dir_path + '\Outputs')
    pymsgbox.alert('Required paths have created. Please place the Files in Input Path.', 'Audio to Text Conversion')
    exit()
else:
    Ipath = dir_path + '\Inputs'
    Opath = dir_path + '\Outputs'
Ipath = dir_path + '\Inputs'
Opath = dir_path + '\Outputs'

files = os.listdir(Ipath)
for name in files:
    full_path = os.path.join(Ipath, name)
    subprocess.call(['ffmpeg', '-i', full_path, Opath + "/" + name.replace(".mp3", "") + ".wav"])

files1 = os.listdir(Opath)
for name in files1:
    full_path = os.path.join(Opath, name)
    r = sr.Recognizer()
    with sr.AudioFile(full_path) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = 'Cannot Able to Convert to Internet!'
    file1 = open(Opath + "/" + name.replace(".wav", "") + ".txt", "w+")
    file1.writelines(text)
    text = ""
    os.remove(full_path)
    file1.close()
pymsgbox.alert('Process Competed Successfully!', 'Audio to Text Conversion')
exit()