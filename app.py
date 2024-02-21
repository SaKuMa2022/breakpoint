
import streamlit as st
import pandas as pd
import numpy as np



st.title('Breakpoint Information')

st.markdown(':blue[Often times finding the correct Breakpoint information for an organism/antimicrobial combination is difficult, we are trying to streamline this process]')


             
    
st.subheader(':red[Select your organism to see your preferred antimicrobial]')

option = st.radio(
    label ='Select your organism',
    options= ('Acinetobacter', 'Aeromonas', 'Enterococcus')
)

if option== 'Acinetobacter':
    st.write('Cefotaxime')
elif option =='Aeromonas':
    st.write('Cefoxitin')
elif option == 'Enterococcus':
    st.write('Daptomycin')

st.subheader(':violet[Enter the antimicrobial from above to see if it matches CLSI Breakpoint]' )

option= st.text_input(
    label= 'Type in your Antimicrobial to see if Breakpoint matches CLSI'
    
).lower()




st.button('Submit')
if option == 'cefotaxime':
    st.write('Match')
elif option == 'cefoxitin':
    st.write('Nomatch')
elif option == 'daptomycin':
    st.write('NoMatch') 







