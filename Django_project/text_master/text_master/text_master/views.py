from django.http import HttpResponse
from django.shortcuts import render
# from translate import Translator
def index(request):
    parmas={'name':"Abhijeet",'place':"Bhopal"}
    return render(request,'index.html',parmas)
    # return HttpResponse("Hello")

def about(request):
    return render(request,'about.html')
def analyze(request):
    puncstr='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    text=request.GET.get('text1','default')
    upper=request.GET.get('upper','off')
    lower=request.GET.get('lower','off')
    punc=request.GET.get('punc','off')
    nremove=request.GET.get('nremove','off')
    lenofstring=request.GET.get('lenofstring','off')
    converttuple=request.GET.get('converttuple','off')
    title=request.GET.get('title','off')
    translateh=request.GET.get('translateh','off')
    translatee=request.GET.get('translatee','off')

    
   
    whitespaceremover=request.GET.get('whitespaceremover','off')
    if upper == 'on':
        parmas={'text1':text.upper(),'purpose':"Convert Into Upper Case::"}
    elif lower == 'on':
        parmas={'text1':text.lower(),'purpose':"Convert Into Lower Case::"}
    elif punc == 'on':
        analyze=''
        for i in text:
            if i not in puncstr:
                analyze+=i
        parmas={'text1':analyze,'purpose':"Remove Punc::"}
    elif nremove=='on':
        analyze=''
        print(text)
        for i in text:
            if i != '\n':
                analyze+=i
                
        parmas={'text1':analyze,'purpose':"New Line Remover::"}
    elif lenofstring == 'on':
        analyze="Length of string "+str(len(text))
        parmas={'text1':analyze,'purpose':"Count Length Of string::"}

    elif converttuple == 'on':
        t=tuple(text)
        parmas={'text1':t,'purpose':"Convert Into Tuple::"}
    elif title == 'on':
        parmas={'text1':text.title(),'purpose':"Convert Into title::"}
    elif whitespaceremover=='on':
         parmas={'text1':text,'purpose':"White Space Remover::"}
    elif translatee == 'on':
        translator= Translator(to_lang="German")
        translation = translator.translate(text)

        parmas={'text1':translation,'purpose':"translate English to German::"}
    elif translateh == 'on':
        translator= Translator(to_lang="Hindi")
        translation = translator.translate(text)

        parmas={'text1':translation,'purpose':"translate English to Hindis::"}

    else:
        
        parmas={'text1':text,'purpose':"Please Select any one::"}
    
    return render(request,'analyze.html',parmas)

def translator(request):
    return HttpResponse("translator")