from ._anvil_designer import Aula_ResponsablesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ..Auth import Login
from anvil.tables import app_tables

class Aula_Responsables(Aula_ResponsablesTemplate):
  def __init__(self, aula, **properties):
    # Set Form properties and Data Bindings.
    user = Login()
    self.aula = app_tables.aulas.get_by_id(aula)
    self.aulaid = aula
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')
