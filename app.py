import streamlit as st
from helper import Download




st.header('Welcome to Application')






with st.sidebar:
    user_option=st.radio('File Format Type', ['Mp4','Mp3'],horizontal=True)

    download_option=st.radio('Select Download Video Options',['single', 'Playlist' ],horizontal=True,)


    


if user_option=='Mp4': 

    url=st.text_input('Enter YouTube Url Here ')
    if len(url)!=0:

        col1,=st.columns(1)
        
        with col1:
            image,title = Download.tumnail_title(url)
            image_title=st.image(image,caption=str(title),use_column_width=True,clamp=True)
            vid_option=st.selectbox('Select ',options=[ 'Select Format',Download.menu(url)])
            if vid_option!='Select Format':
            
                with st.sidebar:
                    if st.button('Download'):
                        my_bar = st.progress(0)
                        Download.menu(url).download()
                        

                        for percent_complete in range(100):
                        
                            my_bar.progress(percent_complete + 1)

if user_option =='Mp4' and download_option =='Playlist':
    pass





             
                    













            


        


















