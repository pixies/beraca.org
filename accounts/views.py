from rest_framework import generics, mixins, permissions

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from accounts.api.serializer import UserSerializer
from accounts.api.permissions import IsAdmin, IsClientOrAdmin, IsProfileOwner, IsClientOwner

User = get_user_model()

class UserList(mixins.ListModelMixin, generics.GenericAPIView):

    http_method_names = ['get', ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    http_method_names = ['post', ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def post(self, request, *args, **kwargs):
        user_create = self.create(request, *args, **kwargs)

        return user_create


class UserDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login(request):

    print(request.user)

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():
            return redirect('/index/search/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})


def profile(request):


    from accounts.models import MyUser
    from client.models import Profile, Client
    from project.models import ProjectcSupport
    from company.models import Company

    cliente_id = request.user.id
    conta = MyUser.objects.get(pk=request.user.id)
    print(cliente_id)
    profile, created = Profile.objects.get_or_create(user_id=cliente_id, is_support=False, is_manager=False, is_admin=False)

    nascimento = ''
    endereco = ''
    
    if created == True:
        if profile.birth_date.exists():
            nascimento = profile.birth_date
            
        else:
            nascimento = ''

        if profile.address.exists():
            endereco = profile.address
        else:
            endereco = ''

    cliente = Client.objects.get(user_id=cliente_id)

    projetcSupport = ProjectcSupport.objects.filter(client_id=cliente_id)

    print(projetcSupport)
    print(cliente)
    print(profile)
    
    full_name = str(conta.first_name) + ' ' + str(conta.last_name)
    email = str(conta.email)
    fone = str(conta.phone)

    for pro in projetcSupport:
        print(pro.project.name)

    context = {
        'full_name': full_name,
        'email': email,
        'nascimento': nascimento,
        'endereco': endereco,
        'fone': fone,

        'company': cliente.company,
        'cnpj': cliente.company.company_reg,

        'projetos': projetcSupport
    }

    return render(request, 'profile.html', context=context)





















