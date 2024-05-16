import os
import dotenv

from langchain import hub
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI

dotenv.load_dotenv()

llm = AzureChatOpenAI(
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_API_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_API_KEY")
)


def load_document(document_path):
    # Load, chunk and index the contents of the pdf.
    loader = PyPDFLoader(document_path)
    pages = loader.load_and_split()

    return pages


def create_embeddings(documents):
    # creates embeddings of text in pages using chroma
    vectorstore = Chroma.from_documents(
        documents=documents, embedding=AzureOpenAIEmbeddings(
            azure_endpoint=os.environ.get("AZURE_OPENAI_API_ENDPOINT"),
            azure_deployment=os.environ.get(
                "AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
        ), persist_directory="./chroma_db"
    )

    return vectorstore


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def generate_response(question):
    prompt = hub.pull("rlm/rag-prompt")
    document = load_document("./public/constitution.pdf")

    retriever = create_embeddings(document).as_retriever()
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    result = rag_chain.invoke(question)
    # vectorstore.delete_collection()

    return result
