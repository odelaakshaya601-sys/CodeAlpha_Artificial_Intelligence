import tkinter as tk
from tkinter import messagebox

# Simple database of frequently asked questions and answers
FAQ_DATA = {
    "what is your return policy?": "We offer a 30-day money-back guarantee. Items must be returned in their original packaging and unused condition.",
    "how long does shipping take?": "Standard domestic shipping takes 3-5 business days. International shipping can take 7-14 business days.",
    "do you ship internationally?": "Yes, we ship to over 50 countries worldwide. Shipping fees are calculated at checkout.",
    "what payment methods do you accept?": "We accept all major credit cards, PayPal, Apple Pay, and Google Pay.",
    "how can i track my order?": "Once your order ships, we will email you a tracking link to follow your package status."
}

def ask_chatbot():
    user_query = user_entry.get().strip().lower()
    if not user_query:
        messagebox.showwarning("Warning", "Please type a question first.")
        return
        
    # Search for matching keywords in our database
    found_answer = None
    for question, answer in FAQ_DATA.items():
        if user_query in question or any(word in user_query for word in question.split()):
            found_answer = answer
            break
            
    # Display the result to the user
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_entry.get() + "\n")
    
    if found_answer:
        chat_display.insert(tk.END, "Bot: " + found_answer + "\n\n")
    else:
        chat_display.insert(tk.END, "Bot: I'm sorry, I don't know the answer to that question yet. Try asking about shipping or returns!\n\n")
        
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END) # Scroll to bottom automatically
    user_entry.delete(0, tk.END) # Clear input box

# Initialize window interface
root = tk.Tk()
root.title("CodeAlpha AI Internship - FAQ Chatbot")
root.geometry("450x450")
root.configure(bg="#f4f6f9")

# Header
tk.Label(root, text="AI FAQ Chatbot", font=("Arial", 14, "bold"), bg="#f4f6f9", fg="#2c3e50").pack(pady=10)

# Conversation Display Panel
chat_display = tk.Text(root, height=15, width=50, font=("Arial", 10), bg="white", state=tk.DISABLED)
chat_display.pack(pady=5)

# Input Field Frame Panel
input_frame = tk.Frame(root, bg="#f4f6f9")
input_frame.pack(pady=10)

user_entry = tk.Entry(input_frame, width=35, font=("Arial", 10))
user_entry.pack(side=tk.LEFT, padx=5)
user_entry.insert(0, "How can I track my order?") # Pre-fills text for easy demoing

send_btn = tk.Button(input_frame, text="Ask Bot", font=("Arial", 10, "bold"), bg="#2c3e50", fg="white", command=ask_chatbot)
send_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()