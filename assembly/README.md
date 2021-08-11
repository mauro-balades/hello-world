<!-- REQUIRED -->
# language: assembly

<!-- REQUIRED -->
In computer programming, assembly language, sometimes abbreviated asm, is any low-level programming language in which there is a very strong correspondence between the instructions in the language and the architecture's machine code instructions.

### how to run


<!-- NOT REQUIRED -->
<!-- ANY EXTRA THINGS LIKE:
    HOW TO DOWNLOAD LANGUAGE
    ANY NOTES
    ... -->

* download: https://www.nasm.us/

<!-- REQUIRED -->
```sh
$ nasm -f elf32 -o main.o main.asm
$ ld -m elf_i386 -o execute_me main.o
$ ./execute_me
```

<!-- REQUIRED -->
### LICENSE

* contributed in [maubg-debug/hello-world](https://github.com/maubg-debug/hello-world) by [maubg-debug](https://github.com/maubg-debug)