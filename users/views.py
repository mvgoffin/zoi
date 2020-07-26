from django.shortcuts import render
from forms import contactformemail
from django.core.mail import send_mail

def contactsendmail(request):
    if request.method=="GET":
        form=contactformemail()
        return render(request,'profiles/templatecontactpage.html',{'form':form})