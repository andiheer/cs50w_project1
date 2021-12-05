from django.shortcuts import render
from django.utils.html import format_html

from . import util 
from .forms import EditForm

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
        "entry": format_html(html_output.convert(util.get_entry(title)))
    })

# Create new entry or edit existiing one
# If title is empty string, create new entry
def edit_entry(request,title):
    
    # Form handling: GET or POST?
    if request.method == 'POST':
        form_entry = EditForm(request.POST)
       # if form_entry.is_valid():


    # GET: show form
    else:
        # Get existing entry if exists
        form_edit= EditForm()
        if title == "new_entry":
            content = ""
            title = ""
        else:
            content = util.get_entry(title)
            if content == "None":
                content = ""
            form_edit.form_title = title
            form_edit.form_content = content        


        return render(request, "encyclopedia/edit_entry.html", {
            'form': form_edit,
            'title': title
        })

        # return render(request, 'name.html', {'form': form})
    