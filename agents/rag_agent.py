import ollama
from config import OLLAMA_MODEL

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def rag_agent(state):

    query = state["query"]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )

    docs = db.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Use ONLY the provided document.

If the answer is not present,
say:

'Information not found in SOP.'

Document:

{context}

Question:

{query}
"""

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {

        "response": response["message"]["content"]

    }