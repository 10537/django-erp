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
__copyright__ = 'Copyright (c) 2013-2014, django ERP Team'
__version__ = '0.0.5'

from djangoerp.core.utils.dependencies import check_dependency

check_dependency('django.contrib.contenttypes')
check_dependency('django.contrib.sites')
check_dependency('djangoerp.core')
check_dependency('djangoerp.menus')

from django.conf import settings
from django.utils.translation import ugettext_noop as _
from djangoerp.core.models import Group, Permission

from models import *

def install(sender, **kwargs):
    users_group, is_new = Group.objects.get_or_create(name="users")
    add_plugget, is_new = Permission.objects.get_or_create_by_natural_key("add_plugget", "pluggets", "plugget")
    
    # Regions.
    footer_region, is_new = Region.objects.get_or_create(
        slug="footer",
        title=_("Footer")
    )
    
    sidebar_region, is_new = Region.objects.get_or_create(
        slug="sidebar",
        title=_("Sidebar")
    )
    
    # Pluggets.
    main_menu_plugget, is_new = Plugget.objects.get_or_create(
        title=_("Main menu"),
        source="djangoerp.pluggets.pluggets.menu",
        template="pluggets/menu.html",
        context='{"name": "main"}',
        region=sidebar_region
    )
    
    powered_by_plugget, is_new = Plugget.objects.get_or_create(
        title=_("Powered by"),
        description=_('Shows a classic "Powered by XYZ" claim.'),
        source="djangoerp.pluggets.pluggets.text",
        template="pluggets/powered-by.html",
        context='{"name": "django ERP", "url": "https://github.com/djangoERPTeam/django-erp"}',
        region=footer_region
    )
    
    # Permissions.
    users_group.permissions.add(add_plugget)
    
 
