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
def get_buckets():
  if anvil.server.session.get('buckets') is None:
    response = call_Api("buckets?select=*")
    anvil.server.session['buckets'] = [(row["name"], row["id"]) for row in response]

  return anvil.server.session.get('buckets')

@anvil.server.callable
def get_payees():
  if anvil.server.session.get('payees') is None:
    response = call_Api("payees?select=*")
    anvil.server.session['payees'] = [(row["name"], row["id"]) for row in response]

  return anvil.server.session['payees']

@anvil.server.callable
def create_expense(bucket, payee, amount, date):
  data = {
            "bucket_id": bucket,
            "payee_id": payee,
            "amount": amount,
            "date": str(date)
          }
  response = call_Api("expenses", data, "POST")
 