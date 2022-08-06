from django.shortcuts import redirect,render
import markdown2
from . import util
import string
from . import forms
import random


# Creating a search form 

form = forms.SearchForm()

def index(request):

	'''
	This function renders the index page of the app	
	'''

	return render(request, "encyclopedia/index.html",{"entries": util.list_entries(),"form":form})

def get_page(request,title):

	'''
	This function as named get a particular page depending on the title given to it 
	
	'''

	# This part of code is for preventing the function from being Case-sensitive	
	page = util.get_entry(title)
	
	if page == None:
		return render(request,"encyclopedia/error.html",{"error":"Error 404","content":"This Page is not found","title":title,"form":form})

	return render(request,"encyclopedia/titlepage.html", { "content":markdown2.markdown(util.get_entry(title)),
			"title":title,
			"form":form })


def search(request):
	'''
	This function search for the corresponding files/entries names for the search query given by the user by:
	
	1. Checking if the search query have the same name as the file
	
	2. Or if the query is a part of a filename or multiple filesnames

	3. if the search query doesn't exist it renders an error page

	'''	

	if request.method == 'GET':
		form = forms.SearchForm(request.GET)	
		
		if form.is_valid():
			
			# Storing all the names of the files we have

			all_entries=util.list_entries()

			# Storing the user's input	

			searchquery = form.cleaned_data["search"].lower()
			
			# Storing all the filenames identical to the input or the input is a part of it   
	
			results=[filename for filename in all_entries if searchquery in filename.lower()]
			
			# If the input and the filename is identical	

			if len(results) == 1 and results[0].lower() == searchquery:

				return get_page(request,results[0])
			
			# If there is no files with such name ( search query ) 

			elif len(results) == 0:

				return render(request,"encyclopedia/search_results.html",{"error":"Sorry there is no results given for this","form":form , "title":"Search Results"})
			
			# If the input is a part of one/multi filenames	

			else:

				return	render(request,"encyclopedia/index.html",{"entries":results , "form":form ,"title":"Search results"})	 

def create_page(request):
	
	if request.method == 'GET':
		articleForm = forms.CreatePage()
		return render(request,"encyclopedia/create_page.html",{"article_form":articleForm,"title":"Create a new page","form":form})

	else:

		pageForm = forms.CreatePage(request.POST)
		if pageForm.is_valid():	

			title = pageForm.cleaned_data["title"]
			content = pageForm.cleaned_data["article"]
			
			for entry in util.list_entries():
				if title.lower() == entry.lower():
					return render(request,"encyclopedia/create_page.html",{"article_form":pageForm,"title":"Create New page","form":form})

			util.save_entry(title,content)
			
			return get_page(request,title) 
		
def edit_page(request):
	#TODO
	editPage = forms.EditPage()		
	return render(request,"encyclopedia/edit.html",{"edit_page":editPage,"form":form})		
	
def random_page(request):
	all_entries = util.list_entries()	
	page = random.choice(all_entries)
	return get_page(request,page)
