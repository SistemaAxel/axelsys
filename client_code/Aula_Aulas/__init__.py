from ._anvil_designer import Aula_AulasTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ..Auth import Login
from anvil.tables import app_tables

class Aula_Aulas(Aula_AulasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.user = Login()
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.aulas.search(users=[self.user])
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_crd.visible = True

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.aulas.add_row(Aula=self.aula.text, Escuela=self.escuela.text, Direccion=self.direccion.text, users=[self.user])
    self.add_crd.visible = False
    self.repeating_panel_1.items = app_tables.aulas.search(users=[self.user])
