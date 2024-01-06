from ._anvil_designer import ExpenseEntryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

class ExpenseEntry(ExpenseEntryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.drop_down_buckets.items = anvil.server.call('get_buckets')
    self.drop_down_payees.items = anvil.server.call('get_payees')
    self.date_picker_date.date = datetime.date.today()

  def clear_inputs(self):
    self.drop_down_buckets.selected_value = None
    self.drop_down_payees.selected_value = None
    self.text_box_amount.text = ""
    self.date_picker_date.date = datetime.date.today()
    
  def button_submit_click(self, **event_args):
    bucket = self.drop_down_buckets.selected_value
    payee = self.drop_down_payees.selected_value
    amount = self.text_box_amount.text
    date = self.date_picker_date.date
    anvil.server.call('create_expense', bucket, payee, amount, date)
    # reset fields
    self.clear_inputs()
    pass