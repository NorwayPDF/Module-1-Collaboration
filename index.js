const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const cors = require("cors");
const Book = require("./models/Book");

dotenv.config();
const app = express();
app.use(express.json());
app.use(cors());

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

// CRUD Routes
app.get("/books", async (req, res) => {
  const books = await Book.find();
  res.json(books);
});

app.post("/books", async (req, res) => {
  const newBook = new Book(req.body);
  await newBook.save();
  res.json(newBook);
});

app.put("/books/:id", async (req, res) => {
  const updatedBook = await Book.findOneAndUpdate({ id: req.params.id }, req.body, { new: true });
  res.json(updatedBook);
});

app.delete("/books/:id", async (req, res) => {
  await Book.findOneAndDelete({ id: req.params.id });
  res.json({ message: "Book deleted" });
});

app.listen(5000, () => console.log("Server running on port 5000"));