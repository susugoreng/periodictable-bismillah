import streamlit as st
import random

# Daftar unsur periodik
periodic_table = [
    {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
    {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
    {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
    {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
    {"name": "boron", "symbol": "B", "number": 5, "group": 13, "period": 2},
    {"name": "karbon", "symbol": "C", "number": 6, "group": 14, "period": 2},
    {"name": "nitrogen", "symbol": "N", "number": 7, "group": 15, "period": 2},
    {"name": "oksigen", "symbol": "O", "number": 8, "group": 16, "period": 2},
    {"name": "fluorin", "symbol": "F", "number": 9, "group": 17, "period": 2},
    {"name": "neon", "symbol": "Ne", "number": 10, "group": 18, "period": 2},
    {"name": "natrium", "symbol": "Na", "number": 11, "group": 1, "period": 3},
    {"name": "magnesium", "symbol": "Mg", "number": 12, "group": 2, "period": 3},
    {"name": "aluminium", "symbol": "Al", "number": 13, "group": 13, "period": 3},
    {"name": "silikon", "symbol": "Si", "number": 14, "group": 14, "period": 3},
    {"name": "fosfor", "symbol": "P", "number": 15, "group": 15, "period": 3},
    {"name": "belerang", "symbol": "S", "number": 16, "group": 16, "period": 3},
    {"name": "klorin", "symbol": "Cl", "number": 17, "group": 17, "period": 3},
    {"name": "argon", "symbol": "Ar", "number": 18, "group": 18, "period": 3},
    {"name": "kalium", "symbol": "K", "number": 19, "group": 1, "period": 4},
    {"name": "kalsium", "symbol": "Ca", "number": 20, "group": 2, "period": 4},
    {"name": "skandium", "symbol": "Sc", "number": 21, "group": 3, "period": 4},
    {"name": "titanium", "symbol": "Ti", "number": 22, "group": 4, "period": 4},
    {"name": "vanadium", "symbol": "V", "number": 23, "group": 5, "period": 4},
    {"name": "chromium", "symbol": "Cr", "number": 24, "group": 6, "period": 4},
    {"name": "mangan", "symbol": "Mn", "number": 25, "group": 7, "period": 4},
    {"name": "besi", "symbol": "Fe", "number": 26, "group": 8, "period": 4},
    {"name": "kobalt", "symbol": "Co", "number": 27, "group": 9, "period": 4},
    {"name": "nikel", "symbol": "Ni", "number": 28, "group": 10, "period": 4},
    {"name": "tembaga", "symbol": "Cu", "number": 29, "group": 11, "period": 4},
    {"name": "zinc", "symbol": "Zn", "number": 30, "group": 12, "period": 4},
    {"name": "gallium", "symbol": "Ga", "number": 31, "group": 13, "period": 4},
    {"name": "germanium", "symbol": "Ge", "number": 32, "group": 14, "period": 4},
    {"name": "arsen", "symbol": "As", "number": 33, "group": 15, "period": 4},
    {"name": "selenium", "symbol": "Se", "number": 34, "group": 16, "period": 4},
    {"name": "bromine", "symbol": "Br", "number": 35, "group": 17, "period": 4},
    {"name": "krypton", "symbol": "Kr", "number": 36, "group": 18, "period": 4},
    {"name": "rubidium", "symbol": "Rb", "number": 37, "group": 1, "period": 5},
    {"name": "strontium", "symbol": "Sr", "number": 38, "group": 2, "period": 5},
    {"name": "yttrium", "symbol": "Y", "number": 39, "group": 3, "period": 5},
    {"name": "zirconium", "symbol": "Zr", "number": 40, "group": 4, "period": 5}
]

# Inisialisasi state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_num' not in st.session_state:
    st.session_state.question_num = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'answer_submitted' not in st.session_state:
    st.session_state.answer_submitted = False

def generate_question():
    element = random.choice(periodic_table)
    question_type = random.choice(["symbol", "number", "group", "period"])
    return {"element": element, "type": question_type}

st.title("🔬 Kuis Tabel Periodik")

if st.session_state.question_num < 5:
    if st.session_state.current_question is None:
        st.session_state.current_question = generate_question()
        st.session_state.answer_submitted = False

    q = st.session_state.current_question
    e = q["element"]
    correct_answer = ""
    
    if q["type"] == "symbol":
        question_text = f"Apa simbol dari unsur '{e['name'].capitalize()}'?"
        correct_answer = e["symbol"]
    elif q["type"] == "number":
        question_text = f"Berapa nomor atom dari '{e['name'].capitalize()}'?"
        correct_answer = str(e["number"])
    elif q["type"] == "group":
        question_text = f"Golongan berapa unsur '{e['name'].capitalize()}'?"
        correct_answer = str(e["group"])
    elif q["type"] == "period":
        question_text = f"Periode berapa unsur '{e['name'].capitalize()}'?"
        correct_answer = str(e["period"])

    user_input = st.text_input(question_text, key=f"input_{st.session_state.question_num}")

    # Tombol kirim jawaban
    if st.button("Kirim Jawaban") and not st.session_state.answer_submitted:
        if user_input.strip().lower() == correct_answer.lower():
            st.session_state.score += 1
            st.session_state.feedback = "✅ Benar!"
        else:
            st.session_state.feedback = f"❌ Salah. Jawaban yang benar: {correct_answer}"
        st.session_state.answer_submitted = True

    # Tampilkan feedback
    st.write(st.session_state.feedback)

    # Tombol lanjut jika sudah kirim jawaban
    if st.session_state.answer_submitted:
        if st.button("Soal Berikutnya"):
            st.session_state.question_num += 1
            st.session_state.current_question = None
            st.session_state.feedback = ""
            st.session_state.answer_submitted = False

    # Skor sementara
    st.markdown(f"### Skor: {st.session_state.score}/5")

# Kuis selesai
if st.session_state.question_num >= 5:
    st.success(f"🎉 Kuis selesai! Skor akhir kamu: {st.session_state.score}/5")
    if st.button("Main Lagi"):
        for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
            if key in st.session_state:
                del st.session_state[key]
