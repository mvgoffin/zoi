
#Contact form view

def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('profiles/templates/contact_form.text')
            content = (
                'contact_name' : request.POST.get('contact_name'),
                'contact_email' : request.POST.get('contact_email'),
                'contact_content' : request.POST.get('contact_content'),
            )

            content = template.render(content)

             email = EmailMessage(
                "New contact form email",
                content,
                "Creative Web" + '',
                ['marco.valgof@gmail.com'],
                header = {'Reply To': contact_email }
        )

        email.send()

        return redirect('thanks')

    return render(request, 'profiles/templates/contact.html', {'form':Contact_Form })
