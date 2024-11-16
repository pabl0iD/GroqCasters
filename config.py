# config.py

# GroqProvider settings
DEFAULT_MODEL = "llama-3.1-70b-versatile"
MAX_TOKENS = {
    "outline": 8000,
    "full_script": 8000,
    "dialogue": 8000
}

# Host profiles
HOST_PROFILES = """
Host1 (Ania): Entuzjastyczny, skłonny do osobistych anegdot, lubi odnosić koncepcje do życia codziennego. Czasami przerywa z podekscytowaniem, aby dodać coś od siebie.
Host2 (Marek): Bardziej analityczny, lubi nawiązywać do popkultury, często zadaje pytania wyjaśniające.Czasami kończy zdania Rachel, gdy widzi, dokąd zmierza.
"""

# Prompt templates
OUTLINE_PROMPT_TEMPLATE = """
Utwórz szczegółowy zarys dwuosobowego odcinka podcastu w oparciu o następujące dane wejściowe:

{input_text}

Konspekt powinien zawierać:
1. Wprowadzenie przyciągające uwagę
2. Główne punkty do omówienia, z możliwością osobistych anegdot i przykładów
3. Ciekawe analogie lub nawiązania do popkultury
4. Wniosek podsumowujący najważniejsze wnioski i zapowiadający następny odcinek

Sformatuj konspekt, używając wyraźnych sekcji i wypunktowań.
"""

EXPAND_PROMPT_TEMPLATE = """
Rozwiń poniższy zarys do pełnego skryptu podcastu dla dwóch gospodarzy, Marka i Anny:

{outline}

Host Profiles:
{host_profiles}

Wytyczne:
- Spraw, aby scenariusz był wciągający, konwersacyjny i łatwy do zrozumienia.
- Dołącz analogie, przykłady i wyjaśnienia, aby ułatwić zrozumienie złożonych koncepcji.
- Dołącz osobiste anegdoty i doświadczenia każdego gospodarza.
- Używaj zwyczajnego języka, w tym słów uzupełniających i wykrzykników (np. „um”, „wiesz”, „mam na myśli”).
- Uwzględnij momenty humoru, entuzjazmu i innych emocji.
- Upewnij się, że gospodarze wykorzystują swoje punkty i od czasu do czasu zadają sobie nawzajem pytania.
- Dodaj płynne przejścia między tematami, korzystając z osobistych komentarzy lub pytań.
- Czasami jeden gospodarz przerywa drugiemu, aby dodać punkt lub zakończyć myśl.

Scenariusz powinien przypominać naturalną rozmowę między przyjaciółmi, a nie formalną prezentację.
"""

DIALOGUE_PROMPT_TEMPLATE = """
Przekształć poniższy skrypt podcastu w naturalny, wciągający dialog pomiędzy Anną i Markiem:

{full_script}

Host Profiles:
{host_profiles}

Wytyczne:
- Naszym celem jest bycie wciągającym i pouczającym, interesującym i rozrywkowym, jak prawdziwa rozmowa między przyjaciółmi.
- W każdej części dialogu zmieniajcie Annę i Marka.
- Spraw, aby rozmowa toczyła się naturalnie, a gospodarze opierali się na swoich spostrzeżeniach.
- Omów obie strony na dowolny temat uczciwie i szczerze.
- Jeżeli są różnice zdań, przedstaw je z szacunkiem i przeanalizuj obie perspektywy.
- Uwzględnij potoczny język, wykrzykniki i słowa uzupełniające (np. „lubię”, „wiesz”, „mam na myśli”).
- Dodaj krótkie osobiste anegdoty i doświadczenia, aby uczynić je bardziej przystępnymi.
- Uwzględnij momenty humoru, entuzjazmu i innych emocji.
- Od czasu do czasu przeredaguj lub doprecyzuj punkty, jak w mowie naturalnej.
- Zapewnij płynne przejścia między tematami, korzystając z osobistych komentarzy lub pytań.
- Zachowaj dokładność naukową i główne punkty, jednocześnie sprawiając, że dialog będzie spontaniczny i wciągający.
- Rzadko i sporadycznie (około 2-3 razy w całym scenariuszu) uwzględniaj przerwy, w których jeden prowadzący wtrąca się lub kończy myśl drugiego. Na przykład:
  Anna: „Jak to mówią, błądzić jest rzeczą ludzką i...”
  Marek: „Przebaczać jest boskie! Dokładnie.”
  Lub
  Marek: „...liczby całkowite, liczby okrągłe--”
  Anna: „Nawet liczby urojone! Prawda?”
  Marek: „Tak! Nie brałem tego pod uwagę.”

Sformatuj dane wyjściowe jako:
Anna: [Dialog Anny]
Marek: [Dialog Marka]
Anna: [Dialog Anny]
...i tak dalej.

Pamiętaj, aby rozmowa brzmiała tak naturalnie i wciągająco, jak to tylko możliwe, tak jakby dwóch przyjaciół swobodnie omawiało ten temat, z okazjonalnymi przyjacielskimi przerwami.
"""
