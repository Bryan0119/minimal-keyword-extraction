from keybert._utils import NotInstalled
from keybert.llm._base import BaseRepresentation
from keybert.llm._textgeneration import TextGeneration


# OpenAI Generator
try:
    from keybert.llm._openai import OpenAI
except ModuleNotFoundError:
    msg = "`pip install openai` \n\n"
    OpenAI = NotInstalled("OpenAI", "openai", custom_msg=msg)

# Cohere Generator
try:
    from keybert.llm._cohere import Cohere
except ModuleNotFoundError:
    msg = "`pip install cohere` \n\n"
    Cohere = NotInstalled("Cohere", "cohere", custom_msg=msg)

# LangChain Generator
try:
    from keybert.llm._langchain import LangChain
except ModuleNotFoundError:
    msg = "`pip install langchain` \n\n"
    LangChain = NotInstalled("langchain", "langchain", custom_msg=msg)

# LiteLLM
try:
    from keybert.llm._litellm import LiteLLM
except ModuleNotFoundError:
    msg = "`pip install litellm` \n\n"
    LiteLLM = NotInstalled("LiteLLM", "litellm", custom_msg=msg)


__all__ = [
    "BaseRepresentation",
    "Cohere",
    "OpenAI",
    "TextGeneration",
    "LangChain",
    "LiteLLM"
]
