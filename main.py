print("Afam update test")

import os
from datetime import datetime
import json
from email_fetch import fetch_latest_email 
from ai_service import summarise

# Helper function
def clear():
    os.system('cls' if os.name=='nt' else 'clear') 

def pause():
    input('\npress enter to continue...')  

# Dashboard
def show_dashboard():
    clear() 
    print('=== INBOXBATE DASHBOARD ===\n')  
    print('Syncing latest emails (latest 5)...\n')
    fetch_latest_email() #saves latest 5 emails to JSON 

    print('\nGenerating summary...\n') 
    summary = summarise() #reads JSON

    print('\n--- SUMMARY OF 5 LATEST EMAILs ---\n') 
    print(summary)  

    pause() 

#send email page
def send_email_page():
    clear() 
    print('=== SEND EMAIL ===\n') 
    to = input('Reciepient Email:').strip() 
    subject = input('Subject:').strip()
    body = input('Message:').strip() 
    from datetime import datetime 

    import json

    email_entry ={ 
        'to': to,
        'subject':subject,
        'body':body,
        'date': str(datetime.now()),
    } 

    try:
        filename = 'sent_emails.json'
        #load existing sent emails 
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                sent_emails=json.load(f)
        except FileNotFoundError:
            sent_emails = []     

        sent_emails.append(email_entry)   

        with open(filename, 'w', encoding='utf-8' ) as f:
            json.dump(sent_emails, f, indent=4, ensure_ascii=False) 

            print('\nEmail saved successfully (simulated send).') 
    except Exception as e:
        print(f'\nError saving email: {e}')     

    pause()   

# main CLI Menu 
def Main():
    while True:
        clear()
        print('===INBOXBATE ===\n') 
        print('1. View Dashboard (latest 5 emails summary)') 
        print('2. Send Email') 
        print('3. Sync Emails Only') 
        print('4. Exit') 

        choice = input('Choose an option').strip() 

        # Logic
        if choice =="1":
            show_dashboard() 

        elif choice =='2':
            send_email_page()

        elif choice =='3': 
            clear()
            print('Syncing latest emails...\n') 
            fetch_latest_email() 
            print('\nDone.') 
            pause() 

        elif choice =='4':
            print('\nGoodbye 👋')    
            break
        else:
            print('\nInvalid option. Try again.') 

            pause() 
# entry Point 
if __name__ == "__main__": 
    Main()

  


      
                    
            

           




