from fastapi import FastAPI
from api import info, last_n_days, new_n, known, keyword

app = FastAPI()

app.include_router(info.router)
app.include_router(last_n_days.router)
app.include_router(new_n.router)
app.include_router(known.router)
app.include_router(keyword.router)
