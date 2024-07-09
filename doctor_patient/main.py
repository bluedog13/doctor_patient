from typing import Any, List, Dict
import os
import autogen
from autogen import ConversableAgent
from autogen.agentchat.chat import ChatResult
from src.agents.patient_agent import PatientAgent
from src.agents.doctor_agent import DoctorAgent


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_llm_configs() -> List[Dict[str, Any]]:
    """
    Load the LLM configuration from the environment or a file.
    """
    llm_config = autogen.config_list_from_json(
        env_or_file="AOAI_CONFIG_LIST",
        file_location=BASE_DIR
    )w
    return llm_config


def start_conversation(doctor: ConversableAgent, patient: ConversableAgent) -> str:
    """
    Start a conversation between the doctor and the patient.
    """
    result:ChatResult = doctor.initiate_chat(
        recipient=patient,
        message="Hello how are you feeling today"
    )
    return result



if __name__ == "__main__":
    llm_configs = load_llm_configs()

    doctor_agent = DoctorAgent(llm_configs).agent
    patient_agent = PatientAgent(llm_configs).agent

    result:ChatResult = start_conversation(doctor_agent, patient_agent)
    print(result.summary)