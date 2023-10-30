from pytube import YouTube

try:
    # Asking the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Getting the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Downloading the video to the current directory
    yd.download()
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))