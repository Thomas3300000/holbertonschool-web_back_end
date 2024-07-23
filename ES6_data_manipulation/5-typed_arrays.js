export default function createInt8TypedArray(lenght, position, value) {
  if (position < 0 || position >= lenght) {
    throw new RangeError('Position outside range');
  }
  const buffer = new ArrayBuffer(lenght);
  const arr = new DataView(buffer);

  arr.setInt8(position, value);

  return arr;
}
