from django.urls import path

from . import views


app_name="wiki"

urlpatterns = [
    path("", views.index, name="index"),
	path("<str:title>",views.get_page, name="title"),
	path("search/",views.search ,name="search"),
	path("create/",views.create_page, name="create_page"),
	path("save_page/",views.save_page,name="save_page")
]
