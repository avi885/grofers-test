from channels import route
import json

reply_channel_array = []

# This function will display all messages received in the console
def message_handler(message):
	print ("Websocket Received")
	print(message['text'])
	send_message('Hello QWERYY')


def ws_echo(message):
	print ("Websocket Connect")
	message.reply_channel.send({"accept": True})
	reply_channel_array.append(message.reply_channel)
	print (len(reply_channel_array))

def ws_disconnect(message):
	print ("Websocket Disconnected")
	print (len(reply_channel_array))
	for reply in reply_channel_array:
		print (reply)

def send_message(message):
    """
    Called to send a message to the room on behalf of a user.
    """
    final_msg = {'message': message}
    for reply in reply_channel_array:
    	reply.send({"text": json.dumps(final_msg)})

channel_routing = [
	route("websocket.receive", message_handler),  # we register our message handler
	route('websocket.connect', ws_echo),
	route('websocket.disconnect', ws_disconnect),
]