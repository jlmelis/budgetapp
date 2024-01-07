from ._anvil_designer import PayeesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Payees(PayeesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_buckets.items = anvil.server.call('get_data', 'payees')

  def button_add_payee_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_payee_name.text
    if name is not "":
      anvil.server.call('create_payee', name)
      self.repeating_panel_buckets.items = anvil.server.call('get_data', 'payees')
      self.text_box_payee_name.text = ""
    

  def button_refresh_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('refresh_data', 'payees')
    self.repeating_panel_buckets.items = anvil.server.call('get_data', 'payees')
    
