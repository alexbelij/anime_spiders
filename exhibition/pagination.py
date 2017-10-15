from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagesCountPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response(
            {
                'count': self.page.paginator.count,
                'pagesCount': self.page.paginator.num_pages,
                'results': data,
            }
        )
