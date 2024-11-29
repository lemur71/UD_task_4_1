from api.help import read_json
from datetime import date, datetime, timedelta
from fastapi import APIRouter

router = APIRouter(tags=["CVEs for past 5 days (max 40 CVEs)"])

@router.get("/get/all")
def get_all():
    return get_recent_cves(5, 40)

def get_recent_cves(days: int, max_quantity: int) -> list:
    """retun list of CVEs added last N days"""
    cve_dict = read_json()
    
    def n_days_ago(days_ago: int) -> str:
        """calculate date for N days ago"""
        return date.today() - timedelta(days=days_ago)

    result = []
    for i, cve in enumerate(cve_dict["vulnerabilities"]):
        date_added = datetime.strptime(cve["dateAdded"], "%Y-%m-%d").date()
        if date_added >= n_days_ago(days) and i < max_quantity:
            result.append(cve)
    return result
