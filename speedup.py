from data import returnth
from person import Korisnik 


class Link:
    def __init__(self, objlist):
        self.objlist = objlist
        self.started = False
        self.done = False


    def startit(self):
        for i in self.objlist:
            i.start()
        self.started = True    

    def joinit(self):
        if self.started:
            for i in self.objlist:
                i.join()
            self.done = True

    def yieldvalues(self):
        for i in self.objlist:
            yield i.value()

    def getvalues(self, printem = True):
        '''Runs .start() and .join() on all threads
        
        Instead of having to .start() each thread and then
        using .join() on each thread. This method does it for you
        you can either run .startit() and .joinit(), as for the printem
        parameter it will either print or yield return values 
        
        
        Keyword Arguments:
            printem {bool} -- if printem = True # it will print them(default: {True})
        
        Returns:
            yields return values or prints them
        '''

        if not self.done:
            self.startit()
            self.joinit()
        if printem:
            for i in self.objlist:
                print(i.value())
        else:
            return self.yieldvalues()
        

