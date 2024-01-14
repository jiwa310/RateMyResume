import mongoose from "mongoose";

const User = mongoose.Schema(
  {
    name: String,
    age: Number
  },
  {
    timestamps: true,
  }
);

export default mongoose.models.User || mongoose.model("User", User);