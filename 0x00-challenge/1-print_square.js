#!/usr/bin/node
/*
    A square with the character # is printed
    
    Square size must be the first argument 
    of the program.
*/


if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1)
}

size = parseInt(process.argv[2])

for (let x = 0 ; x < size ; x ++) {
    for (let y = 0 ; y < size ; y ++) {
        process.stdout.write("#");
    }
    process.stdout.write("\n");
}
