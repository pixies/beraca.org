from rest_framework import generics, mixins, permissions
from django.shortcuts import render

from django.contrib.auth.models import User

from .models import Profile, Client
from client.api.serializers import ProfileSerializer, ProfileDetailSerializer, ClientSerializer, ClientDetailSerializer, ClientListSerializer
from client.api.permissions import IsAdmin, IsClientOrAdmin, IsProfileOwner, IsClientOwner

def home(request):
    """
    Return home page
    """
    return render(request, '.well-known/pki-validation/godaddy.html')

class ProfileList(mixins.ListModelMixin,
                  generics.GenericAPIView):

    http_method_names = ['get', ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):

    http_method_names = ['post', ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProfileDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsProfileOwner]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ClientList(mixins.ListModelMixin,
                 generics.GenericAPIView):

    http_method_names = ['get',]
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [permissions.AllowAny]
#   permission_classes = [permissions.IsAuthenticated,]
#                         IsAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class ClientCreate(mixins.CreateModelMixin,
                   generics.GenericAPIView):

    http_method_names = ['post',]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]
#    permission_classes = [permissions.IsAuthenticated,
#                          IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):

    http_method_names = ['get', 'put', 'delete']
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated,
    #                      IsClientOrAdmin,
    #                      IsClientOwner]



    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class ClientDetailProjects(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):

    http_method_names = ['get', 'put', 'delete']
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated,
    #                      IsClientOrAdmin,
    #                      IsClientOwner]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def index(request):
    return render(request, 'client.html', {})


from django.conf import settings
from django.shortcuts import redirect

