import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.cache_data.clear()
st.set_page_config(layout="wide")

#----2---------Load Data------------------

df = pd.read_csv("newfile.csv")

#-------------Navbar-------------

select = option_menu(
    menu_title=None,
    options=["Home","Player Analysis","Country Insights","Comparison","Data Explorer"],
    icons=["house","person","globe","bar-chart","table"],
    orientation="horizontal"

)

#----------------Home---------------

if select == "Home":

    st.title("Cricket Analytics Dashboard")

    col1,col2,col3 = st.columns(3)

    col1.metric("Total Players", df["Player"].nunique())

    col2.metric("Total Runs", df["Runs"].sum())

    col3.metric("Countries", df["Country"].nunique())

    st.dataframe(df.head())


#--------Player Analysis---------

elif select=="Player Analysis":

    st.title("Player Analysis")

    player = st.selectbox("Select Player", df["Player"])

    pdata = df[df["Player"]==player]

    #opt={"val":["100","50","6s","4s","innings","Strike_rate","Matches","Ave"]}
    #df_opt=pd.DataFrame(opt).reset_index()
    #st.dataframe(df_opt)

    #sl=st.multiselect("Select Choice",options=df_opt["val"],default=df_opt["val"])

    df2=pdata[["100","50","6s","4s","innings","Strike_rate","Matches","Ave"]]
    df3=df2.T.reset_index()
    st.dataframe(df3)
    fig=px.bar(df3,x="index",y=df3.columns[1])
    #st.plotly_chart(fig,use_container_width=True)

    #df_pie=pdata[[]]
    df_pie=pdata[["100","50","6s","4s"]]
    pie1=df_pie.T.reset_index()
    fig_pie=px.pie(pie1,names="index",values=pie1.columns[1])

    col1,col2=st.columns(2)
    with col1:
        st.plotly_chart(fig,use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie,use_container_width=True)


#---------------Country Insight----------

elif select=="Country Insights":

    st.title("Country Insights")

    scountry=st.selectbox("Select Country",df["Country"].unique())

    col1,col2,col3,col4=st.columns(4)

    cdata=df[df["Country"]==scountry]

    players=cdata["Player"].nunique()
    total_runs=cdata["Runs"].sum()
    total_matches=cdata["Matches"].sum()
    total_innings=cdata["innings"].sum()


    col1.metric("Total Players",players)

    col2.metric("Total Runs",total_runs)

    col3.metric("Total Matches",total_matches)

    col4.metric("Total innings",total_innings)


    #country_runs=cdata.groupby("Country")["Runs"].sum().reset_index()


    #fig=px.pie(,name="Country",values="Runs")

    #st.plotly_chart(fig,use_container_width)


    df2=cdata[["Player","Runs"]]

    df3=cdata[["Player","Runs","Matches","100","6s"]]

    df4=["Runs","Matches","100","6s"]

    #ss=st.selectbox("select Player",df2["Player"])

    #cc=df2[df2["Player"]==ss]

    fig=px.pie(df2,names="Player",values="Runs")

    selectc=st.selectbox("Select Choice", df4)

    fig2=px.bar(df3,x="Player",y=selectc,color="Player")

    col1,col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig,use_container_width=True)

    with col2:
        st.plotly_chart(fig2,use_container_width=True)

#----------------------Player comparison------------


elif select == "Comparison":

    st.title("Player Comparison")

    players = st.multiselect(
        "Compare Players",
        df["Player"],
        default=df["Player"].head(5)
    )

    compare = df[df["Player"].isin(players)]

    fig=px.scatter(
        compare,
        x="Strike_rate",
        y="Ave",
        size="Runs",
        color="Country",
        hover_name="Player"
    )

    st.plotly_chart(fig,use_container_width=True)


    #-----------------Data Explorer

elif select=="Data Explorer":

    st.title("Data Explorer")

    st.dataframe(df)


