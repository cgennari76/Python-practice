class Person(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None, job=None, quote=None):
        self.name = name
        self.job = job
        self.quote = quote

class Display:
    personLst = []
    personLst.append(Person("Payne N. Diaz", "coach", "Without exception, there is no rule!"))
    personLst.append(Person("Mia Serts", "bicyclist", "If the world didn't suck, we'd all fall off!"))
    personLst.append(Person("Don B. Sanosi", "teacher", "Work real hard while you wait and good things will come to you!"))
    personLst.append(Person("Hugh Jorgan", "organist", "Age is a very high price to pay for maturity."))
    personLst.append(Person("Herasmus B. Dragon", "dentist", "Enough people can't find work in America!"))
    personLst.append(Person("Adolph Koors", "master-brewer", "Wish you were beer!"))
    personLst.append(Person("Zucker Zahn", "dentist", "If you drink from the fountain of knowledge, quench your thirst slowly."))

    def oneitem():
        print("Show one particular item:")
        print(d.personLst[0].name)
        
    def allitem():
        print("Sort the personLst in place by job ...")
        import operator
        d.personLst.sort(key=operator.attrgetter('job'))

        print("... then show all quotes and who said so:")
        for person in d.personLst:
            print("\"%s\"  %s (%s)" % (person.quote, person.name, person.job))
        
    def zonedesk():
        d = Display
        d.oneitem()
        d.allitem()

d = Display
d.zonedesk()