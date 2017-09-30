# from django.shortcuts import render
# from django.views.generic.base import View
# from usuarios.forms import RegistrarUsuarioForm
# from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm

class RegistrarUsuarioView(View):

    template_name = 'registrar.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        # print('\n--------\n\n')
        # print('data: '+form.data['nome'])
        # print(form.is_valid())
        print('\n---1---')
        if not form.is_valid():
            print('\n2--------2')

        # print('\n---1-'+form.data)  
        print(form.data)   
        if form.is_valid():
            dados_form = form.data
            # dados_form = form.cleaned_data
            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
            perfil = Perfil(nome=dados_form['nome'],
                            email=dados_form['email'],
                            telefone=dados_form['telefone'],
                            usuario=usuario)
            perfil.save()

            return redirect('index')
        return render(request, self.template_name, {'form':form})