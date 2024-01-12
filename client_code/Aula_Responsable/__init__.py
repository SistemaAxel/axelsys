from ._anvil_designer import Aula_ResponsableTemplate
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

class Aula_Responsable(Aula_ResponsableTemplate):
  def __init__(self, responsable, **properties):
    # Set Form properties and Data Bindings.
    self.user = Login()
    self.init_components(**properties)
    self.aula = responsable['Aula']
    self.responsable = responsable
    self.aulaname.text = self.aula['Aula']
    self.name.text = self.responsable['Nombre']
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')

  def button_2_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Aulas')

  def aulaname_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Aula', aula=self.aula)

  def button_2_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Responsables', aula=self.aula)

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Responsable_Tareas', responsable=self.responsable)
