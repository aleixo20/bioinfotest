import subprocess
import shlex

class SnpEffAnnotator:
    def __init__(self, snpeff_path, genome_db, input_vcf, output_vcf):
        self.snpeff_path = snpeff_path
        self.genome_db = genome_db
        self.input_vcf = input_vcf
        self.output_vcf = output_vcf
  
    def run_annotation(self):
        cline = f"java -Xmx4g -jar {self.snpeff_path} {self.genome_db} {self.input_vcf}"
        print(cline)
        with open(self.output_vcf, "w") as vcf_out:
            cmd_cline = subprocess.Popen(shlex.split(cline), stdout=vcf_out)
            cmd_cline.wait()
        print("########### SnpEff annotation completed successfully.")
