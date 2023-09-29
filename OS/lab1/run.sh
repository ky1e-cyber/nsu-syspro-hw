#!/bin/sh

mkdir build

nasm -fbin src/hello_world.asm -o build/boot.bin &&
  dd if=/dev/zero of=build/boot.img bs=1024 count=1440 &&
  dd if=build/boot.bin of=build/boot.img conv=notrunc;

qemu-system-i386 -monitor stdio build/boot.img
