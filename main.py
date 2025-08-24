from fastapi import FastAPI
from routes import event_routes  # 👈 our router package

app = FastAPI(
    title="College Ticket Booking System",
    description="A simple ticket booking system for college events.",
    version="1.0.0"
)

# include event routes
app.include_router(event_routes.router, prefix="/events", tags=["Events"])


@app.get("/")
def root():
    return {"message": "Welcome to the College Ticket Booking System"}

