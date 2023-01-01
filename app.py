import streamlit as st
from helper import Download,Bulk





st.header('Welcome to Application')






with st.sidebar:
    user_option=st.radio('File Format Type', ['Mp4','Mp3'],horizontal=True)

    download_option=st.radio('Select Download Video Options',['Single', 'Playlist'],horizontal=True,)


    

url=st.text_input('Enter YouTube Url Here ')

if user_option=='Mp4' and download_option== 'Single': 

    try:

        if len(url)!=0:

            col1,=st.columns(1)
            
        
            image,title = Download.tumnail_title(url)
            with col1:
                image_title=st.image(image,caption=str(title),use_column_width=True,clamp=True)

                
            with st.sidebar:
                if st.button('Download'):
                    my_bar = st.progress(0)
                    Download.menu(url).download()
                    

                    for percent_complete in range(100):
                    
                        my_bar.progress(percent_complete + 1)
    except:
        st.title('Plese Select Correct Downloaded Options')



elif user_option =='Mp4' and download_option =='Playlist':
    if len(url)!=0:
        try :

            title,tumbnail ,total_videos=Bulk.video_title(url)
            col1,col2=st.columns(2)
            with col1:
                st.title(f'Total Videos {str(total_videos)}')


            with col2:
                st.image(tumbnail,caption=str(title),use_column_width=True,clamp=True)


            
            with st.sidebar:
            
                        if st.button('Download'):
                            my_bar = st.progress(0)
                            Bulk.video_list(url)
                            

                            for percent_complete in range(100):
                            
                                my_bar.progress(percent_complete + 1)
            
        
        except:
                    st.title("""
                    Please Select Correct Downloaded Options (:
                    """)





elif    user_option =='Mp3' and download_option =='Single':
    st.title("""Working on it""")
   


elif user_option =='Mp3' and download_option == 'Playlist':
    st.title("""Working on it""")




    
        

   




             
                    













            


        


















