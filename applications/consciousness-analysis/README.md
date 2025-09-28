# ByT5-Sanskrit Consciousness Analysis Agent

This folder contains code for consciousness analysis of Sanskrit texts using the ByT5-Sanskrit model. The agent is specifically designed to identify, analyze, and annotate consciousness-related concepts, terms, and states in Sanskrit philosophical and spiritual literature.

## Overview

The consciousness analysis agent extends the ByT5-Sanskrit analyzers to provide specialized processing for consciousness studies in Sanskrit texts. It can identify consciousness-related terminology, extract conceptual structures, and analyze states of consciousness as described in various Sanskrit philosophical traditions.

## Features

- **Consciousness Term Identification**: Recognizes and tags consciousness-related Sanskrit terms
- **Conceptual Analysis**: Extracts larger consciousness concepts and their relationships
- **State Analysis**: Identifies mentions of various states of consciousness
- **Comprehensive Analysis**: Combines all analysis modes for complete consciousness annotation

## Data Source

The underlying model training data has been taken from the Digital Corpus of Sanskrit (DCS):
[http://www.sanskrit-linguistics.org/dcs/](http://www.sanskrit-linguistics.org/dcs/)

The consciousness-specific terminology and concepts have been curated from classical Sanskrit philosophical texts including Vedanta, Samkhya, Yoga, Kashmir Shaivism, and Buddhist literature.

## Supported Analysis Modes

1. **consciousness-terms**: Identifies and tags individual consciousness-related terms
2. **consciousness-concepts**: Extracts conceptual structures related to consciousness
3. **consciousness-states**: Identifies states of consciousness mentioned in the text
4. **consciousness-analysis**: Comprehensive analysis combining all modes

## Requirements

- Python 3.6+
- PyTorch
- Transformers
- tqdm
- pandas

You can install these requirements with pip: `pip install torch transformers tqdm pandas`.

## Usage

### Basic Usage

```bash
python run_consciousness_analysis.py --input-file input.txt --mode consciousness-analysis --output-file output.txt
```

### Analysis Modes

1. **Identify consciousness terms only**:
```bash
python run_consciousness_analysis.py --input-file toy-data/consciousness-texts.txt --mode consciousness-terms --output-file consciousness-terms.txt
```

2. **Extract consciousness concepts**:
```bash
python run_consciousness_analysis.py --input-file toy-data/consciousness-texts.txt --mode consciousness-concepts --output-file consciousness-concepts.txt
```

3. **Identify consciousness states**:
```bash
python run_consciousness_analysis.py --input-file toy-data/consciousness-texts.txt --mode consciousness-states --output-file consciousness-states.txt
```

4. **Full consciousness analysis in TSV format**:
```bash
python run_consciousness_analysis.py --input-file toy-data/consciousness-texts.txt --mode consciousness-analysis --output-file full-analysis.tsv --output-mode tsv
```

### Command Line Arguments

- `--input-file`: Path to the input file containing Sanskrit text (required)
- `--mode`: Analysis mode (required)
  - Choices: `consciousness-terms`, `consciousness-concepts`, `consciousness-states`, `consciousness-analysis`
- `--output-file`: Path to the output file (required)
- `--output-mode`: Output format (optional, default: `txt`)
  - Choices: `txt` (plain text), `tsv` (tab-separated values)
- `--batch-size`: Batch size for processing (optional, default: 20)

## Output Formats

### Text Output (txt)
Each analyzed sentence is written on a new line with consciousness annotations embedded in the text.

### TSV Output (tsv)
Tab-separated file with columns:
- `segmentnr`: Unique identifier for each text segment
- `original`: Original Sanskrit text
- `consciousness_analysis`: Analyzed text with consciousness annotations

## Consciousness Terminology

The agent recognizes various categories of consciousness-related terms:

### Core Consciousness Terms
- **cit**: Pure awareness
- **citta**: Mind-consciousness
- **caitanya**: Consciousness principle
- **jñāna**: Knowledge-awareness
- **vijñāna**: Discriminative consciousness
- **prajñā**: Wisdom-consciousness

### States of Consciousness  
- **samādhi**: Absorption states
- **dhyāna**: Meditation states
- **turīya**: The fourth state
- **suṣupti**: Deep sleep state
- **svapna**: Dream state
- **jāgrat**: Waking state

### Cognitive Processes
- **manas**: Mind faculty
- **buddhi**: Intelligence faculty
- **ahaṅkāra**: Ego faculty
- **smṛti**: Memory faculty

### Phenomenological Terms
- **prakāśa**: Luminosity of consciousness
- **vimarśa**: Self-awareness
- **spanda**: Dynamic consciousness
- **sphuraṇā**: Conscious vibration

## Example Input and Output

### Input Text:
```
सर्वं खल्विदं ब्रह्म।
चित्तं तु संस्कारवशात्।
समाधिर्एकाग्रता चित्तस्य।
```

### Sample Output (consciousness-analysis mode):
```
सर्वं खल्विदं ब्रह्म_[CONCEPT]।
चित्तं_mind-consciousness तु संस्कारवशात्।
समाधिर्_absorption-state एकाग्रता चित्तस्य_mind-consciousness।
```

## Integration with Other Sanskrit NLP Tasks

The consciousness analysis agent can be combined with other ByT5-Sanskrit analyzers for comprehensive text processing:

1. First run segmentation and lemmatization
2. Then apply consciousness analysis to identify relevant passages
3. Use dependency parsing for structural analysis of consciousness-related statements

## Research Applications

This agent is particularly useful for:

- Digital humanities research on Sanskrit philosophical texts
- Computational analysis of consciousness studies in Indian philosophy
- Automated annotation of spiritual and philosophical literature
- Comparative studies across different Sanskrit philosophical traditions
- Building consciousness-focused corpora from Sanskrit literature

## Limitations

- The current implementation uses rule-based pattern matching combined with the base ByT5 model
- Consciousness term recognition is based on a curated list and may miss contextual variations
- Complex philosophical arguments about consciousness may require human interpretation
- The analysis is primarily lexical and may not capture deep semantic relationships

## Future Enhancements

- Integration of context-aware consciousness concept detection
- Support for cross-referencing consciousness terms across texts
- Addition of philosophical school-specific consciousness terminology
- Enhanced semantic analysis of consciousness-related arguments
- Support for multilingual consciousness term mapping

## Contributing

To add new consciousness terms or improve analysis accuracy:
1. Update the `consciousness_terms` dictionary in `ca/analysis.py`
2. Add new analysis functions for specific philosophical traditions
3. Contribute example texts and expected outputs for testing

## Citation

If you use this consciousness analysis agent in your research, please cite the underlying ByT5-Sanskrit paper and acknowledge the consciousness-specific extensions.