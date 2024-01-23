import pandas as pd
import numpy as np
#import openpyxl
#import matplotlib.pyplot as plt
import streamlit as st
import warnings
import sys

warnings.filterwarnings("ignore")
st.set_page_config(
    page_title="Intership Report For Data CP,LP and RP",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an extremely cool app!"
    # }
)

st.sidebar.title("Main Menu")
formside = st.sidebar.form("side_form")
#choose = formside.radio("Choose which data you want to see",["Whole data","Cp", "Lp","Rp","Graphite Batch 3","Graphite Batch 4","Graphite Batch 5","slider"], index=None)
choose = formside.radio("Choose which data you want to see",["Whole data","Graphite Batch 3","Graphite Batch 4","Graphite Batch 5"], index=None)
formside.form_submit_button("Submit")
#df = pd.read_excel("NYmasterdatabase.xlsx")
df = pd.read_csv(r"NYmasterdatabase.csv")
df= df.reset_index(drop=True)

if (choose == "Whole data"):
    st.title("Master Database for old experiments")
    st.write(df)
                 
# elif (choose == "Cp"):
#     dfcp = df[['Hz','CpED4','CpDE4','CpED2','CpDE2']]
#     dfD = df[['Hz','DED4','DDE4','DED2','DDE2']]
#     st.dataframe(dfcp)
    
#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("Cp vs Hz")
#     col2.subheader("D-Factor vs Hz")
#     col1.line_chart(dfcp, x="Hz", use_container_width=True)
#     col2.line_chart(dfD, x="Hz")
    

# elif (choose == "Lp"):
#     dfcp = df[['Hz','CpED4','CpDE4','CpED2','CpDE2']]
#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("Lp vs Hz")
#     col2.subheader("D-Factor vs Hz")
    
# elif (choose == "Rp"):
#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("Rp vs Hz")
#     col2.subheader("D-Factor vs Hz")
    

