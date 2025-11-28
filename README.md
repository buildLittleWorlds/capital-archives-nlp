# The Capital Archives: Data Files

A course teaching Natural Language Processing through the Densworld fictional setting.

## Run in Google Colab

Click any badge below to open the tutorial directly in Google Colab:

| Tutorial | Title | Open in Colab |
|----------|-------|---------------|
| 1 | Opening the Archive | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_01_opening_archive.ipynb) |
| 2 | Cleaning the Stacks | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_02_cleaning_stacks.ipynb) |
| 3 | The Word Counters | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_03_word_counters.ipynb) |
| 4 | Patterns in the Stone | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_04_patterns_stone.ipynb) |
| 5 | The Shape of Arguments | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_05_shape_arguments.ipynb) |
| 6 | Sorting the Schools | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_06_sorting_schools.ipynb) |
| 7 | The Voice of Grigsu | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_07_voice_grigsu.ipynb) |
| 8 | Sentiment in the Margins | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_08_sentiment_margins.ipynb) |
| 9 | The Map of Ideas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_09_map_of_ideas.ipynb) |
| 10 | The Forger's Hand | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/capital-archives-nlp/blob/main/tutorial_10_forgers_hand.ipynb) |

> **Note:** After opening in Colab, run the first cell to clone the repository and set up the environment.

---

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total words | 30,342 |
| Documents with text | 44 |
| Unique vocabulary | 5,367 tokens |
| Total sentences | ~3,000 |
| Authors represented | 18 |

## Files Overview

### Data Files

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

### Tutorial Topics

| Tutorial | Title | Topics |
|----------|-------|--------|
| 1 | Opening the Archive | Loading data, pandas basics, exploring a corpus |
| 2 | Cleaning the Stacks | Text cleaning, regex, string manipulation |
| 3 | The Word Counters | Tokenization, word frequency, stopwords |
| 4 | Patterns in the Stone | N-grams, collocations, concordance |
| 5 | The Shape of Arguments | POS tagging, sentence analysis |
| 6 | Sorting the Schools | TF-IDF, document similarity, clustering |
| 7 | The Voice of Grigsu | Authorship attribution, stylometry |
| 8 | Sentiment in the Margins | Sentiment analysis |
| 9 | The Map of Ideas | Topic modeling (LDA) |
| 10 | The Forger's Hand | **Capstone**: Forgery investigation |

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

## The Forgery Mystery (Capstone)

Three manuscripts (MS-0156, MS-0157, MS-0158) claim to show Grigsu recanting his stone-school views. Evidence suggests these were forged by Mink Pavar after Grigsu's death:

1. **Linguistic anomalies:** Water-school vocabulary in supposed stone-school texts
2. **Anachronisms:** References to events that occurred after supposed composition dates
3. **Physical evidence:** Paper and ink inconsistent with claimed dates
4. **Motive:** The kachot dispute (DEB-12) created lasting resentment

Students will use NLP techniques to detect the forgeries:
- TF-IDF and vocabulary analysis
- Stylometric comparison (sentence length, function words)
- Topic modeling (do texts cluster with correct school?)
- Cross-referencing with dated events

## Local Setup

If you prefer to run locally instead of Colab:

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

## Loading the Data

```python
import pandas as pd

scholars = pd.read_csv('scholars.csv')
manuscripts = pd.read_csv('manuscripts.csv')
texts = pd.read_csv('manuscript_texts.csv')
debates = pd.read_csv('debates.csv')
shops = pd.read_csv('archivist_shops.csv')
expeditions = pd.read_csv('expeditions.csv')
word_index = pd.read_csv('word_index.csv')
forgery = pd.read_csv('forgery_evidence.csv')
```

## Sample Queries

```python
# Find all stone-school scholars
stone_school = scholars[scholars['philosophical_school'] == 'stone_school']

# Get texts by Grigsu
grigsu_texts = texts[texts['manuscript_id'].isin(
    manuscripts[manuscripts['author'] == 'Grigsu Haldo']['manuscript_id']
)]

# Find suspected forgeries
forgeries = manuscripts[manuscripts['authenticity_status'] == 'suspected_forgery']

# Get all debates involving Yasho
yasho_debates = debates[debates['participants'].str.contains('SCH-002')]
```

## Connections to Yeller Quarry Course

- Bagbu (Vagabu Olt) appears in both courses
- Expeditions reference the same crews and creatures
- "Yeller numbers" (2, 3, 5, 7, 11) appear as a pattern in both
- The philosophical debate about words provides framework for discussing tokenization

## License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See [LICENSE](LICENSE) for details.
