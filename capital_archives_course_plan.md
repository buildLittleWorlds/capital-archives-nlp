# The Capital Archives: A Course in Natural Language Processing

## Course Overview

Students take on the role of **junior archivists** in the Capital's vast archives district—a labyrinthine network of licensed shops, each with its single round window, housing manuscripts, maps, expedition reports, philosophical treatises, and transcribed debates. The Chief Archivist has tasked them with cataloging, classifying, and ultimately investigating a mystery buried in the collection.

The course teaches **text analysis with Python** (NLTK, spaCy, scikit-learn, pandas) through increasingly sophisticated engagement with the archive's holdings.

---

## Canonical Details Extracted from Source Material

### Named Characters (Scholars & Thinkers)

| Name | Role | Notes |
|------|------|-------|
| **Grigsu** (also Grigsu Haldo) | Scholar, word-philosopher | "Massive frame, thick chest, beard." Believed words burrow into reality. Died mysteriously after Yeller Quarry expedition. From a village where people toss stones after conversations. |
| **Yasho** | Scholar, "towering intellect" | Female. Colleague of Grigsu. Debated word-as-stone theory. Paid thinker with disciples. |
| **Bagbu** (also Vagabu, Vag, Gab, Buva) | Wandering map-sketcher, memoirist | Narrator of the Grigsu story. Not a proper scholar—travels in a "pickbox cart." Played kachot with the scholars. |
| **Boffa** | Scholar | Member of the Grigsu/Yasho circle. |
| **Mink** | Scholar | Member of the circle. |
| **Dannkit** | Stonebreaker, part-linguist | From Grigsu's village. Nearly deaf from hammering. Lost wife and children. The one who got Grigsu to talk. |
| **Fibon** | Inventor, puzzle-maker | Lives in Mirado. Created the "binary world puzzle." Believes words are like pebbles, not drops of water. |
| **Eulr** | Great thinker of Mirado | Famous for expressing that words dissolve like water drops into the pools. |
| **Colonel Viragu** | Military commander | Sieging Mirado for 15-20 years. Has writings/memoirs. Connected to Yeller. |
| **Fyncho/Fincho** | Lieutenant to the Colonel | Only person the Colonel still speaks to. |

### Philosophical Positions (for Generating Debates)

