from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

from .ExpenseEntry import ExpenseEntry
from .Buckets import Buckets
from .Payees import Payees

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    # Any code you write here will run before the form opens.
    self.content_panel.add_component(ExpenseEntry())
    self.link_expense_entry.tag.form_to_open = ExpenseEntry()
    self.link_buckets.tag.form_to_open = Buckets()
    self.link_payees.tag.form_to_open = Payees()



  def nav_link_click(self, **event_args):
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)
    return
    








