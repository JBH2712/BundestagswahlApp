import streamlit as st
import pandas as pd

# Load the article content
article_path = 'article.txt'

with open(article_path, 'r', encoding='utf-8') as file:
    article_content = file.read()

# Parse data for visualization
polling_data = {
    'Party': ['CDU/CSU', 'AfD', 'SPD', 'GRÜNE', 'FDP', 'DIE LINKE', 'FW', 'BSW', 'Sonstige'],
    'Polls': [32.13, 18.94, 16.06, 13.19, 3.63, 3.14, 1.50, 5.31, 7.75]
}

polls_df = pd.DataFrame(polling_data)

# Streamlit app layout
st.title("Bundestagswahl 2025 Analysis")

# Split the article into sections
sections = article_content.split("##")

for section in sections:
    if "Überblick: Aktuelle Umfragewerte und Entwicklungen" in section:
        st.subheader("Überblick: Aktuelle Umfragewerte und Entwicklungen")
        st.write(section.strip())

        # Display visualizations side by side
        col1, col2 = st.columns(2)
        with col1:
            st.image("Viz_Party_Votes.png", caption="Umfragewerte pro Partei", use_column_width=True)
        with col2:
            st.image("party_change.png", caption="Development of Parties Over Time", use_column_width=True)
    else:
        st.subheader(section.strip().split("\n")[0])  # First line as subheader
        st.write("\n".join(section.strip().split("\n")[1:]))  # Rest as content

st.subheader("Insights and Discussion")
if st.button("Show Analysis Summary"):
    st.write("""
    - CDU/CSU leads with 32.13%.
    - AfD shows significant growth with 18.94%.
    - SPD faces challenges with a reduced share of 16.06%.
    - Other parties struggle near or below the 5% threshold.
    - Shifts in voter preferences highlight a dynamic political landscape.
    """)

st.subheader("User Interaction")
user_insights = st.text_area("Share your thoughts or insights on the election analysis:")
if user_insights:
    st.write("Thank you for sharing your insights!")
