1. Overview

This project is a College Event Ticket Booking System where students can view upcoming events and book tickets.
It will support:

Event creation (by admin).

Students booking tickets.

Real-time availability tracking.

Concurrency-safe ticket booking.

The purpose is to learn backend fundamentals (auth, concurrency, Redis, multithreading, websockets, etc.) while producing a resume-worthy project.

2. Goals

Practice backend system design with FastAPI (Python).

Explore Redis for caching and distributed locking.

Understand concurrency in ticket booking.

Experiment with WebSockets for real-time updates (optional extra).

Use JWT authentication for students/admins.

3. Tech Stack

Backend: Python (FastAPI)

Database: PostgreSQL (events, users, tickets)

Cache/Locking: Redis

Auth: JWT (JSON Web Tokens)

Concurrency: asyncio (FastAPI), threading locks, Redis distributed lock

WebSocket: For live ticket availability updates

Deployment (later): Docker + GitHub Actions (CI/CD)

4. Core Features
4.1 Event Management

Admin can create events with:

Event name

Description

Venue

Date & time

Total tickets available

4.2 Ticket Booking

Students can book tickets for an event.

Prevent overselling via:

Atomic Redis locks (or DB transactions).

If tickets = 0 → booking denied.

4.3 User Authentication

Student/Admin signup & login.

JWT token issued on login.

Protected routes (e.g., /events/create requires Admin role).

4.4 Real-Time Updates (Stretch Goal)

Students see ticket counts update live using WebSockets.

Example: If 100 → 99 → 98 as bookings happen.

5. API Endpoints (Draft)

Auth

POST /signup

POST /login

Events

POST /events (Admin only)

GET /events (List all events)

GET /events/{id} (Get event details)

Tickets

POST /events/{id}/book (Book ticket)

GET /events/{id}/status (Check availability)

6. Data Models
User
User {
  id: int
  name: str
  email: str
  password_hash: str
  role: str  # "student" or "admin"
}

Event
Event {
  id: int
  name: str
  description: str
  venue: str
  datetime: datetime
  total_tickets: int
  tickets_remaining: int
}

Ticket
Ticket {
  id: int
  user_id: int
  event_id: int
  booked_at: datetime
}

7. Concurrency & Redis Plan

Race condition risk: If two students try to book the last ticket at the same time.

Solution:

Use Redis lock (SETNX) to lock event booking.

Decrement ticket count safely.

Release lock.

8. Future Enhancements

Payments integration (Stripe mock).

Event categories (Concert, Sports, Tech Fest).

Leaderboard of most popular events.

Admin dashboard with analy