from tkinter import *
from tkinter import filedialog
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("700x500")
root.title("Mp3 Player")
root.configure(background='black')

audio_file_name = ""


def choosefile():
    global audio_file_name
    audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".mp3"), ("All Files", "*.*")))


def play():
    if audio_file_name:  # play sound if just not an empty string
        mixer.music.load(audio_file_name)
        mixer.music.set_volume(0.7)
        mixer.music.play()


def pause():
    mixer.music.pause()


def resume():
    mixer.music.unpause()


PlayPhoto = PhotoImage(file="play.png")
PausePhoto = PhotoImage(file="pause.png")
ResumePhoto = PhotoImage(file="resume.png")

Label(root, text="Mp3 Player", font="Lucida 60").place(x= 150, y= 160)
ChooseFileButton = Button(root, text="Choose Audio", command=choosefile, height=4, width=15, bg="white", font="lucida").place(x=500, y=380)
PlayButton = Button(root, image=PlayPhoto , command=play).place(x=50, y=382)
PauseButton = Button(root, image=PausePhoto, command=pause).place(x=200, y=382)
ResumeButton = Button(root, image=ResumePhoto, command=resume).place(x=350, y=382)
root.mainloop()