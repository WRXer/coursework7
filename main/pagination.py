from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """
    Пагинация
    """
    page_size = 5
