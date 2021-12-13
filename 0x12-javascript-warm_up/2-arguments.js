#!/usr/bin/node
const arg = process.argv;
(arg.length > 3) ? console.log("Arguments found") : (arg.length == 3) ? console.log("Argument found") : console.log('No argument');
