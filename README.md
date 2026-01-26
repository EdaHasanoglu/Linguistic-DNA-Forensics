# 🧬 Linguistic DNA: Forensic Stylometry Tool

> *"Criminals can change their topic, but they can't hide their grammar."*

## 🚀 Overview
**Linguistic DNA** is a digital forensics tool designed to perform **Authorship Attribution**. Unlike simple keyword matching, this tool analyzes **Function Words** (stopwords like *'the', 'to', 'and', 'for'*) to create a grammatical fingerprint of a writer.

This method allows investigators to link an anonymous threat (e.g., a Ransom Note) to a suspect based on their everyday writing (e.g., Emails, Blogs), even if the topics are completely different.

## 🧠 The Science (Stylometry)
Humans use function words subconsciously at specific rates. This tool:
1.  **Tokenizes** the input texts using NLTK.
2.  **Extracts** frequency vectors for the top 23 most common English function words.
3.  **Calculates** the Manhattan Distance between the anonymous note and suspect samples.
4.  **Identifies** the suspect with the lowest statistical deviation (Diff Score).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **NLP Engine:** `nltk` (Natural Language Toolkit)
* **Analysis:** Frequency Vector Analysis & Statistical Scoring

## ⚙️ Installation & Usage

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Linguistic-DNA-Forensics.git](https://github.com/YOUR_USERNAME/Linguistic-DNA-Forensics.git)
    cd Linguistic-DNA-Forensics
    ```

2.  **Install Dependencies:**
    ```bash
    pip install nltk
    ```

3.  **Run the Analyzer:**
    ```bash
    python main.py
    ```

4.  **Input Data:**
    * **Ransom Note:** Provide a `.txt` file containing the anonymous text.
    * **Suspects:** Provide a folder name containing sample `.txt` files for each suspect.

## 📊 Sample Output
```text
[TARGET DNA EXTRACTED] Word Count: 45
------------------------------------------------------------
👤 SUSPECT: suspect1.txt (Business Email)
   👉 DNA DIFF SCORE: 13.27 (Lower is better)
..............................
👤 SUSPECT: suspect2.txt (Casual Chat)
   👉 DNA DIFF SCORE: 35.48
..............................
🚨 [RESULT] PRIME SUSPECT IDENTIFIED: SUSPECT1.TXT