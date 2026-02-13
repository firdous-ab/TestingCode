# ui/app.py
import streamlit as st
import requests

API = "http://localhost:8000"

st.title("Learning Assistant (POC)")

student_id = st.text_input("Student ID", "stu_001")
module_id = st.text_input("Module", "module_1")
lesson_id = st.text_input("Lesson", "1.4")
concepts_raw = st.text_area("Weak concepts (one per line)", "what is data\ntypes of data")
interests_raw = st.text_input("Interests (comma-separated)", "football, crochet")

weak_concepts = [c.strip() for c in concepts_raw.splitlines() if c.strip()]
interests = [i.strip() for i in interests_raw.split(",") if i.strip()]

if "session" not in st.session_state:
    st.session_state.session = {}

if st.button("Generate explanations + questions"):
    payload = {
        "student_id": student_id,
        "student_level": "beginner",
        "student_interests": interests,
        "module_id": module_id,
        "lesson_id": lesson_id,
        "weak_concepts": weak_concepts,
        "answers": None,
    }
    r = requests.post(f"{API}/reinforce", json=payload, timeout=60)
    r.raise_for_status()
    st.session_state.session = r.json()

data = st.session_state.session
if data:
    st.subheader("Session")
    for item in data["items"]:
        concept = item["concept"]
        st.markdown(f"### {concept}")
        st.write(item["explanation"])
        st.info(item["question"])

        ans_key = f"ans_{concept}"
        answer = st.text_input("Student answer", key=ans_key)

        if st.button(f"Grade: {concept}", key=f"grade_{concept}"):
            payload = {
                "student_id": student_id,
                "student_level": "beginner",
                "student_interests": interests,
                "module_id": module_id,
                "lesson_id": lesson_id,
                "weak_concepts": [concept],
                "answers": {concept: answer},
            }
            r = requests.post(f"{API}/reinforce", json=payload, timeout=60)
            r.raise_for_status()
            graded = r.json()["items"][0]
            st.success(f"Score: {graded['score']} | Passed: {graded['passed']}")
            st.write(graded["feedback"])
