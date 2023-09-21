import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.set_page_config(page_title="Darey.io Analytics", page_icon="📈",layout="wide",initial_sidebar_state='collapsed')

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 1rem;
                   
                }
            body {
                        zoom: 0.80; /* Adjust the zoom factor as needed */
                    }
        </style>
        """, unsafe_allow_html=True) 




dash_1 = st.container()
dash_2 = st.container()
dash_3 = st.container()
dash_4 = st.container()

df_may = pd.read_csv('maycohort.csv')
df_may.drop('deferred',axis=1, inplace=True)
df_july = pd.read_csv('julycohort.csv')

with dash_1:
    st.markdown("<h2 style='text-align: center;'>Data Analyst Case Study May and July Cohort</h2>", unsafe_allow_html=True)
    st.write("")


with dash_2:
    col1, col2 = st.columns(2)

    with col1:
        tab1, tab2 = st.tabs(["May cohort data", "July cohort data"])

        with tab1:
            st.dataframe(df_may,height=500,use_container_width=True,hide_index=True)
        with tab2:
            st.data_editor(df_july,height=500,use_container_width=True, hide_index=True)


    with col2:
        chart = alt.Chart(df_may).mark_bar(opacity=0.9).encode(
                y='count(response_sentiment):Q',
                x=alt.X('response_sentiment:N', sort='-x')   
            )
        chart = chart.properties(title="Feedback Sentiments MAY cohort" )

        
        st.altair_chart(chart,use_container_width=True)

        pstv = len(df_may[df_may.response_sentiment == 'positive'])

        st.write(f"The expected number of students likely to complete the program is {pstv}. a ratio of {np.round(pstv/len(df_may)*100,1)}%")
        
        ngv = len(df_may[(df_may['response_sentiment'] == 'negative') | (df_may['response_sentiment'] == 'neutral')])

        st.write(f"The expected number of students likely to  discontinue or lose interest in the program is {ngv}. a ratio of {np.round(ngv/len(df_may)*100,1)}%. This a combination of both the neutral and negative feedbacks.")

        defers= len(df_may[df_may.response_sentiment == 'deferred'])

        st.write(f"The expected number of students likely to defer from the program is {defers}. a ratio of {np.round(defers/len(df_may)*100,1)}%")

        upgrd = len(df_may[df_may.response_sentiment == 'positive'])

        st.write(f"The number of students likely to upgrade to the next cohort is {upgrd}. This assumption is soley based on the positive feedback.")

      
with dash_3:

    col1,col2 = st.columns(2)

    st.write("")
    st.write("")

    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(''' 
                    #### Potential issues indicated by the data(may cohort)
                **Time Commitment and Personal Engagements:** Many students have mentioned personal engagements, work commitments, and difficulties balancing their schedules with the coursework. This suggests that the time commitment required by the program might be challenging for some participants


                **Dissatisfaction with Teaching Styles:** A few students have expressed dissatisfaction with the teaching styles of specific mentors, mentioning issues such as pace and detail. This indicates that there may be differences in how well mentors are delivering the curriculum, which could affect student engagement and satisfaction.


                **Class Duration:** Students have mentioned concerns about class durations, suggesting that classes sometimes exceed the expected time frame. This can impact students' ability to absorb information effectively and could be related to the curriculum structure and mentorship.


                ''')

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        chart = alt.Chart(df_july).mark_bar(opacity=0.9).encode(
                y='count(response_sentiment):Q',
                x=alt.X('response_sentiment:N', sort='-x')   
            )
        chart = chart.properties(title="Feedback Sentiments JULY cohort" )

        
        st.altair_chart(chart,use_container_width=True)

        compl_ju = len(df_july[df_july.response_sentiment == 'positive'])

        st.write(f"Number of people likely to complete the july cohort is {compl_ju} .a ratio of {np.round(compl_ju/len(df_july)*100,1)}%")

        disc_ju = len(df_july[df_july.response_sentiment == 'negative'])

        st.write(f"Number of people likely to discontinue or loss interest in the july cohort is {disc_ju}. a ratio of {np.round(disc_ju/len(df_july)*100,1)}%")

        st.markdown("Comparing the may cohort to the july cohort which is a 2 day class\
                     week learning(may cohort) and 1 day class week learning(july cohort), the both have similar\
                     percentage of students likely to complete the program.\
                    tho most of the feedback are currently neutral as a there are no response or feedback from some learners, giving that it is the beggining of the cohort, there is a posibility of \
                    increase in the percentage of students likely to complete the program.\
                    ")