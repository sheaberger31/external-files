def new_file(file, player):
    save = open(file, 'w')
    save.write("What is your characters name?,")
    save.write(player + ',')
    
    
def read(file, player):   
    open_file = open(file, 'r')
    all_lines = open_file.read()
    print(all_lines)
    open_file.close()
    
    
def main():
    player = input("what is your characters name?")
    file = player + '.txt'
    new_file(file, player)
    read(file, player)


main()
    
    
