Simple program that allows you read and write text in .jpeg files

How it works:
-Every .jpeg file ends with 'FF D9'
-Following this event, the program takes the input, converts it to bytes and then place the information onto the end of the archieve
-Then, in order to read the file, it gets the end bytes and reads the piece of text after it, finally converting the output to text and showing the user
