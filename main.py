#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to /output/entry.txt and prints it.
"""

import os

JOKE = "My boss says we're a family here, so I asked HR for the family discount on my rent \u2014 they closed my ticket as working as intended."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
