from api.help import read_json
from fastapi import APIRouter

router = APIRouter(tags=["Known Ransomware Campain Use (max 10)"])

@router.get("/get/known")
def get_known():
    return get_known_cve(10)

def get_known_cve(max_quantity: int) -> list:
    """retun CVEs that is in ransomware campain use"""
    cve_dict = read_json()
    result = []
    for cve in cve_dict["vulnerabilities"]:
        if cve["knownRansomwareCampaignUse"] == "Known" and len(result) < max_quantity:
            result.append(cve)
    return result