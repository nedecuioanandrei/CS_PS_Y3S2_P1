db = new Mongo().getDB("OldiesApahida");
db.createCollection("users", {capped: false})
db.createCollection("orders", {capped: false})
db.createCollection("dishes", {capped: false})

db.users.insert([
    {
        "pass_sha256": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
        "name": "Andrei",
        "role": "admin",
    },
    {
        "pass_sha256": "9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0",
        "name": "Vasile",
        "role": "employee",
    }
])