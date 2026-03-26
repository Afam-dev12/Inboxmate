import ollama 
import json


def summarise(file_path = "email_fetch.json"):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            emails = json.load(f)
    except FileNotFoundError:
        return "Error: email.json not found. Run fetch_email.py first."
    email_context = ""
    for i, mail in enumerate(emails, 1):
        email_context += f"\n--- Email {i} ---\n"
        email_context += f"From: {mail['from']}\n"
        email_context += f"Subject: {mail['subject']}\n"
        email_context += f"Content: {mail['content'][:500]}\n"

    system_prompt = (
        "You are InboxMate, a helpful local AI assistant. "
        "Summarize the following emails concisely. Highlight action items "
        "like login codes, deadlines, or meeting requests. Be brief and professional."
    )

    print(f"Informing Ollama... (using gemma:2b)")
    try:
        response = ollama.generate(
            model='gemma3:270m', 
            system=system_prompt,
            prompt=f"Here are my latest emails. Please summarize them:\n{email_context}"
        )
        return response['response']
    except Exception as e:
        return f"Ollama Error: {str(e)}"

if __name__ == "__main__":
    summary = summarise()
    print("\n--- INBOXMATE SUMMARY ---")
    print(summary)