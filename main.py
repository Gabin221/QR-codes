import segno


def qrCode(texte_a_scanner, nom_fichier):
	qrcode = segno.make_qr(texte_a_scanner)
	qrcode.save(
        nom_fichier,
        scale=5
    )


if __name__ == "__main__":
	qrCode("texte", "file_name.png")
