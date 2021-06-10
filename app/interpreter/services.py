from .models import Interpreter
from surdo.models import RejectedConsults
import logging
logger = logging.getLogger(__name__)

class InterpreterService():

    def getInterpreter(id):
        return Interpreter.objects.get(user_id = id)

    def getRejectedConsults(id):
        return RejectedConsults.objects.filter(consult = id)