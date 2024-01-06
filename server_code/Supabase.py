import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_buckets():
  response = anvil.http.request("https://tjryiccnllfxwmyzpnrg.supabase.co/rest/v1/buckets?select=*", json=True, 
                            headers = {
                              "Authentication": anvil.secrets.get_secret('supabase_key'),
                              "apikey": anvil.secrets.get_secret('supabase_key')
                            })

  return [(row["name"], row["id"]) for row in response]

@anvil.server.callable
def get_payees():
  response = anvil.http.request("https://tjryiccnllfxwmyzpnrg.supabase.co/rest/v1/payees?select=*", json=True, 
                            headers = {
                              "Authentication": anvil.secrets.get_secret('supabase_key'),
                              "apikey": anvil.secrets.get_secret('supabase_key')
                            })

  return [(row["name"], row["id"]) for row in response]

@anvil.server.callable
def create_expense(bucket, payee, amount, date):
  print(f"payee: {payee}")
  try:
    response = anvil.http.request("https://tjryiccnllfxwmyzpnrg.supabase.co/rest/v1/expenses",
                            method = "POST",
                            headers = {
                              "Authentication": anvil.secrets.get_secret('supabase_key'),
                              "apikey": anvil.secrets.get_secret('supabase_key')
                            },
                            data = {
                              "bucket_id": bucket,
                              "payee_id": payee,
                              "amount": amount,
                              "date": str(date)
                            })
    print(response)
  except anvil.http.HttpError as e:
    print(e)


  