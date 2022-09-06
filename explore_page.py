import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components  # Import components for html


# displays the informatioon about paramteres involved
def display_parameter_info():

    components.html("""<html><head><style>body {font-size: 120%; color: #FF4B4B; }</style></head>
                    <body>&nbsp;  1.   TEACHER LEARNING AND RESOURCES <br> &nbsp;
                     </body></html>""", width=900, height=25)


    components.html("""<html><head><style>body {font-size: 100%;   }</style></head>
                    <body>&nbsp; &nbsp;&nbsp;&nbsp; These parameters are related to the core activities of any place of learning.
                    </body></html>""", width=900, height=25)


    components.html("""<html><head><style>body {font-size: 120%; color: #FF4B4B; }</style></head>
                    <body>&nbsp; 
                     2.   RESEARCH , PROFESSIONAL PRACTICE AND COLLABORATIVE PERFORMANCE <br> &nbsp; 
                     </body></html>""", width=900, height=25)

    components.html("""<html><head><style>body {font-size: 100%;  }</style></head>
                    <body>&nbsp; &nbsp;&nbsp; &nbsp;Excellence in teaching and learning is closely associated with the scholarship.
                    </body></html>""", width=900, height=25)


    components.html("""<html><head><style>body {font-size: 120%; color: #FF4B4B; }</style></head>
                    <body>&nbsp; 
                    3.   GRADUATION OUTCOMES<br> &nbsp;  <br> &nbsp; 
                     </body></html>""", width=900, height=25)


    components.html("""<html><head><style>body {font-size: 100%;   }</style></head>
                    <body>&nbsp; &nbsp;&nbsp; &nbsp;This parameter forms the ultimate test of the effectiveness of the core teaching/learning.
                    </body></html>""", width=900, height=25)



    components.html("""<html><head><style>body {font-size: 120%;color: #FF4B4B;  }</style></head>
                    <body>&nbsp;
                     4.   OUTREACH AND INCLUSIVITY <br> &nbsp; 
                    </body></html>""", width=900, height=25)


    components.html("""<html><head><style>body {font-size: 100%;  }</style></head>
                    <body>&nbsp; &nbsp;&nbsp; &nbsp;The Ranking framework lays special emphasis on representation of women.
                    </body></html>""", width=900, height=25)


    components.html("""<html><head><style>body {font-size: 120%;color: #FF4B4B; }</style></head>
                    <body>&nbsp; 
                     5.   PERCEPTION</body></html>""", width=900, height=25)


    components.html("""<html><head><style>body {font-size: 100%;   }</style></head>
                    <body>&nbsp; &nbsp;&nbsp;&nbsp; The ranking methodology gives a significant importance to the perception of the institution.
                    </body></html>""", width=900, height=25)


    st.markdown("##") #for line spaces
    st.markdown("##")
    st.markdown("##")


# displys scattered graphs
def  display_scatter_plots():

    components.html("""<html><head><style>body {font-size: 220%; margin-left: 25% ; text-decoration: underline;}</style></head>
                    <body> <br> <br> <br> SCATTERED PLOTS :  <br>
                     </body></html>""", width=900, height =200)

    df = pd.read_csv ('EngineeringRanking.csv')
    X = df.iloc [:, 9].values
    y_tlr = df.iloc [:, 4].values
    y_rpc = df.iloc [:, 5].values
    y_go = df.iloc [:, 6].values
    y_oi = df.iloc [:, 7].values
    y_per = df.iloc [:, 8].values

    plt.rcParams['font.size']=20    #for changing the font size of text in graph globally
    
    plt_1=plt.figure(figsize=(20,10))
    plt.scatter(X, y_tlr, color = 'r')
    #plt.plot(y_tlr, X, color = 'r')
    plt.title('TLR vs score')
    plt.xlabel('score')
    plt.ylabel('TLR')
    plt.grid()
    plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)  #to hide the warning display
    st.write( """### 1.TEACHER LEARNING AND RESOURCES""")
    fig=plt.show()
    st.pyplot(fig)

    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.scatter(X, y_rpc, color = 'g')
    plt.title('RPC vs score')
    plt.xlabel('score')
    plt.ylabel('RPC')
    plt.grid()
    st.write( """### 2.RESEARCH , PROFESSIONAL PRACTICE & COLLABORATIVE PERFORMANCE""")
    fig=plt.show()
    st.pyplot(fig)

    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.scatter(X, y_go, color = 'c')
    plt.title('GO vs score')
    plt.xlabel('score')
    plt.ylabel('GO')
    plt.grid()
    st.write( """### 3.GRADUATION OUTCOMES""")
    fig=plt.show()
    st.pyplot(fig)


    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.scatter(X, y_oi, color = 'b')
    plt.title('OI vs score')
    plt.xlabel('score')
    plt.ylabel('OI')
    plt.grid()
    st.write( """### 4.OUTREACH AND INCLUSIVITY""")
    fig=plt.show()
    st.pyplot(fig)

    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.scatter(X, y_per, color = 'm')
    plt.title('Perception vs score')
    plt.xlabel('score')
    plt.ylabel('Perception')
    plt.grid()
    st.write( """### 5.PERCEPTION""")
    fig=plt.show()
    st.pyplot(fig)


