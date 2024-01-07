import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

supabase_url = "https://tjryiccnllfxwmyzpnrg.supabase.co/rest/v1/"

def call_Api(endpoint, data = None, method = "GET"):
  try:
    response = anvil.http.request(supabase_url + endpoint, 
                                  json = True,
                                  method = method,
                                  headers = {
                                    "Authentication": anvil.secrets.get_secret('supabase_key'),
                                    "apikey": anvil.secrets.get_secret('supabase_key')
                                  },
                                 data = data)
    return response
  except anvil.http.HttpError as e:
    if e.status is not 201:
      print(f"error = {e} status = {e.status}")

@anvil.server.callable
def get_data(type):
  if anvil.server.session.get(type) is None:
    response = call_Api(f"{type}?select=*")
    anvil.server.session[type] = response

  return anvil.server.session.get(type)


@anvil.server.callable
def create_expense(bucket, payee, amount, date):
  data = {
            "bucket_id": bucket,
            "payee_id": payee,
            "amount": amount,
            "date": str(date)
          }
  response = call_Api('expenses', data, 'POST')

@anvil.server.callable
def create_bucket(name, target):
  data = {
            "name": name,
            "target": target
          }
  response = call_Api('buckets', data, 'POST')
  # after an add we need to refresh the list of buckets
  refresh_data('buckets')
  
@anvil.server.callable
def create_payee(name):
  data = {
            "name": name
          }
  response = call_Api('payees', data, 'POST')
  # after an add we need to refresh the list of buckets
  refresh_data('payees')

@anvil.server.callable
def refresh_data(type):
  anvil.server.session[type] = None
  get_data(type)

 