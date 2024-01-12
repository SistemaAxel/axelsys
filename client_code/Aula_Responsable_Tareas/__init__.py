from ._anvil_designer import Aula_Responsable_TareasTemplate
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

class Aula_Responsable_Tareas(Aula_Responsable_TareasTemplate):
  def __init__(self, responsable, **properties):
    # Set Form properties and Data Bindings.
    self.user = Login()
    self.init_components(**properties)
    self.aula = responsable['Aula']
    self.aulaid = responsable['Aula'].get_id()
    self.responsable = responsable
    self.aulaname.text = self.aula['Aula']
    self.name.text = "Tareas de " + self.responsable['Nombre']
    self.responsablename.text = self.responsable['Nombre']
    self.repeating_panel_1.items = app_tables.tareas.search(Responsable=self.responsable)
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
    app_tables.tareas.add_row(Responsable=self.responsable, Detalles=self.bxdetalles.text, Fecha=self.bxfecha.date, Tipo=self.bxtarea.text)
    self.addcard.visible = False
    self.repeating_panel_1.items = app_tables.tareas.search(Responsable=self.responsable)
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.addcard.visible = True

  def responsablename_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Responsable', responsable=self.responsable)

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.addcard.visible = False
