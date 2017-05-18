# pycrust

pycrust is a shell for Windows/Unix created in Python. As of now it is pretty simple and only really does small commands. Once I get processes/programs working it'll have more functionality.

# Current commands supported:
exit:
>Syntax: exit num 
>>Exits the shell with the entered exit status (num). Defaults to 0 if num not entered.
 
change directory: 
>Syntax: cd directory
>>Changes to the entered directory, if it exists.

list directory:
>Syntax: ls
>>Lists all files inside the current directory.

make directory:
>Syntax: mkdir directory
>>Creates the specfified directory, if it doesn't already exist.

remove directory:
>Syntax: rmdir directory
>>removes the specified directory, if it exists.

current location:
>Syntax: wh
>>Returns current location within the file system.

push directory onto directory stack:
>Syntax: pushd directory
>>pushes specified directory onto the stack.

pop directory off the stack:
>Syntax: popd
>>Pops off most recent directory and moves to it, if it exists.

view directory stack contents:
>Syntax: dst
>>Lists the contents of the stack

push file onto file stack:
>Syntax: pushf file_name
>>pushes specified file onto the stack (wildcards suuported).

pop file off the stack:
>Syntax: popf
>>Pops file off the stack and copies it to the current directory

view file stack contents:
>Syntax: fst
>>Lists the contents of the stack

empty file stack into current directory:
>Syntax: flushf
>>Empties file stack and copies all entires into current directory

delete file:
>Syntax: delf file_name
>>Deletes the file specified by file_name

  
