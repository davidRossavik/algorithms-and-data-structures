# Huffman Compressor

A text compressor using Huffman coding. Frequent characters get short binary codes, rare ones get longer codes — minimizing total bits used.

Uses `build_huffman_tree` and `generate_codes` from `fundamentals/greedy-algorithms/huffman_coding.py`.

## What it does

1. Counts character frequencies in the input
2. Builds a Huffman tree (greedy: always merge the two least frequent nodes)
3. Encodes the text as a bitstring
4. Decodes it back to verify correctness
5. Reports compression ratio

## How to run

```bash
cd src
py main.py
```

## Example output

```
Input: "aaabbbccddddeeeeeeee"

  Char     Freq  Code    Bits
  e           8  0          1
  a           3  101        3
  b           3  110        3
  d           4  111        3
  c           2  100        3

  Original:   160 bits
  Compressed:  44 bits
  Saved:       72.5%
```

The more skewed the character distribution, the better the compression.
