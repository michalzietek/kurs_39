import collections

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam sed nisl ultrices, mollis lacus ac, aliquam ligula. Ut porttitor diam nibh, vel placerat lectus scelerisque sit amet. Praesent posuere quam a suscipit mollis. Maecenas hendrerit dolor libero, blandit tincidunt nisi consequat ut. Maecenas non elit mi. Nunc non tincidunt erat. In in dignissim libero. In vehicula sem sed velit pellentesque, quis lobortis diam lobortis. "

data = collections.defaultdict(int)

for letter in text:
    data[letter] += 1


counter = collections.Counter(text)
print(counter)
# print(data)