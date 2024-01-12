from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ..Auth import Login
from anvil.tables import app_tables

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user = Login()
    self.menucomedorbtn.visible = get_url_hash() == "edit_comedor" or True

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Responsables')

  def button_1_copy_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Aulas')

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Aulas')

  def menucomedorbtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Comedor_Comedores')
