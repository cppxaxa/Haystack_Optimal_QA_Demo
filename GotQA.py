from haystack import Finder
from haystack.indexing.cleaning import clean_wiki_text
from haystack.indexing.utils import convert_files_to_dicts, fetch_archive_from_http
from haystack.reader.farm import FARMReader
from haystack.reader.transformers import TransformersReader
from haystack.utils import print_answers

# doc_dir = "data/article_txt_got"
# # # s3_url = "https://s3.eu-central-1.amazonaws.com/deepset.ai-farm-qa/datasets/documents/wiki_gameofthrones_txt.zip"
# # # fetch_archive_from_http(url=s3_url, output_dir=doc_dir)
# dicts = convert_files_to_dicts(dir_path=doc_dir, clean_func=clean_wiki_text, split_paragraphs=True)
# # # print(dicts[:1])
# # # print(len(dicts))

from haystack.database.elasticsearch import ElasticsearchDocumentStore
document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")
# document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document", 
#                                             embedding_field="embedding", embedding_dim=768)

# document_store.write_documents(dicts)

from haystack.retriever.sparse import ElasticsearchRetriever
retriever = ElasticsearchRetriever(document_store=document_store)

# from haystack.retriever.dense import DensePassageRetriever
# retriever = DensePassageRetriever(document_store=document_store,
#                                   embedding_model="dpr-bert-base-nq",
#                                   do_lower_case=True, use_gpu=True)
# # document_store.update_embeddings(retriever)

# from haystack.retriever.dense import EmbeddingRetriever
# retriever = EmbeddingRetriever(document_store=document_store,
#                                embedding_model="deepset/sentence_bert",
#                                model_format="farm")



# reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
# reader = TransformersReader(model="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased", use_gpu=-1)
# reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
# reader = FARMReader(model_name_or_path="twmkn9/albert-base-v2-squad2", use_gpu=True)
# reader = FARMReader(model_name_or_path="roberta-large", use_gpu=True)
# reader = FARMReader(model_name_or_path="csarron/mobilebert-uncased-squad-v2", use_gpu=True)
# reader = FARMReader(model_name_or_path="deepset/xlm-roberta-large-squad2", use_gpu=True)

# reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
# reader = FARMReader(model_name_or_path="deepset/xlm-roberta-large-squad2", use_gpu=True)
reader = FARMReader(model_name_or_path="twmkn9/albert-base-v2-squad2", use_gpu=True)
# reader = FARMReader(model_name_or_path="ktrapeznikov/albert-xlarge-v2-squad-v2", use_gpu=True)



finder = Finder(reader, retriever)

prediction = finder.get_answers(question="Who is the father of Arya Stark?", top_k_retriever=40, top_k_reader=5)

print_answers(prediction, details="minimal")

# print("\n\n")
# print(prediction)

