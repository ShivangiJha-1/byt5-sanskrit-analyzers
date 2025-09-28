"""
Consciousness analysis processing for Sanskrit texts.
Handles consciousness-related terms, concepts, and states in Sanskrit literature.
"""

# Sanskrit consciousness-related terms and their categories
consciousness_terms = {
    # Core consciousness terms
    "cit": "awareness",
    "citi": "consciousness", 
    "citta": "mind-consciousness",
    "चित्त": "mind-consciousness",
    "cetana": "awareness-faculty",
    "caitanya": "consciousness-principle",
    "चैतन्य": "consciousness-principle",
    "jñāna": "knowledge-awareness",
    "ज्ञान": "knowledge-awareness", 
    "vijñāna": "discriminative-consciousness",
    "विज्ञान": "discriminative-consciousness",
    "prajñā": "wisdom-consciousness",
    "प्रज्ञा": "wisdom-consciousness",
    "bodhi": "awakened-consciousness",
    "sākṣin": "witness-consciousness",
    "साक्षी": "witness-consciousness",
    
    # States of consciousness
    "samādhi": "absorption-state",
    "समाधि": "absorption-state",
    "dhyāna": "meditation-state",
    "ध्यान": "meditation-state", 
    "dhāraṇā": "concentration-state",
    "धारणा": "concentration-state",
    "nirodha": "cessation-state",
    "निरोध": "cessation-state",
    "laya": "dissolution-state",
    "turīya": "fourth-state",
    "तुरीय": "fourth-state",
    "suṣupti": "deep-sleep-state",
    "svapna": "dream-state",
    "jāgrat": "waking-state",
    
    # Cognitive processes
    "manas": "mind-faculty",
    "मनस्": "mind-faculty",
    "buddhi": "intelligence-faculty",
    "बुद्धि": "intelligence-faculty",
    "ahaṅkāra": "ego-faculty",
    "अहंकार": "ego-faculty",
    "smṛti": "memory-faculty",
    "kalpanā": "imagination-faculty",
    "saṃkalpā": "intention-faculty",
    "vikalpa": "conceptualization",
    "nirvikalpa": "non-conceptual",
    
    # Phenomenological terms  
    "sphuraṇā": "vibration-awareness",
    "spanda": "dynamic-consciousness",
    "prakāśa": "luminosity",
    "प्रकाश": "luminosity",
    "vimarśa": "self-awareness",
    "ānanda": "bliss-consciousness",
    "आनन्द": "bliss-consciousness"
}

def read_consciousness_tags(path):
    """Read consciousness-specific tags from file."""
    result = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        lines = [line.split("\t") for line in lines if line.strip()]
        for line in lines:
            if len(line) >= 2:
                result[line[0]] = line[1].strip()
    except FileNotFoundError:
        # Use default consciousness terms if file not found
        result = consciousness_terms
    return result

def analyze_consciousness_content(sentence, mode="consciousness-analysis"):
    """
    Analyze sentence for consciousness-related content.
    
    Args:
        sentence: Sanskrit text to analyze
        mode: Type of consciousness analysis to perform
    
    Returns:
        Analyzed text with consciousness annotations
    """
    if mode == "consciousness-terms":
        return identify_consciousness_terms(sentence)
    elif mode == "consciousness-concepts":
        return extract_consciousness_concepts(sentence)  
    elif mode == "consciousness-states":
        return identify_consciousness_states(sentence)
    else:
        return full_consciousness_analysis(sentence)

def identify_consciousness_terms(sentence):
    """Identify and tag consciousness-related terms in the sentence."""
    words = sentence.split()
    result = []
    
    for word in words:
        # Remove common Sanskrit punctuation and particles
        clean_word = word.strip("।॥")
        found_match = False
        
        # Check for exact matches first
        if clean_word in consciousness_terms:
            tag = consciousness_terms[clean_word]
            result.append(f"{word}_{tag}")
            found_match = True
        else:
            # Check for partial matches (handling Sanskrit morphology)
            for term, tag in consciousness_terms.items():
                if term in clean_word or clean_word.startswith(term):
                    result.append(f"{word}_{tag}")
                    found_match = True
                    break
        
        if not found_match:
            result.append(word)
    
    return " ".join(result)

def extract_consciousness_concepts(sentence):
    """Extract consciousness concepts and their relationships."""
    # This would identify larger conceptual structures
    # For now, return sentence with concept markers
    consciousness_concepts = [
        "ātman", "आत्मा", "आत्मन्",
        "brahman", "ब्रह्म", "ब्रह्मन्", 
        "puruṣa", "पुरुष",
        "prakṛti", "प्रकृति", 
        "māyā", "माया",
        "mokṣa", "मोक्ष",
        "nirvāṇa", "निर्वाण", 
        "kaivalya", "कैवल्य",
        "samādhi", "समाधि"
    ]
    
    words = sentence.split()
    result = []
    
    for word in words:
        clean_word = word.strip("।॥")
        found_match = False
        
        for concept in consciousness_concepts:
            if concept in clean_word or clean_word.startswith(concept):
                result.append(f"{word}_[CONCEPT]")
                found_match = True
                break
                
        if not found_match:
            result.append(word)
    
    return " ".join(result)

def identify_consciousness_states(sentence):
    """Identify states of consciousness mentioned in the text."""
    consciousness_states = [
        "samādhi", "समाधि",
        "dhyāna", "ध्यान", 
        "dhāraṇā", "धारणा",
        "turīya", "तुरीय", 
        "suṣupti", "सुषुप्ति",
        "svapna", "स्वप्न", 
        "jāgrat", "जाग्रत्",
        "nirodha", "निरोध", 
        "laya", "लय"
    ]
    
    words = sentence.split()
    result = []
    
    for word in words:
        clean_word = word.strip("।॥")
        found_match = False
        
        for state in consciousness_states:
            if state in clean_word or clean_word.startswith(state):
                result.append(f"{word}_[STATE]")
                found_match = True
                break
                
        if not found_match:
            result.append(word)
    
    return " ".join(result)

def full_consciousness_analysis(sentence):
    """Perform comprehensive consciousness analysis."""
    # Combine all analysis types
    result = sentence
    result = identify_consciousness_terms(result)
    result = extract_consciousness_concepts(result) 
    result = identify_consciousness_states(result)
    
    return result

def postprocess_consciousness_analysis(sentence, mode="consciousness-analysis"):
    """
    Postprocess the consciousness analysis output.
    """
    if mode in ["consciousness-terms", "consciousness-concepts", 
                "consciousness-states", "consciousness-analysis"]:
        return analyze_consciousness_content(sentence, mode)
    else:
        return sentence.replace("_", " ")