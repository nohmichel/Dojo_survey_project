from django.shortcuts import render, redirect
 
def index(request):
	return render(request, "index.html")

# def front_page(request):
# 	return render(request, "result_index.html")

def result_index(request):
	if request.method == "POST":
	# print("user submitted form")
	# print(request.POST)
	# print(request.POST['user_name'])
	# request.session['name']= request.POST['user_name']
	# results=respond.GET["location"]
	# request.session['comment']= request.POST['comment']
		context={
			'user_name':request.POST['user_name'],
			'location':request.POST['location'],
			'language':request.POST['language'],
			'comment':request.POST['comment'],
		}
	return render(request,"result_index.html", context)


