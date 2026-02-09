import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)
        if diab_prediction[0] == 1:
            st.subheader("🍬 Diabetes - Diet Recommended")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🧔 Male – Vegetarian")
                st.markdown("""
                - 🏋️ Workout: Brisk walk + bodyweight exercises (push-ups, squats – 30 mins)  
                - 🍽️ Breakfast: Besan chilla + low-fat curd  
                - 🥤 Mid-Morning Snack: Amla juice (30 ml) + 5 boiled peanuts  
                - 🍽️ Lunch:  
                    - 2 bajra rotis  
                    - Methi sabzi  
                    - Masoor dal  
                - ☕ Evening Snack: Sprouts salad + cinnamon tea  
                - 🍽️ Dinner: Tofu stir-fry + mixed greens + ½ cup brown rice  
                """)

                st.markdown("### 🧔 Male – Non-Vegetarian")
                st.markdown("""
                - 🏋️ Workout: Walk + resistance training (light weights)  
                - 🍽️ Breakfast: 2 boiled eggs + oats dosa  
                - 🥤 Mid-Morning Snack: Buttermilk + boiled chana  
                - 🍽️ Lunch:  
                    - 1 multigrain roti  
                    - Grilled chicken (no oil)  
                    - Lauki sabzi  
                - ☕ Evening Snack: Sprouts + green tea with cinnamon  
                - 🍽️ Dinner: Stir-fried tofu + small portion quinoa + methi leaves salad  
                """)

            with col2:
                st.markdown("### 👩 Female – Vegetarian")
                st.markdown("""
                - 🏋️ Workout: 25–30 mins brisk walking or indoor cycling  
                - 🍽️ Breakfast: Besan chilla + mint chutney + 4 almonds  
                - 🥤 Mid-Morning Snack: Amla juice or lemon water  
                - 🍽️ Lunch:  
                    - 1 bajra roti  
                    - Methi dal  
                    - Steamed ridge gourd + salad  
                - ☕ Evening Snack: Green tea + sprouts chaat  
                - 🍽️ Dinner: Tofu stir-fry + sautéed green beans + 1 tsp cinnamon water before bed  
                """)

                st.markdown("### 👩 Female – Non-Vegetarian")
                st.markdown("""
                - 🏋️ Workout: Walk + resistance bands or light dumbbells  
                - 🍽️ Breakfast: 1 boiled egg + moong dal dosa  
                - 🥤 Mid-Morning Snack: Guava or pear  
                - 🍽️ Lunch:  
                    - 1 multigrain roti  
                    - Chicken stew (light spice, no oil)  
                    - Cabbage sabzi  
                - ☕ Evening Snack: Cucumber sticks + mint yogurt dip  
                - 🍽️ Dinner: Stir-fried chicken or tofu + sautéed beans + 1 tsp flaxseed powder mixed in warm water before bed  
                """)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)

        if heart_prediction[0] == 1:
            st.subheader("Diet Recommended")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🧔 Male – Vegetarian")
                st.markdown("""
                    - 🏋️ Early Morning Workout: 30 mins brisk walk or yoga (low-intensity cardio)  
                    - 🍽️ Breakfast: Oats porridge with flaxseeds, almonds, and skim milk  
                    - 🥤 Mid-Morning Snack: Guava or apple + 5 soaked almonds  
                    - 🍽️ Lunch:  
                        - 2 multigrain rotis  
                        - Moong dal (less salt)  
                        - Mixed vegetables (steamed or sautéed in olive oil)  
                        - Cucumber-tomato salad  
                    - ☕ Evening Snack: Roasted chana + green tea  
                    - 🍽️ Dinner: Brown rice + lauki sabzi + plain low-fat curd  
                    """)

                st.markdown("### 🧔 Male – Non-Vegetarian")
                st.markdown("""
                    - 🏋️ Early Morning Workout: 30 mins walk or light swimming  
                    - 🍽️ Breakfast: Boiled eggs (2) + oats with almonds + green tea  
                    - 🥤 Mid-Morning Snack: Apple + 1 tsp flaxseed powder in water  
                    - 🍽️ Lunch:  
                        - Brown rice  
                        - Grilled fish (salmon/mackerel for omega-3)  
                        - Steamed spinach + salad  
                    - ☕ Evening Snack: Roasted pumpkin seeds + herbal tea  
                    - 🍽️ Dinner: Quinoa + boiled egg whites + sautéed vegetables  
                    """)

            with col2:
                st.markdown("### 👩 Female – Vegetarian")
                st.markdown("""
                    - 🏋️ Early Morning Workout: Pranayama + gentle walk  
                    - 🍽️ Breakfast: Ragi porridge with chia seeds + 5 soaked almonds  
                    - 🥤 Mid-Morning Snack: Pomegranate seeds or papaya  
                    - 🍽️ Lunch:  
                        - 1 bajra roti  
                        - Moong dal  
                        - Mixed veg curry  
                        - Cucumber salad  
                    - ☕ Evening Snack: Buttermilk with mint + roasted chana  
                    - 🍽️ Dinner: Brown rice + lauki curry + 1 tsp flaxseed powder in water before bed  
                    """)

                st.markdown("### 👩 Female – Non-Vegetarian")
                st.markdown("""
                    - 🏋️ Early Morning Workout: Yoga, breathing exercises (20–25 mins)  
                    - 🍽️ Breakfast: Vegetable upma + 1 boiled egg  
                    - 🥤 Mid-Morning Snack: Orange slices or papaya  
                    - 🍽️ Lunch:  
                        - 1 multigrain roti  
                        - Grilled fish (salmon or rohu)  
                        - Steamed greens + salad  
                    - ☕ Evening Snack: Buttermilk with a pinch of roasted jeera  
                    - 🍽️ Dinner: Quinoa + sautéed vegetables + 1 egg white omelet  
                    """)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP: RAP')

    with col2:
        PPQ = st.text_input('MDVP: PPQ')

    with col3:
        DDP = st.text_input('Jitter: DDP')

    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')

    with col3:
        APQ = st.text_input('MDVP: APQ')

    with col4:
        DDA = st.text_input('Shimmer: DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)
        if parkinsons_prediction[0] == 1:
            st.subheader("🧠 Parkinson's - Diet Recommended")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🧔 Male – Vegetarian")
                st.markdown("""
                - 🏋️ Workout: Balance and flexibility exercises (Tai Chi, yoga)  
                - 🍽️ Breakfast: 1 egg omelet + whole grain toast + walnuts  
                - 🥤 Mid-Morning Snack: Banana + turmeric milk  
                - 🍽️ Lunch:  
                    - Millets or quinoa  
                    - Grilled chicken breast  
                    - Stir-fried broccoli and bell peppers  
                - ☕ Evening Snack: Sunflower seeds + lemon water  
                - 🍽️ Dinner: Fish stew (light oil) + mixed green salad  
                """)

                st.markdown("### 🧔 Male – Non-Vegetarian")
                st.markdown("""
                - 🏋️ Workout: Stretching + coordination exercises (20–30 mins)  
                - 🍽️ Breakfast: Boiled eggs + oats chilla + walnut pieces  
                - 🥤 Mid-Morning Snack: Banana + turmeric milk (½ glass)  
                - 🍽️ Lunch:  
                    - Quinoa  
                    - Chicken breast (grilled or stewed)  
                    - Steamed broccoli and carrots  
                - ☕ Evening Snack: Pumpkin seeds + lemon water  
                - 🍽️ Dinner: Fish curry (low oil) + small portion brown rice + sautéed spinach  
                """)

            with col2:
                st.markdown("### 👩 Female – Vegetarian")
                st.markdown("""
                - 🏋️ Workout: Tai Chi or gentle yoga  
                - 🍽️ Breakfast: Ragi porridge with chia seeds  
                - 🥤 Mid-Morning Snack: Dates (1–2) + almond milk  
                - 🍽️ Lunch:  
                    - Millets (like jowar)  
                    - Rajma or kala chana  
                    - Mix veg (carrot, beans, peas)  
                - ☕ Evening Snack: Herbal tea + flaxseed ladoo  
                - 🍽️ Dinner: Moong dal soup + beetroot salad + 1 phulka  
                """)

                st.markdown("### 👩 Female – Non-Vegetarian")
                st.markdown("""
                - 🏋️ Workout: Yoga + light mobility exercises  
                - 🍽️ Breakfast: Poha with peas + 5 almonds  
                - 🥤 Mid-Morning Snack: Coconut water + dates (1–2)  
                - 🍽️ Lunch:  
                    - Jowar roti  
                    - Rajma or chole  
                    - Beetroot and spinach sabzi  
                - ☕ Evening Snack: Herbal tea + sesame seed ladoo  
                - 🍽️ Dinner: Moong dal + sautéed pumpkin + 1 tsp flaxseed powder  
                """)
