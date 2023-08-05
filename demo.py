import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = pickle.load(open('C:/Users/geshn/ML Loan Project/Model/ML_Model1.pkl', 'rb'))

# Create a LabelEncoder object
label_encoder = LabelEncoder()

def run():
    st.title("Loan Approval Prediction")

    ## Account No
    account_no = st.text_input('Account number')

    ## Full Name
    fn = st.text_input('Full Name')

    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(gen_display)
    gen = st.selectbox("Gender", gen_options)

    ## For Marital Status
    mar_display = ('No', 'Yes')
    mar_options = list(mar_display)
    mar = st.selectbox("Marital Status", mar_options)

    # Fit the LabelEncoder on the categories and transform 'mar' to numerical value
    mar_numeric = label_encoder.fit_transform([mar])[0]

    ## No of dependets
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(dep_display)
    dep = st.selectbox("Dependents",  dep_options)

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(edu_display)
    edu = st.selectbox("Education", edu_options)

    ## For emp status
    emp_display = ('Job','Business')
    emp_options = list(emp_display)
    emp = st.selectbox("Employment Status", emp_options)

    ## For Property status
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(prop_display)
    prop = st.selectbox("Property Area", prop_options)

    ## For Credit Score
    cred_display = ('Between 300 to 500','Above 500')
    cred_options = list(cred_display)
    cred = st.selectbox("Credit Score", cred_options)

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)

    ## Loan Amount
    loan_amt = st.number_input("Loan Amount", value=0)

    ## loan duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = list(dur_display)
    dur = st.selectbox("Loan Duration", dur_options)

    if st.button("Submit"):
        duration = [60, 180, 240, 360, 480][dur_options.index(dur)]
        features = [[gen_options.index(gen), mar_numeric, dep_options.index(dep), edu_options.index(edu), emp_options.index(emp),
                     mon_income, co_mon_income, loan_amt, duration, cred_options.index(cred), prop_options.index(prop)]]
        print("Features:", features)

        # Make the prediction
        prediction = model.predict(features)
        print("Raw Prediction:", prediction)

        # Transform the prediction to integer
        ans = int(prediction[0])
        if ans == 0:
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations!! you will get the loan from Bank'
            )

if __name__ == '__main__':
    run()
