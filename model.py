from langchain.chat_models import ChatOpenAI
from prompts import (
    SYSTEM_DEFAULT_PROMPT
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class HistoryModel:
    def __init__(self, conversation_type: str = "creative", stream: bool = False, callback_handler: type(StreamingStdOutCallbackHandler) = None):
        temperature = 0.5  # Balanced
        if conversation_type == "creative":
            temperature = 0.9  # Creative
        elif conversation_type == "precise":
            temperature = 0.05  # Precise
        self.chat = ChatOpenAI(
            temperature=temperature,
            model_name="gpt-3.5-turbo",
            max_tokens=1000,
            verbose=False,
            streaming=stream, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
        )

    def get_response(self, input: str, chat_history: list):
        prompt = [
            SystemMessage(content=SYSTEM_DEFAULT_PROMPT),
            HumanMessage(content=input)
        ]
        response = self.chat(prompt)
        return response


if __name__ == "__main__":
    import sys
    from typing import Any, Dict, List
    class OutputStreamingStdOutCallbackHandler(StreamingStdOutCallbackHandler):

        def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
            sys.stdout.write(token)
            sys.stdout.flush()

        def on_llm_start(
            self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
        ) -> None:
            """Run when LLM starts running."""
            print("LLM STARTED")
            print("SERIALIZED: ", serialized)
            print("PROMPTS: ", prompts)
            print("KWARGS: ", kwargs)

    model = HistoryModel(stream=True, callback_handler=OutputStreamingStdOutCallbackHandler)
    print(model.get_response("Hitler getting into vienna art college", []))

