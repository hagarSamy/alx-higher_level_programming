#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    myList.push(list[i]);
  }
  return myList;
};
