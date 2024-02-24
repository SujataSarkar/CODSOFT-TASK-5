import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.root, text="Phone Number:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.root, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5)
        self.entry_address = tk.Entry(self.root)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.button_view = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.label_search = tk.Label(self.root, text="Search:")
        self.label_search.grid(row=6, column=0, padx=5, pady=5)
        self.entry_search = tk.Entry(self.root)
        self.entry_search.grid(row=6, column=1, padx=5, pady=5)
        self.button_search = tk.Button(self.root, text="Search", command=self.search_contact)
        self.button_search.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

    def add_contact(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)

        messagebox.showinfo("Success", "Contact added successfully.")

        self.clear_entries()

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone_number}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        query = self.entry_search.get()
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone_number]
        
        if not results:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone_number}" for contact in results])
            messagebox.showinfo("Search Results", contact_list)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_search.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
