"""Utilities for DNA to RNA transcription."""


def to_rna(dna_strand: str) -> str:
    """Convert a DNA strand to its RNA complement."""

    transcription_map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join(transcription_map[nucleotide] for nucleotide in dna_strand)