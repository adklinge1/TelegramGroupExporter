#  Telegram Group Chat Export Server

This project is a server that allows you to export Telegram chat messages. It provides three APIs: SendCode, Authenticate, and Get messages.

## Requirements

- [Python](https://www.python.org/downloads/): Make sure Python is installed on your system. You can download Python from the official website.
- [pip](https://pip.pypa.io/en/stable/installation/): The Python package manager. It is usually installed by default with Python.


## Installations

1. Clone the repository to your local machine:
```bash
git clone https://github.com/adklinge1/TelegramGroupExporter.git
```

2. Navigate to the project directory
```bash
cd TelegramGroupExporter\src
```
3. Install the required dependencies:

```bash
pip install quart

pip install telethon

python -m asyncio
```
## Running the Server

```bash
python telegram-api.py
```

## How to Get your Group Chat Id

To get a group's chat ID, add the 'Get My ID' bot to the group. Once it joins, send a message in the group chat. The bot will respond with your user ID and Current chat ID. The Current Chat ID, starting with a hyphen (-), is the group chat ID.

## Usage

### 1. SendCode API - receives the user's pohne number and sends the user sms message with authentication code

- Endpoint: `/send_code`
- Method: POST
- Parameters:
  - `phone_number`: The phone number to send the code to.
- Example Usage:
```bash
curl -X POST http://localhost:5000/send_code -d "phone_number=+1234567890"
```

### 2. Authenticate API - receives the authentication code and the user's phone number and authenticates the user

- Endpoint: `/authenticate`
- Method: POST
- Parameters:
- `phone_number`: The phone number used to receive the code.
- `code`: The authentication code received via SMS.
- Example Usage:

```bash
curl -X POST http://localhost:5000/authenticate -d "phone_number=+1234567890&code=12345"
```

### 3. Get messages API - receives a chat id, and a time window, and returns all the messages sent in that chat during this time window

- Endpoint: `/get_messages`
- Method: GET
- Parameters:
- `chat_id`: The ID of the Telegram chat.
- Example Usage:
```bash
curl http://localhost:5000/get_messages?chat_id=1234567890
```

### User Interface (UI)
In addition to the APIs, this project includes a user interface (UI) for a more interactive experience. The UI allows users to perform the same actions as the APIs but with a graphical interface.

To access the UI, open your web browser and navigate to http://localhost:5000 after starting the server.


## Personal Note

The project was carried out as part of the 2024 Dikehathon event and is dedicated to "זיכרון 710" organization, for the commemoration of the events of 10/7 in Israel.


## Contact

For any questions, inquiries, or assistance, please feel free to contact me via email at [klingeradi@gmail.com](mailto:your@email.com).
