import streamlit as st
import openai
import json

st.set_page_config(page_title="MCP Assistant Demo", layout="centered")

st.title("🧠 MCP-Powered AI Assistant")

# User Inputs
st.header("🔧 Build Your Context")

system = st.text_area("System Role", value="You are a helpful assistant.")
user_name = st.text_input("User Name", "Alex")
user_goal = st.text_input("User Goal", "Write a travel itinerary to Japan")
chat_history = st.text_area("Message History (Optional)", value="Hi, can you help me plan a trip?")
instruction = st.text_area("Instruction", value="Provide a detailed 5-day travel plan.")

# MCP Structure
mcp_context = {
    "system": system,
    "user": {
        "name": user_name,
        "goal": user_goal
    },
    "messages": [
        {"role": "user", "content": chat_history}
    ],
    "instructions": instruction
}

st.subheader("📦 MCP Context (Structured)")
st.json(mcp_context)

# Send to Model
if st.button("🚀 Ask the Model"):
    openai.api_key = st.secrets["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"]  # add this in Streamlit Cloud secrets
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": instruction}
            ]
        )
        st.success("✅ Response from Model:")
        st.write(response.choices[0].message["content"])
    except Exception as e:
        st.error(f"❌ Error: {e}")
