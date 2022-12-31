from pytube import YouTube
import requests






class Download():
    
    


    def video():


        pass

    def tumnail_title(url):

        link=YouTube(str(url))


        pic=requests.get(link.thumbnail_url).content
        title=link.title

        return pic,title

    def menu(url):
        link=YouTube(str(url))
        data=link.streams.get_highest_resolution()
        
        return data

        
        
    # def download_video():
        

 
    #    link=YouTube(str(url))
    #    data=link.streams.get_highest_resolution()
       
    #    return data.download()

   










    
        
       












