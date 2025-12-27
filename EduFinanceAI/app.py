import streamlit as st

# --- Uygulama Başlığı ---
st.title("🧠 EduFinance AI - Mini Quiz Sistemi")
st.write("📘 Finansal Bilgini Test Et!")

# --- Soru Havuzu ---
sorular = [
    {
        "soru": "1️⃣ Enflasyon nedir?",
        "secenekler": [
            "A) Fiyatların genel seviyesinin sürekli düşmesi",
            "B) Fiyatların genel seviyesinin sürekli artması",
            "C) Para arzının azalması",
            "D) Üretim miktarının düşmesi"
        ],
        "dogru": "B) Fiyatların genel seviyesinin sürekli artması"
    },
    {
        "soru": "2️⃣ Bireysel emeklilik sisteminin amacı nedir?",
        "secenekler": [
            "A) Vergi oranlarını düşürmek",
            "B) Devletin gelirini artırmak",
            "C) Emeklilik döneminde ek gelir sağlamaktır",
            "D) Faiz oranlarını sabitlemek"
        ],
        "dogru": "C) Emeklilik döneminde ek gelir sağlamaktır"
    },
    {
        "soru": "3️⃣ Faiz oranı neyi ifade eder?",
        "secenekler": [
            "A) Borç verilen paranın maliyetini",
            "B) Enflasyon oranını",
            "C) İşsizlik oranını",
            "D) Borsa endeksini"
        ],
        "dogru": "A) Borç verilen paranın maliyetini"
    }
]

# --- Quiz Formu ---
st.header("📝 Quiz Soruları")

puan = 0
for i, s in enumerate(sorular):
    st.subheader(s["soru"])
    cevap = st.radio(f"Cevabını seç ({i+1}. soru)", s["secenekler"], key=i)
    if st.button(f"Cevabı Gönder ({i+1}. soru)", key=f"btn_{i}"):
        if cevap == s["dogru"]:
            st.success("✅ Doğru cevap!")
            puan += 1
        else:
            st.error(f"❌ Yanlış. Doğru cevap: {s['dogru']}")

# --- Puan Gösterimi ---
if st.button("🎯 Sonucu Göster"):
    st.info(f"Toplam {len(sorular)} sorudan {puan} doğru yaptın.")
    if puan == len(sorular):
        st.success("🌟 Mükemmel! Tüm soruları doğru cevapladın!")
    elif puan >= len(sorular) / 2:
        st.success("👍 Fena değil, biraz daha pratikle daha iyi olabilirsin.")
    else:
        st.warning("💪 Daha fazla çalışman gerekiyor, devam et!")

