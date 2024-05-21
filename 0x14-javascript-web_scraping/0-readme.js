#!/usr/bin/node

if (!process.argv[2]) {
    console.error(error.message);
    process.exit(1); // Exit with error code 1 indicating failure
}

const filename = process.argv[2];
const fs = require('fs');

try {
    const data = fs.readFileSync(filename, 'utf8');
    console.log(data);
} catch (error) {
    console.error(`Failed to read file ${filename}:`, error.message);
}
