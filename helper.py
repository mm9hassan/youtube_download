from pytube import YouTube,Playlist
import requests






class Download():
    
    



    def tumnail_title(url):

        link=YouTube(str(url))


        pic=requests.get(link.thumbnail_url).content
        title=link.title

        return pic,title

    def menu(url):
        link=YouTube(str(url))
        data=link.streams.get_highest_resolution().download()
        
        yield data

        
        
class Bulk():
    
    def video_title(url):

        link=Playlist(str(url))
        for i in link.videos:
            fist=i.thumbnail_url
            break
        
        


        return link.title, fist,len(link.video_urls)

    
    




    def video_list(url):
        link=Playlist(url)
        for i in link.videos_generator():
            video=i.streams.get_highest_resolution().download()
            
        return video



   










    
        
       












