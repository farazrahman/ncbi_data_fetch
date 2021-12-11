import pandas as pd
import matplotlib.pyplot as plt

def _read_fastq(input_file):
    # open and read all lines in the fastq file
    read_lines = []
    with open(input_file, 'r') as fastq_file:
        for lines in fastq_file:
            read_lines.append(lines)
        return read_lines


def parse_fastq(input_file):
    sequence_list = []
    fastq_lines = _read_fastq(input_file=input_file)
    # break into groups of 4
    for line in range(0, len(fastq_lines), 4):
        single_sequence = fastq_lines[line:line + 4]
        sequence_list.append(single_sequence)
    sequence_df = pd.DataFrame(sequence_list, columns=['seq_id', 'reads', 'discard', 'seq_qc'])
    print(f"The count of reads is {len(sequence_df['reads'])}")
    print("Histogram of read lengths")
    plt.hist(sequence_df['reads'].apply(len))
    plt.show()
    return sequence_df


if __name__ == '__main__':
    # print(_read_fastq('sra_data/SRR17066006.fastq'))
    df = parse_fastq('sra_data/SRR17066006.fastq')
    # df.to_csv('seq_df.csv', index=False)
