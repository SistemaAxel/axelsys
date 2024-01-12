from ._anvil_designer import Comedor_ComedoresTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ..Auth import Login
from anvil.tables import app_tables

class Comedor_Comedores(Comedor_ComedoresTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.user = Login()
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.comedores.search()

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')
