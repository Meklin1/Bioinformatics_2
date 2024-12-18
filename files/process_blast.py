from Bio import SeqIO

# Paths to input files
blast_results_file = "tblast_result.txt"       # Tabular BLAST results file
representative_sequences = "representative_sequences.fasta"  # Full sequences of subjects
output_file = "aligned_regions.fasta"          # File to save aligned regions

# Step 1: Parse BLAST output to get alignment regions
alignments = {}  # Dictionary to store alignments {subject_id: [(start, end)]}
with open(blast_results_file, "r") as f:
    for line in f:
        cols = line.strip().split('\t')
        subject_id = cols[1]
        sstart = int(cols[8])
        send = int(cols[9])
        
        # Ensure start < end, in case of reversed alignment
        start, end = sorted((sstart, send))
        
        if subject_id not in alignments:
            alignments[subject_id] = []
        alignments[subject_id].append((start, end))

# Step 2: Extract aligned regions from subject sequences
aligned_regions = []
for record in SeqIO.parse(representative_sequences, "fasta"):
    subject_id = record.id
    if subject_id in alignments:
        for start, end in alignments[subject_id]:
            aligned_seq = record.seq[start-1:end]  # Extract region (1-based index)
            aligned_regions.append(f">{subject_id}_{start}_{end}\n{aligned_seq}\n")

# Step 3: Write aligned regions to output file
with open(output_file, "w") as out_f:
    out_f.writelines(aligned_regions)

print(f"Aligned regions saved to {output_file}")
