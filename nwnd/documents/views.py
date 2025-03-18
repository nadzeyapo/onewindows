from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentUploadForm
from .models import Document
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def index(request):
    documents = Document.objects.all()
    return render(request, 'documents/index.html', {'documents': documents})


def home(request):
    return render(request, 'documents/home.html')


def procedures(request):
    return render(request, 'documents/procedures.html')


def juridical(request):
    return render(request, 'documents/juridical.html')


@login_required
def upload_document(request, category):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.category = category  # Устанавливаем категорию
            document.save()
            messages.success(request, 'Документ успешно загружен!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при загрузке документа. Пожалуйста, попробуйте еще раз.')
    else:
        form = DocumentUploadForm()

    return render(request, 'documents/upload.html', {'form': form, 'current_category': category})

@login_required
def edit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Документ успешно обновлен!')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка при обновлении документа. Пожалуйста, попробуйте еще раз.')
    else:
        form = DocumentUploadForm(instance=document)

    return render(request, 'documents/edit.html', {'form': form, 'document': document})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна! Добро пожаловать!')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, исправьте ошибки.')
    else:
        form = UserCreationForm()
    return render(request, 'documents/register.html', {'form': form})


def category_documents(request, category):
    documents = Document.objects.filter(category=category)
    return render(request, 'documents/{}.html'.format(category), {'documents': documents})

# Добавленные функции для дополнительных маршрутов

def architecture(request):
    documents = Document.objects.filter(category='architecture')
    return render(request, 'documents/architecture.html', {'documents': documents})


def education(request):
    documents = Document.objects.filter(category='education')
    return render(request, 'documents/education.html', {'documents': documents})


def housingrelations(request):
    documents = Document.objects.filter(category='housingrelations')
    return render(request, 'documents/housingrelations.html', {'documents': documents})


def laborandsocialprotection(request):
    documents = Document.objects.filter(category='laborandsocialprotection')
    return render(request, 'documents/laborandsocialprotection.html', {'documents': documents})


def money(request):
    documents = Document.objects.filter(category='money')
    return render(request, 'documents/money.html', {'documents': documents})


def stroitelstvo(request):
    documents = Document.objects.filter(category='stroitelstvo')
    return render(request, 'documents/stroitelstvo.html', {'documents': documents})


def svyz(request):
    documents = Document.objects.filter(category='svyz')
    return render(request, 'documents/juridical/svyz.html', {'documents': documents})


def oos(request):
    documents = Document.objects.filter(category='oos')
    return render(request, 'documents/juridical/oos.html', {'documents': documents})


def shop(request):
    documents = Document.objects.filter(category='shop')
    return render(request, 'documents/shop.html', {'documents': documents})


def sportj(request):
    documents = Document.objects.filter(category='sportj')
    return render(request, 'documents/juridical/sportj.html', {'documents': documents})


def finansy(request):
    documents = Document.objects.filter(category='finansy')
    return render(request, 'documents/finansy.html', {'documents': documents})


def imysh(request):
    documents = Document.objects.filter(category='imysh')
    return render(request, 'documents/imysh.html', {'documents': documents})


def doc(request):
    documents = Document.objects.filter(category='doc')
    return render(request, 'documents/doc.html', {'documents': documents})


def guardianship(request):
    documents = Document.objects.filter(category='guardianship')
    return render(request, 'documents/guardianship.html', {'documents': documents})


def sport(request):
    documents = Document.objects.filter(category='sport')
    return render(request, 'documents/sport.html', {'documents': documents})


def nature(request):
    documents = Document.objects.filter(category='nature')
    return render(request, 'documents/nature.html', {'documents': documents})


def transport(request):
    documents = Document.objects.filter(category='transport')
    return render(request, 'documents/transport.html', {'documents': documents})


def agriculture(request):
    documents = Document.objects.filter(category='agriculture')
    return render(request, 'documents/agriculture.html', {'documents': documents})


def archieve(request):
    documents = Document.objects.filter(category='archieve')
    return render(request, 'documents/archieve.html', {'documents': documents})


def army(request):
    documents = Document.objects.filter(category='army')
    return render(request, 'documents/army.html', {'documents': documents})


def rege(request):
    documents = Document.objects.filter(category='rege')
    return render(request, 'documents/rege.html', {'documents': documents})


def archieve1(request):
    documents = Document.objects.filter(category='archieve1')
    return render(request, 'documents/archieve1.html', {'documents': documents})


def archieva2(request):
    documents = Document.objects.filter(category='archieva2')
    return render(request, 'documents/archieva2.html', {'documents': documents})


def educationj(request):
    documents = Document.objects.filter(category='educationj')
    return render(request, 'documents/educationj.html', {'documents': documents})


