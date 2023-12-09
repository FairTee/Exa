SIMPLE SHELL PROJECT

The term "Simple Shell project" usually refers to a task or exercise in programming that requires writing a simple command-line shell application. A application known as a shell gives users a way to interact with an operating system by typing commands.

The Simple Shell project aims to put into practice a condensed form of a shell software that can comprehend and carry out user instructions. It entails creating and putting into place elements including command execution, command parsing, input/output redirection handling, background process management, and support for fundamental shell capabilities like command history, environment variables, and shell scripting.
In order to gain a better grasp of operating system ideas, process management, and system calls, the Simple Shell project is frequently used as a learning exercise. Knowing programming languages and UNIX is necessary.


GENERAL REQUIREMENT:
Allowed editors: vi, vim, emacs
All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
All your files should end with a new line
A README.md file, at the root of the folder of the project is mandatory
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
Your shell should not have any memory leaks
No more than 5 functions per file
All your header files should be include guarded
Use system calls only when you need to (why?)
Write a README with the description of your project
You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository.

COMPILATION:
Our shell was compiled this way:

gcc -Wall -Werror -Wextra -pedantic -std=gnu89 *.c -o hsh

TESTING
Our shell works like this in interactive mode:

$ ./hsh
($) /bin/ls
hsh main.c shell.c
($)
($) exit
$
Also in non-interactive mode:

$ echo "/bin/ls" | ./hsh
hsh main.c shell.c test_ls_2
$
$ cat test_ls_2
/bin/ls
/bin/ls
$
$ cat test_ls_2 | ./hsh
hsh main.c shell.c test_ls_2
hsh main.c shell.c test_ls_2
$

THE FILES INCLUDED IN THIS PROJECT ARE:

AUTHORS
README
to_build.c
fork.c
line.c
path.c
tok.c
main.c
shell.h
strok.c
uxil.c
value.c
