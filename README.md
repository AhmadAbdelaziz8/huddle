# huddle

A minimal Google Meet clone, built for learning how video calls work under the hood.

Create a room, share the link, and talk face to face with whoever opens it. No accounts, no sign-up. The link is the invite.

## Features

- Create a meeting and get a shareable link
- Join a call by opening the link
- Toggle your mic and camera
- End the call for everyone
- Get notified when the other person leaves or drops

## How it works

Audio and video go **directly between the two browsers** over WebRTC. The server never sees the media. Its only job is to help the browsers find each other.

1. **REST API** (Django REST Framework): creates, checks and closes rooms.
2. **Signaling server** (Django Channels over WebSocket): relays the WebRTC handshake (`offer`, `answer`, `ice-candidate`) between the two peers in a room.

```text
Browser A ──┐                         ┌── Browser B
            │  WebSocket (signaling)  │
            └────────► Django ◄───────┘
Browser A ◄════════ WebRTC media ════════► Browser B
```

## API

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/rooms/` | Create a room. Returns its `join_url` |
| `GET` | `/api/rooms/<id>/` | Check that a room exists and is active |
| `DELETE` | `/api/rooms/<id>/` | End the call and close the room |
| `WS` | `/ws/rooms/<id>/` | Join the room's signaling channel |

## Tech stack

- **Backend:** Python 3.14, Django, Django REST Framework, Django Channels, Daphne
- **Realtime:** WebRTC (peer-to-peer media), WebSockets (signaling)
- **Database:** SQLite

## Getting started

Requires [uv](https://docs.astral.sh/uv/).

```bash
cd backend
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Then create a room:

```bash
curl -X POST http://localhost:8000/api/rooms/
```

Run the tests:

```bash
uv run python manage.py test
```

## Roadmap

- [x] Room model
- [x] Create room endpoint
- [ ] Get and delete room endpoints
- [ ] WebSocket signaling (`offer`, `answer`, `ice-candidate`)
- [ ] Notify peers when someone leaves or the room closes
- [ ] Frontend: camera and mic, call UI, controls

## What I'm learning

- How WebRTC peers connect (SDP offers and answers, ICE candidates, STUN)
- Why a signaling server is needed even for peer-to-peer calls
- Running HTTP and WebSockets side by side with ASGI and Django Channels
