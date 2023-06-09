import streamlit as st
import pandas

st.set_page_config(layout='wide')

hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet lacinia lacus. " \
               "Suspendisse venenatis vel dui ac venenatis. Mauris convallis volutpat risus, " \
               "vulputate convallis augue rutrum eget. Curabitur eros justo, molestie in elementum " \
               "sit amet, dictum ac justo. Nulla in ipsum in ante cursus faucibus. Pellentesque varius et eros " \
               "non eleifend. Nullam nec ex ac eros tincidunt imperdiet. Aliquam luctus egestas fermentum." \
               " Sed viverra nulla enim, vitae mollis nibh hendrerit vel. Mauris ipsum mi, faucibus eu" \
               " ipsum nec, gravida ultricies urna. Ut neque sapien, sagittis non ligula id, tincidunt " \
               "facilisis leo. Aliquam erat volutpat. Maecenas volutpat pretium lacus, at auctor massa" \
               " lobortis ut. Quisque vitae leo porta, " \
               "facilisis tellus nec, mattis leo. In fringilla nisi non diam blandit consequat."

st.title('The Best Company')
st.write(hero_content)

st.subheader('Our Team')

data = pandas.read_csv('best-company-website/data.csv', sep=',')

col1, col2, col3 = st.columns(3)
with col1:
    for index, content in data[:4].iterrows():
        name = f"{content['first name']} {content['last name']}".title()
        st.subheader(name)
        st.write(content['role'])
        st.image(f'best-company-website/images/{content["image"]}')

with col2:
    for index, content in data[4:8].iterrows():
        name = f"{content['first name']} {content['last name']}".title()
        st.subheader(name)
        st.write(content['role'])
        st.image(f'best-company-website/images/{content["image"]}')

with col3:
    for index, content in data[8:12].iterrows():
        name = f"{content['first name']} {content['last name']}".title()
        st.subheader(name)
        st.write(content['role'])
        st.image(f'best-company-website/images/{content["image"]}')
