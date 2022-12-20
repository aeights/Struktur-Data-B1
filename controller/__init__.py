import os
import time
import sqlite3

path_db = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/account.db'

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    
    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_username(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item["username"] == x:
                # print("Item found")
                return True
            n = n.ref
        # print("item not found")
        return False
    
    def search_password(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item["password"] == x:
                # print("Item found")
                return True
            n = n.ref
        # print("item not found")
        return False

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item["username"] == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

# Load Database
def load_db():
    connect = sqlite3.connect(path_db)
    getdata = connect.cursor()
    data = getdata.execute("SELECT * FROM akun")
    row = data.fetchall()
    for i in row:
        list_account.insert_at_end({"username":i[0],"password":i[1]})

# Account Management
def controller_daftar(username,password):
    list_account.insert_at_end({"username":username,"password":password})
    connect=sqlite3.connect(path_db)
    getdata=connect.cursor()
    getdata.execute(f'INSERT INTO akun values("{username}","{password}")')
    connect.commit()

def controller_login(username,password):
    if list_account.search_username(username) == True and list_account.search_password(password) == True:
        # print("Login Berhasil")
        return [True,None]
    else:
        # print("Login Gagal")
        return [False,"Username atau password anda salah"]

def controller_hapus(username):
    if list_account.search_username(username) == True:
        list_account.delete_element_by_value(username)
        connect=sqlite3.connect(path_db)
        getdata=connect.cursor()
        getdata.execute(f'DELETE FROM akun WHERE username="{username}"')
        connect.commit()
        return True
    else:
        # print("Akun salah")
        return False

def controller_edit(username,new_username,new_password):
    list_account.delete_element_by_value(username)
    connect=sqlite3.connect(path_db)
    getdata=connect.cursor()
    getdata.execute(f'DELETE FROM akun WHERE username="{username}"')
    connect.commit()

    list_account.insert_at_end({"username":new_username,"password":new_password})
    connect=sqlite3.connect(path_db)
    getdata=connect.cursor()
    getdata.execute(f'INSERT INTO akun values("{new_username}","{new_password}")')
    connect.commit()

def show_account():
    list_account.traverse_list()

# List akun
list_account = LinkedList()

load_db()
show_account()

# menu()