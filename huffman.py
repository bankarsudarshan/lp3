import heapq
from collections import Counter

# class Huffman:
#     class _Node:
#         __slots__ = '_ch', '_freq', '_left', '_right'
#         def __init__(self, ch, freq):
#             self._ch = ch
#             self._freq = freq
#             self._left = None
#             self._right = None
#         def __lt__(self, other):
#             if self._freq == other._freq:
#                 return self._ch < other._ch
#             return self._freq < other._freq
    
#     def __init__(self, string):
#         self._root = None
#         self._codes = {}
#         self.__build_tree(string)
    
#     def __build_tree(self, string):
#         if not string:
#             self._root = None
#             self._codes.clear()
#             return
#         freq_map = Counter(string)
#         pq = [self._Node(ch, freq) for ch, freq in freq_map.items()]
#         heapq.heapify(pq)
#         while len(pq) > 1:
#             left = heapq.heappop(pq)
#             right = heapq.heappop(pq)
#             parent = self._Node('#', left._freq + right._freq)
#             parent._left = left
#             parent._right = right
#             heapq.heappush(pq, parent)
#         self._root = pq[0]
#         self.__generate_codes(self._root, '')

#     def __generate_codes(self, root, code):
#         if not root:
#             return
#         if not root._left and not root._right:
#             self._codes[root._ch] = code
#             return
#         self.__generate_codes(root._left, code + '0')
#         self.__generate_codes(root._right, code + '1')
    
#     def display_codes(self):
#         print("Character : Code")
#         for ch, code in self._codes.items():
#             print(f"{ch} : {code}")

#     def encode_str(self, text):
#         """Convert text to Huffman encoded binary string."""
#         return ''.join(self._codes.get(ch, '') for ch in text)

#     def decode_str(self, encoded_text):
#         """Decode binary string back to original text."""
#         curr = self._root
#         decoded = ""
#         for bit in encoded_text:
#             curr = curr._left if bit == '0' else curr._right
#             if not curr._left and not curr._right:
#                 decoded += curr._ch
#                 curr = self._root
                
#         return decoded

class Huffman:
    class _Node:
        def __init__(self, ch, freq):
            self._ch = ch
            self._freq = freq
            self._left = None
            self._right = None
        def __lt__(self, other):
            if self._freq == other._freq:
                return self._ch < other._ch
            return self._freq < other._freq

    def __init__(self, string):
        self._root = None
        self._codes = {}
        self.__build_tree(string)
    def __build_tree(self, string):
        if not string:
            root = None
            self._codes.clear()
            return
        freq_map = Counter(string)
        pq = [self._Node(ch, freq) for ch, freq in freq_map.items()]
        heapq.heapify(pq)
        while(len(pq) > 1):
            left = heapq.heappop(pq)
            right = heapq.heappop(pq)
            parent = self._Node('#', left._freq+right._freq)
            parent._left = left
            parent._right = right
            heapq.heappush(pq, parent)
        self._root = pq[0]
        self.__generate_codes(self._root, '')
    def __generate_codes(self, root, code):
        if not root:
            return
        if not root._left and not root._right:
            self._codes[root._ch] = code
            return
        self.__generate_codes(root._left, code + '0')
        self.__generate_codes(root._right, code + '1')
    def display_codes(self):
        print("Character: Code")
        for ch, code in self._codes.items():
            print(ch, ': ', code)
    def encode_str(self, text):
        return ''.join(self._codes.get(ch, '') for ch in text)
    def decode_str(self, code):
        curr = self._root
        decoded = ''
        for bit in code:
            curr = curr._left if bit == '0' else curr._right
            if not curr._left and not curr._right:
                decoded += curr._ch
                curr = self._root
        return decoded

if __name__ == "__main__":
    hf = Huffman('sudarshan')
    hf.display_codes()

    text = input("Enter a string to encode: ")
    encoded = hf.encode_str(text)
    print("Encoded:", encoded)

    decoded = hf.decode_str(encoded)
    print("Decoded:", decoded)
