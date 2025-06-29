import streamlit as st
from agents.arena_agent import ArenaAgent
from agents.evaluator_agent import EvaluatorAgent
from prompts.challenges import ChallengePrompts
from tools import get_tools_by_name

class ChatUI:
    def __init__(self):
        if "selected_challenge" not in st.session_state:
            st.session_state.selected_challenge = "Confession Trap"
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "agent" not in st.session_state:
            self.set_agent()

    def set_agent(self):
        challenge = ChallengePrompts.CHALLENGES[st.session_state.selected_challenge]
        tools = get_tools_by_name(challenge["tools"])
        st.session_state.agent = ArenaAgent(
            model_name=challenge["model"],
            system_prompt=challenge["prompt"],
            tools=tools
        )
        st.session_state.evaluator_agent = EvaluatorAgent(
            system_prompt=challenge["evaluator_prompt"]
        )

    def launch(self):
        st.title("JailBreak Arena")

        challenge_options = {
            f"{name} - {ChallengePrompts.CHALLENGES[name]['description']}": name
            for name in ChallengePrompts.CHALLENGES
        }
        selected_label = st.selectbox("Choose a challenge:", list(challenge_options.keys()))
        selected_challenge = challenge_options[selected_label]

        if selected_challenge != st.session_state.selected_challenge:
            st.session_state.selected_challenge = selected_challenge
            self.clear()

        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        user_input = st.chat_input("Ask something:")
        if user_input:
            with st.chat_message("user"):
                st.markdown(user_input)

            response = st.session_state.agent.run(user_input)
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

            if st.session_state.evaluator_agent.run(response):
                st.balloons()
                st.success("🎉 You Win!")
                st.stop()

        if st.button("Clear chat"):
            self.clear()

    def clear(self):
        st.session_state.chat_history = []
        self.set_agent()
        st.rerun()