elif (choose == "Graphite Batch 3"):
    st.title("Batch 3 of Graphite")
    dfcpraw = pd.read_excel(r"Graphite Batch 3.xlsx", sheet_name= "Cp")
    dfrpraw = pd.read_excel(r"Graphite Batch 3.xlsx", sheet_name= "Rp")
    dflpraw = pd.read_excel(r"Graphite Batch 3.xlsx", sheet_name= "Lp")
    dfcpraw = df.reset_index(drop=True)
    dfrpraw = df.reset_index(drop=True)
    dflpraw = df.reset_index(drop=True)
    
    # Create a copy of the original DataFrame
    # dfcpcleaned = df.copy()
    # dfrpcleaned = df.copy()
    # dflpcleaned = df.copy()
    
    dfBatch3 = pd.read_excel(r"Graphite Batch 3.xlsx", sheet_name= "RawData")
    wholerawdata = dfBatch3[['Freq','Cp','CpD','Rp','RpQ','Lp','LpQ']]
    st.dataframe(wholerawdata)

    #column 1 
    container = st.container(border=True)
    col1, col2 = container.columns([2, 2])
    col1.subheader("LCR Meter readings")
    col1.write("raw data for Cp")
    col2.write("Clean data")

    freq = col1.slider("Slider for Frequency", 50, 100000, 100)

    dfcpraw1 = (wholerawdata.loc[(wholerawdata['Freq']>=freq)])
    dfcpraw1 = dfcpraw1[['Freq','Cp','CpD']]
    dfrpraw1 = (wholerawdata.loc[(wholerawdata['Freq']>=freq)])
    dfrpraw1 = dfrpraw1[['Freq','Rp','RpQ']]
    dflpraw1 = (wholerawdata.loc[(wholerawdata['Freq']>=freq)])
    dflpraw1 = dflpraw1[['Freq','Lp','LpQ']]

    # dfcpraw1 = wholerawdata[['Freq','Cp','CpD']]
    # dfrpraw1 = wholerawdata[['Freq','Rp','RpQ']]
    # dflpraw1 = wholerawdata[['Freq','Lp','LpQ']]
    
    col1.write("Raw data for Cp")
    col1.dataframe(dfcpraw1)
    col1.line_chart(dfcpraw1, x="Freq",y="Cp", use_container_width=True)
    col1.scatter_chart(dfcpraw1, x="Freq",y="Cp", use_container_width=True)

    col1.write("Raw data for Rp")
    col1.dataframe(dfrpraw1)
    col1.line_chart(dfrpraw1, x="Freq",y="Rp", use_container_width=True)
    col1.scatter_chart(dfrpraw1, x="Freq",y="Rp", use_container_width=True)

    col1.dataframe(dflpraw1)
    # col1.write("")
    # col1.write("")
    # col1.write("")
    # col1.write("")
    col1.write("Raw data for Lp")
    col1.line_chart(dflpraw1, x="Freq",y="Lp", use_container_width=True)
    col1.scatter_chart(dflpraw1, x="Freq",y="Lp", use_container_width=True)
    

    MaxFCp = dfcpraw1["Freq"].max()
    MaxCp = dfcpraw1["Cp"].max()
    # with col1.()
    #st.write("The maximum (outliers) is = ", MaxFCp , ',', MaxCp)
    

    #column 2

    dfcpraw1 = wholerawdata[['Freq','Cp','CpD']]
    dfrpraw1 = wholerawdata[['Freq','Rp','RpQ']]
    dflpraw1 = wholerawdata[['Freq','Lp','LpQ']]
    
    col2.write("Cleaned data for Cp")
    dfcpcleaned = dfcpraw1.copy()
    dfcpcleaned.drop(dfcpcleaned[dfcpcleaned['Cp'] == -0.0000095203].index, inplace=True)
    dfcpcleaned.drop(dfcpcleaned[dfcpcleaned['Cp'] == 0.0000109053].index, inplace=True)
    col2.dataframe(dfcpcleaned)
    col2.line_chart(dfcpcleaned, x="Freq",y="Cp", use_container_width=True)
    col2.scatter_chart(dfcpcleaned, x="Freq",y="Cp", use_container_width=True)
    
    col2.write("cleaned data for Rp")
    dfrpcleaned = dfrpraw1.copy()
    dfrpcleaned.drop(dfrpcleaned[dfrpcleaned['Rp'] > 500000000].index, inplace=True)
    col2.dataframe(dfrpcleaned)
    col2.line_chart(dfrpcleaned, x="Freq",y="Rp", use_container_width=True)
    col2.scatter_chart(dfrpcleaned, x="Freq",y="Rp", use_container_width=True)

    col2.write("cleaned data for Lp")
    dflpcleaned = dflpraw1.copy()
    dflpcleaned.drop(dflpcleaned[dflpcleaned['Lp'] > 2000000].index, inplace=True)
    dflpcleaned.drop(dflpcleaned[dflpcleaned['Lp'] < -150].index, inplace=True)
    dflpcleaned.drop(dflpcleaned[dflpcleaned['Freq'] > 100000].index, inplace=True)
    col2.dataframe(dflpcleaned)
    col2.line_chart(dflpcleaned, x="Freq",y="Lp", use_container_width=True)
    col2.scatter_chart(dflpcleaned, x="Freq",y="Lp", use_container_width=True)

    st.line_chart(dflpcleaned, x="Freq",y="Lp", use_container_width=True)

    # df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
    #                 'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
 
    # df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],
    #                     'Age': ['12', '13', '14', '12']})
     
    # # the default behaviour is join='outer'
    # # inner join
     
    # result = pd.concat([df1, df3], axis=1, join='inner')
    # display(result)
      
    
    
    st.title("D-factor, Q-Factors")
    container = st.container(border=True)
    col1, col2 = container.columns([2, 2])
    col1.subheader("Raw Factor graphs")
    col2.subheader("Cleaned Factor graphs")
    
   
    #column 1

    col1.write("Raw data for Cp-D")
    #col1.dataframe(dfcpraw1)
    col1.write("D-factor for Capacitance vs Frequency")
    col1.line_chart(dfcpraw1, x="Freq",y="CpD", use_container_width=True)
    col1.scatter_chart(dfcpraw1, x="Freq",y="CpD", use_container_width=True)

    col1.write("Raw data for Rp-Q")
    #col1.dataframe(dfrpraw1)
    col1.write("Q-factor for Resistance vs Frequency")
    col1.line_chart(dfrpraw1, x="Freq",y="RpQ", use_container_width=True)
    col1.scatter_chart(dfrpraw1, x="Freq",y="RpQ", use_container_width=True)

    col1.write("Raw data for Lp-Q")
    #col1.dataframe(dflpraw1)
    col1.write("Q-factor for Inductance vs Frequency")
    col1.line_chart(dflpraw1, x="Freq",y="LpQ", use_container_width=True)
    col1.scatter_chart(dflpraw1, x="Freq",y="LpQ", use_container_width=True)



    #column 2

    col2.write("Cleaned D-factor for Capacitance vs Frequency")
    dfcpcleaned = dfcpraw1.copy()
    dfcpcleaned.drop(dfcpcleaned[dfcpcleaned['CpD'] > 140].index, inplace=True)
    #col2.dataframe(dfcpcleaned)
    col2.line_chart(dfcpcleaned, x="Freq",y="CpD", use_container_width=True)
    col2.scatter_chart(dfcpcleaned, x="Freq",y="CpD", use_container_width=True)
    
    col2.write("Cleaned Q-factor for Resistance vs Frequency")
    dfrpcleaned = dfrpraw1.copy()
    dfrpcleaned.drop(dfrpcleaned[dfrpcleaned['Freq'] > 80000].index, inplace=True)
    #col2.dataframe(dfrpcleaned)
    col2.line_chart(dfrpcleaned, x="Freq",y="RpQ", use_container_width=True)
    col2.scatter_chart(dfrpcleaned, x="Freq",y="RpQ", use_container_width=True)

    col2.write("Cleaned Q-factor for Inductance vs Frequency")
    dflpcleaned = dflpraw1.copy()
    dflpcleaned.drop(dflpcleaned[dflpcleaned['LpQ'] > 2].index, inplace=True)
    dflpcleaned.drop(dflpcleaned[dflpcleaned['Freq'] > 80000].index, inplace=True)
    #col2.dataframe(dflpcleaned)
    col2.line_chart(dflpcleaned, x="Freq",y="LpQ", use_container_width=True)
    col2.scatter_chart(dflpcleaned, x="Freq",y="LpQ", use_container_width=True)


