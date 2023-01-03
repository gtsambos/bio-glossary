#!/usr/bin/env python

import argparse
import pandas as pd

# Read in word and definition.
parser = argparse.ArgumentParser()

parser.add_argument(
    '--word',
    type=str,
    dest='word',
    nargs="+",
    help="The word to add."
)

parser.add_argument(
    '--definition',
    type=str,
    dest='definition',
    nargs="+",
    help="The definition of the word."
)

# Read in words and join as a single string if needed.
args = parser.parse_args()
word = args.word
definition = args.definition

# concatenate
word = " ".join(word)
definition = " ".join(definition)

print("word:", word)
print("definition:", definition)

# Read in existing words.
gls = pd.read_csv(
    "glossary.txt",
    names = ["word", "definition"],
    sep = "\t",
    )

# Iterate through words to find position.
old_words = gls["word"].tolist()
old_definitions = gls["definition"].tolist()
num_words = len(old_words)

new_index = 0
for i, w in enumerate(old_words):
    if word < w:
        break
    new_index += 1

# Add new row.
if i == 0:
    old_words = [f'{word}'] + old_words
    old_definitions = [f'{definition}'] + old_definitions
elif i == num_words:
    old_words.append(word)
    old_definitions.append(definition)
else:
    old_words = old_words[:new_index] + [word] + old_words[new_index:]
    old_definitions = old_definitions[:new_index] + [definition] + old_definitions[new_index:]

# Save back to dataframe and output to text.
gls = pd.DataFrame({
    'word' : old_words,
    'definition' : old_definitions
})
gls.to_csv("glossary.txt", sep="\t", header=False, index=False)