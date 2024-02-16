import os

from llama_index import ServiceContext
# from llama_index.llms import OpenAI
from llama_index.llms import AzureOpenAI
from llama_index.embeddings import AzureOpenAIEmbedding

def create_base_context():
    return ServiceContext.from_defaults(
        llm=AzureOpenAI(
            engine=os.getenv("AZURE_ENGINE"),
            model=os.getenv("MODEL", "gpt-3.5-turbo"),
            api_key=os.getenv("OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION")
        ),
        embed_model=AzureOpenAIEmbedding(
            model=os.getenv("AZURE_EMBEDDING_MODEL"),
            deployment_name=os.getenv("AZURE_EMBEDDING_DEPLOYMENT_NAME"),
            api_key=os.getenv("OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION")
        ),
    )