# elif (choose == "Graphite Batch 4"):
#     st.title("Batch 4 of Graphite")
#     dfBatch4 = pd.read_excel(r"Graphite Batch 4.xlsx", sheet_name = "RawData")
#     st.dataframe(dfBatch4)
    
#     # dfcprawB4 = pd.read_excel(r"D:\Nine G Solutions\LCR data\Graphite Batch 4.xlsx", sheet_name= "Cp")
#     # dfrprawB4 = pd.read_excel(r"D:\Nine G Solutions\LCR data\Graphite Batch 4.xlsx", sheet_name= "Rp")
#     # dflprawB4 = pd.read_excel(r"D:\Nine G Solutions\LCR data\Graphite Batch 4.xlsx", sheet_name= "Lp")
#     # dfcprawB4 = dfcprawB4.reset_index(drop=True)
#     # dfrprawB4 = dfcprawB4.reset_index(drop=True)
#     # dflprawB4 = dfcprawB4.reset_index(drop=True)
#     # st.dataframe(dfrprawB4)

#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("LCR Meter readings")
#     col2.subheader("Cleaned data")
#     col1.write("Raw data")
#     col2.write("Clean data")

#     # Column 1

#     col1.write("Raw data for Cp")
#     dfcprawB4 = dfBatch4[['Freq','Cp','CpD']]
#     dfrprawB4 = dfBatch4[['Freq','Rp','RpQ']]
#     dflprawB4 = dfBatch4[['Freq','Lp','LpQ']]

#     col1.write("Raw data for Cp")
#     col1.dataframe(dfcprawB4)
#     col1.line_chart(dfcprawB4, x="Freq",y="Cp", use_container_width=True)
#     col1.scatter_chart(dfcprawB4, x="Freq",y="Cp", use_container_width=True)

#     col1.write("Raw data for Rp")
#     col1.dataframe(dfrprawB4)
#     col1.line_chart(dfrprawB4, x="Freq",y="Rp", use_container_width=True)
#     col1.scatter_chart(dfrprawB4, x="Freq",y="Rp", use_container_width=True)

#     col1.write("Raw data for Lp-Q")
#     col1.dataframe(dflprawB4)
#     col1.write("")
#     col1.write("")
#     col1.write("")
#     col1.write("")
#     col1.line_chart(dflprawB4, x="Freq",y="Lp", use_container_width=True)
#     col1.scatter_chart(dflprawB4, x="Freq",y="Lp", use_container_width=True)

#     #column 2

