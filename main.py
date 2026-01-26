import os
import math
import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK data is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    print("[INIT] Downloading NLTK resources...")
    nltk.download('punkt')
    nltk.download('punkt_tab')

def preprocess_text(text):
    """
    Normalizes text: converts to lowercase and tokenizes.
    Removes punctuation to focus purely on word usage.
    """
    text = text.lower()
    tokens = word_tokenize(text)
    # Keep only alphanumeric words
    words = [word for word in tokens if word.isalpha()]
    return words

def get_function_word_freq(words):
    """
    Extracts the 'Grammatical Fingerprint' of the author.
    Analyzes the frequency of 'Function Words' (Stopwords) which are 
    used subconsciously and are independent of the topic.
    """
    # These words act as the 'DNA' of writing style
    common_fingerprints = [
        "the", "to", "and", "of", "a", "in", "that", "is", 
        "for", "it", "with", "as", "was", "on", "at", "by",
        "be", "this", "have", "from", "or", "not", "but"
    ]
    
    total_words = len(words)
    if total_words == 0: return {}
    
    frequencies = {}
    for fp_word in common_fingerprints:
        count = words.count(fp_word)
        # Calculate percentage usage (e.g., 'the' constitutes 5% of text)
        frequencies[fp_word] = (count / total_words) * 100
        
    return frequencies

def compare_fingerprints(freq1, freq2):
    """
    Calculates the 'Manhattan Distance' between two linguistic fingerprints.
    Lower score = Higher similarity (Same author probability).
    """
    diff_score = 0
    for word in freq1:
        val1 = freq1[word]
        val2 = freq2.get(word, 0) # Get 0 if word not found
        
        # Absolute difference accumulation
        diff_score += abs(val1 - val2)
        
    return diff_score

def main():
    print("\n--- 🕵️‍♀️ LINGUISTIC DNA ANALYZER (FUNCTION WORD FORENSICS) ---")
    print("[INFO] Analyzing grammatical patterns independent of text topic.\n")

    ransom_file = input("Enter Ransom Note filename (e.g., ransom.txt): ").strip()
    suspects_folder = input("Enter Suspects Folder name (e.g., suspects): ").strip()

    # Validation
    if not os.path.exists(ransom_file):
        print(f"❌ [ERROR] File '{ransom_file}' not found.")
        return
    
    if not os.path.isdir(suspects_folder):
        print(f"❌ [ERROR] Directory '{suspects_folder}' not found.")
        return

    # 1. ANALYZE TARGET (RANSOM NOTE)
    try:
        with open(ransom_file, 'r', encoding='utf-8') as f:
            ransom_text = f.read()
    except Exception as e:
        print(f"❌ Read Error: {e}")
        return
    
    r_words = preprocess_text(ransom_text)
    r_freq = get_function_word_freq(r_words)

    print(f"\n📄 [TARGET DNA EXTRACTED] Word Count: {len(r_words)}")
    print("-" * 60)

    # 2. ANALYZE SUSPECTS
    suspects = [f for f in os.listdir(suspects_folder) if f.endswith('.txt')]
    
    if not suspects:
        print("❌ No text files found in the suspects folder.")
        return

    best_match = None
    lowest_diff = float('inf') # Start with infinity

    for suspect in suspects:
        path = os.path.join(suspects_folder, suspect)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                suspect_text = f.read()
        except:
            continue
        
        s_words = preprocess_text(suspect_text)
        s_freq = get_function_word_freq(s_words)
        
        # Compare DNA
        diff_score = compare_fingerprints(r_freq, s_freq)
        
        print(f"👤 SUSPECT: {suspect}")
        print(f"   - Word Count: {len(s_words)}")
        print(f"   👉 DNA DIFF SCORE: {diff_score:.2f} (Lower is better)")
        print("." * 30)

        if diff_score < lowest_diff:
            lowest_diff = diff_score
            best_match = suspect

    print("-" * 60)
    if best_match:
        print(f"🚨 [RESULT] PRIME SUSPECT IDENTIFIED: {best_match.upper()}")
        print(f"   (Linguistic DNA match confirm. Diff Score: {lowest_diff:.2f})")
    else:
        print("❌ Inconclusive Analysis.")

if __name__ == "__main__":
    main()