#ifndef SHELL_H
#define SHELL_H
#define _GNU_SOURCE

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <errno.h>

extern char **environ;

void shell_exit(char **argument, char *input_line, int exit_code);
void print_env(char **environ);
int fork_execute(char **argmt, char **pn, char **envr, char *input, int pid, int cf);
int _putchar(char c);
char *net_path_from_env(char **envir);
char **tokenize_input(char *input);
char *read_user_input(void);
char *string_concat(char *target, char *origin);
char *string_copy(char *target, char *origin);
size_t string_compare(char *lace1, char *lace2, size_t num);
int string_length(char *lace);
int strin_compare(char *lace1, char *lace2);
char *tokenize_string(char *in_len, const char *del);
int find_executable(char **command, char **envir);
char *charac_string(const char *l, int w);
size_t comp_string(const char *lace1, const char *lace2);
size_t point_string(const char *lace1, const char *lace2);

#endif
