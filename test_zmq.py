import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://172.16.16.197:10000")

for i in xrange(10):
    print "send message ", i, "..."
    socket.send("oh my god")
    msg = socket.recv()
    print "receive message ", i, "[", msg, "]"
