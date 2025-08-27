import subprocess
import shlex

class Sam2Bam:
    def __init__(self, sam, sample_name):
        self.sam = sam
        self.sample_name = sample_name
     
    def sam_2_bam(self):
        cline = f"samtools view -bo {self.sample_name}.bam {self.sam}"
        print(cline)
        cline = shlex.split(cline)
        cmd_cline = subprocess.Popen(cline)
        cmd_cline.wait()
        print("###########Convertion completed successfully.")

class Sort:
    def __init__(self, bam, sample_name):
        self.bam = bam
        self.sample_name = sample_name
    
    def sort(self):
        cline = f"samtools sort -o {self.sample_name}.sorted.bam {self.bam}"
        print(cline)
        cline = shlex.split(cline)
        cmd_cline = subprocess.Popen(cline)
        cmd_cline.wait()
        print("###########Convertion completed successfully.")

class AddReadGroups:
    def __init__(self, bam, sample_name):
        self.bam = bam
        self.sample_name = sample_name

    def add_rg(self):
        cline = f"picard AddOrReplaceReadGroups --INPUT {self.bam} --OUTPUT {self.sample_name}.rg.bam --RGID 1 --RGLB lib1 --RGPL ILLUMINA --RGPU unit1 --RGSM {self.sample_name}"
        print(cline)
        cline = shlex.split(cline)
        cmd_cline = subprocess.Popen(cline)
        cmd_cline.wait()
        print("########### Read Groups added successfully.")

class Dedup:
    def __init__(self, bam, sample_name):
        self.bam = bam  # agora será o BAM com RG
        self.sample_name = sample_name

    def duplicates(self):
        cline = f"picard MarkDuplicates --INPUT {self.bam} --OUTPUT {self.sample_name}.dedup.bam --METRICS_FILE {self.sample_name}_marked_dup_metrics.txt --CREATE_INDEX true"
        print(cline)
        cline = shlex.split(cline)
        cmd_cline = subprocess.Popen(cline)
        cmd_cline.wait()
        print("###########Dedup completed successfully.")
