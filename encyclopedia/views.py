from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Prints out selected entry
def view_entry(request,title):
    return render(request, "encyclopedia/view_entry.html", {
        "entry": util.get_entry(title)
    })
