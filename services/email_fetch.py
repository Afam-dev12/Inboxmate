import json
from imap_tools import MailBox, AND

def fetch_latest_emails(config_path='config.json', output_filename='email.json'):
    """
    Fetches the 5 latest emails and saves them to a JSON file.
    """
    # 1. Load configuration
    try:
        with open(config_path, 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: {config_path} not found.")
        return

    email = config_data.get("EMAIL")
    password = config_data.get("PASSWORD")
    host = config_data.get("HOST")

    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print(f"Logging in as {email}")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    emails_list = []
    
    # 2. Connect and Fetch
    try:
        with MailBox(host).login(email, password) as mailbox:
            # We use limit=5 and reverse=True to get the absolute latest
            for msg in mailbox.fetch(AND(all=True), limit=5, reverse=True):
                entry = {
                    "uid": msg.uid,
                    "from": msg.from_,
                    "subject": msg.subject,
                    "date": str(msg.date),
                    "content": msg.text.strip()
                }
                emails_list.append(entry)
    except Exception as e:
        print(f"IMAP Error: {e}")
        return

    # 3. Save to JSON
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(emails_list, f, indent=4, ensure_ascii=False)
        print(f"Successfully synced 5 emails to {output_filename}")
    except Exception as e:
        print(f"File Write Error: {e}")

# This allows you to still run this file directly for testing
if __name__ == "__main__":
    fetch_latest_emails()