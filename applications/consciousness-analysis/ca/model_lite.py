"""
Lightweight version of consciousness analysis for testing without ML dependencies.
This version uses rule-based analysis instead of the ByT5 model.
"""

def process_batch(batch, mode):
    """
    Process a batch of Sanskrit texts for consciousness analysis using rule-based methods.
    This is a lightweight version that doesn't require the heavy ML model.
    
    Args:
        batch: List of Sanskrit text strings
        mode: Analysis mode (consciousness-terms, consciousness-concepts, consciousness-states)
    
    Returns:
        List of analyzed texts with consciousness annotations (same as input for rule-based)
    """
    # For rule-based analysis, we return the input as-is since postprocessing does the work
    return batch