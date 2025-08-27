# main.py
from scripts.align import Aligner
from scripts.samtools import Sam2Bam, Sort, Dedup, AddReadGroups
from scripts.variant_calling import VariantCalling
from scripts.annotation import SnpEffAnnotator

# ---------- Definições iniciais ----------
reference = "files/bwa/hg19.fasta"
reads1 = "files/510-7-BRCA_S8_L001_R1_001.fastq.gz"
reads2 = "files/510-7-BRCA_S8_L001_R2_001.fastq.gz"
sample_name = "brca_align"
threads = 2

# Arquivo de regiões alvo (BRCA1 e BRCA2)
target_list = "files/BRCA_fixed.list"

snpeff_path = "snpEff/snpEff.jar"  # caminho para o snpEff.jar
genome_db = "hg19"
output_vcf = f"{sample_name}_annotated.vcf"

# ---------- Alinhamento ----------
aligner = Aligner(reference, reads1, reads2, threads, sample_name)
aligner.sample_name = sample_name  # necessário para usar no > {sample_name}.sam
aligner.run_alignment()

# ---------- SAM -> BAM ----------
sam2bam = Sam2Bam("brca_align.sam", "brca_align")
sam2bam.sam_2_bam()

# Sort BAM
sorter = Sort("brca_align.bam", "brca_align")
sorter.sort()

# Add Read Groups
addrg = AddReadGroups("brca_align.sorted.bam", "brca_align")
addrg.add_rg()

# Dedup
deduper = Dedup("brca_align.rg.bam", "brca_align")
deduper.duplicates()

# ---------- Variant Calling ----------
vcaller = VariantCalling(reference, "brca_align.dedup.bam", sample_name, target_list)
vcaller.run_Vcalling()

# ---------- SnpEff Annotation ----------
annotator = SnpEffAnnotator(snpeff_path, genome_db, f"{sample_name}.vcf", output_vcf)
annotator.run_annotation()
