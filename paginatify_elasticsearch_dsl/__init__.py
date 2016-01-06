from paginatify import Pagination as _Pagination


class SearchWrapper(object):
    def __init__(self, search):
        self.search = search

    def __len__(self):
        return self.search.count()

    def __getitem__(self, item):
        self.result_set = self.search.__getitem__(item).execute()
        return self.result_set


class Pagination(_Pagination):
    def __init__(self, search, **kwargs):
        wrapper = SearchWrapper(search)
        super(Pagination, self).__init__(wrapper, **kwargs)
        self.result_set = wrapper.result_set
