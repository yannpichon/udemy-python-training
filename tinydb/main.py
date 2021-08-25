from tinydb import TinyDB, Query, where

db = TinyDB("data.json", indent=4)
# db.insert_multiple([{"name": "Patrick", "score": 0},{"name": "Paul", "score": 120}])

db.update({"score": 10}, where("name") == "Patrick")
db.update({"roles": ["Junior"]})
db.update({"roles": ["Consultant"]}, where ("name") == "Patrick")
db.upsert({"name": "Pierre", "score": 0, "roles": ["Senior"]}, where("name") == "Pierre")

db.remove(where("score") == 0)
db.truncate()