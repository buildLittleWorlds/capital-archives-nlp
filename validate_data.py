"""
Capital Archives Data Validation Script

This script loads and validates all data files for the Capital Archives NLP course.
Run this to verify the data is properly formatted and internally consistent.

Usage: python validate_data.py
"""

import pandas as pd
import os
from collections import Counter

def load_all_data(data_dir='.'):
    """Load all CSV files from the data directory."""
    files = {
        'scholars': 'scholars.csv',
        'manuscripts': 'manuscripts.csv',
        'texts': 'manuscript_texts.csv',
        'debates': 'debates.csv',
        'shops': 'archivist_shops.csv',
        'expeditions': 'expeditions.csv',
        'word_index': 'word_index.csv',
        'forgery': 'forgery_evidence.csv'
    }
    
    data = {}
    for name, filename in files.items():
        filepath = os.path.join(data_dir, filename)
        try:
            data[name] = pd.read_csv(filepath)
            print(f"✓ Loaded {name}: {len(data[name])} rows")
        except Exception as e:
            print(f"✗ Error loading {name}: {e}")
    
    return data

def validate_references(data):
    """Check that cross-references between tables are valid."""
    print("\n--- Validating References ---")
    
    # Get valid IDs
    scholar_ids = set(data['scholars']['scholar_id'])
    manuscript_ids = set(data['manuscripts']['manuscript_id'])
    expedition_ids = set(data['expeditions']['expedition_id'])
    
    # Check manuscript texts reference valid manuscripts
    text_ms_ids = set(data['texts']['manuscript_id'])
    invalid_text_refs = text_ms_ids - manuscript_ids
    if invalid_text_refs:
        print(f"⚠ Texts reference unknown manuscripts: {invalid_text_refs}")
    else:
        print(f"✓ All text manuscript references valid")
    
    # Check forgery evidence references valid manuscripts
    forgery_ms_ids = set(data['forgery']['manuscript_id'])
    invalid_forgery_refs = forgery_ms_ids - manuscript_ids
    if invalid_forgery_refs:
        print(f"⚠ Forgery evidence references unknown manuscripts: {invalid_forgery_refs}")
    else:
        print(f"✓ All forgery manuscript references valid")
    
    # Check debates reference valid scholars
    all_debate_participants = set()
    for participants in data['debates']['participants']:
        for p in participants.split(','):
            all_debate_participants.add(p.strip())
    invalid_participants = all_debate_participants - scholar_ids
    if invalid_participants:
        print(f"⚠ Debates reference unknown scholars: {invalid_participants}")
    else:
        print(f"✓ All debate participant references valid")
    
    return True

def analyze_text_content(data):
    """Basic analysis of manuscript text content."""
    print("\n--- Text Content Analysis ---")
    
    texts = data['texts']
    
    # Combine text sections by manuscript
    combined = texts.groupby('manuscript_id')['text'].apply(' '.join).reset_index()
    combined['word_count'] = combined['text'].str.split().str.len()
    
    print(f"Total manuscripts with text: {len(combined)}")
    print(f"Total words: {combined['word_count'].sum():,}")
    print(f"Average words per manuscript: {combined['word_count'].mean():.0f}")
    print(f"Longest manuscript: {combined.loc[combined['word_count'].idxmax(), 'manuscript_id']} ({combined['word_count'].max()} words)")
    
    # Check for key vocabulary
    all_text = ' '.join(combined['text']).lower()
    key_terms = ['dissolution', 'stone', 'pebble', 'word', 'yeller', 'grigsu', 'yasho', 'mirado']
    print("\nKey term frequencies:")
    for term in key_terms:
        count = all_text.count(term)
        print(f"  {term}: {count}")
    
    return combined

def check_forgery_evidence(data):
    """Verify the forgery evidence aligns with manuscripts."""
    print("\n--- Forgery Evidence Check ---")
    
    forgery = data['forgery']
    manuscripts = data['manuscripts']
    
    # High suspicion manuscripts
    high_suspicion = forgery[forgery['suspicion_level'].isin(['high', 'confirmed'])]
    print(f"High/Confirmed suspicion manuscripts: {len(high_suspicion)}")
    
    for _, row in high_suspicion.iterrows():
        ms_id = row['manuscript_id']
        ms_info = manuscripts[manuscripts['manuscript_id'] == ms_id]
        if len(ms_info) > 0:
            status = ms_info.iloc[0]['authenticity_status']
            author = ms_info.iloc[0]['author']
            print(f"  {ms_id}: {author} - status: {status}")

def print_summary(data):
    """Print a summary of the dataset."""
    print("\n" + "="*50)
    print("CAPITAL ARCHIVES DATA SUMMARY")
    print("="*50)
    
    print(f"\nScholars: {len(data['scholars'])}")
    schools = data['scholars']['philosophical_school'].value_counts()
    for school, count in schools.items():
        print(f"  {school}: {count}")
    
    print(f"\nManuscripts: {len(data['manuscripts'])}")
    genres = data['manuscripts']['genre'].value_counts()
    for genre, count in genres.head(5).items():
        print(f"  {genre}: {count}")
    
    print(f"\nDebates: {len(data['debates'])}")
    print(f"Expeditions: {len(data['expeditions'])}")
    print(f"Archive Shops: {len(data['shops'])}")
    print(f"Word Index Terms: {len(data['word_index'])}")
    
    # Suspected forgeries
    forgeries = data['manuscripts'][data['manuscripts']['authenticity_status'] == 'suspected_forgery']
    print(f"\nSuspected Forgeries: {len(forgeries)}")
    for _, row in forgeries.iterrows():
        print(f"  {row['manuscript_id']}: {row['title'][:50]}...")

if __name__ == '__main__':
    # Load data
    data = load_all_data()
    
    if len(data) == 8:  # All files loaded
        # Run validations
        validate_references(data)
        
        # Analyze content
        analyze_text_content(data)
        
        # Check forgery setup
        check_forgery_evidence(data)
        
        # Print summary
        print_summary(data)
        
        print("\n✓ Data validation complete!")
    else:
        print("\n✗ Some files failed to load. Check file paths.")
