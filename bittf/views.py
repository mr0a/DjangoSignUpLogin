from django.shortcuts import render


def indexView(request):
    # mail_subject = 'Activate your blog account.'
    # message = render_to_string('acc_active_email.html', {
    #             'user': request.user,
    #             'domain': current_site.domain,
    #             'uid':urlsafe_base64_encode(force_bytes(user.pk)),
    #             'token':account_activation_token.make_token(user),
    #         })
    # to_email = 'aravindhan2413km@gmail.com'
    # email = EmailMessage(
    #     mail_subject, message, to=[to_email]
    #     )
    # email.send()
    return render(request, 'index/index.html')
