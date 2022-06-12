msg1 = 'tell me what you are thinking about'
msg2 = 'input q could exit the conversation'
input_msg = ''
while input_msg != 'q':
    input_msg = input(f"{msg1}. {msg2}. : ")
    if input_msg != 'q': print(input_msg)