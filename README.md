# Load the images and extract text using OCR-- Code to extract string using tesseract:
image_paths = ['/mnt/data/test_3.jpg', '/mnt/data/test_2.webp']
extracted_texts = []

# Extract text from each image
for path in image_paths:
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    extracted_texts.append(text)

# Display the extracted texts for review
extracted_texts
--------------------------------------------------------------------------------------
Sample Ouptus:

Set 1:
Walmart
Save Money. Live Better.
Manager: Raymond Mercado
420 Buckland Hills Dr, Manchester CT 06042

ST# 01891 OP# 007393 TE# 16 TR# 01513
GVDISHORGGEL 007874230281 2.98 N
GVDTSHLEMGEL 007874228330 2.98 N
CEREAL BARLY 001500007002 F 2.98
GB CEREAL 001500007033 F 2.98
EFG NON-GMO 030087911768 F 21.98
SPINBR SLIM 076687801900 F 9.88
TOMATO ROMA 3.88 N
EGGS 12CT 007874214825 F 2.88
**VOIDED ENTRY**

SUBTOTAL 76.72
TAX 1 6.35%
TOTAL 77.54
DISCOVERY CREDIT: ***** 4568
APPROVAL: 02138R

ITEMS SOLD: 14
DATE: 04/21/17





SET 2:

2 MILK 007874235187 F 1.79
FREEZER BAGS 002570000381 4.66
91 ALCOHOL 068113117588 6.92 N
70 ALCOHOL 068113117586 9.92 N
OF REPLENISH 030065035605H 14.98
MAY MASCARA 004155442061 6.78
REESE EGG 003400047851 F 2.98
KING SIZE 003400000229 F 1.48
TOTAL 118.97
TAX 1: 8.00%
CASH TENDERED: 120.00
CHANGE: 1.03
ITEMS SOLD: 23
DATE: 01/11/20

10 th iteration Output: 


+----------+------------------+---------------------+-------------+
| Receipt  | Item             | Details             | Price (USD) |
+----------+------------------+---------------------+-------------+
| 1        | GVDISHORGGEL     | 007874230281        | 2.98        |
| 1        | GVDTSHLEMGEL     | 007874228330        | 2.98        |
| 1        | CEREAL BARLY     | 001500007002        | 2.98        |
| 1        | GB CEREAL        | 001500007033        | 2.98        |
| 1        | EFG NON-GMO      | 030087911768        | 21.98       |
| 1        | SPINBR SLIM      | 076687801900        | 9.88        |
| 1        | TOMATO ROMA      | -                   | 3.88        |
| 1        | EGGS 12CT        | 007874214825        | 2.88        |
| 2        | MILK             | 007874235187        | 1.79        |
| 2        | FREEZER BAGS     | 002570000381        | 4.66        |
| 2        | 91 ALCOHOL       | 068113117588        | 6.92        |
| 2        | 70 ALCOHOL       | 068113117586        | 9.92        |
| 2        | OF REPLENISH     | 030065035605H       | 14.98       |
| 2        | MAY MASCARA      | 004155442061        | 6.78        |
| 2        | REESE EGG        | 003400047851        | 2.98        |
| 2        | KING SIZE        | 003400000229        | 1.48        |
+----------+------------------+---------------------+-------------+

