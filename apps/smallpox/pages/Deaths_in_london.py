import streamlit as st
import plotly.express as px
import pandas as pd


def read_decade_orig_df():
    df = pd.read_csv("data/deaths-from-smallpox-in-london.csv")

    i = 0
    tups = []
    while i < len(df):
        cur_row = df.iloc[i]
        year = cur_row['Year']
        decade_start = year - (year % 10)
        decade_end = decade_start + 10
        decade_range = f"{decade_start}-{decade_end}"
        
        death_rate = cur_row['Smallpox death rate in London 1629-1902 (OWID, 2017)']
        count = 1
        
        i += 1
        while i < len(df) and df.iloc[i]['Year'] < decade_end:
            death_rate += df.iloc[i]['Smallpox death rate in London 1629-1902 (OWID, 2017)']
            count += 1
            i += 1
            
        death_rate /= count
            
        tups.append((decade_range, death_rate))
        
    decade_df = pd.DataFrame(tups, columns=['decade', 'avg death rate'])

    return decade_df, df


def max_min_death_rows(df):
    min_rate = float('inf')
    max_rate = float('-inf')
    min_row = max_row = None

    for _, row in df.iterrows():
        if row['Smallpox death rate in London 1629-1902 (OWID, 2017)'] < min_rate:
            min_rate = row['Smallpox death rate in London 1629-1902 (OWID, 2017)']
            min_row = row
        if row['Smallpox death rate in London 1629-1902 (OWID, 2017)'] > max_rate:
            max_rate = row['Smallpox death rate in London 1629-1902 (OWID, 2017)']
            max_row = row

    return max_row, min_row


def app():
    st.set_page_config(
        layout="wide",
        page_title="Deaths due to smallpox in London",
    )

    st.write("# Deaths due to smallpox in London")

    st.write("The dataset contains average death rates for smallpox in London from 1629 to 1902. The original dataset contained information about the average death rate per year, I converted it into buckets of 10 years (a decade).")

    decade_df, df = read_decade_orig_df()

    max_row, min_row = max_min_death_rows(df)

    st.markdown(f"The year with maximum deaths was **{max_row['Year']}** with a death rate of **{round(max_row['Smallpox death rate in London 1629-1902 (OWID, 2017)'], 2)}%**.")
    st.markdown(f"The year with minimum deaths was **{min_row['Year']}** with a death rate of **{round(min_row['Smallpox death rate in London 1629-1902 (OWID, 2017)'], 2)}%**.")

    fig = px.line(
        decade_df, 
        title="Avg death rate per decade",
        x='decade', 
        y='avg death rate', 
        width=1200, 
        height=600
        ).update_traces(mode="markers+lines",)
    st.plotly_chart(fig)

    st.title("Evaluating Results")

    st.write("Some interesting facts from this graph and the dataset are:")
    st.markdown("- We see that the year 1796 saw the most number of deaths due to small pox in London, this was the same year when the vaccine for smallpox was developed by Edward Jenner.")
    st.markdown("- After the decade of 1790-1800, we see the rapid drop in the death rate for the next few decades, this is because it took some time for the mass production and distribution of the vaccine to reach the London population.")


if __name__ == "__main__":
    app()