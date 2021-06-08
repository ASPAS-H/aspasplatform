from .models import Interpreter
import logging
logger = logging.getLogger(__name__)

class InterpreterService():

    def getInterpreter(id):
        return Interpreter.objects.get(user_id = id)
    
