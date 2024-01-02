import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def getBuckets():
  response = anvil.http.request("https://tjryiccnllfxwmyzpnrg.supabase.co/rest/v1/buckets?select=*", json=True, 
                            headers = {
                              "Authentication": anvil.secrets.get_secret('supabase_key'),
                              "apikey": anvil.secrets.get_secret('supabase_key')
                            })

  return [(row["name"], row["id"]) for row in response]