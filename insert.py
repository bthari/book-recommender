from retrieve.models import Book
fr = open("new-books.txt", "r")
idt = 0
b = Book(book_id=0,title='-')
while idt < 576:
	txt = fr.readline()
	if "\"ID\"" in txt:
		b.save()
		print(str(idt)+" done.\n")
		idt = idt + 1
		b = Book(book_id=idt)
	if "\"title\"" in txt:
		tmp = txt.split(":")
		b.title = tmp[1]
	if "\"description\"" in txt:
		tmp = txt.split(":")
		b.description = tmp[1]
print("Finished.")