import random
import vocabulary1 as v

class Word:
    def __init__(self):
        pass
    def pick(self, list):
        size = len(list)
        pick = random.randrange(0, size)
        word = list[pick]
        return word

class Subject:
    def __init__(self) -> None:
        pass
    def get(self):
        r = random.randrange(0,2)
        if r == 1:
            return Word.pick(self, v.subject)
        return "I"
    def getExis(self):
        f = ["I am","You are","They are","He is","She is"]
        idx = random.randrange(0,4)
        return f[idx]

class Object:
    def __init__(self) -> None:
        pass
    def get(self):
        return Word.pick(self, v.noun)

class Action:
    def __init__(self) -> None:
        pass
    def get(self):
        return Word.pick(self, v.verb)

class Dialogue:
    def __init__(self) -> None:
        self.subject = Subject()
        self.verb = Action()
        self.target = Subject()
    
    def get(self):
        s = []
        s.append(Subject.get(self) + " will " + Action.get(self) + " the " + Object.get(self) + ".")
        s.append("A " + Entity.get(self) + " should " + Action.get(self) + " the " + Object.get(self) + ".")
        s.append(Subject.getExis(self) + " a " + Entity.get(self) + ".")
        s.append("How do the " + Entity.get(self) + "s " + Action.get(self) + "?")
        s.append("Can the " + Entity.get(self) + "s " + Action.get(self) + " the " + Entity.get(self) + "?")
        pick = random.randrange(0,5)
        select = s[pick]
        return select

class Entity:
    #Creates an sentence object or a sentence direct object. Called enity so as not to conflict with entity.
    def __init__(self):
        self.part = "empty"
        self.adjective = "adjective"
        self.noun = "noun"
        self.definitive = False

    def get(self):
        return Word.pick(self, v.adjective) + " " + Word.pick(self, v.noun)

class Cast:
    def __init__(self) -> None:
        self.personae = []
        self.scene = []
    def makeCast(self):
        numActors = random.randrange(6,9)
        for i in range(numActors):
            c = []
            c.append(Word.pick(self, v.subject))
            c.append("A " + Entity.get(self))
            self.personae.append(c[random.randrange(0,2)])
    def makeScene(self):
        numActors = random.randrange(3, len(self.personae))
        c = []
        for i in range(numActors):
            r = random.randrange(len(self.personae))
            while(self.personae[r] in c):
                r = random.randrange(len(self.personae))
            c.append(self.personae[r])
        self.scene = c
            
    def getChar(self):
        return self.scene[random.randrange(0,len(self.scene))]


class Line:
    def __init__(self) -> None:
        pass
    def get(self, cast):
        c = []
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append(Cast.getChar(cast) + ": " + Dialogue.get(self))
        c.append("<i>" + Cast.getChar(cast) + " " + Action.get(self)+"s.</i>")
        c.append("<i>" + Cast.getChar(cast) + " " + "exits.</i>")
        c.append("<i>" + Cast.getChar(cast) + " " + "enters.</i>")
        return c[random.randrange(0,13)]

class Scene:
    def __init__(self) -> None:
        pass
    def get(self, cast):
        return "<i>" + Word.pick(self, v.locations) + ". " + Cast.getChar(cast) +" enters, speaking of " + Entity.get(self) + "s.</i>"