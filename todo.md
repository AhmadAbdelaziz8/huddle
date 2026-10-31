
# functional requirements
    - generate link
    - control on mic, camera
    - join call
    - End call

# Non functional requirements:
    - graceful error handling: if user disconnect, the rest know
    - simple auth ( clicking the link )

# API
    - POST api/rooms/ create room, returns the "join_url"
    - GET api/rooms/:id check if the room is there and active before joining
    - api/wss:/rooms/:id join room with it's id "signaling server through WS"
    - DELETE api/rooms/id delete the room (when call ends)

# implementation plan
## backend
create the endpoints using 
- django rest framework for the endpoints
- django channels for websocket 

checklist
[x] Room model: id, created_at, is_active
[x] POST /api/rooms/ → returns { "join_url": "https://.../rooms/abc123" }
[ ] DELETE /api/rooms/:id → sets is_active=False, broadcasts room-closed to peers
[ ] WebSocket: handle offer, answer, ice-candidate, peer-left messages
[ ] Graceful disconnect: if WS drops, broadcast peer-left to the other peer


