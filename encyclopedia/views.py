from django.shortcuts import render

from . import util

from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Prints out selected entry
def view_entry(request,title):
    # Convert markdown to HTML
    # using markdown2
    html_output = Markdown()
    html_output.convert(util.get_entry(title))

    return render(request, "encyclopedia/view_entry.html", {
        "entry": html_output.convert(util.get_entry(title)),
        "title": title
    }
    

    
    )
