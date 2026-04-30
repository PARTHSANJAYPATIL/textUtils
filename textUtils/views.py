from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the Text
    djtext =request.POST.get('text', 'default')
    remPunc =request.POST.get('removePunc', 'off')
    capA = request.POST.get('capAll', 'off')
    newLineRem = request.POST.get('newLineRemover' , 'off')
    spaceRem = request.POST.get('spaceRemover' , 'off')
    charC = request.POST.get('charCount', 'off')
    operation = ""
    char_count = ""
    if remPunc == 'on':
        operation += "\nRemove Puntuations"
        # Remove Punctuations
        djtext = removePunc(djtext)
    
    if capA == 'on':
        operation += "\nUPPERCASE"
        # Change to UpperCase
        djtext = capAll(djtext)
        
    if newLineRem == 'on' :
        operation += "\nNew Line Remover"
        # New Line Remover
        djtext = newLineRemover(djtext)
    
    if spaceRem == 'on' :
        operation += "\nExtra Space Remover"
        # Extra Space Remover
        djtext = spaceRemove(djtext)
        
    if charC == 'on' :
        operation += "\nCounting Char with space"
        # Counting Char with space
        char_count = charCount(djtext)
    params = {
        'purpose' : operation,
        'analyzed_text' : djtext,
        'char_count' : char_count,
    }
    return render(request, 'analyze.html', params)
    


# Remove Punctuations
def removePunc(text):
    punctuatuions = '''!(){}[]:;'"\/,.<>?~`@#$%^&*_-'''
    analyzed = ""
    for char in text:
        if char not in punctuatuions:
            analyzed = analyzed + char
    return analyzed

# Change to UpperCase
def capAll(text):
    return text.upper()

# New Line Remover
def newLineRemover(text):
    analyzed = ""
    for  char in text:
        if char != "\n" and char != "\r":
            analyzed = analyzed + char
    return analyzed

# Space Remover
def spaceRemove(text):
    analyzed = ""
    for index, char in enumerate(text):
        if text[index] == " " and text[index+1] == " ":
            pass
        else:
            analyzed = analyzed + char
    return analyzed

def charCount(text):
    char = 0
    for i in text:
        char += 1
    return char