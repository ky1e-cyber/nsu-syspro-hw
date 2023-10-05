#!/bin/sh

image=boot.img
src_file=hello_world.asm

mkdir build

nasm -fbin "./src/$src_file" -o ./build/out.bin &&
  dd if=/dev/zero of="build/$image" bs=1024 count=1440 &&
  dd if=build/out.bin of="build/$image" conv=notrunc;