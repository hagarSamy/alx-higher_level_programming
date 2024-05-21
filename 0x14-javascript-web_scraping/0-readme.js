#!/usr/bin/node

if (process.argv[2]) {
    const filename = process.argv[2];
    const fs = require('fs');

    try {
        const data = fs.readFileSync(filename, 'utf8');
        console.log(data);
    } catch (error) {
    console.error(error);
    }
}
