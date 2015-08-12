from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, streaming_bulk
from datetime import datetime


synonym_mapping = { "filter": { 
                    "synonym": {
                        "type" : "synonym",
                        "synonyms" : [
                            "i-pods, i pod => ipod",
                            "universe, cosmos"
                            ]
                        }
                    }
                }

def create_index(client):
    client.indices.create(index="synonym-test", body=synonym_mapping, ignore=400) 


if __name__ == '__main__':
    es = Elasticsearch()
    create_index(es)
    es.index(index="synonym-test", doc_type="test-type", id=42, body={any: "rohi"})
