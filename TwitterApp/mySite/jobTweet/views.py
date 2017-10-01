# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from jobTweet.utils import search
from jobTweet.models import Tweet

# Create your views here.

def name(request):
	model = Tweet
	if 'search_phrase' in request.POST:
		
		#print 'Debug: %s' %request.POST['search_phrase']
		return render(request, 'index.html',{'search_phrase':search(request.POST['search_phrase'])})
	else:
		return render(request, 'index.html', {})

