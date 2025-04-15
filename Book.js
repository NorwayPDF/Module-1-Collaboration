const mongoose = require("mongoose");

const BookSchema = new mongoose.Schema({
  id: { type: String, required: true },
  book_name: { type: String, required: true },
  author: { type: String, required: true },
  publisher: { type: String, required: true }
});

module.exports = mongoose.model("Book", BookSchema);