from typing import Any, List, Dict
from autogen import ConversableAgent

class DoctorAgent():
    """
    A class to represent a doctor agent.
    """
    def __init__(self, llm_config: List[Dict[str, Any]]) -> None:
        self._agent = ConversableAgent(
            name="doctor",
            system_message="""You are a doctor with expertise in definitive diagnosis. \
            To provide an accurate diagnosis and appropriate health advice, ask one question at a time \
            to understand the patient's symptoms thoroughly. Use the information gathered to 
            offer a precise diagnosis and relevant health recommendations.
            """,
            llm_config={"config_list":llm_config},
            human_input_mode="ALWAYS"
        )

    @property
    def agent(self) -> ConversableAgent:
        """
        Return the ConversableAgent object.
        """
        return self._agent