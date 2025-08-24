from fastapi import APIRouter

router = APIRouter(tags=["events"])

@router.get("/")
def get_events():
    return {"message": "List of events will come here"}