1. **Words as Stones** (Grigsu's village tradition)
   - Words are hard, discrete, can be passed from person to person unchanged
   - Villages toss stones after conversations "so as not to lose any words"
   - "Lose a stone, forget its name"

2. **Words as Water Drops** (Mirado/Eulr tradition)
   - Each word dissolves into the whole when spoken
   - Can never be recovered—absorbed into the seventy pools
   - The pristine, anti-dirt philosophy of Mirado

3. **Words as Pebbles** (Fibon's position)
   - Words come from an ancient place and return there
   - "On loan" to speakers temporarily
   - Connected to counting, numbers, the origin of language

4. **Literalism** (the siege of Mirado = pursuit of literalism)
   - "Literalism is the demand that all sides of a symbol be visible at once"

### The Kachot Game

- A card game played by scholars
- Uses: cards, knots, scoring hooks
- Has "old rules" vs. "new rules" (swindlers play new rules)
- Played in cardhouses in the Capital
- Scholars would debate between rounds

### Archive System Details

- Archives district near the Senate-house
- Licensed and registered shops
- Each shop has a single round window (no walk-in entrance)
- Window is "a third the size of the archivist's head"
- Archivists barter over sketches, maps, books of notes
- "Back-alley archivists" for rarer/shadier materials
- Maps of Mirado are particularly sought after
- Yeller Quarry family trees are essential documents ("outrageous," "absurdly complex")

### Geographic/Institutional References

| Location | Character |
|----------|-----------|
| **The Capital** | Grid-patterned streets. Political center. Archives district. Senate-house. |
| **Yeller Quarry** | Source of creature specimens, dangerous expeditions. Stall towns on roads leading there. |
| **Tripas** | Aggregated stall-town city on southern highway near Capital |
| **Miasto** | Capital city of Yeller Quarry region |
| **Mirado** | Hovering tower in desert. City of spiraling streets. 70 pools/pipes. No dirt. |
| **Dens/Densmok** | Primordial muck, edge of disintegration |
| **Dead River** | Western region, "exists because a map named it" |
| **The North** | Isolated villages, ascetic traditions |

---

## Data Files to Generate

### 1. `manuscripts.csv` — The Core Corpus
~200 records of archived texts

**Columns:**
- `manuscript_id` (MS-0001 through MS-0200)
- `title` 
- `author` (named scholars, anonymous, attributed)
- `date_composed` (year, some approximate)
- `date_archived` 
- `genre` (treatise, debate_transcript, expedition_report, map_notes, correspondence, poetry, legal_document, family_record)
- `subject_tags` (comma-separated: words, Yeller, Mirado, creatures, expedition, philosophy, trade, family_trees)
- `word_count`
- `condition` (pristine, good, fair, damaged, fragmentary)
- `shelf_location` (shop identifier + shelf code)
- `language` (Common, Old Quarry, Mirado Script, mixed)
- `authenticity_status` (verified, disputed, suspected_forgery, unknown)
- `acquisition_source` (estate, purchase, donation, expedition, confiscation)
- `notes`

### 2. `manuscript_texts.csv` — Full Text Content
The actual text of ~50 key manuscripts (shorter pieces, excerpts, summaries)

**Columns:**
- `manuscript_id`
- `section` (for longer works: chapter/section number)
- `text` (the actual content)

**Content types to generate:**
- Philosophical treatises on word theory (in the style of Grigsu, Yasho, Fibon)
- Expedition reports from Yeller Quarry (in the style of the Boss's expedition)
- Transcribed debates between scholars
- Creature taxonomy entries
- Map annotations and travel journals
- Letters between scholars
- Kachot game records with commentary
- Legal documents (archivist licenses, expedition contracts)
- Poetry and songs
- Family tree excerpts with annotations

### 3. `scholars.csv` — Biographical Registry
~40 scholars across several generations

**Columns:**
- `scholar_id`
- `name`
- `also_known_as` (alternative names/spellings)
- `birth_year` (approximate)
- `death_year` (if known)
- `birth_place`
- `primary_affiliation` (Capital, Mirado, Independent, Quarry)
- `specialty` (word_theory, natural_philosophy, cartography, creature_taxonomy, history, legal)
- `philosophical_school` (stone_school, water_school, pebble_school, literalist, none)
- `known_associates` (comma-separated scholar_ids)
- `expeditions` (comma-separated expedition_ids)
- `major_works` (comma-separated manuscript_ids)
- `manner_of_death` (natural, unknown, expedition_casualty, executed, disappeared)
- `notes`

### 4. `debates.csv` — Recorded Arguments
~30 transcribed debates

**Columns:**
- `debate_id`
- `date`
- `location` (cardhouse name, scholar's home, public hall)
- `participants` (comma-separated scholar_ids)
- `topic`
- `winner` (if declared, else null)
- `stones_cast` (number—the village tradition of tossing stones)
- `transcript_manuscript_id` (link to manuscripts.csv)
- `summary`

### 5. `archivist_shops.csv` — Licensed Establishments
~25 shops in the archives district

**Columns:**
- `shop_id`
- `shop_name`
- `proprietor`
- `license_year`
- `specialty` (maps, expedition_reports, legal, general, rare_manuscripts, creature_taxonomy)
- `distance_from_senate` (blocks)
- `reputation` (excellent, good, fair, questionable, notorious)
- `known_for`
- `price_range` (low, moderate, high, exorbitant)
- `notes`

### 6. `expeditions.csv` — Yeller Quarry & Beyond
~20 documented expeditions

**Columns:**
- `expedition_id`
- `name`
- `year`
- `destination` (Yeller Quarry, Mirado Desert, Dens Border, North, Dead River)
- `sponsor` (Capital department, private, scholarly society)
- `leader`
- `crew_size`
- `scholars_attached` (comma-separated scholar_ids)
- `purpose` (survey, creature_collection, mapping, trade_route, military)
- `duration_days`
- `outcome` (successful, partial_success, failed, disaster, unknown)
- `casualties`
- `reports_filed` (comma-separated manuscript_ids)
- `notable_events`

### 7. `word_index.csv` — Terminology Registry
~100 terms with their disputed meanings

**Columns:**
- `term`
- `common_definition`
- `stone_school_definition`
- `water_school_definition`
- `pebble_school_definition`
- `first_attested_manuscript_id`
- `disputes` (brief description of controversy)
- `related_terms`

### 8. `forgery_evidence.csv` — For the Capstone Investigation
~15 suspected forgeries with clues

**Columns:**
- `manuscript_id`
- `suspicion_level` (low, medium, high, confirmed)
- `linguistic_anomalies` (comma-separated)
- `historical_anachronisms`
- `physical_evidence`
- `cui_bono` (who benefits from the forgery)
- `investigator_notes`

---

## Tutorial Structure

### Tutorial 1: Opening the Archive
**Skills:** Loading text data, basic string operations, len(), word counts
**Narrative:** First day as junior archivist. The Chief hands you the manuscript catalog. Your first task: basic inventory statistics.
**Exercise:** Count manuscripts by genre, find longest/shortest texts, identify damaged items needing attention.

### Tutorial 2: Cleaning the Stacks
**Skills:** String cleaning, regex basics, handling missing data
**Narrative:** Many manuscripts have transcription errors, inconsistent formatting. The water-school archivists insist on pristine text.
**Exercise:** Standardize author names, clean titles, handle encoding issues in Old Quarry texts.

### Tutorial 3: The Word Counters
**Skills:** Tokenization, word frequency, stopwords
**Narrative:** The stone-school scholars believe counting words reveals hidden patterns. You're assigned to generate frequency reports.
**Exercise:** Tokenize manuscript texts, remove stopwords, find most common words by genre and by author.

### Tutorial 4: Patterns in the Stone
**Skills:** N-grams, collocations, concordance
**Narrative:** Grigsu's final writings mention "patterns in the stone." The Chief wants you to find recurring phrases.
**Exercise:** Extract bigrams/trigrams, find collocations, build concordance for key terms like "Yeller," "stone," "word."

### Tutorial 5: The Shape of Arguments
**Skills:** Sentence segmentation, POS tagging, basic parsing
**Narrative:** The debate transcripts need grammatical analysis. Which scholars use more nouns? More verbs? The water-school claims this reveals temperament.
**Exercise:** POS tag debate transcripts, compare noun/verb ratios across scholars, identify question patterns.

### Tutorial 6: Sorting the Schools
**Skills:** TF-IDF, document similarity, clustering
**Narrative:** The Chief suspects some "anonymous" manuscripts can be attributed by style. Can you sort them into philosophical schools?
**Exercise:** Compute TF-IDF vectors, measure cosine similarity, cluster documents, visualize with t-SNE or PCA.

### Tutorial 7: The Voice of Grigsu
**Skills:** Authorship attribution, stylometrics
**Narrative:** Three manuscripts claim Grigsu as author. One is suspected to be a forgery. Can statistical analysis identify the imposter?
**Exercise:** Extract stylometric features (sentence length, vocabulary richness, function word frequency), train a classifier.

### Tutorial 8: Sentiment in the Margins
**Skills:** Sentiment analysis, opinion mining
**Narrative:** Marginal annotations reveal what readers thought of these texts. The Chief wants a "reception history" based on sentiment.
**Exercise:** Analyze marginalia for positive/negative sentiment, track how reception of key texts changed over time.

### Tutorial 9: The Map of Ideas
**Skills:** Topic modeling (LDA), visualization
**Narrative:** The archive is chaos. Can you create a "map" showing how topics connect across the collection?
**Exercise:** Run LDA on the corpus, interpret topics, visualize topic distributions across time and schools.

### Tutorial 10: The Forger's Hand
**Skills:** Capstone investigation combining all techniques
**Narrative:** A scandal: three recently "discovered" manuscripts that rewrite the history of Yeller may be forgeries created to discredit the stone-school. The Chief needs proof.

**The Investigation:**
- Linguistic analysis shows anachronistic terms
- Stylometric comparison to known authors
- Topic modeling reveals inconsistent themes
- Sentiment analysis of the "discoverer's" other writings
- Cross-referencing with expedition dates (some manuscripts describe events that hadn't happened yet)

**Hidden Answer:** The forgeries were created by [character] to support a political faction in the Senate. The linguistic fingerprint matches their other writings. Clues are planted throughout the earlier tutorials.

---

## Sample Generated Content

### Philosophical Treatise (Stone School)
```
ON THE PERMANENCE OF THE UTTERED
by Grigsu Haldo

A word is not a hard thing like a stone to be passed from one person 
to another—that is the slander of my opponents. I say instead: a word 
IS a hard thing, harder than stone, for it can be passed and yet remain, 
be given and yet kept, be thrown into the darkness of the Dens and 
emerge unscathed where stone would dissolve into the muck.

The villages of my birth understood this. After a conversation of weight, 
we cast stones—not the words themselves, but offerings to the words, 
tributes to their durability. The stones dissolve back into the earth. 
The words remain.

Yasho asks: if words are stones, why do we forget them? I answer: 
we do not forget the words. We forget where we put them. The word 
remains in its place. It is we who wander.
```

### Expedition Report
```
REPORT OF THE THIRD SURVEYING EXPEDITION TO YELLER QUARRY
Commissioned by the Department of Natural Inventory
Year of the Seventy-Third Senate

Day 12. We have passed Tripas and the road narrows. Bagbu insists 
on sketching every rock formation, which slows us considerably. Grigsu 
has been sullen since we crossed into stall-town territory. He says 
the merchants here have "lost their stones" and cannot be trusted to 
keep a bargain. Yasho finds this superstitious and told him so. They 
argued for an hour while I checked the family tree diagrams against 
our guide's claims. Without the correct lineage documentation, we 
will not be permitted past the inner checkpoints.

Day 15. A yeller five on the road last night. I have only read of them. 
Grigsu says they are "words made flesh" but would not elaborate. 
Yasho called this "more stone-school nonsense." I recorded their 
movements in my notebook: onto the road, off the road, in patterns 
of two, three, five. Prime numbers, as in the old counting rhymes.
```

### Debate Transcript
```
THE CARDHOUSE DEBATES, NIGHT VII
Present: Grigsu, Yasho, Bagbu, Mink, Boffa
Topic: Whether a word spoken in the Dens can be heard in the Capital

YASHO: The question is absurd on its face. Sound does not travel 
through marsh and stone for hundreds of miles.

GRIGSU: I did not say *sound*. I said *word*. You dissolve everything 
into its physical residue and then claim victory when the residue 
fails to perform miracles.

YASHO: And you inflate everything into metaphysics and then claim 
persecution when we ask for evidence.

MINK: Perhaps we might—

GRIGSU: [standing] What do you know about anything?

[At this point Grigsu departed. Twelve stones were cast by the 
remaining participants. The debate was ruled incomplete.]
```

---

## Technical Requirements

### Python Libraries
- pandas, numpy (data handling)
- nltk (tokenization, POS tagging, sentiment)
- spaCy (NER, parsing)
- scikit-learn (TF-IDF, clustering, classification)
- gensim (topic modeling)
- matplotlib, seaborn, plotly (visualization)
- wordcloud (for fun)

### Data Generation Approach
1. **Skeleton from canon:** Names, places, relationships, philosophical positions from the ore files
2. **Extrapolation:** Generate scholars who could have existed in the same world, manuscripts they would have written
3. **Stylistic consistency:** All generated text maintains the voice and concerns of Densworld
4. **Hidden structure:** Plant the forgery clues deliberately; create genuine statistical patterns that students can discover

---

## Connection to Existing Course

- References Yeller Quarry data (creatures, crews) as "field reports" in the archive
- Bagbu appears in both (the wandering map-maker)
- "Yeller numbers" (2, 3, 5, 7, 11) appear as a pattern in both courses
- The philosophical debate about words provides conceptual framework for discussing tokenization, embeddings, meaning

---

## Capstone Answer Key (Hidden)

The three forged manuscripts were created by **Mink** after Grigsu's death, attempting to discredit the stone-school by making its claims appear absurd. Evidence:

1. **Linguistic:** Uses terms ("dissolution," "residue") that appear nowhere in authentic stone-school texts but frequently in Mink's own notes
2. **Stylometric:** Sentence length distribution matches Mink's verified writings, not Grigsu's
3. **Anachronism:** References the "Third Surveying Expedition" in a manuscript supposedly written before it occurred
4. **Topic modeling:** The "forged" Grigsu texts cluster with water-school documents, not stone-school
5. **Motive:** Mink's correspondence (discoverable in Tutorial 8) reveals resentment toward Grigsu dating back to a kachot game dispute
