import pandas as pd
import streamlit as st

from availability import get_availability

st.title('Vaccine Availability')


@st.cache
def get_data():
    return pd.read_csv('districts.csv')

data = get_data()

mapper = dict(data.values)
avail_districts = list(mapper.keys())
min_age_limit = st.radio('Min age limit', [18, 45])
option = st.multiselect('District', avail_districts, "Ahmedabad Corporation")

district_ids = [mapper[val] for val in option]


