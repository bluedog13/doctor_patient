from typing import Any, List, Dict
from autogen import ConversableAgent

class PatientAgent():
    """
    A class to represent a patient agent.
    """
    def __init__(self, llm_config: List[Dict[str, Any]]) -> None:
        self._agent = ConversableAgent(
            name="patient",
            system_message="""You are a patient. You can talk to a doctor about your health problems. \
            You have a headache and want to seek treatment. \
            You can answer questions from the doctor to help them understand your symptoms. \
            """,
            llm_config={"config_list":llm_config},
            is_termination_msg=lambda msg: "exit" in msg["content"],
            human_input_mode="NEVER",
        )

    @property
    def agent(self) -> ConversableAgent:
        """
        Return the ConversableAgent object.
        """
        return self._agent