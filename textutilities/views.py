from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dic={'name':'Nitish',
         'state':'surat'}
    return render(request,'index.html',dic)
def countwords(request):
    c=request.POST.get('ta')
    print(len(c))
    dict={'c':len(c)}
    return render(request,'count.html',dict)
def suffix(request):
    return render(request,'suffix.html')
def suffixadded(request):
    text=list(request.POST.get('sta'))
    suf=request.POST.get('suf')
    word=""
    lst=[]
    for a in text:
      if(a is "\r" or a is "\n"):
        lst.append(word+suf)
        word=""
      else:
          word=word+a
    lst.append(word+suf)
    lst=set(lst)
    lst.remove(suf)
    lst=list(lst)
    dict={'values':lst}
    return render(request,'suffixadded.html',dict)
def prefix(request):
    return render(request,'prefix.html') 
def prefixadded(request):
    text=list(request.POST.get('text'))
    pre=request.POST.get('pre')
    word=""
    lst=[]
    for a in text:
      if(a is "\r" or a is "\n"):
        lst.append(pre+word)
        word=""
      else:
          word=word+a
    lst.append(pre+word)
    lst=set(lst)
    lst.remove(pre)
    lst=list(lst)
    dict={'values':lst}
    return render(request,'prefixadded.html',dict)