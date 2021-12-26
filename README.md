# ncbi_data_fetch

#### This repository locates the First SARS-CoV-2- Omicron variant data in the NCBI's website, dowloads the Sequence Read Archive (SRA) data using NCBI's SRA toolkit and CLI commands to dowload the SRA data in fastq format and then uses a python script to parse the fastq file.

## Table of contents
1. [LOCATE THE DATA](#LOCATE THE DATA)
2. [DOWNLOAD AND INSTALL THE SRA TOOLKIT](#DOWNLOAD AND INSTALL THE SRA TOOLKIT)
3. [DOWNLOAD THE SRA DATA](#DOWNLOAD THE SRA DATA)
4. [PARSE AND ANALYZE THE SRA DATA](#PARSE AND ANALYZE THE SRA DATA)
5. [RUN FASTQC FOR QUALITY CHECK](#RUN FASTQC FOR QUALITY CHECK)



#### 1. LOCATE THE DATA:
- Locate the data in NCBI website: First SARS-CoV-2- Omicron variant in Europe and note the SRR run id i.e. SRR17066006
Link: https://www.ncbi.nlm.nih.gov/sra/?term=omicron+europe


#### 2. DOWNLOAD AND INSTALL THE SRA TOOLKIT:
- In order to access the fastq file through the NCBI CLI commands, we need to download and install the SRA toolkit provided by NCBI to access and manipulate custom data from NCBI’s website. https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit#ncbi-sra-toolkit


- Download and install the SRA toolkit using the curl command:
  ```
  Curl –output sratoolkit.tar.gz https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-mac64.tar.gz
  ```

- OUTPUT: 
    ```
    zip sratoolkit file
    ```
- Extract the content using: 
    ```
    tar -vxzf sratoolkit.tar.gz
    ```

- Append the path to the binaries to your PATH environment variable and verify the binaries:
    ````
    export PATH=$PATH:$PWD/sratoolkit.2.4.0-1.mac64/bin
  ````
    ````
    which fastq-dump
    ````
- Configure the toolkit to access the data on the cloud:
    ````
    vdb-config -i
    ````

#### 3. DOWNLOAD THE SRA DATA:
- Once the SRA toolkit is configured, use the prefetch tool from the SRA toolkit to download the SRA data  using the following command: 
    ````
    Vdb-config -prefetch-to-cwd
    ````
    ````
    Prefetch SRR17066006
    ````

- Use the fastq-dump tool to convert the SRA data to fastq format:
    ````
    Fasterq-dump SRR17066006
    ````

#### 4. PARSE AND ANALYZE THE SRA DATA WHICH IS IN FASTQ FORMAT:

- Refer `parse_ncbi_data.py` and `analysis.ipynb` scripts that converts the fastq file into usbale format for further analysis.


#### 5. RUN FASTQC FOR QUALITY CHECK:

- Download the FastQC(a quality control tool for high thorughput sequence data) from https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
and run the quality check


