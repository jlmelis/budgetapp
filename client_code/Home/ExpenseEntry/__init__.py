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
    self.date_picker_date.date = datetime.date.today()
    #self.refresh_data()

  def refresh_data(self):
    self.drop_down_buckets.items = [(row["name"], row["id"]) for row in anvil.server.call('get_data', 'buckets')]
    self.drop_down_payees.items = [(row["name"], row["id"]) for row in anvil.server.call('get_data', 'payees')]

  def clear_inputs(self):
    self.drop_down_buckets.selected_value = None
    self.drop_down_payees.selected_value = None
    self.text_box_amount.text = ""
    self.date_picker_date.date = datetime.date.today()
    self.label_error.text = ""
    self.label_error.visible = False
    
  def button_submit_click(self, **event_args):
    bucket = self.drop_down_buckets.selected_value
    payee = self.drop_down_payees.selected_value
    amount = self.text_box_amount.text
    date = self.date_picker_date.date
    if bucket is None or payee is None or not amount:
      self.label_error.text = "*Please fill out all fields"
      self.label_error.visible = True
    else:
      anvil.server.call('create_expense', bucket, payee, amount, date)
      # reset fields
      self.clear_inputs()

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.refresh_data()
    pass
    