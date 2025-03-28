makeblastdb -in rdrps.fasta -dbtype prot
blastx -query fasta/SRR7554416_rnaspades.fasta -db rdrps.fasta -outfmt 6 > blast_output_test.out
