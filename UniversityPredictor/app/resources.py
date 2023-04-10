from import_export import resources
from .models import Engineering_College_Detail

class PersonResource(resources.ModelResource):
    class Meta:
        model = Engineering_College_Detail