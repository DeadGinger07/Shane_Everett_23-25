#imports tkinter
from tkinter import messagebox, simpledialog, Tk

#the definitions
def get_task():
    task=simpledialog.askstring('Task','Do you want to perform encryption or decryption? (Type encrypt or decrypt)')
    return task

#for messsages
def get_message():
    message = simpledialog.askstring('Secret Message','Enter the secret message: ')
    return message

#defines the is_even function
def is_even(number):
    return number % 2 == 0

#for even letters
def get_even_letters(message):
    even_letters = []
    for counter in range (0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

#for odd letters
def get_odd_letters(message):
    odd_letters = []
    for counter in range (0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

#function to swap letters
def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counteer in range (0, int(len(message)/2)):
        letter_list.append(odd_letters[counteer])
        letter_list.append(even_letters[counteer])
    new_message = ' '.join(letter_list)
    return new_message

#encryption and decryption functions
def encrypt(message):
    swapped_message = swap_letters(message)
    encrypted_message = ''.join(reversed(swapped_message))
    return encrypted_message

def decrypt(message):
    unreversed_message = ''.join(reversed(message))
    decrypted_message = swap_letters(unreversed_message)
    return decrypted_message

#the root
root = Tk()

#used to make app work
while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo('Ciphertext of the secret message is: ', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = decrypt(message)
        messagebox.showinfo('plaintext of the secret message is: ', decrypted)
    else:
        break
    
#another root
root.mainloop()
