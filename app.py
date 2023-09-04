import os
import pandas as pd
import streamlit as st
from streamlit.locale import gettext as _
from PIL import Image
import data.symptom  as symptom
import data.symptom_weight as sw
import pickle


st.set_page_config(layout="wide")

data_weight = sw.sw

symptoms = []

def get_weight_symptom(symptom1):
    for i in range(len(data_weight)):
        if (data_weight[i]["Symptom"] == symptom1):
            symptoms.append(data_weight[i]["weight"])

    return symptoms

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("header.jpg"))
st.markdown(_("# Go Doctor, Ask"))


st.write('\n')
st.markdown(_("\n ##### 1st Symptom: Skin 🖐️"))
selected_symptom1 = st.selectbox(
    label="How do you feel with your skin?",
    options=symptom.skin,
    )
get_weight_symptom(selected_symptom1)


st.markdown(_("##### 2nd Symptom: Nose 👃"))
selected_symptom2 = st.selectbox(
    label="How do you feel with your nose?",
    options=symptom.nose,
    )
get_weight_symptom(selected_symptom2)

st.write('\n')
st.markdown(_("##### 3rd Symptom: Stomach 🍕"))
selected_symptom3 = st.selectbox(
    label="How do you feel with your stomach? ",
    options=symptom.stomach,
    )
get_weight_symptom(selected_symptom3)

st.write('\n')
st.markdown(_("##### 4th Symptom: Mouth 👄"))
selected_symptom4 = st.selectbox(
    label="How do you feel with your mouth? ",
    options=symptom.mouth,
    )
get_weight_symptom(selected_symptom4)

st.write('\n')
st.markdown(_("##### 5th Symptom: Body 👧"))
selected_symptom5 = st.selectbox(
    label="What changes did you feel in your body? ",
    options=symptom.body_changes,
    )
get_weight_symptom(selected_symptom5)

st.write('\n')
st.markdown(_("##### 6th Symptom: Body 🦵"))
selected_symptom6 = st.selectbox(
    label="What part of your body hurts the most?? ",
    options=symptom.body_pain,
    )
get_weight_symptom(selected_symptom6)

st.write('\n')
st.markdown(_("##### 7th Symptom: Temperature 🔥"))
selected_symptom7 = st.selectbox(
    label="How is your body temperature? ",
    options=symptom.body_temp,
    )
get_weight_symptom(selected_symptom7)

st.write('\n')
st.markdown(_("##### 8th Symptom: Excretion 💦"))
selected_symptom8 = st.selectbox(
    label="What happens with your excretion system? ",
    options=symptom.excretion,
    )
get_weight_symptom(selected_symptom8)

st.write('\n')
st.markdown(_("##### 9th Symptom: Feelings 💝 "))
selected_symptom9 = st.selectbox(
    label="How do you feel with your feelings? ",
    options=symptom.heart,
    )
get_weight_symptom(selected_symptom9)

st.write('\n')
st.markdown(_("##### 10th Symptom: Eyes 👀"))
selected_symptom10 = st.selectbox(
    label="How do you feel with your eyes? ",
    options=symptom.eye,
    )
get_weight_symptom(selected_symptom10)

st.write('\n')
st.markdown(_("##### 11th Symptom: Head 🧠"))
selected_symptom11 = st.selectbox(
    label="How do you feel with your head? ",
    options=symptom.head,
    )
get_weight_symptom(selected_symptom11)

st.write('\n')
st.markdown(_("##### 12th Symptom: Muscle 💪"))
selected_symptom12 = st.selectbox(
    label="How do you feel with your nerve? ",
    options=symptom.muscle,
    )
get_weight_symptom(selected_symptom12)

st.write('\n')
st.markdown(_("##### 13th Symptom: Nails 💅"))
selected_symptom13 = st.selectbox(
    label="How do you feel with your nails? ",
    options=symptom.nails,
    )
get_weight_symptom(selected_symptom13)


st.write('\n')
st.markdown(_("##### 14th Symptom: Activity 👪"))
selected_symptom14 = st.selectbox(
    label="What have you ever had or done that could be the cause of an illness? ",
    options=symptom.behavior,
    )
get_weight_symptom(selected_symptom14)

nulls = [0,0,0]
symptoms= [symptoms + nulls]
# st.write(symptoms)

load_model = pickle.load(open('/mount/src/godoc/model.pkl', 'rb'))
st.markdown("---")
if st.button("Predict", type="primary", use_container_width =True):
    if all(v == 0 for v in symptoms[0]):
        st.info("Enter symptoms first.")
    else:
        st.write('\n \n \n')
        st.markdown("---")
        prediction = load_model.predict([symptoms[0]])
        st.markdown(_("# 🗓️ Disease Result: {result}").format(result=prediction[0]))
        st.markdown(_("## {result}").format(result=prediction[0]))

        if os.path.isfile(f"data/symptom_Description.csv"):
            df = pd.read_csv(f"data/symptom_Description.csv", engine="python")
            for i in range(len(df)):
                if(df.Disease[i]==prediction[0]):
                    st.markdown(_(" {result}").format(result=df.Description[i]))




with st.expander(_("About GoDoc")):
    st.markdown(_(
        """
    The **GoDoc** is a web application designed to help you get started to know your diseases immediately.
    
    Particularly, you'll be able to:
    - Choose appropriate symptoms 
    - Know your disease result
    - Understand your disease and how to cope with it
    """
    ))

# Sidebar
st.sidebar.header(_("About"))
st.sidebar.markdown(_(
    "GoDoc is a web aplication that allows the detection of disease  based on human's symptoms body such as skin, mouth, stomach, etc."
))

st.sidebar.header(_("Author"))
st.sidebar.markdown(_(
    "[Karisa Zihni Lutfiana](https://linkedin/in/karisazihni)"
))

st.sidebar.header(_("Connect"))
st.sidebar.markdown(_(
    """
- My [Linkedin](https://www.linkedin.com/in/karisazihni)
- My [Github](https://www.github.com/karisazsh)
- My [Instagram](https://www.instagram.com/karisazsh) 
"""
))





