from tkinter import Tk, simpledialog, messagebox
# read file info
def read_from_file():
    with open('state_capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            state, city = line.split('/')
            the_united_states[state] = city
# tells it how to read the txt document
def write_to_file(state, city):
    with open('new_data.txt','a') as file:
        file.write('\n' + state + '/' + city)
    #first thing the end user sees in window
    print('Ask the Expert - United States Capital Cities Editon')
#this is for root
root = Tk()
root.withdraw()
the_united_states = {}
#reads from file
read_from_file()
# the code here is what makes it am expert
while True:
    query_state = simpledialog.askstring('US state', 'Type the name of a state in the United States: ')
# for if in document
    if query_state in the_united_states:
        result = the_united_states[query_state]
        messagebox.showinfo('Answer' , 'The capital city of ' + query_state + ' is ' + result + '!')
# for if not in document
    else:
        new_city = simpledialog.askstring('Teach Me', 'I don\'t know. What is the capital of ' + query_state + '?')
        the_united_states[query_state] = new_city
        write_to_file(query_state,new_city)
#the code should contain data to close the window when press cancel or close tan

root.mainloop()
#print(the_united_states)
