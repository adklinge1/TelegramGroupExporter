from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (you can replace this with your own data source)
group_chats = [
    {'id': 1, 'name': 'Group 1', 'code': '12345', 'chat': 'Lorem ipsum dolor sit amet...'},
    {'id': 2, 'name': 'Group 2', 'code': '67890', 'chat': 'Consectetur adipiscing elit...'}
]

# Endpoint to export group chat
@app.route('/api/export_group_chat', methods=['GET'])
def export_group_chat():
    group_id = request.args.get('groupId')
    code = request.args.get('code')
    phone_number = request.args.get('phoneNumber')

    # Validate the code and phone number
    if code != 'your_secret_code':
        return jsonify({'error': 'Invalid code'}), 400
    if not phone_number:
        return jsonify({'error': 'Phone number is required'}), 400

    # Find the group chat by ID
    group_chat = next((item for item in group_chats if str(item['id']) == group_id), None)
    if group_chat:
        del group_chat['name']  # Remove the 'name' field from the response
        return jsonify({'group_chat': group_chat})
    return jsonify({'error': 'Group chat not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
