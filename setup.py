from setuptools import setup

setup(
        name='paginatify-elasticsearch-dsl',
        version='0.0.2',
        packages=['paginatify_elasticsearch_dsl'],
        zip_safe=False,
        install_requires=['paginatify', 'elasticsearch-dsl>=0.0.9']
)
