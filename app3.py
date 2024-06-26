import streamlit as st
import pandas as pd


# Sample data for the table
data = {
    'Organism': ['Pseudomonas spp.', 'Enterobacterales', 'Enterobacterales', 'Acinetobacter spp.'],
    'Antibiotic': ['Zosyn', 'Primaxin', 'Cipro', 'Doribax'],
    'MIC Breakpoints(mg/L)': [0.001, 0.001, 0.125, 0.001]
}
df = pd.DataFrame(data)

# Function to filter data based on search input
def filter_data(df, query):
    return df[df.apply(lambda row: query.lower() in row.astype(str).str.lower().values, axis=1)]

# Main function to run the Streamlit app

st.title('Breakpoint Information')

st.markdown(':blue[Often times finding the correct Breakpoint information for an organism/antimicrobial combination is difficult, we are trying to streamline this process]')


def main():
    st.title('Breakpoint information')
    
    # Search input box
    search_query = st.text_input('Type in your organism or antibiotic:', '')
    
    # Submit button
    if st.button('Submit'):
        # Filter data based on search query
        filtered_df = filter_data(df, search_query)
        
        # Display search results
        if not filtered_df.empty:
            for index, row in filtered_df.iterrows():
                st.write(f"Organism: {row['Organism']}, Antibiotic: {row['Antibiotic']}, MIC_Breakpoint: {row['MIC Breakpoint(mg/L)']}")
        else:
            st.write('No results found.')
        
        # Clear search query after submission
        search_query = ''

if __name__ == "__main__":
    main()
