from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_5_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.P1.text and self.P2.text and self.P3.text and self.P4.text and self.P5.text and self.P6.text and self.P7.text and self.P8.text and self.P9.text and self.P10.text and self.P11.text and self.P12.text and self.P13.text and self.P14.text and self.P15.text and self.P16.text and self.P17.text and self.P18.text and self.P19.text and self.P20.text and self.P21.text and self.P22.text and self.P23.text and self.P24.text and self.P25.text and self.P26.text and self.P27.text and self.P28.text and self.Mud.text:
      
      predicted = anvil.server.call('predict_water_quality', 
                                    self.model_Selection.selected_value,
                                    self.P1.text,
                                    self.P2.text,
                                    self.P3.text,
                                    self.P4.text,
                                    self.P5.text,
                                    self.P6.text,
                                    self.P7.text,
                                    self.P8.text,
                                    self.P9.text,
                                    self.P10.text,
                                    self.P11.text,
                                    self.P12.text,
                                    self.P13.text,
                                    self.P14.text,
                                    self.P15.text,
                                    self.P16.text,
                                    self.P17.text,
                                    self.P18.text,
                                    self.P19.text,
                                    self.P20.text,
                                    self.P21.text,
                                    self.P22.text,
                                    self.P23.text,
                                    self.P24.text,
                                    self.P25.text,
                                    self.P26.text,
                                    self.P27.text,
                                    self.P28.text,
                                    self.Mud.text)
      
      if predicted == 1:
        self.prediction.visible = True
        self.prediction.text='1'
        self.prediction_image.source = 'https://www.cdc.gov/healthywater/emergency/images/GettyImages-940598788-medium.jpg?_=60241'         
      else:
        self.prediction.visible = True
        self.prediction.text='0'
        self.prediction_image.source = 'https://cdn4.vectorstock.com/i/1000x1000/47/28/drinking-water-sign-this-water-is-safe-to-drink-vector-10934728.jpg'  
    pass

#   def model_Selection_change(self, **event_args):
#     """This method is called when an item is selected"""
#     pass






