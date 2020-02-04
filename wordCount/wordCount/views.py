from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def count(request):
    fulltext = request.GET['fulltext']
    fullList = fulltext.split()
    words = len(fullList)
    wordDictionary = {}
    for word in fullList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
        
    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext':fulltext, 'words' : words, 'sortedDictionary' : sortedWords})