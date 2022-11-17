import pytube

SAVE_PATH = "C:/"

video_links = [
    "https://www.youtube.com/watch?v=jNQXAC9IVRw",
]

def download_video(video_link="", SAVE_PATH="C:/", resolution="720p"):
    try:
        yt = pytube.YouTube(video_link)   

        print('Downloading "' + yt.title+ '"') 
        stream = yt.streams.filter(res=resolution).first() # specifying the resolution of the video
        stream.download(SAVE_PATH)

        print('Video "' + yt.title + '" was downloaded') 
        print('Size: ' + str(stream.filesize) + ' bytes')

    except pytube.exceptions.VideoPrivate:
        print('Index '+ yt.title +' is private')

    except pytube.exceptions.VideoRegionBlocked:
        print('Index '+ yt.title +' was blocked in your region')

    except pytube.exceptions.MembersOnly:
        print('Index '+ yt.title + ' is members-only')
    
    except pytube.exceptions.AgeRestrictedError:
        print('Index '+ yt.title + ' age restricted')

    except pytube.exceptions.ExtractError or pytube.exceptions.HTMLParseError or pytube.exceptions.RegexMatchError:
        print('An unknown error occured while parsing, extracting or matching regex patterns')


def download_videos(links_list, SAVE_PATH="C:/", resolution="720p"):
    for link in links_list:
        try:
            yt = pytube.YouTube(link)   

            stream = yt.streams.filter(res=resolution).first()# specifying the resolution of the video
            stream.download(SAVE_PATH)

            print('Video ' + yt.title + ' was downloaded') 
            print('Size: ' + str(stream.filesize) + ' bytes\n')

        except pytube.exceptions.VideoPrivate:
            print('Index '+ yt.title +' is private')

        except pytube.exceptions.VideoRegionBlocked:
            print('Index '+ yt.title +' was blocked in your region')
        
        except pytube.exceptions.MembersOnly:
            print('Index '+ yt.title + ' is members-only')
        
        except pytube.exceptions.AgeRestrictedError:
            print('Index '+ yt.title + ' age restricted')
        
        except pytube.exceptions.ExtractError or pytube.exceptions.HTMLParseError or pytube.exceptions.RegexMatchError:
            print('An unknown error occured while parsing, extracting or matching regex patterns')

if __name__ == "__main__":
   pass
