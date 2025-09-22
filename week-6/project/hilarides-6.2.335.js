// a. Display all students.
db.students.find()

/* b. Add a new student. Ensure the fields in the new document match the
existing fields in the collection. Next, prove the new student was added
successfully */
db.students.insertOne({
  "firstName": "Neb",
  "lastName": "Snape",
  "studentId": "s1019",
  "houseId": "h1010"
})

db.students.findOne({ firstName: "Neb", lastName: "Snape" })

/* c. Update one of the properties from the student you added in step b. Next,
prove the property was updated successfully. */
db.students.updateOne(
  { firstName: "Neb", lastName: "Snape" },
  { $set: { lastName: "Black" } }
)

db.students.findOne({ firstName: "Neb", lastName: "Black" })

/* d. Delete the student you created in step b. Next, prove the student was
removed successfully. */
db.students.deleteOne({ firstName: "Neb", lastName: "Black" })

db.students.findOne({ firstName: "Neb", lastName: "Black" })

/* e. Display all students by house. */
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  },
  { $project: {
    _id: 0,
    houseId: 1,
    mascot: 1,
    founder: 1,
    students: 1 } }
])

/* f. Display all students in house Gryffindor. */
db.houses.aggregate([
  {
    $match: { founder: "Godric Gryffindor" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  },
  { $project: {
    _id: 0,
    houseId: 1,
    students: 1 } }
])

/* g. Display all students in the house with an Eagle mascot. */
db.houses.aggregate([
  {
    $match: { mascot: "Eagle" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  },
  { $project: {
    _id: 0,
    houseId: 1,
    students: 1 } }
])