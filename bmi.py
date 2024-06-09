# a) Making an function that calculates bmi by given user's input.
def bmi_calculator(height,weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Under Weight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Over Weight"
    else:
        category = "Obesity"

    return bmi,category

# Calling the function and  printing the Result.
__name__ = "__main__" 
height = 1.61
weight = 30
bmi,category = bmi_calculator(height,weight)
print(f"Your BMI is {bmi}.2f and Your Category is {category}")

# b) Making an streamlit UI.

import streamlit as st
def main():
    st.title("BMI CALCULATOR")
    st.write("Please Enter the weight in (kg) and height in (m).")
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (m)")
    if st.button("Calculate BMI"):
        bmi,category = bmi_calculator(height,weight)
        st.write(f"Your BMI is {bmi}.2f and Your Category is {category}")
if __name__ == "__main__":
    main()  

























































# import streamlit as st
# def main():
#     st.title("BMI Calculator")
#     st.write("Please enter your weight in kilograms (kg) and your height in meters (m).")
#     weight = st.number_input("Weight (kg)")
#     height = st.number_input("Height (m)")
#     if st.button("Calculate BMI"):
#         bmi, category = bmi_calculator(height, weight)
#         st.write(f"Your BMI is {bmi:.2f}. You are in the '{category}' category.")

# if __name__ == "__main__":
#     main()






























































# b) 

# st.title("BMI Calculator")
# st.write("Please enter your weight in kilograms (kg) and your height in centimeters (cm).")
# weight = st.number_input("Weigth (kg)")
# height = st.number_input("Height (m)")
# if st.button("Calculate BMI"):
#     bmi,category