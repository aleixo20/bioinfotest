import subprocess
import shlex

class VariantCalling:
    def __init__(self, reference, bam, sample_name, target_list=None):
        self.reference = reference
        self.bam = bam
        self.sample_name = sample_name
        self.target_list = target_list  # arquivo de regiões alvo opcional
  
    def run_Vcalling(self):
        if self.target_list:
            cline = f"freebayes -f {self.reference} -t {self.target_list} {self.bam}"
        else:
            cline = f"freebayes -f {self.reference} {self.bam}"

        print(cline)
        with open(f"{self.sample_name}.vcf", "w") as vcf_out:
            cmd_cline = subprocess.Popen(shlex.split(cline), stdout=vcf_out)
            cmd_cline.wait()
        print("########### Variant Calling completed successfully.")