#     col2.write("Cleaned data for Cp")
#     dfcpcleanedb4 = dfcprawB4.copy()
#     #dfcpcleanedb4.drop(dfcpcleanedb4[dfcpcleanedb4['Cp'] > 0.0001].index, inplace=True)
#     dfcpcleanedb4.drop(dfcpcleanedb4[dfcpcleanedb4['Freq'] > 9000].index, inplace=True)
#     col2.dataframe(dfcpcleanedb4)
#     col2.line_chart(dfcpcleanedb4, x="Freq",y="Cp", use_container_width=True)
#     col2.scatter_chart(dfcpcleanedb4, x="Freq",y="Cp", use_container_width=True)

#     col2.write("Cleaned data for Rp")
#     dfrpcleanedb4 = dfrprawB4.copy()
#     dfrpcleanedb4.drop(dfrpcleanedb4[dfrpcleanedb4['Rp'] > 35*10^9].index, inplace=True)
#     dfrpcleanedb4.drop(dfrpcleanedb4[dfrpcleanedb4['Rp'] == -843301000].index, inplace=True)
#     dfrpcleanedb4.drop(dfrpcleanedb4[dfrpcleanedb4['Rp'] == -227279000].index, inplace=True)
#     # dfrpcleanedb4.drop(dfrpcleanedb4[dfrpcleanedb4['Rp'] < -60000].index, inplace=True)
#     dfrpcleanedb4.drop(dfrpcleanedb4[dfrpcleanedb4['Freq'] > 80000].index, inplace=True)
#     col2.dataframe(dfrpcleanedb4)
#     col2.line_chart(dfrpcleanedb4, x="Freq",y="Rp", use_container_width=True)
#     col2.scatter_chart(dfrpcleanedb4, x="Freq",y="Rp", use_container_width=True)

#     col2.write("Cleaned data for Lp")
#     dflpcleanedb4 = dflprawB4.copy()
#     dflpcleanedb4.drop(dflpcleanedb4[dflpcleanedb4['Lp'] > 2.4*100000].index, inplace=True)
#     dflpcleanedb4.drop(dflpcleanedb4[dflpcleanedb4['Lp'] < -60000].index, inplace=True)
#     col2.dataframe(dflpcleanedb4)
#     col2.line_chart(dflpcleanedb4, x="Freq",y="Lp", use_container_width=True)
#     col2.scatter_chart(dflpcleanedb4, x="Freq",y="Lp", use_container_width=True)

     
#     st.title("D-factor, Q-Factors")
#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("Raw Factor graphs")
#     col2.subheader("Cleaned Factor graphs")
    

#     #Column 1
    
#     #col1.dataframe(dfcpraw1)
#     col1.write("D-factor for Capacitance vs Frequency")
#     col1.line_chart(dfcprawB4, x="Freq",y="CpD", use_container_width=True)
#     col1.scatter_chart(dfcprawB4, x="Freq",y="CpD", use_container_width=True)

#     #col1.dataframe(dfrpraw1)
#     col1.write("Q-factor for Resistance vs Frequency")
#     col1.line_chart(dfrprawB4, x="Freq",y="RpQ", use_container_width=True)
#     col1.scatter_chart(dfrprawB4, x="Freq",y="RpQ", use_container_width=True)
    
#     #col1.dataframe(dflpraw1)
#     col1.write("Q-factor for Inductance vs Frequency")
#     col1.line_chart(dflprawB4, x="Freq",y="LpQ", use_container_width=True)
#     col1.scatter_chart(dflprawB4, x="Freq",y="LpQ", use_container_width=True)

    
#     #column 2

#     col2.write("Cleaned D-factor for Capacitance vs Frequency")
#     dfcpcleanedb4 = dfcprawB4.copy()
#     dfcpcleanedb4.drop(dfcpcleanedb4[dfcpcleanedb4['CpD'] > 800].index, inplace=True)
#     #col2.dataframe(dfcpcleaned)
#     col2.line_chart(dfcpcleanedb4, x="Freq",y="CpD", use_container_width=True)
#     col2.scatter_chart(dfcpcleanedb4, x="Freq",y="CpD", use_container_width=True)

#     col2.write("Cleaned Q-factor for Resistance vs Frequency")
#     dfrpcleanedb4 = dfrprawB4.copy()
#     dfrpcleanedb4.drop(dfrpcleanedb4[dfrpcleanedb4['RpQ'] < -140].index, inplace=True)
#     #col2.dataframe(dfcpcleaned)
#     col2.line_chart(dfrpcleanedb4, x="Freq",y="RpQ", use_container_width=True)
#     col2.scatter_chart(dfrpcleanedb4, x="Freq",y="RpQ", use_container_width=True)
    

