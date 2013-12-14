#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Emanuele Bertoldi'
__version__ = '0.0.3'

from django import forms
from django.utils.translation import ugettext_lazy as _
from djangoerp.core.forms import enrich_form

from models import Bookmark

class BookmarkForm(forms.ModelForm):
    """Form for bookmark data.
    """
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'description', 'new_window']
    
    def __init__(self, *args, **kwargs):
        self.menu = kwargs.pop("menu", None)
        super(BookmarkForm, self).__init__(*args, **kwargs)
    
    def clean_title(self):
        title = self.cleaned_data['title']
       
        try:
            bookmark = Bookmark.objects.get(title=title, menu=self.menu)
            if bookmark != self.instance:
                raise forms.ValidationError(_("This title is already in use."))
                
        except Bookmark.DoesNotExist:
            pass
            
        return title

enrich_form(BookmarkForm)
