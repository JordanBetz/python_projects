from ._anvil_designer import Form1Template 
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.
    
    chars = ["1", "2", "3", "4", "d", "c",
            "5", "6","7", "8", "+", "-",
            "9", "0", ".", "*", "/", "="]
    self.btn = {}
    gp = GridPanel()

    for idx, i in enumerate(chars):
        if i == "=":
            clr="#78993D"
        elif i in ["c", "d"]:
            clr="purple"
        elif i in ["+", "-", "*", "/"]:
            clr="#3A3A49"
        else:
            clr="#717093"
            
        if idx < 6:
            row='A'
        elif 6<=idx<12:
            row='B'
        else:
            row='C'
            
    self.btn[i] = Button(text=i, font="Consolas", bold=True, foreground="#FFF", background=clr)
    self.btn[i].tag.name = i
    self.btn[i].set_event_handler('click', self.click)
    gp.add_component(self.btn[i], row=row, col_xs=3, width_xs=1)
    

# add grid to interface
    self.add_component(gp)
    self.space = Spacer(height=500)
    self.add_component(self.space)

  def click(self, **event_args):
    val = event_args['sender'].tag.name
    if val == "=":
        self.text_box_1.text = eval(self.text_box_1.text)
    elif val=="c":
        self.text_box_1.text = ""
    elif val=="d":
        self.text_box_1.text = self.text_box_1.text[:-1]
    else: 
        self.text_box_1.text += val