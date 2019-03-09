from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=FM7MFYoylVs')

print(yt.streams.filter(progressive=True).all())

yt.streams.filter(progressive=True,subtype='mp4').order_by('resolution').first().download()

# def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
#     print(stream," ",chunk," ",bytes_remaining)


#yt.register_on_progress_callback(show_progress_bar)