#     col2.write("Cleaned Q-factor for Inductance vs Frequency")
#     dflpcleanedb4 = dflprawB4.copy()
#     dflpcleanedb4.drop(dflpcleanedb4[dflpcleanedb4['LpQ'] > 2000].index, inplace=True)
#     #col2.dataframe(dflpcleaned)
#     col2.line_chart(dflpcleanedb4, x="Freq",y="LpQ", use_container_width=True)
#     col2.scatter_chart(dflpcleanedb4, x="Freq",y="LpQ", use_container_width=True)

# elif (choose == "Graphite Batch 5"):
#     st.title("Batch 5 of Graphite")
#     dfBatch5 = pd.read_excel(r"Batch 5 LCR.xlsx", sheet_name = "RawData")
#     st.dataframe(dfBatch5)

#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("LCR Meter readings")
#     col2.subheader("Cleaned data")
#     col1.write("Raw data")
#     col2.write("Clean data")

#     # Column 1

#     dfcprawB5 = dfBatch5[['Freq','Cp','CpD']]
#     dfrprawB5 = dfBatch5[['Freq','Rp','RpQ']]
#     dflprawB5 = dfBatch5[['Freq','Lp','LpQ']]

#     col1.write("Raw data for Cp")
#     col1.dataframe(dfcprawB5)
#     col1.line_chart(dfcprawB5, x="Freq",y="Cp", use_container_width=True)
#     col1.scatter_chart(dfcprawB5, x="Freq",y="Cp", use_container_width=True)

#     col1.write("Raw data for Rp")
#     col1.dataframe(dfrprawB5)
#     col1.line_chart(dfrprawB5, x="Freq",y="Rp", use_container_width=True)
#     col1.scatter_chart(dfrprawB5, x="Freq",y="Rp", use_container_width=True)

#     col1.write("Raw data for Lp-Q")
#     col1.dataframe(dflprawB5)
#     col1.line_chart(dflprawB5, x="Freq",y="Lp", use_container_width=True)
#     col1.scatter_chart(dflprawB5, x="Freq",y="Lp", use_container_width=True)


#     #column 2

#     col2.write("Cleaned data for Cp")
#     dfcpcleanedb5 = dfcprawB5.copy()
#     dfcpcleanedb5.drop(dfcpcleanedb5[dfcpcleanedb5['Cp'] > 0.000003].index, inplace=True)
#     col2.dataframe(dfcpcleanedb5)
#     col2.line_chart(dfcpcleanedb5, x="Freq",y="Cp", use_container_width=True)
#     col2.scatter_chart(dfcpcleanedb5, x="Freq",y="Cp", use_container_width=True)
    
#     col2.write("cleaned data for Rp")
#     dfrpcleanedb5 = dfrprawB5.copy()
#     dfrpcleanedb5.drop(dfrpcleanedb5[dfrpcleanedb5['Rp'] > 35*10^9].index, inplace=True)
#     col2.dataframe(dfrpcleanedb5)
#     col2.line_chart(dfrpcleanedb5, x="Freq",y="Rp", use_container_width=True)
#     col2.scatter_chart(dfrpcleanedb5, x="Freq",y="Rp", use_container_width=True)

#     col2.write("cleaned data for Lp")
#     dflpcleanedb5 = dflprawB5.copy()
#     dflpcleanedb5.drop(dflpcleanedb5[dflpcleanedb5['Freq'] > 88000].index, inplace=True)
#     col2.dataframe(dflpcleanedb5)
#     col2.line_chart(dflpcleanedb5, x="Freq",y="Lp", use_container_width=True)
#     col2.scatter_chart(dflpcleanedb5, x="Freq",y="Lp", use_container_width=True)


#     st.title("D-factor, Q-Factors")
#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("Raw Factor graphs")
#     col2.subheader("Cleaned Factor graphs")
    
#     #Column 1
    
#     #col1.dataframe(dfcpraw1)
#     col1.write("D-factor for Capacitance vs Frequency")
#     col1.line_chart(dfcprawB5, x="Freq",y="CpD", use_container_width=True)
#     col1.scatter_chart(dfcprawB5, x="Freq",y="CpD", use_container_width=True)

