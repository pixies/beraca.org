from rest_framework import generics, mixins, permissions
from django.shortcuts import render

from django.contrib.auth.models import User

from .models import Profile, Client
from client.api.serializers import ProfileSerializer, ProfileDetailSerializer, ClientSerializer, ClientDetailSerializer, ClientListSerializer
from client.api.permissions import IsAdmin, IsClientOrAdmin, IsProfileOwner, IsClientOwner


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

def search(request):
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

    from project.models import Project
    projeto = Project.objects.get(pk=pk)

    #rates_response = JsonResponse(projeto)
    # rates_response2 = JsonResponse(full_cat)

    context = {
        'projeto': projeto
    }


    #return HttpResponse(rates_response)
    return render(request, 'projectpage.html', context=context )

def get_projects_rates_per_client(request, pk):

    from project.models import Project
    projects = Project.objects.all().filter(products__in=pk)

    p = Project.objects.all()
    from project.models import Project, ProjectCategory

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

    p_cat_l_1 = []
    for project in projects:
        if project.project_totals <= 10000:
            msg = 'Até 10.000,00'
            range_1.append(project.id)
            #range_1.append(project.get_category())
            full[msg] = range_1

            cat_1.append(project.id)
            full_cat[str(project.get_category())] = cat_1
            #print(project.id, project.project_totals)
        elif  10000 < project.project_totals <= 30000:
            msg = 'De 10.000,00 até 30.000,00'
            range_2.append(project.id)
            #range_2.append(project.get_category())
            full[msg] = range_2
            cat_2.append(project.id)
            full_cat[str(project.get_category())] = cat_2
            #print(project.id, project.project_totals)
        elif  30000 < project.project_totals <= 40000:
            msg = 'De 30.000,00 até 40.000,00'
            range_3.append(project.id)
            #range_3.append(project.get_category())
            full[msg] = range_3
            cat_3.append(project.id)
            full_cat[str(project.get_category())] = cat_3
            #print(project.id, project.project_totals)
        elif  40000 < project.project_totals <= 50000:
            msg = 'De 40.000,00 até 50.000,00'
            range_4.append(project.id)
            #range_4.append(project.get_category())
            full[msg] = range_4
            cat_4.append(project.id)
            full_cat[str(project.get_category())] = cat_4
            #print(project.id, project.project_totals)
        elif  project.project_totals > 50000:
            msg = 'Acima 50.000,00'
            range_5.append(project.id)
            #range_5.append(project.get_category())
            full[msg] = range_5
            cat_5.append(project.id)
            full_cat[str(project.get_category())] = cat_5
            #print(project.id, project.project_totals)


    #full['categories'] = full_cat
    #print(full)
    rates_response = JsonResponse(full)
    #rates_response2 = JsonResponse(full_cat)

    #print(rates_response)
    #print(rates_response2)

    return HttpResponse(rates_response)


def get_projects_per_categorie(request, pk):

    from project.models import Project
    projects = Project.objects.all().filter(products__in=pk)

    p = Project.objects.all()
    from project.models import Project, ProjectCategory

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

    p_cat_l_1 = []
    for project in projects:
        if project.project_totals <= 10000:
            msg = 'Até 10.000,00'
            range_1.append(project.id)
            #range_1.append(project.get_category())
            full[msg] = range_1

            cat_1.append(project.id)
            full_cat[str(project.get_category())] = cat_1
            #print(project.id, project.project_totals)
        elif  10000 < project.project_totals <= 30000:
            msg = 'De 10.000,00 até 30.000,00'
            range_2.append(project.id)
            #range_2.append(project.get_category())
            full[msg] = range_2
            cat_2.append(project.id)
            full_cat[str(project.get_category())] = cat_2
            #print(project.id, project.project_totals)
        elif  30000 < project.project_totals <= 40000:
            msg = 'De 30.000,00 até 40.000,00'
            range_3.append(project.id)
            #range_3.append(project.get_category())
            full[msg] = range_3
            cat_3.append(project.id)
            full_cat[str(project.get_category())] = cat_3
            #print(project.id, project.project_totals)
        elif  40000 < project.project_totals <= 50000:
            msg = 'De 40.000,00 até 50.000,00'
            range_4.append(project.id)
            #range_4.append(project.get_category())
            full[msg] = range_4
            cat_4.append(project.id)
            full_cat[str(project.get_category())] = cat_4
            #print(project.id, project.project_totals)
        elif  project.project_totals > 50000:
            msg = 'Acima 50.000,00'
            range_5.append(project.id)
            #range_5.append(project.get_category())
            full[msg] = range_5
            cat_5.append(project.id)
            full_cat[str(project.get_category())] = cat_5
            #print(project.id, project.project_totals)


    #full['categories'] = full_cat
    #print(full_cat)
    #rates_response = JsonResponse(full)
    rates_response2 = JsonResponse(full_cat)

    #print(rates_response)
    #print(rates_response2)

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

def project_support(request):
    context = {}
    return render(request, 'add_support.html', context=context)