"""
This file is used by the appearenceDialog.py
"""

from MyDialog import *

import string

class _QueryDialog(MyDialog):

    def __init__(self, title, prompt,
                 initialvalue=None,
                 minvalue = None, maxvalue = None,
                 parent = None):

        if not parent:
            import Tkinter
            parent = Tkinter._default_root

        self.prompt   = prompt
        self.minvalue = minvalue
        self.maxvalue = maxvalue

        self.initialvalue = initialvalue

        MyDialog.__init__(self, parent, title)

    def body(self, master):

        w = Label(master, text=self.prompt, justify=LEFT)
        w.grid(row=0, padx=5, sticky=W)

        self.entry = Entry(master, name="entry")
        self.entry.grid(row=1, padx=5, sticky=W+E)

        if self.initialvalue:
            self.entry.insert(0, self.initialvalue)
            self.entry.select_range(0, END)

        return self.entry

    def validate(self):

        import tkMessageBox

        try:
            result = self.getresult()
        except ValueError:
            tkMessageBox.showwarning(
                "Illegal value",
                self.errormessage + "\nPlease try again",
                parent = self
            )
            return 0

        if self.minvalue is not None and result < self.minvalue:
            tkMessageBox.showwarning(
                "Too small",
                "The allowed minimum value is %s. "
                "Please try again." % self.minvalue,
                parent = self
            )
            return 0

        if self.maxvalue is not None and result > self.maxvalue:
            tkMessageBox.showwarning(
                "Too large",
                "The allowed maximum value is %s. "
                "Please try again." % self.maxvalue,
                parent = self
            )
            return 0

        self.result = result

        return 1


class _QueryString(_QueryDialog):
    def getresult(self):
        return self.entry.get()

def askstring(title, prompt, **kw):
    d = apply(_QueryString, (title, prompt), kw)
    return d.result
