python manage.py shell
from perfis.models import Perfil
p = Perfil(nome='Hugo Ladeira', email='hhhhhhh@gmail.com', telefone='909090')
p.save()
p2 = Perfil(nome='romuloko', email='romulo@iiiii.com', telefone='122222')
p2.save()
p3 = Perfil(nome='lucas', email='lululululu@gmakkkkil.com', telefone='99999')
p3.save()


from perfis.models import Convite, Perfil
p = Perfil.objects.get(id=1)
p2 = Perfil.objects.get(id=2)
p2.convidar(p)
p.convidar(p2)
p.convites_recebidos.all()
p2.convites_recebidos.all()


# continuar: https://cursos.alura.com.br/course/introducao-ao-django/task/7837

comandos iniciais/anotações:
python manage.py startapp usuarios
vai no settings.py >> INSTALLED_APPS >> 'usuarios'

