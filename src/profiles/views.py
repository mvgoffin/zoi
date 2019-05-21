from django.shortcuts import render

# Create your views here.
#def home(request):
#    context = locals()
#    template = 'home.html'
#    return render(request,template,context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request,template,context)

def success(request):
    context = locals()
    template = 'success.html'
    return render(request,template,context)

def code_granted(request):
    context = locals()
    template = 'code_granted.html'
    return render(request,template,context)

def home(request):
    form = AccessForm(request.POST)

    email = request.POST.get('email')
    obj = Account.objects.create(email=email)

    if form.is_valid():

        send_mail(
        'A new LEAD',
        'From our servers, a new LEAD has been created.' +
        ': email: {}'.format(email),
        'hi@plntprotein.com',
        ['marco@plntprotein.com'],
        #fail_silently=False,
        )

        form.save()
        
        response = redirect('code_granted')
        return response
    else:
        form = AccessForm()
    
     #context = {'form': form}
     #template = 'register_mx.html'
     #return render(request,template,context)
    return render(request, 'home.html', {'form': form}) #this is render on HTML

