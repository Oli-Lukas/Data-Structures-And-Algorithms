function binarySearch(array: number[], target: number): number
{
  let left = 0;
  let right = array.length - 1;

  while (left <= right)
  {
    const mid = Math.floor((left + right) / 2);

    if (array[mid] === target) return mid;

    if (array[mid] < target)
      left = mid + 1;
    else
      right = mid - 1;
  }

  return -1;
}

const sortedArray = [1, 3, 5, 7, 9];
const targetNumber = 5;

const resultIndex = binarySearch(sortedArray, targetNumber);

if (resultIndex !== -1)
  console.log(`O número ${targetNumber} foi encontrado no índice ${resultIndex}.`);
else
  console.log(`O número ${targetNumber} não foi encontrado no array.`);