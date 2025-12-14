import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def get_module():
    load_dotenv('../.env.local')

    token = os.getenv('API_TOKEN')
    endpoint = os.getenv('ENDPOINT')
    module_name = os.getenv('MODULE_NAME')

    module_client = ChatOpenAI(
        api_key=token,
        base_url=endpoint,
        model=module_name
    )
    return module_client