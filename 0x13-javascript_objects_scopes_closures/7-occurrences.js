#!/usr/bin/node

// func that count a repated ele in a lsit
exports.nbOccurences = function (list, searchElement) {
  if (!list || !searchElement) return (0);
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) counter++;
  }

  return (counter);
};
