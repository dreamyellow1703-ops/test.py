import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
from datetime import datetime
from PIL import Image, ImageTk
import os

class PythonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Python Desktop App")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f8f9fa')
        
        # Data storage
        self.contacts = []
        self.load_data()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Header
        header_frame = tk.Frame(self.root, bg='#667eea', height=80)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🐍 Python Desktop App", 
                              font=('Arial', 24, 'bold'), bg='#667eea', fg='white')
        title_label.pack(pady=20)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f8f9fa')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left sidebar - Features
        sidebar = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        sidebar.pack(side='left', fill='y', padx=(0, 20), pady=10)
        
        tk.Label(sidebar, text="Features", font=('Arial', 16, 'bold'), 
                bg='white', fg='#333').pack(pady=20)
        
        # Feature buttons
        features = [
            ("📝 Add Contact", self.add_contact),
            ("👥 View Contacts", self.view_contacts),
            ("📊 Stats", self.show_stats),
            ("⚙️ Settings", self.settings)
        ]
        
        for text, command in features:
            btn = tk.Button(sidebar, text=text, font=('Arial', 12), 
                          bg='#ff6b6b', fg='white', bd=0, pady=15, cursor='hand2',
                          command=command, relief='flat', width=18)
            btn.pack(pady=5, padx=20, fill='x')
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#ff5252'))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#ff6b6b'))
        
        # Right content area
        self.content_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        self.content_frame.pack(side='right', fill='both', expand=True, pady=10)
        
        # Welcome screen
        self.show_welcome()
    
    def show_welcome(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="Welcome to Python App!", 
                        font=('Arial', 28, 'bold'), bg='white', fg='#667eea')
        title.pack(pady=50)
        
        subtitle = tk.Label(self.content_frame, text="Your all-in-one Python desktop solution", 
                           font=('Arial', 16), bg='white', fg='#666')
        subtitle.pack(pady=10)
        
        desc = tk.Label(self.content_frame, 
                       text="• Add and manage contacts\n• View statistics\n• Beautiful modern UI\n• Data persistence\n• Built with Python & Tkinter",
                       font=('Arial', 12), bg='white', fg='#333', justify='left')
        desc.pack(pady=30)
    
    def add_contact(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="Add New Contact", 
                font=('Arial', 24, 'bold'), bg='white', fg='#667eea').pack(pady=30)
        
        # Form frame
        form_frame = tk.Frame(self.content_frame, bg='white')
        form_frame.pack(pady=20)
        
        # Name
        tk.Label(form_frame, text="Name:", font=('Arial', 12, 'bold'), 
                bg='white').grid(row=0, column=0, sticky='w', pady=10)
        self.name_entry = tk.Entry(form_frame, font=('Arial', 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Email
        tk.Label(form_frame, text="Email:", font=('Arial', 12, 'bold'), 
                bg='white').grid(row=1, column=0, sticky='w', pady=10)
        self.email_entry = tk.Entry(form_frame, font=('Arial', 12), width=30)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Phone
        tk.Label(form_frame, text="Phone:", font=('Arial', 12, 'bold'), 
                bg='white').grid(row=2, column=0, sticky='w', pady=10)
        self.phone_entry = tk.Entry(form_frame, font=('Arial', 12), width=30)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Buttons
        btn_frame = tk.Frame(self.content_frame, bg='white')
        btn_frame.pack(pady=30)
        
        save_btn = tk.Button(btn_frame, text="💾 Save Contact", font=('Arial', 12, 'bold'),
                           bg='#4caf50', fg='white', bd=0, pady=12, padx=30,
                           command=self.save_contact)
        save_btn.pack(side='left', padx=10)
        
        cancel_btn = tk.Button(btn_frame, text="↩️ Back", font=('Arial', 12),
                             bg='#ff9800', fg='white', bd=0, pady=12, padx=30,
                             command=self.show_welcome)
        cancel_btn.pack(side='left', padx=10)
    
    def save_contact(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        
        if not name or not email:
            messagebox.showerror("Error", "Name and Email are required!")
            return
        
        contact = {
            'name': name,
            'email': email,
            'phone': phone or '',
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.contacts.append(contact)
        self.save_data()
        
        messagebox.showinfo("Success", "Contact saved successfully! 🎉")
        self.show_welcome()
    
    def view_contacts(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="📋 Your Contacts", 
                font=('Arial', 24, 'bold'), bg='white', fg='#667eea').pack(pady=30)
        
        if not self.contacts:
            tk.Label(self.content_frame, text="No contacts yet. Add some!", 
                    font=('Arial', 16), bg='white', fg='#666').pack(pady=50)
            return
        
        # Contacts listbox
        listbox = tk.Listbox(self.content_frame, font=('Arial', 11), height=15)
        listbox.pack(pady=20, padx=20, fill='both', expand=True)
        
        for i, contact in enumerate(self.contacts):
            date = contact['date_added']
            text = f"{contact['name']} | {contact['email']} | {contact.get('phone', 'N/A')} | {date}"
            listbox.insert(tk.END, text)
        
        # Buttons
        btn_frame = tk.Frame(self.content_frame, bg='white')
        btn_frame.pack(pady=20)
        
        back_btn = tk.Button(btn_frame, text="↩️ Back", font=('Arial', 12),
                           bg='#ff6b6b', fg='white', bd=0, pady=12, padx=30,
                           command=self.show_welcome)
        back_btn.pack()
    
    def show_stats(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="📊 Statistics", 
                font=('Arial', 24, 'bold'), bg='white', fg='#667eea').pack(pady=30)
        
        total = len(self.contacts)
        stats_text = f"""
Total Contacts: {total}

Recent Activity:
- Contacts added: {total}
- First contact: {self.contacts[0]['date_added'] if self.contacts else 'None'}
- Last contact: {self.contacts[-1]['date_added'] if self.contacts else 'None'}

App Status: ✅ Running Perfectly!
        """
        
        stats_label = tk.Label(self.content_frame, text=stats_text.strip(), 
                              font=('Arial', 14), bg='white', fg='#333', 
                              justify='left', anchor='w')
        stats_label.pack(pady=30, padx=50)
        
        back_btn = tk.Button(self.content_frame, text="↩️ Back", font=('Arial', 12),
                           bg='#ff6b6b', fg='white', bd=0, pady=12, padx=30,
                           command=self.show_welcome)
        back_btn.pack(pady=20)
    
    def settings(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="⚙️ Settings", 
                font=('Arial', 24, 'bold'), bg='white', fg='#667eea').pack(pady=30)
        
        tk.Label(self.content_frame, text="App is ready for customization!\n\n• Change colors\n• Add database\n• Export data\n• Themes", 
                font=('Arial', 14), bg='white', fg='#666', justify='center').pack(pady=50)
        
        back_btn = tk.Button(self.content_frame, text="↩️ Back", font=('Arial', 12),
                           bg='#ff6b6b', fg='white', bd=0, pady=12, padx=30,
                           command=self.show_welcome)
        back_btn.pack(pady=20)
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def save_data(self):
        with open('contacts.json', 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def load_data(self):
        try:
            if os.path.exists('contacts.json'):
                with open('contacts.json', 'r') as f:
                    self.contacts = json.load(f)
        except:
            self.contacts = []

def main():
    root = tk.Tk()
    app = PythonApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()