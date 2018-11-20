from django import template
from django.template import RequestContext
from ..models import ApartmentUnit, House

register = template.Library()

@register.simple_tag
def apartmentunit_total():
    count = ApartmentUnit.objects.fitler(owner=request.user).count()
    

