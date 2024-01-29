import PyPDF2


def merge_pdfs(pdf_files, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            pdf_merger.append(file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f'Merged {len(pdf_files)} PDFs into {output_filename}')


if __name__ == '__main__':
    # List of PDF files to merge
    pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
    output_filename = 'merged.pdf'  # Output merged PDF filename

    merge_pdfs(pdf_files, output_filename)
