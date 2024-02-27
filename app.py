

import streamlit as st
import pandas as pd
import numpy as np



st.title('Breakpoint Information')

st.markdown(':blue[Often times finding the correct Breakpoint information for an organism/antimicrobial combination is difficult, we are trying to streamline this process]')


             
    
st.subheader(':red[Select your organism to see your preferred antimicrobial]')

option = st.radio(
    label ='Select your organism',
    options= ('Acinetobacter', 'Aeromonas', 'Enterococcus','Pseudomonas')
)

if option== 'Acinetobacter':
    st.write('Cefotaxime')
elif option =='Aeromonas':
    st.write('Cefoxitin')
elif option == 'Enterococcus':
    st.write('Daptomycin')
elif option == 'Pseudomonas':
    st.write('Amikacin')

st.subheader(':violet[Enter the antimicrobial from above to see if it matches CLSI Breakpoint and a brief explanation]' )

option= st.text_input(
    label= 'Type in your Antimicrobial to see if Breakpoint matches CLSI'
    
).lower()




st.button('Submit')
if option == 'cefotaxime':
    st.write("Match: using correct CLSI breakpoint")
elif option == 'cefoxitin':
    st.write("Nomatch: CLSI does not test against non-enterobac GNB")
elif option == 'daptomycin':
    st.write('''NoMatch:
             Enterococcus pp other than faecium: S≤2,I=4,R≥8, 
             for E.faecium: SDD ≤ 4, R≥ 8''')  
elif option == 'amikacin':
    st.write('''NoMatch:
             Urinary breakpoints only; 
             Per CLSI: S≤16,I=32, R≥64''')
        









             
    










