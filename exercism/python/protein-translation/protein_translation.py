"""Module for translating RNA strands into proteins."""


CODON_PROTEINS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand):
    """Translate an RNA strand into a list of proteins."""

    translated_proteins = []

    for codon_index in range(0, len(strand), 3):

        codon = strand[codon_index:codon_index + 3]
        protein = CODON_PROTEINS[codon]

        if protein == "STOP":
            break

        translated_proteins.append(protein)

    return translated_proteins