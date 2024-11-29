from api.help import read_json
from fastapi import APIRouter
import json
import re

router = APIRouter(tags=["Search by keyword"])

@router.get("/get")
def get_keyword(query: str):
    return find_keyword(query)

def find_keyword(keyword: str) -> list:
    """return all CVEs where keyword was found"""
    result = []
    cve_dict = read_json()
    for cve in cve_dict["vulnerabilities"]:
        text = json.dumps(cve)
        if re.search(keyword, text, re.IGNORECASE):
            result.append(cve)
    return result
