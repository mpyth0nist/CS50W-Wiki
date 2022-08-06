from django.urls import path

from . import views


app_name="wiki"

urlpatterns = [
    path("", views.index, name="index"),
	path("<str:title>",views.get_page, name="title"),
	path("search/",views.search ,name="search"),
	path("create/",views.create_page, name="create_page"),
	path("edit/",views.edit_page, name="edit_page"),
	path("random/",views.random_page,name="random_page")
]
