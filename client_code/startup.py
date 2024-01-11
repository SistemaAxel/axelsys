import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
hash = get_url_hash()
if hash == "":
  open_form('Main')
elif hash["p"] == "menucomedor":
  open_form("Embed_menucomedor")