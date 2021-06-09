from .models import Interpreter#, RejectedConsults
import logging
logger = logging.getLogger(__name__)

class InterpreterService():

    def getInterpreter(id):
        return Interpreter.objects.get(user_id = id)

    #def getRejectedConsults(id):
    #    return RejectedConsults.objects.filter(interpreter = id)
    
