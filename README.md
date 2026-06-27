# 🧬 ADN-ARM-Polypeptide Translator

A Python program that simulates the process of **DNA transcription and RNA translation** to generate polypeptide sequences.

---

## 📌 Project Description

This project converts a DNA sequence into an RNA sequence and translates it into a sequence of polypeptides using genetic codons.

The program performs three main steps:

🧬 **DNA → RNA transcription**

- Reads a DNA sequence composed of:
  - `A`
  - `C`
  - `G`
  - `T`

- Groups the DNA sequence into blocks of 3 letters (codons)
- Replaces every `T` by `U` to create the RNA sequence

---

🧫 **RNA → Polypeptide translation**

Each RNA codon is translated into an amino acid.


Special codons beginning with `U` are handled using a custom translation function.

---

# 🚀 Features

✨ The program can:

- 📝 Validate the sequence size `N`
- 🧬 Fill a DNA array with valid nucleotides
- 🔄 Convert DNA (`ADN`) into RNA (`ARM`)
- 🧩 Split RNA into codons of 3 letters
- 🔍 Detect STOP codons
- 🧫 Translate codons into polypeptides
- 📋 Display the final polypeptide sequence

---

# 🛠️ Technologies Used

🐍 Python 3

Concepts used:

- Functions
- Lists (Arrays)
- Loops
- Conditions
- Dictionaries
- String manipulation
- Biological sequence processing

---

