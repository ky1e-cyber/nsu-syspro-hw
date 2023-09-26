#!/bin/sh


nasm -fbin ./src/hello.asm -o ./_build/boot.bin &&
  dd if=/dev/zero of=_build/boot.img bs=1024 count=1440 &&
  dd if=_build/boot.bin of=_build/boot.img conv=notrunc;

qemu-system-i386 -monitor stdio ./_build/boot.img
