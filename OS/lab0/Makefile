SOURCE = ./src/hello.asm
BUILD_DIR = ./_build
IMG = boot

clean:
	rm -rf $(BUILD_DIR)

build:
	nasm -fbin ./src/hello.asm -o $(BUILD_DIR)/$(IMG).bin && 
	dd if=/dev/zero of=$(BUILD_DIR)/$(IMG).img bs=1024 count=1440 &&
	dd if=$(BUILD_DIR)/$(IMG).bin of=$(BUILD_DIR)/$(IMG).img conv=notrunc