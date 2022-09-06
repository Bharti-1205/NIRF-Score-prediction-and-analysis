import streamlit as st
import pickle
import numpy as np

# function contains implementation of multiple Linear regressor takes the testing tuple and returns the predicted score
def load_model(Z):
    import pandas as pd
    import numpy as np
    from keras.wrappers.scikit_learn import KerasRegressor
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import KFold
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import train_test_split
    

    dataset = pd.read_csv("EngineeringRanking.csv")
    X = dataset.iloc[:, 4:9].values
    y = dataset.iloc[:, 9].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 20)


    #Scale data, otherwise model will fail.
    #Standardize features by removing the mean and scaling to unit variance
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(Z)
    return y_pred
   
    






# def load_model():
#     with open('saved_steps.pkl', 'rb') as file:
#         data = pickle.load(file)
#     return data

# data = load_model()

# regressor = data["model"]

# displays the content on predict page 
def show_predict_page():
    st.title("NIRF based Institute - Score Prediction")
    st.write("")

    st.write("""### We need some information to predict the score""")
    st.write("")
    st.markdown("##")
    

    # my_num=st.number_input("Enter a number", min_value=0,max_value=100,step=0.1)

    params=dict()

    tlr = st.slider(label="TEACHER LEARNING AND RESOURCES",max_value=0.,min_value=100., step=0.01,format="%.2f")
    params["TLR"]=tlr

    rpc = st.slider(label="RESEARCH , PROFESSIONAL PRACTICE AND COLLABORATIVE PERFORMANCE",max_value=0.,min_value=100., step=0.01,format="%.2f")
    params["RPC"]=rpc

    go = st.slider(label="GRADUATION OUTCOMES",max_value=0.,min_value=100., step=0.01,format="%.2f")
    params["GO"]=go

    oi = st.slider(label="OUTREACH AND INCLUSIVITY",max_value=0.,min_value=100., step=0.01,format="%.2f")
    params["OI"]=oi

    perception = st.slider(label="PERCEPTION",max_value=0.,min_value=100., step=0.01,format="%.2f")
    params["PERCEPTION"]=perception

    ok = st.button("Calculate Score")
    if ok:
        Y = np.array([[params["TLR"], params["RPC"], params["GO"],params["OI"],params["PERCEPTION"] ]] )
        score=load_model(Y)
        # st.write("The score is")
        st.subheader(f"The estimated score is :  {score[0]:.2f}")



# show_predict_page()