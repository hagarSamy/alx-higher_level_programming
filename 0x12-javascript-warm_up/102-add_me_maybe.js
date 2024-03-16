#!/usr/bin/node
module.exports.addMeMaybe = function (x, theFunction) {
  theFunction(++x);
};
