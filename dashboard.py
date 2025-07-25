import streamlit as st, pandas as pd, sqlite3
df = pd.read_sql("SELECT * FROM jobs", sqlite3.connect("jobs.db"))

tech = st.multiselect("Filtrer par technologie", df.tags.str.split(", ").explode().unique(),
                      default=["python"])
days = st.slider("Publié il y a moins de ... jours", 0, 30, 7)

mask = df.tags.str.contains("|".join(tech), case=False) & \
       (pd.to_datetime(df.date) > pd.Timestamp.utcnow() - pd.Timedelta(days=days))

st.dataframe(df[mask][["date","title","company","tags","link"]])
