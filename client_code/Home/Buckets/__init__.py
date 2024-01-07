from ._anvil_designer import BucketsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Buckets(BucketsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_buckets.items = anvil.server.call('get_data', 'buckets')

  def button_add_bucket_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_bucket_name.text
    target = self.text_box_target.text
    if name is not "" and target is not None:
      anvil.server.call('create_bucket', name, target)
      self.repeating_panel_buckets.items = anvil.server.call('get_data', 'buckets')
      self.text_box_bucket_name.text = ""
      self.text_box_target.text = None
    

  def button_refresh_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('refresh_data', 'buckets')
    self.repeating_panel_buckets.items = anvil.server.call('get_data', 'buckets')
    
