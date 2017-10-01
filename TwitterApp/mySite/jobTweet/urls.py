from django.conf.urls import url
from jobTweet import views

urlpatterns = [
	url(r'^$', views.name, name='name'),
]