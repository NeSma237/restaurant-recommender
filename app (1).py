import streamlit as st
import pandas as pd


df = pd.read_csv('cleaned_zomato_data.csv', encoding='latin-1')

def filter_and_rank(df, cuisines=None, budget=None, city=None, top_n=10):
    filtered = df.copy()
    if city:
        filtered = filtered[filtered['city'].str.lower() == city.lower()]
    if cuisines:
        if isinstance(cuisines, str):
            cuisines = [cuisines]
        cuisines = [c.lower() for c in cuisines]
        filtered = filtered[filtered['primary_cuisine'].str.lower().isin(cuisines)]
    if budget:
        filtered = filtered[filtered['cost_category'].str.lower() == budget.lower()]
    filtered = filtered.dropna(subset=['rating'])
    filtered['score'] = filtered['rating'] * (filtered['cost'] / (filtered['cost'].max() + 1))
    filtered = filtered.sort_values(by='score', ascending=False)
    return filtered.head(top_n)

def explain_row(row):
    return f"Matched on {row['primary_cuisine'].title()} cuisine, {row['cost_category']} budget with {row['rating']}★ rating"

st.title("🍽️ Knowledge-Based Restaurant Recommender")

st.sidebar.header("Your Preferences")

city_input = st.sidebar.text_input("Enter city (e.g. New Delhi, Makati City):")

cuisine_options = df['primary_cuisine'].dropna().unique().tolist()
cuisine_input = st.sidebar.multiselect("Select cuisine(s):", options=cuisine_options)

budget_input = st.sidebar.selectbox("Select budget:", options=['', 'low', 'medium', 'high'], index=0)

top_n = st.sidebar.slider("Number of recommendations:", 1, 20, 10)

if st.sidebar.button("Show Recommendations"):
    results = filter_and_rank(df, cuisines=cuisine_input, budget=budget_input, city=city_input, top_n=top_n)
    if results.empty:
        st.warning("No restaurants found matching your criteria.")
    else:
        for idx, row in results.iterrows():
            st.markdown(f"### {row['name']}")
            st.write(f"- Cuisine: **{row['primary_cuisine'].title()}**")
            st.write(f"- Cost Category: **{row['cost_category'].title()}** (Approx ₹{int(row['cost'])} for two)")
            st.write(f"- Rating: **{row['rating']}★**")
            st.write(explain_row(row))
            st.markdown("---")
