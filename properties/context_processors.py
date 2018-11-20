from .models import Apartment, ApartmentUnit, House



def apartment_count(request):
    count = Apartment.objects.count()
    return {'apartment_count': count}

def apartmentunit_count(request):

    count = ApartmentUnit.objects.filter(owner=request.user).count()
    
    if request.user.is_authenticated():
        return {'apartmentunit_count': count}