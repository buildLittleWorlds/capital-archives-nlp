# Capital Archives NLP

## A Natural Language Processing Tutorial Series

---

*"A word is not a hard thing like a stone to be passed from one person to another. When Grigsu speaks a word, it dissolves into the air and reforms—imperfectly—in Yasho's mind. What arrives is never what departed."*

---

## Course Overview

This course teaches Natural Language Processing through the Capital Archives—a vast collection of philosophical manuscripts, scholarly debates, and historical records from the world of Densworld. You'll learn real NLP techniques while investigating a centuries-old mystery: are certain manuscripts attributed to the philosopher Grigsu Haldo actually forgeries?

### The Forgery Investigation

Three manuscripts (MS-0156, MS-0157, MS-0158) claim to show Grigsu recanting his stone-school views. Evidence suggests these were forged by Mink Pavar after Grigsu's death. Throughout this course, you'll build the NLP skills needed to detect these forgeries using:

- TF-IDF and vocabulary analysis
- Stylometric comparison (sentence length, function words)
- Topic modeling (do texts cluster with correct school?)
- Cross-referencing with dated events

---

## Prerequisites

- Basic Python experience
- Familiarity with pandas (or complete [Yeller Quarry Data Science](https://github.com/buildLittleWorlds/yeller-quarry-data-science) first)

## Compute Requirements

- **Free Google Colab** — No GPU required, no paid subscriptions needed
- All tutorials run in your browser with one click

---

## Learning Objectives

By the end of this course, you will be able to:

1. Load and explore text corpora using pandas
2. Clean and preprocess text (tokenization, stopwords, normalization)
3. Analyze word frequencies and build vocabulary profiles
4. Find patterns using n-grams and collocations
5. Perform part-of-speech tagging and syntactic analysis
6. Calculate document similarity using TF-IDF
7. Conduct authorship attribution using stylometry
8. Analyze sentiment in historical texts
9. Apply topic modeling (LDA) to discover themes
10. Use all techniques to detect forged manuscripts

---

## The Tutorials

| # | Tutorial | Notebook |
|---|----------|----------|
| 1 | Opening the Archive | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_01_opening_archive.ipynb) |
| 2 | Cleaning the Stacks | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_02_cleaning_stacks.ipynb) |
| 3 | The Word Counters | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_03_word_counters.ipynb) |
| 4 | Patterns in the Stone | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_04_patterns_stone.ipynb) |
| 5 | The Shape of Arguments | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_05_shape_arguments.ipynb) |
| 6 | Sorting the Schools | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_06_sorting_schools.ipynb) |
| 7 | The Voice of Grigsu | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_07_voice_grigsu.ipynb) |
| 8 | Sentiment in the Margins | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_08_sentiment_margins.ipynb) |
| 9 | The Map of Ideas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_09_map_of_ideas.ipynb) |
| 10 | The Forger's Hand (Capstone) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_10_forgers_hand.ipynb) |

---

## The Datasets

| File | Records | Description |
|------|---------|-------------|
| `scholars.csv` | 40 | Biographical registry of philosophers, scientists, historians |
| `manuscripts.csv` | 125 | Catalog of archived texts (metadata only) |
| `manuscript_texts.csv` | 169 sections | Actual text content for NLP analysis (~30,000 words) |
| `debates.csv` | 30 | Recorded scholarly arguments |
| `archivist_shops.csv` | 25 | Licensed archive establishments |
| `expeditions.csv` | 20 | Documented journeys to Yeller Quarry, Mirado, etc. |
| `word_index.csv` | 73 | Disputed terms with school-specific definitions |
| `forgery_evidence.csv` | 15 | Evidence for the capstone forgery investigation |

### Dataset Statistics

| Metric | Value |
|--------|-------|
| Total words | 30,342 |
| Documents with text | 44 |
| Unique vocabulary | 5,367 tokens |
| Total sentences | ~3,000 |
| Authors represented | 18 |

---

## Key Characters

**The Grigsu Circle (Capital scholars, ~860-890):**
- **Grigsu Haldo** (SCH-001): Stone-school philosopher. Died mysteriously after Yeller Quarry expedition.
- **Yasho Krent** (SCH-002): Water-school philosopher. Grigsu's intellectual rival.
- **Vagabu Olt / Bagbu** (SCH-003): Wandering cartographer. Narrator and connector.
- **Boffa Trent** (SCH-004): Natural philosopher. Taxonomist.
- **Mink Pavar** (SCH-005): Historian. Later suspected of forgery.

**Mirado Philosophers:**
- **Eulr Voss** (SCH-007): Codified the water-school position.
- **Fibon Arrel** (SCH-006): Created the pebble-school. Inventor of the binary world puzzle.

## Philosophical Schools

**Stone-School:** Words are permanent, discrete, can be passed unchanged.
- Key term: "permanence"
- Vocabulary markers: stone, casting, persistence, retrieval

**Water-School:** Words dissolve into collective meaning when spoken.
- Key term: "dissolution"
- Vocabulary markers: dissolution, residue, flow, pool, absorbed

**Pebble-School:** Words are temporarily "on loan" from an ancient source.
- Key term: "lending"
- Vocabulary markers: pebble, lending, return, origin, counting

---

## Getting Started

### Option 1: Google Colab (Recommended)

Click any "Open in Colab" badge in the tutorial table above. No local setup required.

1. Click the badge for Tutorial 1
2. Sign in with a Google account
3. Go to **File > Save a copy in Drive** to keep your work
4. Run the first cell to clone the repository and set up the environment

### Option 2: Local Installation

```bash
# Clone the repository
git clone https://github.com/buildLittleWorlds/capital-archives-nlp.git
cd capital-archives-nlp

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (run in Python)
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
```

---

## Course Series Context

This is a **foundational course** in the Densworld series. After completing this course, you can continue with:

- [ML Math with Densworld](https://github.com/buildLittleWorlds/ml-math-with-densworld) — Mathematical Foundations
- [The Hugging Face Series](https://github.com/buildLittleWorlds/archivist-inference-engine) — Modern AI/ML (7 courses)

### Connections to Other Courses

- **Bagbu (Vagabu Olt)** appears in both this course and Yeller Quarry
- **Expeditions** reference the same crews and creatures from Yeller Quarry
- **"Yeller numbers"** (2, 3, 5, 7, 11) appear as patterns in both courses
- The philosophical debate about words provides framework for discussing tokenization

---

## License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See [LICENSE](LICENSE) for details.

---

*"The Archives contain shadows, not the reality. Every manuscript is a copy of a thought that once lived in someone's mind—and copies decay."*
