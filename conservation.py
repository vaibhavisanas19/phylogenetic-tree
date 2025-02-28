import streamlit as st
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import matplotlib.pyplot as plt
from io import StringIO

# Streamlit App Title
st.title("Phylogenetic Tree Generator")

# User Input Section
st.header("Enter Your Sequences")
sequences_input = st.text_area("Enter sequences in FASTA format:",
""">Seq1
ATCGTACGATCG
>Seq2
ATGGTACGATCA
>Seq3
ATCGTACGCTCG
""")

# Button to Generate Tree
if st.button("Generate Phylogenetic Tree"):
    try:
        # Convert the input into a StringIO object
        fasta_io = StringIO(sequences_input)

        # Read sequences into an alignment object
        alignment = AlignIO.read(fasta_io, "fasta")

        # Compute distance matrix
        calculator = DistanceCalculator('identity')
        distance_matrix = calculator.get_distance(alignment)

        # Construct tree using Neighbor-Joining
        constructor = DistanceTreeConstructor()
        tree = constructor.nj(distance_matrix)

        # Plot the tree
        fig, ax = plt.subplots(figsize=(5, 5))
        Phylo.draw(tree, axes=ax)

        # Display the tree in Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {str(e)}")