# for diplaying horizontal plots
def display_h_plots():

    components.html("""<html><head><style>body {font-size: 220%; margin-left: 20%; text-decoration: underline;}</style></head>
                    <body> ANALYSIS & PLOTS :  <br>
                     </body></html>""", width=900, height =100)
    df = pd.read_csv ('EngineeringRanking.csv')
    X = df.iloc [:, 9].values
    y_tlr = df.iloc [:, 4].values
    y_rpc = df.iloc [:, 5].values
    y_go = df.iloc [:, 6].values
    y_oi = df.iloc [:, 7].values
    y_per = df.iloc [:, 8].values

    plt.rcParams['font.size']=20    #for changing the font size of text in graph globally
    
    plt_1=plt.figure(figsize=(20,10))
    plt.plot(X, y_tlr, color = 'r')
    #plt.plot(y_tlr, X, color = 'r')
    plt.title('TLR vs score')
    plt.xlabel('score')
    plt.ylabel('TLR')
    plt.grid()
    plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)  #to hide the warning display
    st.write( """### 1.TEACHER LEARNING AND RESOURCES""")
    fig=plt.show()
    st.pyplot(fig)

    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.plot(X, y_rpc, color = 'g')
    plt.title('RPC vs score')
    plt.xlabel('score')
    plt.ylabel('RPC')
    plt.grid()
    st.write( """### 2.RESEARCH , PROFESSIONAL PRACTICE & COLLABORATIVE PERFORMANCE""")
    fig=plt.show()
    st.pyplot(fig)

    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.plot(X, y_go, color = 'c')
    plt.title('GO vs score')
    plt.xlabel('score')
    plt.ylabel('GO')
    plt.grid()
    st.write( """### 3.GRADUATION OUTCOMES""")
    fig=plt.show()
    st.pyplot(fig)


    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.plot(X, y_oi, color = 'b')
    plt.title('OI vs score')
    plt.xlabel('score')
    plt.ylabel('OI')
    plt.grid()
    st.write( """### 4.OUTREACH AND INCLUSIVITY""")
    fig=plt.show()
    st.pyplot(fig)

    st.write("   ")
    plt_1=plt.figure(figsize=(20,10))
    plt.plot(X, y_per, color = 'm')
    plt.title('Perception vs score')
    plt.xlabel('score')
    plt.ylabel('Perception')
    plt.grid()
    st.write( """### 5.PERCEPTION""")
    fig=plt.show()
    st.pyplot(fig)



# main function
def show_explore_page():
    
    
    st.title('NIRF ATTRIBUTES vs SCORE')
    st.title("   ")
    st.write("Here, we will explore and analyse the dependencies of the score upon the different input paramaters or attributes.")
    st.write("The attributes for determining NIRF score are: ")
    
    display_parameter_info()
    display_h_plots()
    display_scatter_plots()
