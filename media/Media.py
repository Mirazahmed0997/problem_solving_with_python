import streamlit as st

st.title("Insert file")
st.divider()

images=st.file_uploader("Choose your file",type=['jpg','jpeg','png'],accept_multiple_files=True)

print(type(images))

if(images):
   cols = st.columns(len(images))

   for i, img in enumerate(images):
        with cols[i]:st.image(img)
