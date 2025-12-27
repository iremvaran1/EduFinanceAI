# rag_demo_streamlit.py
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import pipeline
import streamlit as st

st.title("EduFinance AI – RAG Demo")
st.write("Bu sayfa yapay zekâ destekli bilgi alma (Retrieval-Augmented Generation) demo sayfasıdır.")

# Metin koleksiyonu
texts = [
    "Finansal okuryazarlık, bireylerin finansal kararlarını bilinçli şekilde verebilmelerini sağlar.",
    "Yatırım yapmak, risk ve getiri arasındaki dengeyi anlamayı gerektirir.",
    "Bütçe planlaması, kişisel mali hedeflerin gerçekleştirilmesi için temel bir adımdır.",
    "Kredi kartı borçlarını zamanında ödemek, finansal sağlığın korunması açısından önemlidir."
]

# Belgeleri böl
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = [Document(page_content=t) for t in texts]

# Embedding
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embeddings)

# Model
model = pipeline(
    "text-generation",
    model="murat/bert2bert-turkish-summarization",
    max_new_tokens=150
)
llm = HuggingFacePipeline(pipeline=model)

# RAG zinciri
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Streamlit input/output
query = st.text_input("🧠 Sorunuzu yazın:")
if query:
    result = qa.run(query)
    st.write(f"🤖 Yanıt: {result}")
