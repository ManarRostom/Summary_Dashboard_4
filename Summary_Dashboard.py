
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

df = pd.read_json('Analyzed_Dataset_json.json')
df_languages = pd.read_csv('languages_df.csv')
df_technologies = pd.read_csv('technologies_df.csv')

Numerical_Variables = ['Age','Years_of_Experience','Current_Salary','Bonus+Stocks','Salary_One_Year_Ago','Bonus+Stocks_One_year_Ago','Number_of_Vacation_Days','Percentage_of_Salary_Change','Percentage_of_Bonus_Stocks_Change']
Categorical_Variables = ['Gender','City','Position','Level','Main_Language_at_Work','Main_Technology','Contract_Duration','Company_Type','Company_Size','Year']

## Fixing Year Column
df['Year'] = df['Year'].apply(lambda r:str(r).split('.')[0])

st.markdown('<p style="color:#0000e6;font-size:50px;text-align:center;"><strong>Summary Dashboard </strong></p>',unsafe_allow_html=True)

col1_1 , col1_2 , col1_3 = st.columns([2,1,2])
col2_1 , col2_2 , col2_3 = st.columns([2,1,2])
col3_1 , col3_2 , col3_3 = st.columns([2,1,2])


with col1_1:
    # Show the top 5 cities
    df_city_head = df['City'].value_counts().head().reset_index()
    fig1 = px.histogram(data_frame=df_city_head , x = 'count' , y = 'City' , height=300,width=450,text_auto=True ,
                        color_discrete_sequence=['#2929a3']).update_yaxes(categoryorder='total ascending',automargin=True).update_layout(yaxis_title=' ',title={'text':' ','x':0.5,'xanchor': 'center','y':0.95,'font':{'color':'#2929a3','size':25}})  
    st.plotly_chart(fig1)
with col2_1:   
    ## Show the Percentage of Gender Column
    df_Gender_Percentage = (df['Gender'].value_counts(normalize=True)*100).round(1).reset_index()
    colors_Gender = ['#2929a3','#cc0000','#008000']
    fig3 = px.pie(data_frame=df_Gender_Percentage,values='proportion',names='Gender',color_discrete_sequence=colors_Gender,
                  height=300,width=400)
    st.plotly_chart(fig3)
with col3_1:    
    #Show The Distribution of Languages
    fig5 = px.bar(data_frame=df_languages.sum().sort_values(ascending=False).head(4),text_auto=True,
                  color_discrete_sequence=['#2929a3'],width=490,height=300,orientation='h').update_yaxes(categoryorder='total ascending').update_layout(xaxis_title='Language',yaxis_title='Count')
    st.plotly_chart(fig5)

                                            
with col1_3:
    #Show the top 5 Positions
    df_top5_position = df['Position'].value_counts().head().reset_index()
    fig2 = px.histogram(data_frame=df_top5_position , x='count',y='Position',text_auto=True,color_discrete_sequence=['#2929a3'],
                        width=450,height=300).update_yaxes(categoryorder='total ascending',tickfont=dict(size=10),automargin=True)           
    st.plotly_chart(fig2)
with col2_3:
    #Show top 10 Technologies
    df_top10_technologies = df_technologies.sum().sort_values(ascending = False).head(10).reset_index().rename(columns={'index':'Technology',0:'Count'}) 
    fig4 = px.bar(data_frame= df_top10_technologies,x='Count',y='Technology',text_auto=True ,
                  color_discrete_sequence=['#2929a3'], height=300,width=450).update_yaxes(categoryorder='total ascending',tickfont=dict(size=10),automargin=True).update_layout(font=dict(size=12))
    st.plotly_chart(fig4)
with col3_3:    
    #Average Salary in each Year 
    df_year_salary = df.groupby('Year')['Current_Salary'].mean().round(0).reset_index().rename(columns={'Current_Salary':'Average_Salary'})
    fig6 = px.line(data_frame=df_year_salary, x='Year',y='Average_Salary',color_discrete_sequence=['#2929a3'],
                   height=300,width=450)                 
    st.plotly_chart(fig6)   
    
    
#Highest 10 Position in Salary
df_Top10_Position_Salary = df.groupby('Position')['Current_Salary'].mean().sort_values(ascending=False).head(10).reset_index()
fig7 = px.bar(data_frame=df_Top10_Position_Salary,x='Current_Salary',y='Position',text_auto=True,color_discrete_sequence=['#2929a3'],width=900,height=400).update_layout(yaxis_title=' ',title={'text':'','x':0.5,'xanchor': 'center','y':0.95,'font':{'color':'#2929a3','size':25}}).update_yaxes(categoryorder='total ascending',tickfont=dict(size=10),automargin=True)
st.plotly_chart(fig7)
