from celery import shared_task
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .models import Project
from client.models import Client

@shared_task
def project_support_request(client_id, project_id):
    client = Client.objects.get(id=client_id)
    project = Project.objects.get(id=project_id)

    ctx = {
        'client': client,
        'project': project
    }

    email_template = get_template('project/emails/support_request.html')
    email_content = email_template.render(ctx)
    subject = _("Novo apoiador")

    email = EmailMultiAlternatives(subject,
                                   email_content,
                                   client.user.email,
                                   [settings.DEFAULT_FROM_EMAIL],)
    email.content_subtype = 'text/html'
    email.attach_alternative(email_content, 'text/html')
    email_sent = email.send()

    return email_sent

