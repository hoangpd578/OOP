import datetime

last_id = 0

class Note:

	def __init__(self, memo, tags= ""):
		self.memo = memo
		self.tags = tags
		self.create_date = datetime.datetime.now()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filters):

		return filters in self.memo or filters in self.tags

class Notebook:

	def __init__ (self):
		self.notes = []

	def new_note(self, memo, tags = ''):
		self.notes.append(Note(memo, tags))

	def modify_memo(self, note_id, memo):

		self.find_note(note_id).memo = memo
		
	def modify_tags(self, note_id, tags):

		for note in self.notes:
			if note.id == note_id:
				note.tags == tags
				break
	def search(self, filters):
		return[note for note in self.notes if note.match(filters)]

	def find_note(self, note_id):
		for note in self.notes:
			if note.id == note_id:
				return note
		return None
