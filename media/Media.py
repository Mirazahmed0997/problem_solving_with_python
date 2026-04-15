import streamlit as st

st.title("Insert image file",anchor=False)
st.divider()

images=st.file_uploader("Choose your image",type=['jpg','jpeg','png'],accept_multiple_files=True)

print(type(images))

if images:
    if len(images) > 2:
        st.warning("Doesn't allow to upload more than two images")
    else:
        cols = st.columns(len(images))

        for i, img in enumerate(images):
            with cols[i]:
                st.image(img)

st.title("Insert audio file",anchor=False)
st.divider()

audios=st.file_uploader("Choose your image",type=['mp3','ogg','flac'])

if(audios):
    st.audio(audios)



st.title("Insert video file",anchor=False)
st.divider()

videos=st.file_uploader("Choose your image",type=['mp4','mkv'])

button= st.button("Click to upload", type='primary')

if button :
    if videos:
        st.video(videos)
        st.success("File uploaded")
    else: 
        st.error("Select a file first")   

