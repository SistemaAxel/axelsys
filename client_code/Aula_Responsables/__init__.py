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
    self.aula_back.text = self.aula['Aula']
    self.repeating_panel_1.items = app_tables.responsables.search(Aula = self.aula)
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_2_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Aulas')

  def aula_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Aula', aula=self.aulaid)

  def button_1_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.responsables.add_row(Aula=self.aula, Nombre=self.nombre.text, Correo=self.Correo.text, Telefono=self.telefono.text, Notas=self.notas.text)
    self.addcard.visible = False
    self.repeating_panel_1.items = app_tables.responsables.search(Aula = self.aula)