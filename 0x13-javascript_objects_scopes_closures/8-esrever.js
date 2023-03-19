#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  for (let i = 0; len - i > 0; i++, len--) {
    const tmp = list[len];
    list[len] = list[i];
    list[i] = tmp;
  }
  return list;
};
