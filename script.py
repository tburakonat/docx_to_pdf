from docx2pdf import convert


def main():
    # convert every docx file in the certificates/docx folder to pdf and put them in the certificates/pdf folder

    convert("certificates/docx", "certificates/pdf")


if __name__ == "__main__":
    main()
