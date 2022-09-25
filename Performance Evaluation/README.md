## Tugas 2 - Performance Evaluation

**`Python 3.10.4`** **`scikit-learn 1.1.2`**

## Instructions
`Individual Assignment`

1. Amati **email** anda untuk periode tertentu (boleh seminggu, dua minggu, atau sebulan
sedemikian sehingga masing-masing kategori ada isinya). 
- Terdapat sejumlah kelas atau kategori email (minimal 2 buah)
- Berikan penjelasan masing-masing kategori email

2. Berdasarkan email yang masuk, buatlah tabel yang terdiri dari 3 kolom: 
- **Nomor**
- **Actual**
- **Predicted**

> | No | Actual | Predicted |
> | :---: | :---: | :---: |
> | 1 | `Spam` | `Spam` |
> | 2 |  |  |
> | | ... | |

3. Hitunglah berapa nilai **TP**, **TN**, **FP**, **FN**.
- Berikan penjelasan secara garis besar bagaimana cara anda menghitung nilai masing-masing. 
- Tunjukkan *pseudocode* atau algoritme untuk menghitung nilai tsb.

4. Kemudian tunjukkan ***confusion matrix***-nya.

5. Buat function `python` untuk menghitung **akurasi**, **precision**, **recall**, dan **F-Measure**.

6. Bandingkan hasilnya dengan *built-in function* `python`, misal dengan function
**classification_report(actual, predicted)**. Untuk menggunakan script tsb, anda perlu
mendefinisikan array ***actual*** dan ***predicted***.

7. Dataset email yang anda gunakan tersebut apakah termasuk dataset yang seimbang (**balanced**) atau tidak seimbang (**imbalanced**)? 
- Apa konsekuensinya jika dataset tersebut **balanced** atau **imbalanced**? (*Tunjukkan reference yang mendukung penjelasan anda*)

8. Dari berbagai ukuran performance yang dihasilkan, mana yang memberikan nilai paling kecil?
- Jelaskan mengapa nilainya kecil dibandingkan dengan yang lain?