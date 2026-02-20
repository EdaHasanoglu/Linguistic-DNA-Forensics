import os
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# NLTK kütüphaneleri (Kelime ayırıcılar)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("[INIT] Downloading NLTK resources...")
    nltk.download('punkt')

def lexical_richness(text):
    """
    Type-Token Ratio (Sözdizimsel Zenginlik) hesaplar.
    Yazarın kelime dağarcığı ne kadar geniş? Toplam kelime sayısına oranla kaç farklı kelime kullanmış?
    """
    tokens = word_tokenize(text.lower())
    words = [word for word in tokens if word.isalpha()]
    if not words: return 0
    return len(set(words)) / len(words)

def extract_linguistic_dna(ransom_text, suspects_texts):
    """
    TF-IDF ve N-Gram kullanarak metinleri vektör uzayına çevirir ve 
    Kosinüs Benzerliği (Cosine Similarity) ile karşılaştırır.
    """
    # Ransom Note (Fidye Mektubu) ilk sıraya, şüpheliler arkasına ekleniyor.
    all_documents = [ransom_text] + suspects_texts
    
    # ngram_range=(1, 2) demek: Hem tek kelimelere (Unigram) hem de ikili kelime gruplarına (Bigram) bak!
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    
    # Metinleri matematiksel matrislere çeviriyoruz
    tfidf_matrix = vectorizer.fit_transform(all_documents)
    
    # İlk matris (Ransom Note) ile diğer matrisleri (Şüpheliler) karşılaştır
    # [0:1] fidye mektubu, [1:] şüphelilerin tamamı
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    
    return similarities[0]

def main():
    print("=" * 60)
    print("🧬 LINGUISTIC DNA FORENSICS V2.0 (STYLOMETRY ENGINE)")
    print("=" * 60)

    # 1. READ RANSOM NOTE
    ransom_path = 'ransom.txt'
    if not os.path.exists(ransom_path):
        print("❌ 'ransom.txt' bulunamadı!")
        return
        
    with open(ransom_path, 'r', encoding='utf-8') as f:
        ransom_text = f.read()
        
    r_richness = lexical_richness(ransom_text)
    print(f"\n📄 [TARGET DNA EXTRACTED]")
    print(f"   - Lexical Richness (Kelime Çeşitliliği): %{r_richness*100:.2f}")
    print("-" * 60)

    # 2. READ SUSPECTS
    suspects_folder = 'suspects'
    if not os.path.exists(suspects_folder):
        print(f"❌ '{suspects_folder}' klasörü bulunamadı!")
        return

    suspect_files = [f for f in os.listdir(suspects_folder) if f.endswith('.txt')]
    if not suspect_files:
        print("❌ Şüpheli dosyaları bulunamadı.")
        return

    suspects_texts = []
    for suspect in suspect_files:
        path = os.path.join(suspects_folder, suspect)
        with open(path, 'r', encoding='utf-8') as f:
            suspects_texts.append(f.read())

    # 3. DNA ANALYSIS (Makine Öğrenmesi Devrede)
    print("🧠 TF-IDF ve N-Gram Analizi Başlatılıyor...")
    similarity_scores = extract_linguistic_dna(ransom_text, suspects_texts)

    best_match = None
    highest_score = 0

    print("\n🔍 ANALİZ SONUÇLARI:")
    for idx, score in enumerate(similarity_scores):
        suspect_name = suspect_files[idx]
        s_richness = lexical_richness(suspects_texts[idx])
        
        # Yüzdelik dilime çeviriyoruz
        match_percentage = score * 100
        
        print(f"\n👤 SUSPECT: {suspect_name}")
        print(f"   - Lexical Richness: %{s_richness*100:.2f}")
        print(f"   👉 DNA EŞLEŞME ORANI: %{match_percentage:.2f} (Daha yüksek daha iyi)")
        
        if match_percentage > highest_score:
            highest_score = match_percentage
            best_match = suspect_name

    print("=" * 60)
    if highest_score > 0:
        print(f"🚨 KESİNLEŞMİŞ HEDEF: {best_match} (%{highest_score:.2f} Benzerlik)")
    else:
        print("❓ Yeterli DNA eşleşmesi bulunamadı.")
    print("=" * 60)

if __name__ == "__main__":
    main()