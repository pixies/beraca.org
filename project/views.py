from rest_framework import generics, permissions, mixins, response
from django.utils.translation import ugettext_lazy as _

from .models import Project, ProjectCategory, ProjectcSupport
from .serializers import ProjectSerializer, ProjectCategorySerializer, ProjectSupportSerializer
from .tasks import project_support_request

from accounts.permissions import IsAdmin, IsManagerOrAdmin, IsManagerClientOrAdmin
from client.models import Client
from community.models import Community
from django.contrib.auth import get_user_model

from libib.elasticemail import SendElastic

User = get_user_model()

class ProjectList(mixins.ListModelMixin,
                  generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]#IsAuthenticated,]
                          #IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        if request.GET.get('product_id', ''):
            product_id = int(request.GET.get('product_id', ''))
            communities = Community.objects.filter(products=product_id)
            queryset = Project.objects.filter(community__in=communities)
            serializer = self.get_serializer(queryset, many=True)

            return response.Response(serializer.data)

        return self.list(request, *args, **kwargs)


class ProjectCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny, #IsAuthenticated,
                          IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny] #IsAuthenticated,]
                          #IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'client'):
            client_id = Client.objects.get(user=request.user).id
            project_id = kwargs.get('pk', '')
            project_support_request.delay(client_id, project_id)

            return response.Response(data={'message': _("Email enviado com sucesso")}, status=200)

        return response.Response(data={'message': _("É necessário ser cliente para apoiar um projeto")}, status=500)

class ProjectUpdate(mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['put', 'get']
    permission_classes = [permissions.AllowAny] #IsAuthenticated,]
                          #IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProjectCategoryList(mixins.ListModelMixin,
                          generics.GenericAPIView):

    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny] #IsAuthenticated,]
                         # IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectCategoryCreate(mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny, #IsAuthenticated,
                          IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectCategoryUpdate(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['get','put','delete']
    permission_classes = [permissions.AllowAny, #IsAuthenticated,
                          IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProjectCategoryDetail(mixins.RetrieveModelMixin,
                            generics.GenericAPIView):
    http_method_names = ['get']
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [permissions.AllowAny] #IsAuthenticated,]
                         # IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProjectSupportCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    http_method_names = ['post',]
    queryset = ProjectcSupport.objects.all()
    serializer_class = ProjectSupportSerializer
    #permission_classes = [permissions.AllowAny] #IsAuthenticated]

    def post(self, request, *args, **kwargs):
        obj = self.create(request, *args, **kwargs)

        '''
                E-mail dados
                    subject:
                    from_mail:
                    to_list:
                    message:
        '''
        subject = _('ReparteBR :: Apoio ao Projeto: (%s)') % (str(Project.objects.get(pk=obj.data['project']).name))
        message = _("O cliente %s (%s) demonstrou interesse no projeto '%s'. Clique aqui para ver detalhes 'http://admin.repartebr.com/project/projectcsupport/%s/change/'") % (
            str(Client.objects.get(pk=obj.data['client']).user.full_name),
            str(Client.objects.get(pk=obj.data['client']).user),
            str(Project.objects.get(pk=obj.data['project']).name),
            str(obj.data['project_support_id'])
        )

        #get user list
        user_list = User.objects.all()
        admin_user = []

        #filtering admin user in user list
        for user in user_list:
            if user.is_admin == True:
                admin_user.append(user)

        # renaming admins_user to to_list, better understanding to configure container email
        list = ''
        for email in admin_user:
            list += str(email) + '; '

        # removing ';' from the admin mailing list
        list += " " + str(Client.objects.get(pk=obj.data['client']).user)
        #list = list[0:-2]

        #print(subject, message, list)
        print(SendElastic(subject, to_list=list, html_body=message, mail_from="contato@institutoberaca.org"))
        return obj


class ProjectSupportList(mixins.ListModelMixin, generics.GenericAPIView):
    http_method_names = ['get',]
    queryset = ProjectcSupport.objects.all()
    serializer_class = ProjectSupportSerializer
    permission_classes = [permissions.AllowAny] #IsAuthenticated]

    def get(self, request):
        return self.list(request)

class ProjectSupportDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    http_method_names = ['get',]
    queryset = ProjectcSupport.objects.all()
    serializer_class = ProjectSupportSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


from django.shortcuts import HttpResponseRedirect, render

