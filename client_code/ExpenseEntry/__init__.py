from ._anvil_designer import ExpenseEntryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import datetime

class ExpenseEntry(ExpenseEntryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    # Any code you write here will run before the form opens.
    self.drop_down_category.items = anvil.server.call('getBuckets')
    self.date_picker_date.date = datetime.date.today()

  def button_submit_click(self, **event_args):
    category = self.drop_down_category.selected_value
    payee = self.text_box_payee.text
    amount = self.text_box_amount.text
    date = self.date_picker_date.date
    print(f"category: {category}, payee: {payee}, amount:{amount}, date: {date}")
    pass
