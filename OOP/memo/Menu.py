import sys
from notebook import Note, Notebook


class Menu:

	def __init__ (seft):
		seft.notebook = Notebook()
		seft.choices = {
		"1": seft.show_notes,
		"2": seft.search_note,
		"3": seft.add_note,
		"4": seft.modify_note,
		"5": seft.quit
		}

	def display(seft):
		print("""
			Notebook Menu:
			1. Show all Notes
			2. Serach Notes
			3. Add Note
			4. Modify Notes
			5. Quit""")
	def run(self):
		while True:
			self.display()
			choice = input("Lua chon option:")
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print("{0} khong phai gia tri duoc chon".format(choice))

	def show_notes(self, notes= None):
		notes = self.notebook.notes
		for note in notes:
			print("{0}: {1}\n {2}".format(note.id, note.tags, note.memo))
	def search_note(self):
		filter = input("Tim Note:")
		notes = self.notebook.search(filter)
		self.show_notes(notes)

	def add_note(self):
		memo = input("Nhap ghi chu cua ban:")
		self.notebook.new_note(memo)
		print("Ghi chu cua ban da duoc them")
	def modify_note(self):
		id = input("Nhap id can sua:")
		memo = input("Noi dung:")
		tags = input("tags:")
		if memo:
			self.notebook.modify_memo(id, memo)
		if tags:
			self.notebook.modify_tags(id, tags)
	def quit(self):
		print("Thank you")
		sys.exit()
if __name__ == "__main__":
	Menu().run()
