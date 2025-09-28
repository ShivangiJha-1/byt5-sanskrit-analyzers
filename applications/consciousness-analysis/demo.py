#!/usr/bin/env python3
"""
Demonstration script for consciousness analysis capabilities.
Shows all analysis modes with example Sanskrit texts.
"""

from ca.analysis import (
    identify_consciousness_terms, 
    extract_consciousness_concepts, 
    identify_consciousness_states, 
    full_consciousness_analysis
)

def demonstrate_analysis():
    print("ByT5-Sanskrit Consciousness Analysis Agent Demonstration")
    print("=" * 60)
    
    # Sample Sanskrit texts from various philosophical traditions
    sample_texts = [
        "सर्वं खल्विदं ब्रह्म।",  # Chandogya Upanishad
        "आत्मा वा अरे द्रष्टव्यः।",  # Brihadaranyaka Upanishad
        "चित्तवृत्तिनिरोधो योगः।",  # Yoga Sutras
        "समाधिर्एकाग्रता चित्तस्य।",  # Yoga Sutras
        "तुरीयं तत्प्रज्ञानम्।",  # Mandukya Upanishad
        "प्रकाशविमर्शमयं चैतन्यम्।",  # Kashmir Shaivism
        "साक्षिचैतन्यमशेषवृत्तिसाक्षी।",  # Vedanta
    ]
    
    print("\nSample Sanskrit Texts:")
    print("-" * 30)
    for i, text in enumerate(sample_texts, 1):
        print(f"{i}. {text}")
    
    print("\n" + "=" * 60)
    print("ANALYSIS MODES DEMONSTRATION")
    print("=" * 60)
    
    for text in sample_texts:
        print(f"\nOriginal: {text}")
        print("-" * len(text))
        
        # Consciousness Terms Analysis
        terms_result = identify_consciousness_terms(text)
        if terms_result != text:
            print(f"Terms:    {terms_result}")
        
        # Consciousness Concepts Analysis
        concepts_result = extract_consciousness_concepts(text)
        if concepts_result != text:
            print(f"Concepts: {concepts_result}")
        
        # Consciousness States Analysis
        states_result = identify_consciousness_states(text)
        if states_result != text:
            print(f"States:   {states_result}")
        
        # Full Analysis
        full_result = full_consciousness_analysis(text)
        if full_result != text:
            print(f"Full:     {full_result}")
        
        if all(result == text for result in [terms_result, concepts_result, states_result]):
            print("No consciousness-related terms detected.")
    
    print("\n" + "=" * 60)
    print("LEGEND")
    print("=" * 60)
    print("Terms: Individual consciousness-related terms with their categories")
    print("Concepts: Major philosophical concepts related to consciousness") 
    print("States: States or modes of consciousness")
    print("Full: Comprehensive analysis combining all modes")
    print("\nFormat: sanskrit_word_[TAG] or sanskrit_word_category-description")
    
    print("\n" + "=" * 60)
    print("For full CLI usage, see README.md or run:")
    print("python run_consciousness_analysis_lite.py --help")
    print("=" * 60)

if __name__ == "__main__":
    demonstrate_analysis()