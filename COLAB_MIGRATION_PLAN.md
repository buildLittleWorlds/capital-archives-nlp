# Plan: Making Capital Archives NLP Colab-Ready

## Overview
Prepare the Capital Archives NLP course for GitHub publication with Google Colab compatibility, enabling students to run notebooks directly from the repository.

---

## Phase 1: Repository Setup Files

### 1.1 Create `.gitignore`
- Exclude `.DS_Store`, `__pycache__/`, `.ipynb_checkpoints/`
- Exclude any local virtual environments

### 1.2 Create `requirements.txt`
Dependencies needed:
```
pandas
numpy
matplotlib
nltk
scikit-learn
```

### 1.3 Add `LICENSE` file
- Recommend CC-BY-4.0 for educational content
- Allows reuse with attribution

---

## Phase 2: Colab Setup Infrastructure

### 2.1 Create `colab_setup.py` helper script
A small utility that:
- Clones the repo (if not already present)
- Changes to the correct directory
- Installs requirements
- Downloads NLTK data
- Confirms setup complete

### 2.2 Create standardized Colab setup cell
Template to add to each notebook:
```python
# Run this cell first to set up the environment
!git clone https://github.com/USERNAME/capital-archives-nlp.git 2>/dev/null || true
%cd capital-archives-nlp
!pip install -q -r requirements.txt
```

---

## Phase 3: Notebook Modifications

### 3.1 Add Colab badge and setup cell to each notebook
For all 10 tutorials, add as first cell:
- "Open in Colab" badge linking to the notebook
- Setup code that clones repo and installs dependencies
- NLTK downloads (for notebooks that need them)

### 3.2 Notebooks requiring NLTK setup
Based on my review:
- **Tutorial 3** (Word Counters): tokenization, stopwords
- **Tutorial 4** (Patterns): tokenization
- **Tutorial 5** (Shape of Arguments): POS tagging
- **Tutorial 7** (Voice of Grigsu): tokenization, stopwords, POS
- **Tutorial 8** (Sentiment): VADER
- **Tutorial 9** (Map of Ideas): tokenization, stopwords
- **Tutorial 10** (Forger's Hand): all of the above

### 3.3 Notebooks with sklearn (no special setup needed)
- **Tutorial 6** (Sorting Schools): TF-IDF, clustering, PCA
- **Tutorial 7, 9, 10**: Also use sklearn

---

## Phase 4: Documentation Updates

### 4.1 Update README.md
Add sections:
- **"Run in Google Colab"** - instructions for students
- **"For YouTube Walkthrough Students"** - link to playlist
- Badge for each notebook with direct Colab link

### 4.2 Create `CONTRIBUTING.md` (optional)
If you want others to contribute improvements

---

## Phase 5: Testing

### 5.1 Test each notebook in fresh Colab environment
- Open each notebook via Colab badge
- Run all cells
- Verify no errors
- Check all visualizations render

### 5.2 Verify data loading works
- Confirm relative paths resolve correctly after `%cd`
- Test the validation script runs cleanly

---

## Implementation Order

| Step | Task | Files Affected |
|------|------|----------------|
| 1 | Create `.gitignore` | New file |
| 2 | Create `requirements.txt` | New file |
| 3 | Create `LICENSE` | New file |
| 4 | Add Colab setup to Tutorial 01 | `tutorial_01_opening_archive.ipynb` |
| 5 | Add Colab setup to Tutorial 02 | `tutorial_02_cleaning_stacks.ipynb` |
| 6 | Add Colab setup to Tutorial 03 | `tutorial_03_word_counters.ipynb` |
| 7 | Add Colab setup to Tutorial 04 | `tutorial_04_patterns_stone.ipynb` |
| 8 | Add Colab setup to Tutorial 05 | `tutorial_05_shape_arguments.ipynb` |
| 9 | Add Colab setup to Tutorial 06 | `tutorial_06_sorting_schools.ipynb` |
| 10 | Add Colab setup to Tutorial 07 | `tutorial_07_voice_grigsu.ipynb` |
| 11 | Add Colab setup to Tutorial 08 | `tutorial_08_sentiment_margins.ipynb` |
| 12 | Add Colab setup to Tutorial 09 | `tutorial_09_map_of_ideas.ipynb` |
| 13 | Add Colab setup to Tutorial 10 | `tutorial_10_forgers_hand.ipynb` |
| 14 | Update README with Colab links | `README.md` |
| 15 | Test all notebooks in Colab | Manual testing |

---

## Colab Setup Cell Template

```python
# ============================================
# COLAB SETUP - Run this cell first!
# ============================================
import os

# Clone the repository if not already present
if not os.path.exists('capital-archives-nlp'):
    !git clone https://github.com/USERNAME/capital-archives-nlp.git

# Change to the repository directory
%cd capital-archives-nlp

# Install dependencies
!pip install -q pandas numpy matplotlib scikit-learn nltk

# Download NLTK data (uncomment lines needed for this tutorial)
# import nltk
# nltk.download('punkt', quiet=True)
# nltk.download('punkt_tab', quiet=True)
# nltk.download('stopwords', quiet=True)
# nltk.download('averaged_perceptron_tagger', quiet=True)
# nltk.download('averaged_perceptron_tagger_eng', quiet=True)
# nltk.download('vader_lexicon', quiet=True)

print("✓ Setup complete! You can now run the rest of the notebook.")
```

---

## Notes for YouTube Integration

- Each notebook will have a consistent first cell students can run
- Consider adding a comment at the top of each notebook: `# YouTube Walkthrough: [LINK]`
- README can have a table mapping tutorials to video links

---

## Questions to Resolve

1. **GitHub username/repo name**: Need this to generate correct Colab badge URLs
2. **License preference**: CC-BY-4.0 recommended, but confirm
3. **YouTube playlist URL**: To add to README once available
