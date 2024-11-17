# Streamlit Fitness Tracker
import streamlit as st
import pygame
import random

# Initialize Streamlit leaderboard
if 'leaderboard' not in st.session_state:
    st.session_state['leaderboard'] = {}

# Fitness questions and options
questions = [
    {"question": "How often do you exercise?", "options": ["Rarely", "Sometimes", "Regularly"], "key": "exercise_frequency"},
    {"question": "How balanced is your diet?", "options": ["Unhealthy", "Average", "Healthy"], "key": "diet_balance"},
    {"question": "How much water do you drink daily?", "options": ["<3L", "3-4L", ">4L"], "key": "water_intake"},
    {"question": "How much sleep do you get per night?", "options": ["<5 hours", "5-7 hours", "7-9 hours"], "key": "sleep_duration"},
]

# Generate fitness recommendations
def generate_recommendations(answers):
    recommendations = []
    if answers.get("exercise_frequency") == "Rarely":
        recommendations.append("Start with 10-minute daily walks.")
    elif answers.get("exercise_frequency") == "Sometimes":
        recommendations.append("Add 20-minute cardio sessions thrice a week.")
    elif answers.get("exercise_frequency") == "Regularly":
        recommendations.append("Incorporate strength training or yoga.")

    if answers.get("diet_balance") == "Unhealthy":
        recommendations.append("Include more vegetables and lean proteins.")
    elif answers.get("diet_balance") == "Average":
        recommendations.append("Reduce processed foods and eat more whole grains.")
    elif answers.get("diet_balance") == "Healthy":
        recommendations.append("Maintain your healthy eating habits.")

    if answers.get("water_intake") == "<3L":
        recommendations.append("Drink at least 4 liters of water daily.")
    elif answers.get("water_intake") == "3-4L":
        recommendations.append("Keep up with your hydration!")
    elif answers.get("water_intake") == ">4L":
        recommendations.append("Excellent hydration level. Keep it up!")

    if answers.get("sleep_duration") == "<5 hours":
        recommendations.append("Aim for 7-9 hours of sleep each night.")
    elif answers.get("sleep_duration") == "5-7 hours":
        recommendations.append("Try to get consistent 7-8 hours of sleep.")
    elif answers.get("sleep_duration") == "7-9 hours":
        recommendations.append("Great sleep routine. Maintain it!")

    return recommendations


# Display leaderboard
def display_leaderboard():
    st.subheader("Leaderboard")
    sorted_leaderboard = sorted(st.session_state['leaderboard'].items(), key=lambda x: x[1], reverse=True)
    for rank, (name, points) in enumerate(sorted_leaderboard, start=1):
        st.write(f"{rank}. {name} - {points} points")

# Wellness Tips and Activities
def wellness_section():
    wellness_tips = [
        "Take a deep breath and relax for a moment.",
        "Remember to stay hydrated. A glass of water can do wonders.",
        "Consider journaling to express your thoughts and emotions.",
        "Enjoy a moment of silence and stillness.",
        "Just relax and listen to some calming music.",
        "Step away from your device and have a small digital detox.",
        "Take a short nap to recharge your battery.",
        "Eat a healthy snack.",
        "Listen or chant some positive affirmations.",
        "Talk to friends or families."
    ]
    st.subheader("Your Wellness Tip for Today:")
    st.write(random.choice(wellness_tips))

    # Mood selection
    mood = st.radio("Select your mood:", ["Happy", "Okay", "Sad", "Stressed", "Angry"])
    if mood == "Happy":
        st.write("That's great! Keep up the positivity!")
    elif mood == "Okay":
        st.write("It's good to take it one step at a time. You're doing great!")
    elif mood == "Sad":
        st.write("It's okay to feel this way. Take care of yourself and remember things will get better.")
    elif mood == "Stressed":
        st.write("Take a moment to breathe and relax. Focus on something positive.")
    elif mood == "Angry":
        st.write("Try to let go of the frustration. A deep breath can help, or you can listen to some calming music.")

    # Suggest a relaxation activity
    if st.button("Show Me a Relaxation Activity"):
        relaxation_activities = [
            "Close your eyes and take 10 deep breaths.",
            "Stretch your arms and legs for a minute.",
            "Do a quick 5-minute meditation.",
            "Visualize a peaceful scene like a beach or forest.",
            "Listen to calming music or nature sounds."
        ]
        st.write(random.choice(relaxation_activities))

# Streamlit app
st.title("ZzenFit")
st.subheader("FITNESS")

# User input for name
user_name = st.text_input("Enter your name:")

if user_name:
    st.header("Answer Fitness Questions")
    answers = {}
    for q in questions:
        answers[q["key"]] = st.selectbox(q["question"], q["options"], key=q["key"])

    if st.button("Generate Recommendations"):
        recommendations = generate_recommendations(answers)
        st.subheader("Your Personalized Fitness Plan")
        for rec in recommendations:
            st.write(f"- {rec}")

    st.header("Wellness & Relaxation")
    wellness_section()

else:
    st.warning("Please enter your name to proceed!")
