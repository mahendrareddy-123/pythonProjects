import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # GUI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.display_button = tk.Button(root, text="Display Contacts", command=self.display_contacts)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)

        # Grid layout
        self.name_label.grid(row=0, column=0, sticky=tk.E)
        self.name_entry.grid(row=0, column=1)

        self.phone_label.grid(row=1, column=0, sticky=tk.E)
        self.phone_entry.grid(row=1, column=1)

        self.email_label.grid(row=2, column=0, sticky=tk.E)
        self.email_entry.grid(row=2, column=1)

        self.address_label.grid(row=3, column=0, sticky=tk.E)
        self.address_entry.grid(row=3, column=1)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.display_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=8, column=0, columnspan=2, pady=10)
        self.quit_button.grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)

        messagebox.showinfo("Success", "Contact added successfully!")

        # Clear entry fields after adding contact
        self.clear_entry_fields()

    def display_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts found.")
        else:
            contact_info = "\n".join([
                                         f"{i + 1}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}"
                                         for i, contact in enumerate(self.contacts)])
            messagebox.showinfo("Contacts", contact_info)

    def update_contact(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts found.")
            return

        try:
            index = int(simpledialog.askstring("Update Contact", "Enter the index of the contact to update.")) - 1
            selected_contact = self.contacts[index]
        except (ValueError, IndexError, TypeError):
            messagebox.showinfo("Invalid Selection", "Please enter a valid index.")
            return

        # Update contact details
        self.name_entry.insert(0, selected_contact["Name"])
        self.phone_entry.insert(0, selected_contact["Phone"])
        self.email_entry.insert(0, selected_contact["Email"])
        self.address_entry.insert(0, selected_contact["Address"])

        # Remove the updated contact from the list
        self.contacts.pop(index)

        messagebox.showinfo("Update Contact", "Update the contact details and click 'Add Contact'.")

    def delete_contact(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts found.")
            return

        try:
            index = int(simpledialog.askstring("Delete Contact", "Enter the index of the contact to delete.")) - 1
            selected_contact = self.contacts[index]
        except (ValueError, IndexError, TypeError):
            messagebox.showinfo("Invalid Selection", "Please enter a valid index.")
            return

        # Delete the selected contact
        self.contacts.pop(index)

        messagebox.showinfo("Delete Contact", f"Contact {selected_contact['Name']} deleted successfully.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter the name or phone number:")

        if search_term is not None:
            search_term = search_term.lower()

            results = []
            for contact in self.contacts:
                if search_term in contact['Name'].lower() or search_term == contact['Phone']:
                    results.append(contact)

            if results:
                contact_info = "\n".join([
                                             f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}"
                                             for contact in results])
                messagebox.showinfo("Search Results", contact_info)
            else:
                messagebox.showinfo("No Results", "No matching contacts found.")

    def clear_entry_fields(self):
        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
