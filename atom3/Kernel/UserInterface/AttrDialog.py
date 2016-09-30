from Dialog  import *
from Tkinter import *

class AttrDialog(Dialog):

    def __init__(self, title,
                 parent = None,
                 entry = None
                ):

        if not parent:
            import Tkinter
            parent = Tkinter._default_root

        if entry:
            self.attr_name = entry[0]
            self.attr_type = entry[1]
            self.initialvalue = entry[2]
        else:
            self.attr_name = ""
            self.attr_type = 0
            self.initialvalue = 0

        self.result_ok = 0

        Dialog.__init__(self, parent, title)

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        Label(master, text = "Attribute name:").grid(row = 0, padx = 5, sticky = E)
        Label(master, text = "Attribute type:").grid(row = 1, padx = 5, sticky = E)
        Label(master, text = "Initial value:").grid(row = 2, padx = 5, sticky = E)

        self.name_entry = Entry(master)
        self.name_entry.grid(row = 0, column = 1, columnspan = 2)
        self.name_entry.insert(0, self.attr_name)
        self.name_entry.select_range(0, END)

        self.type = IntVar()
        self.type.set(self.attr_type)
        Radiobutton(master, text = "integer", value = 0, variable = self.type).grid(row = 1, column = 1)
        Radiobutton(master, text = "string", value = 1, variable = self.type).grid(row = 1, column = 2)

        self.value_entry = Entry(master)
        self.value_entry.grid(row = 2, column = 1, columnspan = 2)
        self.value_entry.insert(0, self.initialvalue)

        return self.name_entry

    def validate(self):

        import tkMessageBox
        import string

        try:
            if self.type.get() == 0:
                string.atoi(self.value_entry.get())
        except ValueError:
            tkMessageBox.showwarning(
                "Illegal value",
                "Type mismatch.\nPlease try again",
                parent = self
            )
            return 0

        if self.name_entry.get() == "":
            tkMessageBox.showwarning(
                "Illegal value",
                "Attribute must have a name.",
                parent = self
            )
            return 0

        return 1

    def apply(self):

        self.result_ok = 1
        self.attr_name = self.name_entry.get()
        self.attr_type = self.type.get()
        self.initialvalue = self.value_entry.get()
