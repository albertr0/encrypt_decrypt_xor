How to run:
	python encrypt.py -key -inputFile -outputFile


example:
	python encrypt.py cheie input.txt out1.bin
	
	python decrypt.py out1.txt cheie out2.bin
	

Cum functioneaza:
1. encrypt.py

	Am citit datele necesare in command prompt.
	
	Citim sirul din fisier iar apoi il transformam in sir binar.
	
	Luam lungimea cheii si o multiplicam astefel incat 
	lungimea sirului format din multiplicarea cheii sa aiba lungimea cel putin egala cu a sirului ce trebui xorat. 
	
	Parcurgem fiecare caracter (0 sau 1) din sirul initial transformat in binar si il xoram.

	Trecem apoi in output

2. decrypt.py
	
	Pentru a decripta codul binar obtinut si a restitui mesajul initial am urmat un procedeu similar cu cel de la partea de criptare.

	Pentru inceput am facut xor bit cu bit intre sirul binar obtinut si sirul binar echivalent parolei , pentru a obtine sirul binar echivalent mesajului .

	Am definit o functie de conversie care transforma grupuri de cate 8 biti in codul ascii echivalent , iar apoi am afisat caracterul corespunzator acelui cod ascii
