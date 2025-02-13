# Telegram Auto Insult

This is built using the Telethon library. It listens for messages from a specific user (e.g., your friend) and replies with a random insult from a predefined list.

---

## How to Use

0. **Clone the Repository**:
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/Heiliger4/Auto-telegram-insult.git
     ```
   - Navigate to the project directory:
     ```bash
     cd Auto-telegram-insult
     ```

1. **Install Dependencies**:
   - Install the required libraries using the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

2. **Set Up Telegram API**:
   - Go to [my.telegram.org](https://my.telegram.org) and create a new application to get your `api_id` and `api_hash`.

3. **Replace Placeholder Values**:
   - Replace the following placeholders in the script:
     ```python
     api_id = 'xxxx'  # Replace with your api_id from my.telegram.org
     api_hash = 'xxxx'  # Replace with your api_hash from my.telegram.org
     phone_number = 'xxxx'  # Replace with your phone number used on Telegram
     ```
   - **Ask your friend for their user ID**:
     - Your friend can use the Telegram bot [@userinfobot](https://t.me/userinfobot) to find their user ID. They just need to send any message to the bot, and it will reply with their user ID. You can find more about this bot on its [GitHub page](https://github.com/nadam/userinfobot).
     - Once you get their user ID, replace the `event.sender_id` in the script:
       ```python
       if event.sender_id == xxxx:  # Replace xxxx with your friend's user ID
       ```

4. **Run the Bot**:
   - Execute the script:
     ```bash
     python insult.py
     ```
   - The bot will start and listen for messages from the specified user. When a message is received, it will reply with a random insult after a 2-second delay.

---

## What It Does
- The bot listens for new messages.
- If the message is from the specified user, it waits for 2 seconds and then sends a random insult from the predefined list.

---

