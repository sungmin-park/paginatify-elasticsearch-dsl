from elasticsearch_dsl import DocType, Index, Integer
from elasticsearch_dsl.connections import connections

from paginatify_elasticsearch_dsl import Pagination

conn = connections.create_connection(hosts=['localhost'])

index = Index('test-paginatify-elasticsearch-dsl')


@index.doc_type
class Item(DocType):
    id = Integer(index='not_analyzed')


def paginate(count, page=1):
    if conn.indices.exists(index._name):
        index.delete()
    index.create()
    try:
        Item.init()
        for i in range(1, count + 1):
            Item(id=i, meta={'id': i}).save(refresh=True)
        return Pagination(Item.search().sort('id'), page=page,
                          map_=lambda x: x.id,
                          per_page=3, per_nav=3)
    finally:
        index.delete()


def test_len():
    assert paginate(0).total == 0
    assert paginate(10).total == 10


def test_getitem():
    assert paginate(0).items == []
    assert paginate(10, 2).items == [4, 5, 6]


def test_result_set():
    assert paginate(0).result_set.hits.total == 0
    assert paginate(10, 2).result_set.hits.total == 10
    assert len(paginate(10, 2).result_set.hits) == 3