#     #col1.dataframe(dfrpraw1)
#     col1.write("Q-factor for Resistance vs Frequency")
#     col1.line_chart(dfrprawB5, x="Freq",y="RpQ", use_container_width=True)
#     col1.scatter_chart(dfrprawB5, x="Freq",y="RpQ", use_container_width=True)
    
#     #col1.dataframe(dflpraw1)
#     col1.write("Q-factor for Inductance vs Frequency")
#     col1.line_chart(dflprawB5, x="Freq",y="LpQ", use_container_width=True)
#     col1.scatter_chart(dflprawB5, x="Freq",y="LpQ", use_container_width=True)


#     #Column 2

#     col2.write("Cleaned D-factor for Capacitance vs Frequency")
#     dfcpcleanedb5 = dfcprawB5.copy()
#     dfcpcleanedb5.drop(dfcpcleanedb5[dfcpcleanedb5['CpD'] > 45].index, inplace=True)
#     #col2.dataframe(dfcpcleaned)
#     col2.line_chart(dfcpcleanedb5, x="Freq",y="CpD", use_container_width=True)
#     col2.scatter_chart(dfcpcleanedb5, x="Freq",y="CpD", use_container_width=True)

#     col2.write("Cleaned Q-factor for Resistance vs Frequency")
#     dfrpcleanedb5 = dfrprawB5.copy()
#     dfrpcleanedb5.drop(dfrpcleanedb5[dfrpcleanedb5['RpQ'] < -70].index, inplace=True)
#     #col2.dataframe(dfcpcleaned)
#     col2.line_chart(dfrpcleanedb5, x="Freq",y="RpQ", use_container_width=True)
#     col2.scatter_chart(dfrpcleanedb5, x="Freq",y="RpQ", use_container_width=True)
    



# elif (choose == "slider"):
#     container = st.container(border=True)
#     col1, col2 = container.columns([2, 2])
#     col1.subheader("Rp vs Hz")
#     col2.subheader("D-Factor vs Hz")





    # col2.write("Cleaned Q-factor for Inductance vs Frequency")
    # dflpcleanedb5 = dflprawB5.copy()
    # dflpcleanedb5.drop(dflpcleanedb5[dflpcleanedb5['LpQ'] > 2000].index, inplace=True)
    # #col2.dataframe(dflpcleaned)
    # col2.line_chart(dflpcleanedb5, x="Freq",y="LpQ", use_container_width=True)
    # col2.scatter_chart(dflpcleanedb5, x="Freq",y="LpQ", use_container_width=True)



    # # Extracting x and y data
    # ypoints = dfcp[['CpED4', 'CpDE4', 'CpED2', 'CpDE2']]
    # xpoints = dfcp['Hz']

    # # Plotting the graph
    # st.write.plot(xpoints, ypoints, marker='o')
    # st.write.title("Cp vs Hz")
    # st.write.xlabel("Hz")
    # st.write.ylabel("CP")
    # st.write.legend(['CpED4', 'CpDE4', 'CpED2', 'CpDE2'])
    
    # # Display the plot in Streamlit
    # st.pyplot()

















    
    # Cp_chart = (dfcp.loc[(df['Hz']) & (dfcp[['CpED4','CpDE4','CpED2','CpDE2','CpSED','CpSDE']])])
    # #st.line_chart(Cp_chart)
    # st.line_chart(dfcp, x="Hz", y="CpED4", color="CpED4")
    
   # st.line_chart(data=dfcp, x=df['Hz'], y= df[['CpED4','CpDE4','CpED2','CpDE2','CpSED','CpSDE']], color=None, width=0, height=0, use_container_width=True)



    # plt.plot(df.Hz, df.CpED4, marker = 'o')
    # # plt.plot(df.Hz, df.DED4, marker = 'o') #D-factor
    # plt.plot(df.Hz, df.CpDE4, marker = 'o')
    # # plt.plot(df.Hz, df.DDE4, marker = 'o') #d-factor
    # plt.plot(df.Hz, df.CpED2, marker = 'o')
    # plt.plot(df.Hz, df.CpDE2, marker = 'o')
    # plt.title( "CP vs Hz")
    # plt.xlabel ('Frequency (Hz)')
    # plt.ylabel('Cp')
    # plt. legend (['CpED4','CpDE4','CpED2','CpDE2'])
        
    
   




     
     


