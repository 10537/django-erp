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
__version__ = '0.0.4'

from django.conf.urls import *

from views import *

urlpatterns = patterns('',

    url(r'^pluggets/add/(?P<slug>[-\w]+)/$', view=PluggetWizard.as_view(PluggetWizard.DEFAULT_FORMS), name='plugget_add'),
    url(r'^pluggets/(?P<pk>[\d]+)/edit/$', view=PluggetWizard.as_view(PluggetWizard.DEFAULT_FORMS), name='plugget_edit'),
    url(r'^pluggets/(?P<pk>[\d]+)/delete/$', view=DeletePluggetView.as_view(), name='plugget_delete'),
)
