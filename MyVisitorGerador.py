from NaluthaVisitor import NaluthaVisitor
from MyVisitorGeradorUtils import getType, listModels, listFields, listSerializers, alterar_linha, nova_linha, getFieldSize
import os

class MyVisitorGerador(NaluthaVisitor):
    def __init__(self):
        self.project = ''
        self.api = ''

    def visitProgram(self, ctx):
        self.project = ctx.config().projectName.text
        self.api = ctx.config().apiName.text
        if not os.path.exists(self.project):
            os.system('django-admin startproject ' + self.project)
            os.chdir(self.project)
            os.system('python3 manage.py startapp ' + self.api)
            os.chdir('..')
        
        with open(self.project + '/' + self.api + '/models.py', 'w') as arq:
            arq.write('from django.db import models')

        with open(self.project + '/' + self.api + '/serializers.py', 'w') as arq:
            arq.write('from rest_framework import serializers')
            arq.write('\n')
            arq.write('from .models import ' + listModels(ctx.model().entity()))

        with open(self.project + '/' + self.api + '/admin.py', 'w') as arq:
            arq.write('from django.contrib import admin')
            arq.write('\n')
            arq.write('from .models import ' + listModels(ctx.model().entity()))
            arq.write('\n')

        with open(self.project + '/' + self.api + '/views.py', 'w') as arq:
            arq.write('from django.shortcuts import render')
            arq.write('\n')
            arq.write('from rest_framework import viewsets')
            arq.write('\n\n')
            arq.write('from .serializers import ' + listSerializers(ctx.model().entity()))
            arq.write('\n')
            arq.write('from .models import ' + listModels(ctx.model().entity()))
            arq.write('\n')

        with open(self.project + '/' + self.api + '/urls.py', 'w') as arq:
            arq.write('from django.urls import include, path')
            arq.write('\n')
            arq.write('from rest_framework import routers')
            arq.write('\n')
            arq.write('from . import views')
            arq.write('\n\n')
            arq.write('router = routers.DefaultRouter()')
            arq.write('\n')

        alterar_linha(self.project + '/' + self.project + '/urls.py', 17, 'from django.urls import path, include\n')
        nova_linha(self.project + '/' + self.project + '/urls.py', 20,  '    path("", include("' + self.api + '.urls")),\n')

        nova_linha(self.project + '/' + self.project + '/settings.py', 39,  '    "rest_framework",\n')
        nova_linha(self.project + '/' + self.project + '/settings.py', 40,  '    "' + self.api + '.apps.' + self.api.capitalize() + 'Config",\n')
        
        return self.visitChildren(ctx)

    def visitModel(self, ctx):
        with open(self.project + '/' + self.api + '/urls.py', 'a') as arq:
            for ctxEntity in ctx.entity():
                arq.write('\n')
                arq.write('router.register(r"'+ ctxEntity.Id().getText().lower() + '", views.' + ctxEntity.Id().getText() +'ViewSet)')
        
            arq.write('\n\n')
            arq.write('urlpatterns = [')
            arq.write('\n')
            arq.write('    ')
            arq.write('path("", include(router.urls)),')
            arq.write('\n')
            arq.write('    ')
            arq.write('path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))')
            arq.write('\n')
            arq.write(']')

        return self.visitChildren(ctx)
        

    def visitEntity(self, ctx):
        with open(self.project + '/' + self.api + '/models.py', 'a') as arq:
            arq.write('\n\n')
            arq.write('class ' + ctx.Id().getText() +'(models.Model):')

            for ctxField in ctx.field():
                arq.write('\n')
                arq.write('    ')
                arq.write(ctxField.fieldName.text + ' = models.' + getType(ctxField.fieldType.text) + 'Field(')
                getType(ctxField.fieldType.text) and arq.write('max_length=' + getFieldSize(ctxField.fieldSize))
                arq.write(')')
            arq.write('\n\n')
            arq.write('    ')
            arq.write('def __str__(self):')
            arq.write('\n')
            arq.write('    ')
            arq.write('    ')
            arq.write('return self.' + ctx.field()[0].fieldName.text)

        with open(self.project + '/' + self.api + '/serializers.py', 'a') as arq:
            arq.write('\n\n')
            arq.write('class ' + ctx.Id().getText() + 'Serializer(serializers.HyperlinkedModelSerializer):')
            arq.write('\n')
            arq.write('    ')
            arq.write('class Meta:')
            arq.write('\n')
            arq.write('    ')
            arq.write('    ')
            arq.write('model = ' + ctx.Id().getText())
            arq.write('\n')
            arq.write('    ')
            arq.write('    ')
            arq.write('fields = (' + listFields(ctx.field()) + ')')

        with open(self.project + '/' + self.api + '/admin.py', 'a') as arq:
            arq.write('\n')
            arq.write('admin.site.register(' + ctx.Id().getText() + ')')

        with open(self.project + '/' + self.api + '/views.py', 'a') as arq:
            arq.write('\n')
            arq.write('class ' + ctx.Id().getText() + 'ViewSet(viewsets.ModelViewSet):')
            arq.write('\n')
            arq.write('    ')
            arq.write('queryset = ' + ctx.Id().getText() + '.objects.all()')
            arq.write('\n')
            arq.write('    ')
            arq.write('serializer_class = ' + ctx.Id().getText() + 'Serializer')
            arq.write('\n')

        return self.visitChildren(ctx)

        