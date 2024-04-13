import logging
from quart import Quart, jsonify, request, render_template
import asyncio
from telethon import TelegramClient

app = Quart(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the log level to DEBUG

# Define the Telethon client setup
async def setup_telegram_client(api_id, api_hash):
    client = TelegramClient('session_name', api_id, api_hash)
    await client.connect()
    return client

# Send authentication code request
async def send_code_request(client, phone_number):
    await client.send_code_request(phone_number)

# Authenticate user
async def authenticate_user(client,phone_number, code):
    await client.sign_in(phone_number, code)

# Get messages from group
async def get_group_messages(client, group_name):
    messages = []
    group = await client.get_entity(int(group_name))

    async for message in client.iter_messages(group):
        sender =  await client.get_entity(message.from_id)

        messages.append({'date': message.date, 'sender': message.sender_id, 'message': message.message})
    return messages

@app.route('/')
async def index():
    return await render_template('index.html')

@app.route('/send_code', methods=['POST'])
async def send_code():
    try:
        data = await request.get_json()
        phone_number = data.get('phone_number')

        api_id = "28479308"
        api_hash = 'a4f1ffa4c55177e2e35cac280cfb6031'
        
        global client 
        client = await setup_telegram_client(api_id, api_hash)
        
        await send_code_request(client, phone_number)
        # await client.disconnect()  # Close the client session after use
        return jsonify({'message': 'Code sent successfully.'}), 200
    except Exception as e:
        logging.error(f'Error in send_code: {str(e)}')
        return jsonify({'error': 'Internal Server Error'}), 500  # Return a generic error message with HTTP status code 500 (Internal Server Error)

@app.route('/authenticate', methods=['POST'])
async def authenticate():
    try:
        data = await request.get_json()
        
        auth_code = data.get('auth_code')
        phone_number = data.get('phone_number')

        api_id = "28479308"
        api_hash = 'a4f1ffa4c55177e2e35cac280cfb6031'

        # client = await setup_telegram_client(api_id, api_hash)

        await authenticate_user(client, phone_number, auth_code)
        # await client.disconnect()  # Close the client session after use
        return jsonify({'message': 'Authentication successful.'}), 200
    except Exception as e:
        logging.error(f'Error in authenticate: {str(e)}')
        return jsonify({'error': 'Internal Server Error'}), 500  # Return a generic error message with HTTP status code 500 (Internal Server Error)

@app.route('/get_messages', methods=['POST'])
async def get_messages():
    try:
        data = await request.get_json()
        group_name = data.get('group_name')

        api_id = "28479308"
        api_hash = 'a4f1ffa4c55177e2e35cac280cfb6031'
        # client = await setup_telegram_client(api_id, api_hash)

        messages = await get_group_messages(client, group_name)
        await client.disconnect()  # Close the client session after use
        return jsonify(messages), 200
    except Exception as e:
        logging.error(f'Error in get_messages: {str(e)}')
        return jsonify({'error': 'Internal Server Error'}), 500  # Return a generic error message with HTTP status code 500 (Internal Server Error)

if __name__ == '__main__':
    app.run(debug=True)
