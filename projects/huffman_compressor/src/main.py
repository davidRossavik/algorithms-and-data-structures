import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../fundamentals/greedy-algorithms"))
from huffman_coding import build_huffman_tree, generate_codes


def encode(text, codes):
    return "".join(codes[ch] for ch in text)


def decode(bits, root):
    result = []
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            result.append(node.char)
            node = root
    return "".join(result)


def compress(text):
    freq = Counter(text)

    # Edge case: single unique character
    if len(freq) == 1:
        char = next(iter(freq))
        codes = {char: "0"}
        root = build_huffman_tree(list(freq.items()))
    else:
        root = build_huffman_tree(list(freq.items()))
        codes = generate_codes(root)

    encoded = encode(text, codes)
    return encoded, codes, root


def print_codes(codes, freq):
    print(f"\n  {'Char':<8} {'Freq':>6}  {'Code':<16} {'Bits':>4}")
    print("  " + "-" * 40)
    for char, code in sorted(codes.items(), key=lambda x: len(x[1])):
        display = repr(char) if char == " " else char
        print(f"  {display:<8} {freq[char]:>6}  {code:<16} {len(code):>4}")


def main():
    samples = [
        "hello world",
        "aaabbbccddddeeeeeeee",
        "the quick brown fox jumps over the lazy dog",
    ]

    for text in samples:
        print("=" * 52)
        print(f"  Input: \"{text}\"")

        freq = Counter(text)
        encoded, codes, root = compress(text)

        original_bits = len(text) * 8
        compressed_bits = len(encoded)
        ratio = (1 - compressed_bits / original_bits) * 100

        print_codes(codes, freq)

        print(f"\n  Original:   {len(text)} chars × 8 bits = {original_bits} bits")
        print(f"  Compressed: {compressed_bits} bits")
        print(f"  Saved:      {ratio:.1f}%")

        decoded = decode(encoded, root)
        print(f"  Decoded ok: {decoded == text}")


if __name__ == "__main__":
    main()
