import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.users = {"admin": "123"} 
        self.title("Library Management System")
        self.geometry("800x500")
        self.resizable(False, False)
        
        
        try:
            self.bg_image = Image.open("library.jpg")
            self.bg_image = self.bg_image.resize((800, 500), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            
            self.bg_label = tk.Label(self, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.configure(bg="#2c3e50")

        self.main_title = tk.Label(self, text="Library Management System", 
                                   font=("Arial", 24, "bold"), fg="white", bg="#3d4d5e")
        self.main_title.pack(pady=30)

        self.show_login()

    def show_login(self):
        self.login_frame = tk.Frame(self, bg="#f0f0f0")
        
        
        self.login_frame = tk.Frame(self, bg="#e0e0e0", bd=0)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)
        tk.Label(self.login_frame, text="Login", font=("Arial", 16), bg="#e0e0e0", fg="#333333").pack(pady=20)


        def on_entry_click(event, entry, text):
            if entry.get() == text:
               entry.delete(0, "end")
               entry.insert(0, '')
               entry.config(fg='black')

        def on_focusout(event, entry, text):
           if entry.get() == '':
              entry.insert(0, text)
              entry.config(fg='grey')

        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 10), fg='grey')
        self.username_entry.insert(0, 'username') 
        self.username_entry.bind('<FocusIn>', lambda e: on_entry_click(e, self.username_entry, 'username'))
        self.username_entry.bind('<FocusOut>', lambda e: on_focusout(e, self.username_entry, 'username'))
        self.username_entry.pack(pady=10, ipady=5, padx=30, fill="x")
        
    
        self.password_entry = tk.Entry(self.login_frame, font=("Arial", 10), fg='grey')
        self.password_entry.insert(0, 'password')
        self.password_entry.bind('<FocusIn>', lambda e: (
        self.password_entry.delete(0, 'end') if self.password_entry.get() == 'password' else None,
        self.password_entry.config(fg='black', show='*')))

        self.password_entry.bind('<FocusOut>', lambda e: (
        (self.password_entry.insert(0, 'password'), 
        self.password_entry.config(fg='grey', show='')) 
        if self.password_entry.get() == '' else None))

        self.password_entry.pack(pady=10, ipady=5, padx=30, fill="x")

        
        self.login_btn = tk.Button(self.login_frame, text="Login", bg="#d9534f", fg="white", font=("Arial", 10, "bold"), width=10, command=self.check_login)
        self.login_btn.pack(pady=20)

        tk.Button(self.login_frame, text="Create New Account", fg="#3d4d5e", bg="#e0e0e0", font=("Arial", 10, "underline"), bd=0, cursor="hand2", command=self.show_signup_window).pack(pady=10)


    
    def check_login(self):
        user = self.username_entry.get()
        password = self.password_entry.get()
        
        if user == "esraa" and password == "1234":
            self.open_dashboard()
        elif user != " " and password != " ":
            self.show_user_library()
        else:
            messagebox.showerror("Error", "Invalid username or password")


    def show_signup_window(self):
        self.signup_win = tk.Toplevel(self)
        self.signup_win.title("Sign Up")
        self.signup_win.geometry("400x500")
        self.signup_win.configure(bg="#f0f0f0")

        tk.Label(self.signup_win, text="Create New Account", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

        
        tk.Label(self.signup_win, text="Username:", bg="#f0f0f0").pack()
        self.new_user = tk.Entry(self.signup_win, width=30)
        self.new_user.pack(pady=5)

       
        tk.Label(self.signup_win, text="Password:", bg="#f0f0f0").pack()
        self.new_pass = tk.Entry(self.signup_win, width=30, show="*")
        self.new_pass.pack(pady=5)


        tk.Label(self.signup_win, text="Confirm Password:", bg="#f0f0f0").pack()
        self.conf_pass = tk.Entry(self.signup_win, width=30, show="*")
        self.conf_pass.pack(pady=5)

        tk.Button(self.signup_win, text="Register", bg="#d9534f", fg="white", width=15, command=self.process_signup).pack(pady=30)
    


    def process_signup(self):
        u = self.new_user.get()
        p = self.new_pass.get()
        cp = self.conf_pass.get()

        if u == "" or p == "":
            messagebox.showwarning("Error", "Fields cannot be empty!")
        elif p != cp:
            messagebox.showerror("Error", "Passwords do not match!")
        elif u in self.users:
            messagebox.showwarning("Error", "Username already exists!")
        else:
            self.users[u] = p  
            messagebox.showinfo("Success", f"Account created for {u}!")
            self.signup_win.destroy()

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            for widget in self.winfo_children():
                widget.destroy()
            self.geometry("800x500")
            self.bg_label = tk.Label(self, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            self.main_title = tk.Label(self, text="Library Management System", font=("Arial", 24, "bold"), fg="white", bg="#3d4d5e")
            self.main_title.pack(pady=10)

            self.show_login()

    

    def open_dashboard(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        self.geometry("1100x650")
        self.configure(bg="#f8f9fa")
        self.title("LMS - Admin Dashboard")
        
        header = tk.Frame(self, bg="#2c3e50", height=70)
        header.pack(fill="x")

        
        tk.Button(header, text="Logout", bg="#c0392b", fg="white", 
                  font=("Arial", 10, "bold"), bd=0, padx=10,
                  command=self.logout).pack(side="right", padx=20, pady=20)
        
        tk.Label(header, text="Library Management System", 
                 fg="white", bg="#2c3e50", font=("Verdana", 16, "bold")).pack(pady=20)
        
        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="+ Add New Book", bg="#27ae60", fg="white", 
                  font=("Arial", 11, "bold"), width=18, height=2, bd=0,command=self.add_book_window).grid(row=0, column=0, padx=10)

        tk.Button(btn_frame, text="Update Book", bg="#f39c12", fg="white", 
                  font=("Arial", 11, "bold"), width=18, height=2, bd=0, command=self.update_book_window).grid(row=0, column=1, padx=10)

        tk.Button(btn_frame, text="Delete Book", bg="#e74c3c", fg="white", 
                  font=("Arial", 11, "bold"), width=18, height=2, bd=0,command=self.delete_book).grid(row=0, column=2, padx=10)

        table_frame = tk.Frame(self, bg="white", bd=2, relief="flat")
        table_frame.pack(pady=10, padx=30, fill="both", expand=True)

      
        style = ttk.Style()
        style.theme_use("clam")  
        
        style.configure("Treeview", 
                        background="#ffffff", 
                        foreground="#333333", 
                        rowheight=35, 
                        fieldbackground="#ffffff", 
                        font=("Arial", 11))
        
        style.configure("Treeview.Heading", 
                        background="#34495e", 
                        foreground="white", 
                        font=("Arial", 12, "bold"))

    
        style.map("Treeview", background=[('selected', '#3498db')])

        
        list_frame = tk.Frame(self, bg="white", bd=0)
        list_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.book_tree = ttk.Treeview(list_frame, columns=("ID", "Title", "Author", "Status"), show="headings")
        
        self.book_tree.heading("ID", text="ID")
        self.book_tree.heading("Title", text="BOOK TITLE")
        self.book_tree.heading("Author", text="AUTHOR")
        self.book_tree.heading("Status", text="STATUS")

        self.book_tree.column("ID", width=80, anchor="center")
        self.book_tree.column("Title", width=350, anchor="w")
        self.book_tree.column("Author", width=250, anchor="w")
        self.book_tree.column("Status", width=120, anchor="center")

        
        initial_books = [
            ("1024", "Clean Code", "Robert C. Martin", "Available"),
            ("2050", "The Alchemist", "Paulo Coelho", "Borrowed"),
            ("3012", "Python Crash Course", "Eric Matthes", "Available"),
            ("5520", "Atomic Habits", "James Clear", "Available"),
            ("1102", "1984", "George Orwell", "Borrowed")
        ]

        for book in initial_books:
            self.book_tree.insert("", "end", values=book)

        self.book_tree.pack(fill="both", expand=True)
        

    def add_book_window(self):
        self.add_win = tk.Toplevel(self)
        self.add_win.title("Add New Book")
        self.add_win.geometry("400x400")
        self.add_win.configure(bg="#f8f9fa")

        tk.Label(self.add_win, text="Book Details", font=("Arial", 14, "bold"), bg="#f8f9fa").pack(pady=20)

    
        tk.Label(self.add_win, text="Book Title:", bg="#f8f9fa", font=("Arial", 10)).pack(pady=5)
        self.title_entry = tk.Entry(self.add_win, width=35, font=("Arial", 11))
        self.title_entry.pack(pady=5)

        tk.Label(self.add_win, text="Author Name:", bg="#f8f9fa", font=("Arial", 10)).pack(pady=5)
        self.author_entry = tk.Entry(self.add_win, width=35, font=("Arial", 11))
        self.author_entry.pack(pady=5)

        tk.Button(self.add_win, text="Save to Inventory", bg="#27ae60", fg="white", 
                  font=("Arial", 11, "bold"), width=20, height=2, bd=0,
                  command=self.save_book_to_tree).pack(pady=30)

    def save_book_to_tree(self):
        book_title = self.title_entry.get()
        book_author = self.author_entry.get()

        if book_title.strip() == "" or book_author.strip() == "":
            messagebox.showwarning("Empty Fields", "Please enter both Title and Author!")
        else:
            import random
            book_id = random.randint(1000, 9999)
            
            
            try:
                self.book_tree.insert("", "end", values=(book_id, book_title, book_author, "Available"))
                messagebox.showinfo("Success", f"'{book_title}' has been added!")
                self.add_win.destroy()
            except AttributeError:
           
                self.tree("", "end", values=(book_id, book_title, book_author, "Available"))
                messagebox.showinfo("Success", f"'{book_title}' has been added!")
                self.add_win.destroy()

                


    def update_book_window(self):
        
        selected = self.book_tree.focus()
        if not selected:
            messagebox.showwarning("Selection", "Please select a book from the table first!")
            return

        
        values = self.book_tree.item(selected, 'values')

        
        self.up_win = tk.Toplevel(self)
        self.up_win.title("Update Book")
        self.up_win.geometry("400x400")
        self.up_win.configure(bg="#fef9e7") 

        tk.Label(self.up_win, text="Update Details", font=("Arial", 14, "bold"), bg="#fef9e7").pack(pady=20)

        
        tk.Label(self.up_win, text="New Title:", bg="#fef9e7").pack()
        self.up_title = tk.Entry(self.up_win, width=30)
        self.up_title.insert(0, values[1]) 
        self.up_title.pack(pady=5)

        tk.Label(self.up_win, text="New Author:", bg="#fef9e7").pack()
        self.up_author = tk.Entry(self.up_win, width=30)
        self.up_author.insert(0, values[2]) 
        self.up_author.pack(pady=5)

        
        tk.Button(self.up_win, text="Confirm Update", bg="#f39c12", fg="white", 
                  width=20, command=self.apply_update).pack(pady=30)

    def apply_update(self):
        selected = self.book_tree.focus()
        new_t = self.up_title.get()
        new_a = self.up_author.get()
        
        old_values = self.book_tree.item(selected, 'values')
        self.book_tree.item(selected, values=(old_values[0], new_t, new_a, old_values[3]))
        
        self.up_win.destroy()
        messagebox.showinfo("Updated", "Book info updated successfully!")


    def delete_book(self):
        selected_item = self.book_tree.focus()
        
        if not selected_item:
            messagebox.showwarning("Delete Error", "Please select a book to delete!")
            return
        
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this book?")
        
        if confirm:
            self.book_tree.delete(selected_item)
            messagebox.showinfo("Deleted", "Book has been removed successfully!")

    def show_user_library(self):
        
            for widget in self.winfo_children():
                widget.destroy()
    
            
            self.geometry("900x600")
            self.configure(bg="#f4f4f9")
    
            header = tk.Frame(self, bg="#2c3e50", height=80)
            header.pack(fill="x")
            tk.Label(header, text="Digital Library Explorer", font=("Arial", 24, "bold"), 
                     fg="white", bg="#2c3e50").pack(pady=20)
    
            main_frame = tk.Frame(self, bg="#f4f4f9")
            main_frame.pack(pady=20, padx=30, fill="both", expand=True)
    
            titles_frame = tk.Frame(main_frame, bg="#e0e0e0")
            titles_frame.pack(fill="x")
            
            headers = [("Book Name", 30), ("Author", 20), ("Status", 15)]
            for text, w in headers:
                tk.Label(titles_frame, text=text, font=("Arial", 12, "bold"), 
                         bg="#e0e0e0", width=w, anchor="w").pack(side="left", padx=10, pady=5)
    
        
            books_data = [
                {"title": "Python Programming", "author": "John Smith", "status": "Available"},
                {"title": "Data Science Handbook", "author": "Jake Vander", "status": "Borrowed"},
                {"title": "Machine Learning", "author": "Andrew Ng", "status": "Available"},
                {"title": "Deep Learning", "author": "Ian Goodfellow", "status": "Available"},
                {"title": "Tkinter GUI Design", "author": "Alan Moore", "status": "Available"},
                {"title": "Clean Code", "author": "Robert Martin", "status": "Borrowed"},
                {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "status": "Available"},
            ]
    
            for book in books_data:
                row = tk.Frame(main_frame, bg="white", highlightbackground="#cccccc", highlightthickness=1)
                row.pack(fill="x", pady=2)
    
                
                tk.Label(row, text=book["title"], font=("Arial", 11), bg="white", width=33, anchor="w").pack(side="left", padx=10)
                
                tk.Label(row, text=book["author"], font=("Arial", 11), bg="white", width=22, anchor="w").pack(side="left", padx=10)
                
                status_color = "#27ae60" if book["status"] == "Available" else "#e74c3c"
                tk.Label(row, text=book["status"], font=("Arial", 10, "bold"), 
                         fg=status_color, bg="white", width=15).pack(side="left", padx=10)
    
            tk.Button(self, text="Logout", command=self.logout, bg="#c0392b", fg="white", 
                      font=("Arial", 12, "bold"), width=15, bd=0, cursor="hand2").pack(pady=20)
                
if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()