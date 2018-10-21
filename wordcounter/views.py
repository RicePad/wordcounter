from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import operator



#
# def Home(request):
#     return HttpResponse("Hello, This is a word counter app!")

class Home(TemplateView):
    template_name = "home.html"



def count(request):
    fulltext = request.GET["fulltext"]

    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary[word] = 1


    sortedwords = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html",{"fulltext": fulltext, "count": len(wordlist), "sortedwords": sortedwords})
