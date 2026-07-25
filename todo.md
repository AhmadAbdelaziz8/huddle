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
    - GET api/rooms/:id join room with it's id
    - DELETE api/rooms/id delete the room (when call ends)
    - Signaling server through ws 

# implementation plan
## backend
create the endpoints using django 