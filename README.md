# Projeto Django2

## Projeto 
***
Sistema de cadastro de produtos.

## Fontes
***
Este projeto foi elaborado na seção 04 do curso "Programação Web com Python e Django Framework: Essencial" da Geek University na plataforma Udemy

O deploy foi configurado com base no tutorial "Tutorial como fazer deploy de um projeto Django usando Heroku", do canal Fabio Ruicci na plataforma YouTube.

## Python Versão
- Python 3.8.8
- Django 3.1.7

## Produção
***
Foi utilizado a biblioteca dj-static para servir os arquivos estáticos utilizados na aplicação.

## Requerimentos
***
Todas bibliotecas e pacotes necessários para execução eficiente do projeto estão registradas no arquivo requirements.txt

## Configuração das variáveis de ambiente no Deploy no HEROKU
Heroku CLI
Após a criação da app:
- heroku config:set ALLOWED_HOSTS=nome_sua_app_heroku.herokuapp.com
- heroku config:set DJANGO_SETTINGS_MODULE=sua_app_django.settings.heroku
- heroku config:set SECRET_KEY=sua_secret_key
- heroku config:set DEBUG=False

Criação do Banco de Dados PostgreSQL no Heroku
- heroku addons:create heroku-postgresql:hobby-dev