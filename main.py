from src.services.base import ServiceBase  
from src.classes.Importer import Importer
services = Importer().import_from('./src/services', verboose=True, superclass=ServiceBase )
print(services['ServiceProvider'].status)