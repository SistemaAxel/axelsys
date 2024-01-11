from ._anvil_designer import Aula_AulaTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ..Auth import Login
from anvil.tables import app_tables

class Aula_Aula(Aula_AulaTemplate):
  def __init__(self, aula: int, **properties):
    # Set Form properties and Data Bindings.
    user = Login()
    self.aula = app_tables.aulas.get_by_id(aula)
    self.aulaid = aula
    self.init_components(**properties)
    self.aula_name.text = f"{self.aula['Aula']}, {self.aula['Escuela']}"
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Responsables', aula=self.aulaid)
