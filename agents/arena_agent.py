import os
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.schema import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langchain_core.runnables.history import RunnableWithMessageHistory


class ArenaAgent:

    def __init__(self, model_name=None, system_prompt=None, tools=[]):
        self.llm = ChatGroq(model=model_name, api_key=os.getenv("GROQ_API_KEY"))
        self.max_history = 50
        self.histories = {}

        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

        agent = create_tool_calling_agent(
            llm=self.llm,
            tools=tools,
            prompt=prompt,
        )

        base_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=5)

        self.executor = RunnableWithMessageHistory(
            base_executor,
            lambda session_id: self._get_history(session_id),
            input_messages_key="input",
            history_messages_key="chat_history",
        )

    def run(self, user_input: str) -> str:
        result = self.executor.invoke({"input": user_input}, config={"configurable": {"session_id": "arena"}})
        return result["output"]

    def _get_history(self, session_id):
        if session_id not in self.histories:
            self.histories[session_id] = InMemoryChatMessageHistory()
        history = self.histories[session_id]
        if len(history.messages) > self.max_history:
            history.messages = history.messages[-self.max_history:]
        return history

