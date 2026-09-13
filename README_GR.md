\# Script Backup MikroTik



\[English version](README.md)



Python script που δημιουργεί binary backup σε MikroTik RouterOS και το κατεβάζει αυτόματα στον φάκελο Documents των Windows.



\## Τι κάνει



1\. Συνδέεται στο MikroTik μέσω SSH.

2\. Δημιουργεί αρχείο RouterOS binary backup (`.backup`).

3\. Περιμένει να ολοκληρωθεί η δημιουργία του αρχείου.

4\. Ανοίγει SFTP channel μέσω της υπάρχουσας SSH σύνδεσης.

5\. Κατεβάζει το backup στον φάκελο Documents του τρέχοντος Windows χρήστη.

6\. Κλείνει τις συνδέσεις SFTP και SSH.



\## Προϋποθέσεις



\- Windows

\- Python 3

\- Δικτυακή πρόσβαση προς το MikroTik

\- Ενεργοποιημένο SSH και SFTP στο MikroTik

\- Python package `paramiko`



\## Εγκατάσταση



Από PowerShell:



```powershell

py -m pip install paramiko

```



\## Ρύθμιση κωδικού



Ο κωδικός του MikroTik δεν αποθηκεύεται μέσα στο Python script.



Αποθήκευσέ τον μία φορά ως Windows environment variable:



```powershell

setx MIKROTIK\_PASSWORD "ο\_κωδικός\_του\_router"

```



Μετά κλείσε και ξανάνοιξε το PowerShell ή το terminal.



> Μην ανεβάζεις ποτέ κωδικούς στο GitHub.



\## Ρύθμιση script



Άλλαξε τις παρακάτω τιμές στο `mikrotik-backup.py`, αν χρειάζεται:



```python

router\_ip = "192.168.10.1"

username = "admin"

backup\_name = "Weekly\_10\_1\_backup"

```



\## Εκτέλεση



Από τον φάκελο του project:



```powershell

py mikrotik-backup.py

```



Το backup αποθηκεύεται εδώ:



```text

C:\\Users\\ΤΟ\_ΟΝΟΜΑ\_ΣΟΥ\\Documents

```



\## Προγραμματισμένη εκτέλεση



Χρησιμοποίησε το Windows Task Scheduler για αυτόματη εκτέλεση συγκεκριμένη ημέρα και ώρα.



\- \*\*Program/script:\*\* η διαδρομή προς το `python.exe`

\- \*\*Add arguments:\*\* η πλήρης διαδρομή προς το `mikrotik-backup.py`



\## Ασφάλεια



\- Μην βάζεις κωδικούς στο Python αρχείο.

\- Μην ανεβάζεις `.backup` αρχεία στο GitHub.

\- Τα binary backups του RouterOS ενδέχεται να περιέχουν ευαίσθητες ρυθμίσεις.

\- Το `.gitignore` αποκλείει backup και environment αρχεία.