def search(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    else:
        return render(request, 'search.html', {})


from django.http import HttpResponse
from django.http import JsonResponse

def get_products_per_client(request):

    client = Client.objects.get(pk=int(request.user.client.id))
    #print(  request.user.client.id)
    products = client.get_products()

    data = []
    for product in products:
        data.append({'id': product.id, 'common_name': product.common_name})

    from json import dumps
    #print(dumps(data))
    return JsonResponse(data, safe=False)

def projeto_detalhe(request, pk):

    from project.models import Project, ProjectPicture
    projeto = Project.objects.get(pk=pk)
    images = ProjectPicture.objects.filter(project_id=pk)

    #rates_response = JsonResponse(projeto)
    # rates_response2 = JsonResponse(full_cat)

    context = {
        'projeto': projeto
    }


    print(type(images.all()))
    #return HttpResponse(rates_response)
    return render(request, 'projectpage.html', context=context )

def get_projects_rates_per_client(request, pk):

    from project.models import Project, ProjectCategory
    print('----------------- Inicio get_projects_rates_per_client -----------------')
    projects = Project.objects.all().filter(products__in=pk)


#    p = Project.objects.all()
#    from project.models import Project, ProjectCategory
    #print(projects)
    msg = ''
    range_1 = []
    range_2 = []
    range_3 = []
    range_4 = []
    range_5 = []

    cat_1 = []
    cat_2 = []
    cat_3 = []
    cat_4 = []
    cat_5 = []

    full = {}
    full_cat = {}

    pro_1 = []
    pro_2 = []
    pro_3 = []
    pro_4 = []
    pro_5 = []
    print('passou por aqui')
    p_cat_l_1 = []
    for project in projects:

        if project.project_totals <= 10000:
            msg = 'Até 10.000,00'
            print(msg)
            range_1.append(project.id)
            #range_1.append(project.get_category())
            full[msg] = range_1
            cat_1.append(project.id)
            full_cat[str(project.get_category())] = cat_1
            print(project.id, project.project_totals)
        elif  10000 < project.project_totals <= 30000:
            msg = 'De 10.000,00 até 30.000,00'
            range_2.append(project.id)
            print(msg)
            #range_2.append(project.get_category())
            full[msg] = range_2
            cat_2.append(project.id)
            full_cat[str(project.get_category())] = cat_2
            print(project.id, project.project_totals)
        elif  30000 < project.project_totals <= 40000:
            msg = 'De 30.000,00 até 40.000,00'
            print(msg)
            range_3.append(project.id)
            #range_3.append(project.get_category())
            full[msg] = range_3
            cat_3.append(project.id)
            full_cat[str(project.get_category())] = cat_3
            print(project.id, project.project_totals)
        elif  40000 < project.project_totals <= 50000:
            msg = 'De 40.000,00 até 50.000,00'
            print(msg)
            range_4.append(project.id)
            #range_4.append(project.get_category())
            full[msg] = range_4
            cat_4.append(project.id)
            full_cat[str(project.get_category())] = cat_4
            print(project.id, project.project_totals)
        elif  project.project_totals > 50000:
            msg = 'Acima 50.000,00'
            print(msg)
            range_5.append(project.id)
            #range_5.append(project.get_category())
            full[msg] = range_5
            cat_5.append(project.id)
            full_cat[str(project.get_category())] = cat_5
            print(project.id, project.project_totals)


    #full['categories'] = full_cat
    #print(full)

    print('----------------- fim get_projects_rates_per_client ------------------')
    rates_response = JsonResponse(full)
    #rates_response2 = JsonResponse(full_cat)

    #print(rates_response)
    #print(rates_response2)

    return HttpResponse(rates_response)





from project.models import Project

def get_categorie(request, pk):
    print(pk);

    categoria_id = pk.split(',')


    print('----------------- Inicio get_projects_per_categorie -----------------')
    

    projects = Project.objects.filter(pk__in=categoria_id)

    cat_projes = {

        'social': [],
        'infraestrutura': [],
        'exclusiva': []

    }

    for project in projects:
        if project.get_category() == 'social' or project.get_category() == 'Social' :
            cat_projes['social'].append(project.id)
        if project.get_category() == 'infraestrutura' or project.get_category() == 'Infraestrutura' :
            cat_projes['infraestrutura'].append(project.id)
        if project.get_category() == 'exclusivo' or project.get_category() == 'Exclusivo' :
            cat_projes['exclusiva'].append(project.id)

    print(cat_projes)

    full_cat = {
            'p':'p'
        }

    n_dic = {}
    l = []
    for key in cat_projes:
        if len(cat_projes[key]) != 0:
            n_dic[key] = cat_projes[key]
        
        

    print('lista')
    print(l)
    print(n_dic)
    #n_dic['url'] = categoria_id
    print(cat_projes)


    rates_response2 = JsonResponse(n_dic)
    print('----------------- fim get_projects_per_categorie ----------------- ')
    return HttpResponse(rates_response2)


"""
    #return projects
    range = []
    range_1 = []
    range_2 = []
    range_3 = []
    range_4 = []
    range_5 = []

    def get_range(project):

        if project.project_totals <= 10000:  # <= 10000:
            return range_1.append(project.project_totals)

        elif 10000 > project.project_totals <= 30000:
            return range_2.append(project.project_totals)

        elif 10000 > project.project_totals <= 30000:
            return range_3.append(project.project_totals)

        elif 30000 > project.project_totals <= 50000:
            return range_4.append(project.project_totals)

        elif project.project_totals > 50000:
            return range_5.append(project.project_totals)

        print(' Ate 10k {0} 2 {1} 3 {2} 4 {3} Acima de 50k {4}'.format(range_1, range_2, range_3, range_4, range_5))

        


    for project in projects:
        print(get_range(project))
     #   print(project.project_totals)




    return HttpResponse(projects)



"""
"""
   for project in projects:
        if project.project_totals <= 10000: # <= 10000:
            print(1)
            print(msg)
        elif 10000 > project.project_totals <= 30000:
            print(2)
            print(msg)

        elif 10000 > project.project_totals <= 30000:
            print(3)
            print(msg)

        elif 30000 > project.project_totals <= 50000:
            print(4)
            print(msg)

        elif project.project_totals > 50000:
            print(5)
            print(msg)

    if msg_1:
        print(msg_1)
        #else:

#            range_list6 = []
#            msg = ''
#            total_pro = []
#            print(project.name)
#            print(project.project_totals)
#            print('Saindo')

        #rates[msg] = {
                #'id': project.id,
                #'project_totals': project.project_totals,
        #        'valor': project.project_totals,
        #        'select_msg': msg,
        #        'ranges': range_list,

                #dict_projects['id']: 1,
                #str(dict_projects["project_totals"]): str(project.project_totals),
        #}

        rates[msg] = {
            'projects': total_pro,
        }


    rates_response = JsonResponse(rates)

    return HttpResponse(rates_response)

"""
from libib.elasticemail import SendElastic





def apoio_project(request, pk, pk2):

    from project.models import ProjectcSupport, Project
    from django.utils.translation import ugettext_lazy as _
    
    """
        <input type="hidden" name="id_cliente" value="{{ user.client.id }}">
        <input type="hidden" name="id_projeto" value="{{ projeto.id }}">                    
    """

    id_client = pk #request.POST['id_cliente']
    id_projeto = pk2 #request.POST['id_projeto']

    print(id_client)
    print(id_projeto)
    projeto = Project.objects.get(pk=id_projeto)
    cliente = Client.objects.get(pk=id_client)
    print(projeto.name)

    
    obj,created = ProjectcSupport.objects.get_or_create(project_id=id_projeto, client_id=id_client)


    """
        Send msg

        subject = _('ReparteBR :: Apoio ao Projeto: (%s)') % (str(Project.objects.get(pk=obj.data['project']).name))
        message = _("O cliente %s (%s) demonstrou interesse no projeto '%s'. Clique aqui para ver detalhes 'http://admin.repartebr.com/project/projectcsupport/%s/change/'") % (
        str(Client.objects.get(pk=obj.data['client']).user.full_name),
        str(Client.objects.get(pk=obj.data['client']).user),
        str(Project.objects.get(pk=obj.data['project']).name),
        str(obj.data['project_support_id'])
    )
        SendElastic(subject, to_list=list, html_body=message, mail_from="contato@institutoberaca.org")
    
    """
    from django.contrib.auth import get_user_model
    User = get_user_model()

    subject = _('Institutoberaca :: Apoio ao Projeto: (%s)') % (projeto.name)
    message = _("O cliente %s (%s) demonstrou interesse no projeto '%s'. Clique aqui para ver detalhes 'http://admin.repartebr.com/project/projectcsupport/%s/change/'") % (
                cliente.user.full_name,
                cliente.user,
                projeto.name,
                str(obj.project_support_id)
            )
    #print(subject)
    #print(message)
    
    user_list = User.objects.all()
    print('user list' + str(user_list))
    admin_user = []

    #filtering admin user in user list
    for user in user_list:
        if user.is_admin == True:
            admin_user.append(user)

    # renaming admins_user to to_list, better understanding to configure container email
    list = ''
    for email in admin_user:
        list += str(email) + '; '

    list = list[:-1]
    # removing ';' from the admin mailing list
    #list += " " + str(Client.objects.get(cliente.user))
    print('user admin ' + list[:-1])
    if created:
        context = {'Registration Successful': 'Registration Successful'}

        print(SendElastic(subject, to_list=list[:-1], html_body=message, mail_from="cleyton.flb@gmail.com"))
        print(context)
#        SendElastic(subject, to_list=list, html_body=message, mail_from="contato@institutoberaca.org")

    else:
        context = {'You already support this project': 'You already support this project'}
        #print(context)
        #print(SendElastic(subject, to_list="cleyton.flb@gmail.com", html_body=message, mail_from="cleyton.flb@gmail.com"))

#    Proj = Project.objects.get(pk=id_projeto)   
#    context['projeto'] = Proj

    context_json = JsonResponse(context)
    return HttpResponse(context_json)

#    return render(request, 'projectpage.html', context=context)
    #HttpResponse(context['msg']) 



















