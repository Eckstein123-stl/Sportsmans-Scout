import streamlit as st
import pandas as pd

st.title("Sportsman's Scout")

df = pd.read_csv("data/player_data.csv")

teams = st.sidebar.multiselect("Select Team", options=df["Team"].unique(), default=df["Team"].unique())
positions = st.sidebar.multiselect("Select Position", options=df["Position"].unique(), default=df["Position"].unique())

filtered_df = df[df["Team"].isin(teams) & df["Position"].isin(positions)]

st.subheader("Player Leaderboard")
st.dataframe(filtered_df)
