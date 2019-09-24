from django.conf.urls import url,include
# from .api import AuthorDetail, AuthorList
from .api import AuthorViewSet
from rest_framework.routers import DefaultRouter

# author_list = AuthorViewSet.as_view({
#         # 'get': 'list',
#         'get': 'retrieve',
# })

# author_detail = AuthorViewSet.as_view(
#     {
#         # 'get': 'retrieve',
#         'get': 'list',
#         'post': 'create',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy',
#     }
# )

router = DefaultRouter()
router.register(r'^authors', AuthorViewSet)

urlpatterns = []

# urlpatterns += [
#     # url(r'^author_list/$', AuthorList.as_view(), name="author_list"),
#     # url(r'^author_detail/(?P<pk>[0-9]+)/$', AuthorDetail.as_view(), name="author_detail"),
#     # url(r'^author_list/$', author_list, name="author_list"),
#     # url(r'^author_detail/(?P<pk>[0-9]+)/$', author_list, name="author_detail"),
#     # url(r'^author_list/$', author_detail, name="author_list"),
#     # url(r'^author_detail/(?P<pk>[0-9]+)/$', author_detail, name="author_detail"),
#     url(r'^', include(router.urls)),
# ]
urlpatterns += router.urls