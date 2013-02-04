#!/usr/bin/python
from cmd import Cmd
from kppy import *
from lib_lewm.common import copy2clip,  opendb

class HelloWorld(Cmd):
    """Simple command processor example."""
    
    def __init__(self, db):
        Cmd.__init__(self)
        groups={}
        self.cur_root=None
        self.isuser=True
        for gr1 in db.groups:
            if self.cur_root ==None:
                self.cur_root=gr1
                self.change_group()
            groups[gr1.title]=gr1
        self.groups=groups

    def do_group(self, person):
        if person:
            self.cur_root = self.groups[person]
            self.change_group()
        else:
            print('hi')

    def do_isuser(self):
        self.isuser = not self.isuser 

    def change_group(self):
        entries={}
        for ent1 in self.cur_root.entries:
            entries[ent1.title]=ent1
        self.entries=entries

    def help_group(self):
        print('\n'.join([ 'group [person]',
                           'group the named person',
                           ]))
    def complete_group(self, text, line, begidx, endidx):
        comp1 = list(self.groups.keys())
        if not text:
            completions = comp1[:]
        else:
            completions = [ f
                            for f in comp1
                            if f.startswith(text)
                            ]
        return completions

    def do_entrie(self, person):
        if person:
            tmp1 = self.entries[person]
            print('comment :  ',tmp1.comment)
            print('url :  ',tmp1.url)
            copy2clip(self.cur_root.title+'.'+tmp1.title,'password',tmp1.password)
            if self.isuser:
                copy2clip(self.cur_root.title+'.'+tmp1.title,'username',tmp1.username)
        else:
            print('hi')

    def help_entrie(self):
        print('\n'.join([ 'entrie [person]',
                           'entrie the named person',
                           ]))
    

    def complete_entrie(self, text, line, begidx, endidx):
        comp1 = list(self.entries.keys())
        if not text:
            completions = comp1[:]
        else:
            completions = [ f
                            for f in comp1
                            if f.startswith(text)
                            ]
        return completions


    def do_EOF(self, line):
        return True

def main():
    db=opendb('~/.config/lewm/config')
    HelloWorld(db).cmdloop()

if __name__ == '__main__':
    main()
