from api.help import read_json
from fastapi import APIRouter

router = APIRouter(tags=["10 newest CVEs"])

@router.get("/get/new")
def get_new():
    return get_n_new_cves(10)

def get_n_new_cves(quantity: int) -> list:
    """retun list of N newest CVEs"""
    cve_dict = read_json()
    result = []

    for i, cve, in enumerate(cve_dict["vulnerabilities"]):
        if i >= quantity:
            break
        result.append(cve)
    return result
