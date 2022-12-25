from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
# Create your views here.

def home(request):
    allposts = Post.objects.all()
    context = {'allposts' : allposts}
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages.success(request, 'Message sent Successfully')
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        allposts = Post.objects.none()
    else:
        allpoststitle = Post.objects.filter(title__icontains=query)
        allpostscontent = Post.objects.filter(content__icontains=query)
        allposts = allpoststitle.union(allpostscontent)
        params = {'allposts' : allposts, 'query' : query}
        return render(request, 'home/search.html', params)

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters.')
            return redirect('home')
        if not username.isalnum() :
            messages.error(request, 'Username only contains letters and numbers. Account not created')
            return redirect('home')
        if not username.islower() :
            messages.error(request, 'Username contains only lower characters')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your account created successfully')
        return redirect('/')

    else:
        return HttpResponse('404 - Not Allowed')

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged In')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials')
        return redirect('home')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Succesfully Logged Out')
    return redirect('home')