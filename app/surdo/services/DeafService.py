from .forms import NewDeafForm
from address.forms import AddressForm
from .models import Deaf
from address.models import Address

def create(fields):
    address_add = Address(fields)
    address_add.save() 