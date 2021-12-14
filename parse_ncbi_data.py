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


class ParseFastq:
    def __init__(self, input_file):
        self.input_file = input_file
        self.read_lines = []
        self.sequence_list = []

        # open and read all lines in the fastq file
        with open(self.input_file, 'r') as fastq_file:
            for lines in fastq_file:
                self.read_lines.append(lines)

        # break into groups of 4
        for line in range(0, len(self.read_lines), 4):
            single_sequence = self.read_lines[line:line + 4]
            self.sequence_list.append(single_sequence)

    def fastq_to_csv(self):
        sequence_df = pd.DataFrame(self.sequence_list, columns=['seq_id', 'seq_reads', 'id2', 'seq_quality'])
        print(sequence_df)
        return sequence_df

    def fastq_to_dict(self):
        pass

    @staticmethod
    def count_reads(seq_df):
        count_reads = len(seq_df['seq_reads'])
        print(f"The count of reads is {count_reads}")

    @staticmethod
    def distribution_reads(seq_df):
        dist = seq_df['seq_reads'].apply(len)
        print(f"read_distribution {dist.describe()}")
        print("Histogram of read lengths")
        plt.hist(dist)
        plt.show()


if __name__ == '__main__':
    # df = parse_fastq('sra_data/SRR17066006.fastq')
    # df.to_csv('seq_df.csv', index=False)

    seq = ParseFastq('sra_data/SRR17066006.fastq')
    df = seq.fastq_to_csv()
    seq.count_reads(df)
    seq.distribution_reads(df)
