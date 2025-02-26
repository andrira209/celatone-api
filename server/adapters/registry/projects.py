import json

from adapters.core import accounts, assets
from adapters.cosmwasm import codes, contracts


def load_project_data(chain, network):
    loaded_accounts = accounts.get_accounts(chain, network)
    loaded_assets = assets.get_assets(chain, network)
    loaded_codes = codes.get_codes(chain, network)
    loaded_contracts = contracts.get_contracts(chain, network)
    return loaded_accounts, loaded_assets, loaded_codes, loaded_contracts


def load_project(entity, accounts, assets, codes, contracts):
    relevant_accounts = [
        account for account in accounts if account["slug"] == entity["slug"]
    ]
    relevant_assets = [asset for asset in assets if entity["slug"] in asset["slugs"]]
    relevant_codes = [code for code in codes if code["slug"] == entity["slug"]]
    relevant_contracts = [
        contract for contract in contracts if contract["slug"] == entity["slug"]
    ]
    if relevant_accounts or relevant_codes or relevant_contracts:
        return {
            "slug": entity["slug"],
            "details": {
                "name": entity["name"],
                "description": entity["description"],
                "website": entity["website"],
                "github": entity["github"],
                "logo": f"https://celatone-api.alleslabs.dev/images/entities/{entity['slug']}",
                "socials": entity["socials"],
            },
            "accounts": relevant_accounts,
            "assets": relevant_assets,
            "codes": relevant_codes,
            "contracts": relevant_contracts,
        }
    return None


def load_projects(chain, network):
    entities = json.load(open(f"../registry/data/entities.json"))
    accounts, assets, codes, contracts = load_project_data(chain, network)
    projects = []
    for entity in entities:
        entity_dict = load_project(entity, accounts, assets, codes, contracts)
        if entity_dict is not None:
            projects.append(entity_dict)
    return projects


def get_projects(chain, network):
    projects = load_projects(chain, network)
    return projects


def get_project(chain, network, slug):
    accounts, assets, codes, contracts = load_project_data(chain, network)
    entities = json.load(open(f"../registry/data/entities.json"))
    entity = [entity for entity in entities if entity["slug"] == slug][0]
    project = load_project(entity, accounts, assets, codes, contracts)
    if project is None:
        return []
    return project
