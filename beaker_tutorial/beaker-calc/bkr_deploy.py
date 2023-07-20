from bkr_contract import app, add
from beaker import sandbox, client

# Build and compilling application in TEAL
app.build().export("./artifacts")

# Getting the accounts from sandbox
accounts = sandbox.kmd.get_accounts()
sender = accounts[0]

# Application client, allows easier creation/interation with app
app_client = client.ApplicationClient(
    client = sandbox.get_algod_client(),
    app = app,
    sender = sender.address,
    signer = sender.signer,
    )

# Using app client to create app
app_id, addr, txid = app_client.create()
print(
    f"""\nThis application returns the app details and works as a weird calculator that can add two numbers together.\n
    App Details:
    Deployed app in txid {txid}
    App ID: {app_id}
    App Address {addr}
    """
)

# Returning value by calling of APP CLIENT to call ADD method 
return_value = app_client.call(add, a = 10, b = 5).return_value
print(f"Addition Calculation:\nadd => {return_value}")
