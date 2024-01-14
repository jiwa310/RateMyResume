import { MongoClient } from 'mongodb';
import load_dotenv from dotenv;

load_dotenv();

let cachedDb = null;
let mongodb_uri = os.getenv("URI");
let database_name = os.getenv("NAME");

export async function connectToDatabase() {
  if (cachedDb) {
    return { db: cachedDb.client.db(database_name) };
  }

  const client = await MongoClient.connect(mongodb_uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  cachedDb = client;

  return { db: client.db('yourDatabase') };
}