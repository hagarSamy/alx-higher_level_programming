#!/usr/bin/node
// a value is undefined if the var is defined but given no vALUE
if (typeof (process.argv[2]) === 'undefined') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
