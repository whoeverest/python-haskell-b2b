def inputTxt():
    text = raw_input("Human: ")
    return text

def outputTxt(txt=None):
    if txt is not None:
        print("Computor:" + txt)
    else:
        print("Computor: Huh?")
   
txt_current = None
txt_past = ""    

while True:
    txt_current = inputTxt()
    if txt_current is None:
        outputTxt()        
    else:
        outputTxt(txt_past)
        txt_past = txt_current

