
# abstract event handler class
# An event handler for the icon editor of AToM3 must inherit from EventHandler.
class EventHandler:
    def __init__(self):
        raise NotImplementedError, 'EventHandler is an abstract class'

    def start(self):
        """starts the handler"""
        pass
    
    def stop(self):
        """stops the handler"""
        pass

### GF events
    def onGFEnter(self, gf):
        """cursor entered GF area"""
        pass

    def onGFLeave(self, gf):
        """cursor left GF area"""
        pass

    def onGFButton(self, gf, event):
        """GF button event"""
        pass

    def onGFShiftButton(self, gf, event):
        """GF button event while holding the Shift key"""
        pass

    def onGFDoubleButton(self, gf, event):
        """GF double button event"""
        pass

    def onGFShiftDoubleButton(self, gf, event):
        """GF double button event while holding the Shift key"""
        pass

    def onGFButtonMotion(self, gf, event):
        """GF mouse motion event while a button is being pressed"""
        pass

    def onGFButtonRelease(self, gf, event):
        """GF button release event"""
        pass

### canvas events
    def onCanvasButton(self, event):
        """Canvas button event"""
        pass
    
    def onCanvasDoubleButton(self, event):
        """Canvas double button event"""
        pass

    def onCanvasMotion(self, event):
        """Canvas mouse motion event"""
        pass

    def onCanvasShiftMotion(self, event):
        """Canvas mouse motion event while holding the Shift key"""
        pass

    def onCanvasButtonMotion(self, event):
        """Canvas mous motion event while a button is being pressed"""
        pass

    def onCanvasShiftButtonMotion(self, event):
        """Canvas mouse motion event while a button is being pressed and while holding the Shift key."""
        pass

    def onCanvasButtonRelease(self, event):
        """Canvas button release event"""
        pass

### Keyboard events
    def onKey(self, event):
        """key pressed"""
        pass

    def onShiftKey(self, event):
        """key pressed while holding the Shift key"""
        pass

    def onControlKey(self, event):
        """key pressed while holding the Control key"""
        pass

### Color events    
    def onFillColor(self, color):
        """new fill color selected"""
        pass

    def onOutlineColor(self, color):
        """new outline color selected"""
        pass
    
### tool selection event
    def onToolSelection(self, toolName):
        pass
    
### outline/fill option event
    def onOutlineFillOption(self, option):
        """new outline/fill option selected"""
        pass
    
### line width event
    def onLineWidth(self, lineWidth):
        """new line width selected"""
        pass

### file events
    def onSave(self):
        """Save"""
        pass

    def onExport(self):
        """Export"""
        pass
    
### edit events
    def onEditMenu(self, editMenu):
        """Edit menu is brought up"""
        pass

    def onUndo(self):
        """undo"""
        pass

    def onCut(self):
        """cut"""
        pass

    def onCopy(self):
        """copy"""
        pass

    def onPaste(self):
        """paste"""
        pass
    
    def onDelete(self):
        """delete"""
        pass
    
    def onBringToTop(self):
        """to Top""" 
        pass
    
    def onPushToBottom(self):
        """to Bottom"""
        pass
    
    def onGroup(self):
        """Group"""
        pass
    
    def onUngroup(self):
        """Ungroup"""
        pass
    
    def onProperties(self):
        """Properties"""
        pass
