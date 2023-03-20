import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "Shuvadeep", "Marks": 420, "Pass": True},
       {"command": "Sayan", "Marks": 200, "Pass": False},
       {"command": "Souvik", "Marks": 410, "Pass": True},
   ]
)
edited_df = st.experimental_data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["Marks"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
