import pureautomatism as pa
import random

def getscript():
    cast = pa.Cast()
    cast.makeCast()

    s = ""

    cast.makeScene()
    s += "Act 1:<br/>"
    s += (pa.Scene()).get(cast) + "<br/>"
    for i in range(random.randrange(3,9)):
        s += (pa.Line()).get(cast) + "<br/>" 
    s += "<i>All exit.</i><br/>"

    s += "<br/>Act 2:"
    s += (pa.Scene()).get(cast) + "<br/>"
    for i in range(random.randrange(3,9)):
        s += (pa.Line()).get(cast) + "<br/>"
    s += "<i>All exit.</i><br/>"

    s += "<br/>Act 3:<br/>"
    s += (pa.Scene()).get(cast) + "<br/>"
    for i in range(random.randrange(3,9)):
        s += (pa.Line()).get(cast) + "<br/>"
    s += "<i>All bow, and exit.</i><br/>"

    return s