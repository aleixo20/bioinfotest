import subprocess
import shlex

class Aligner:
    def __init__(self, reference, reads1, reads2, threads, sample_name):
        self.reference = reference
        self.reads1 = reads1
        self.reads2 = reads2
        self.threads = threads
        self.sample_name = sample_name

     
    def run_alignment(self):
        cline = f"bwa mem {self.reference} {self.reads1} {self.reads2} -t {self.threads} > {self.sample_name}.sam"
        print(cline)
        cmd_cline = subprocess.Popen(cline, shell=True)  # Apenas shell=True
        cmd_cline.wait()
        print("########### Alignment completed successfully.")