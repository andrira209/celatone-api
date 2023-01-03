from flask import Flask, send_file
import os

import func.codes as codes
import func.contracts as contracts
import func.accounts as accounts
import func.assets as assets
import func.projects as projects
import func.entities as entities
import func.balances as balances

from apiflask import APIFlask

app = APIFlask(__name__)

# Root


@app.route("/", methods=["GET"])
def hello_world():
    return {"gm": "gm"}


# Codes


@app.route("/codes/<chain>/<network>", methods=["GET"])
def get_codes(chain, network):
    """Get details of all known codes.

    Returns a list of all the known codes based on the input chain and network
    """
    return codes.get_codes(chain, network)


@app.route("/codes/<chain>/<network>/<code_id>", methods=["GET"])
def get_code(chain, network, code_id):
    """Get the details of a specific code ID.

    Returns a specific code based on the input chain, network, and code_id
    """
    return codes.get_code(chain, network, code_id)


# Contracts


@app.route("/contracts/<chain>/<network>", methods=["GET"])
def get_contracts(chain, network):
    """Get details of all known contracts.

    Returns a list of all the known contracts based on the input chain and network"""
    return contracts.get_contracts(chain, network)


@app.route("/contracts/<chain>/<network>/<contract_address>", methods=["GET"])
def get_contract(chain, network, contract_address):
    """Get the details of a specific contract address.

    Returns a specific contract based on the input chain, network, and contract_address"""
    return contracts.get_contract(chain, network, contract_address)


# Accounts


@app.route("/accounts/<chain>/<network>", methods=["GET"])
def get_accounts(chain, network):
    return accounts.get_accounts(chain, network)


@app.route("/accounts/<chain>/<network>/<account_address>", methods=["GET"])
def get_account(chain, network, account_address):
    return accounts.get_account(chain, network, account_address)


# Assets


@app.route("/assets/<chain>/<network>", methods=["GET"])
def get_assets(chain, network):
    return assets.get_assets(chain, network)


@app.route("/assets/<chain>/<network>/type/<asset_type>", methods=["GET"])
def get_asset_by_type(chain, network, asset_type):
    return assets.get_asset_by_type(chain, network, asset_type)


@app.route("/assets/<chain>/<network>/slug/<asset_slug>", methods=["GET"])
def get_asset_by_slug(chain, network, asset_slug):
    return assets.get_asset_by_slug(chain, network, asset_slug)


@app.route("/assets/<chain>/<network>/<asset_id>", methods=["GET"])
def get_asset(chain, network, asset_id):
    return assets.get_asset(chain, network, asset_id)


@app.route("/assets/<chain>/<network>/ibc/<hash>", methods=["GET"])
def get_asset_ibc(chain, network, hash):
    return assets.get_asset_ibc(chain, network, hash)


@app.route("/assets/<chain>/<network>/factory/<creator>/<symbol>", methods=["GET"])
def get_asset_factory(chain, network, creator, symbol):
    return assets.get_asset_factory(chain, network, creator, symbol)


@app.route("/assets/<chain>/<network>/gamm/pool/<pool_id>", methods=["GET"])
def get_asset_gamm(chain, network, pool_id):
    return assets.get_asset_gamm(chain, network, pool_id)


# Projects


@app.route("/projects/<chain>/<network>", methods=["GET"])
def get_projects(chain, network):
    return projects.get_projects(chain, network)


@app.route("/projects/<chain>/<network>/<project_id>", methods=["GET"])
def get_project(chain, network, project_id):
    return projects.get_project(chain, network, project_id)


# Entities


@app.route("//entities", methods=["GET"])
def get_entities():
    return entities.get_entities()


@app.route("//entities/<entity_slug>", methods=["GET"])
def get_entity(entity_slug):
    return entities.get_entity(entity_slug)


# Balances


@app.route("/balances/<chain>/<network>/<account_address>", methods=["GET"])
def get_balances(chain, network, account_address):
    return balances.get_balances(app, chain, network, account_address)


# Images


@app.route("/images/entities/<entity_slug>", methods=["GET"])
def get_entity_image(entity_slug):
    return send_file(f"../registry/assets/entities/{entity_slug}.png")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))