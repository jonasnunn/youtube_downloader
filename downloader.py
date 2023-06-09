from tkinter import *
from pytube import YouTube

def main():
    root = Tk()
    root.geometry('1000x600') # This sets the size of the window.
    root.resizable(0, 0) # makes the window adjustable with its feautures.
    root.title("Youtube Downloader")

    Label(root, text="Jonas's Youtube Downloader", font='san-serif 20 bold').pack()
    link = StringVar() # Specifying the variable type
    Label(root, text="Insert Url", font='san-serif 15 bold').place(x=440, y=120)
    link_enter = Entry(root, width=100, textvariable=link).place(x=200, y=85)

    stream_options_list = StringVar(root)
    stream_options_list.set("Audio")
    select_stream_menu = OptionMenu(root, stream_options_list, "Audio", "HD Video", "LQ Video",)
    select_stream_menu.pack()

    def download():

        # Get the option from the dropdown menu of the user.
        option_selection = stream_options_list.get()
        print(option_selection)

        # Download the audio file as an mp4
        def audio_download():
            url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
            video = url.streams.get_audio_only() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
            video.download() # This is the method with the instruction to download the video.
            Label(root, text="DOWNLOADED AUDIO", font="arial 15").place(x=180, y=250) #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.
            
        
        # Download the highest quality video availble.
        def high_quality_video_download():
            url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
            video = url.streams.get_highest_resolution() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
            video.download() # This is the method with the instruction to download the video.
            Label(root, text="DOWNLOADED HD VIDEO", font="arial 15").place(x=180, y=250) #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.
            

        # Download the lowest quality video availble.
        def low_quality_video_download():
            url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
            video = url.streams.get_lowest_resolution() # This captures the lowest stream quality available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
            video.download() # This is the method with the instruction to download the video.
            Label(root, text="DOWNLOADED LQ VIDEO", font="arial 15").place(x=180, y=250) #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.
        

        # Identify and run the correct download option. 
        if option_selection == 'Audio':
            return audio_download() 
        elif option_selection == 'HD Video':
            return high_quality_video_download()
        elif option_selection == 'LQ Video':
            return low_quality_video_download()

    # This makes the download button 
    Button(root, text='Download', font='san-serif 16 bold', bg="pink", padx=2,command=download).place(x=430, y=175)

    root.mainloop()
    return True

if __name__ == "__main__":
    main()