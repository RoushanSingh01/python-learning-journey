"""Transform legacy Scrabble score format into a new format."""


def transform(legacy_data):
    """Convert score-to-letters mapping into letter-to-score mapping."""
    
    result = {}

    for key, value_lst in legacy_data.items():
        for value in value_lst:
            result[value.lower()] = key

    return result