from browser import document, bind

conv={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":1,"k":2,"l":3,"m":4,"n":5,"o":6,"p":7,"q":8,"r":9,"s":1,"t":2,"u":3,"v":4,"w":5,"x":6,"y":7,"z":8}

def get_input(event):
    result=document["input1"].value
    
    if result !="":
        all_char=[]   
        unique=""
        for letter in result.lower():            
            if letter not in all_char:
                unique+=letter
                all_char.append(letter)

        sigil=""
        for unique_letter in unique:
            if unique_letter in conv:
                sigil+=str(conv[unique_letter])

        document["result"].clear()
        document["result_head"].clear()
        document["result_head"] <= "Sigil:"
        document["result"] <= sigil


document["button1"].bind("click",get_input)