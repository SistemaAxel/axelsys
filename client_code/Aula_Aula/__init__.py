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
    self.user = Login()
    self.aula = aula
    self.aulaid = aula
    self.init_components(**properties)
    self.aula_name.text = f"{self.aula['Aula']}, {self.aula['Escuela']}"
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Responsables', aula=self.aula)

  def button_2_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Aula_Aulas')

  def button_x_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    us = app_tables.users.search(email=self.correo.text)
    if len(us) == 0:
      alert("El usuario no existe, el usuario debe de estar registrado en Sistemas Axel para continuar.")
      return
    users = self.aula['users']
    users.append(us[0])
    self.aula.update(users=users)
    self.add_card.visible = False

  def button_1_copy_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_card.visible = False

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_card.visible = True

  def button_1_copy_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    if alert("¿Deseas borrar esta aula?"):
      self.aula.delete()
      open_form('Aula_Aulas')
